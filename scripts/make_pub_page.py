import re
from collections import defaultdict


"""
The citations.txt file is created by an internal XSL script
It is almost YML but contains some characters that do not mix well with YML
so for now we use a naive parse to transform these contents to markdown
"""

# The following authors are or were on our team and their names
# will be shown in bold in the publication page
our_team = [
    "Robinson PN",
    "Robinson, PN",
    "Booms P",
    "Tiecke F",
    "Palz M",
    "Katzke S",
    "Böhme U",
    "Ney A",
    "Guo G",
    "Bauer S",
    "Sebastian Bauer",
    "Schulz MH",
    "Köhler S",
    "Koehler S",
    "Ibn-Salem J",
    "Ott CE",
    "Rödelsperger C",
    "Krawitz PM",
    "Jäger M",
    "Doelken SC",
    "Heinrich V",
    "Bhushan R",
    "Grünhagen J",
    "Hansen P",
    "Krüger U",
    "Mensah MA",
    "Zemojtel T",
    "Kuchenbecker L",
    "Zhu N",
    "Schubach M",
    "Carmody L",
    "Danis D",
    "Blau H",
    "Karlebach G",
    "Ravanmehr V",
    "Gargano MA",
    "Coleman BD"
]

class Publication:

    def __init__(self, pmid, authors, year, title, journal, volume, pages, top):
        self._pmid = pmid
        self._authors = authors
        self._year = int(year)
        self._title = title
        self._journal = journal
        if volume is None or len(volume) == 0:
            volume = "n/a"
        self._volume = volume
        self._pages = pages
        self._top = top.lower() == "true"


    @property
    def year(self):
        return self._year

    @property
    def title(self):
        return self._title

    @property
    def journal(self):
        return self._journal

    def get_link(self):
        return f"[PMID:{self._pmid}](https://pubmed.ncbi.nlm.nih.gov/{self._pmid}/)"

    def get_first_author(self):
        athrs = self._authors.split(",")
        return athrs[0]

    def is_top(self):
        return self._top


    def _prcess_authors(self, authors):
        authors = re.sub("{\\\\\"{a}}", "ä", authors)
        authors = re.sub("{\\\\\"{o}}", "ö", authors)
        authors = re.sub("\\\\\"{o}", "ö", authors)
        authors = re.sub("{\\\\\"{u}}", "ü", authors)
        authors = re.sub("\\\\\"{u}", "ü", authors)
        authors = re.sub("{\\\\~{n}}", "ñ", authors)
        authors = re.sub("\\\\~{n}", "ñ", authors)
        authors = re.sub("\\\\\'{o}", "ó", authors)
        authors = re.sub("\\\\\'{i}", "í", authors)

        return authors


    def get_markdown(self):
        authors = self._prcess_authors(self._authors)
        authors = authors.replace("{\\bf Robinson PN}", "Robinson PN")
        authors = authors.replace("{\\bf Robinson P}", "Robinson P")
        authors = authors.replace("{\\bf Robinson N}", "Robinson N")
        authors = re.sub(r"\.\s?", "", authors)
        for a in our_team:
            authors = authors.replace(a, f"**{a}**")
        # The following sometimes use their middle initial :-0
        authors = authors.replace("Gargano M", "**Gargano M**")
        authors = authors.replace("Krawitz P", "**Krawitz P**")
        authors = authors.replace("Coleman B", "**Coleman B**")

        mdown = f"{authors}  \n{self._title}  \n *{self._journal}*, {self._year}; **{self._volume}**:{self._pages}"
        if self._pmid is not None and self._pmid != "n/a":
            mdown = f"{mdown} [PMID:{self._pmid}](https://pubmed.ncbi.nlm.nih.gov/{self._pmid}/)" + "{:target=\"_blank\"}"
        return mdown






publication_file = "../data/citations.txt"

def get_item(line):
    fields = line.strip().split(":")
    item = "".join(fields[1:])
    item = item.strip()
    item = item.replace("--", "-")
    return item



pub_d = defaultdict(list)

inEntry = False
with open(publication_file, 'r') as fh:
    pmid, authors, year, title, journal, volume, pages,top = None, None, None, None, None, None, None, None
    for line in fh:
        if line.startswith("-pmid:"):
            pmid, authors, year, title, journal, volume, pages, top = None, None, None, None, None, None, None, None
            pmid = get_item(line)
            inEntry = True
        elif line.startswith("authors:"):
            authors = get_item(line)
            for line in fh:
                if line.startswith("year:"):
                    year = get_item(line)
                    break
                else:
                    authors = authors + " " + line.strip()
        elif line.startswith("journal:"):
            journal = get_item(line)
        elif line.startswith("title:"):
            title = get_item(line)
        elif line.startswith("volume:"):
            volume = get_item(line)
        elif line.startswith("pages:"):
            pages = get_item(line)
        elif line.startswith("top:"):
            top = get_item(line)
        elif inEntry and len(line) < 5:
            inEntry = False
            try:
                pub = Publication(pmid=pmid, authors=authors, year=year, title=title,
                              journal=journal, volume=volume, pages=pages, top=top)
                pub_d[pub.year].append(pub)
            except:
                print(f"[ERROR] Not able to create publication for {title}")



def write_top_publications_table(pub_d, years, fh):
    top_pubs = []
    for year in years:
        publist = pub_d.get(year)
        for pub in publist:
            if pub.is_top():
                top_pubs.append(pub)
    print(f"We got {len(top_pubs)} top publications")
    fh.write("## Highlights\n\n")
    fh.write("| Author | Year   | Title  | Journal | PMID |\n")
    fh.write("|:------ |:------ |:------ |:------- |:------ |\n")
    for pub in top_pubs:
        fa = "**" + pub.get_first_author() + "**"
        items = [fa, str(pub.year), pub.title, pub.journal, pub.get_link()]
        fh.write("|".join(items) + "\n")
    fh.write("\n\n")


fh = open("../docs/publications.md", "wt")
fh.write("# Publications\n\n")
fh.write("Authors who are lab members or alumni are shown in **bold** font.\n\n")
years = sorted(list(pub_d.keys()), reverse=True)
write_top_publications_table(pub_d, years, fh)

citation_i = 0
for year in years:
    publist = pub_d.get(year)
    fh.write(f"## {year} Publications\n\n")

    for pub in publist:
        citation_i += 1
        fh.write(f"{citation_i}. {pub.get_markdown()}\n")
fh.close()

print(f"We output {citation_i} publications.")



