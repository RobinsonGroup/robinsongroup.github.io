import re
from collections import defaultdict


"""
The citations.txt file is created by an internal XSL script
It is almost YML but contains some characters that do not mix well with YML
so for now we use a naive parse to transform these contents to markdown
"""



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
        self._top = top


    @property
    def year(self):
        return self._year


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
        authors = authors.replace("Robinson, PN", "**Robinson, PN**")
        authors = authors.replace("Robinson PN", "**Robinson, PN**")
        mdown = f"{authors}  \n{self._title}  \n *{self._journal}*, {self._year}; **{self._volume}**:{self._pages}"
        if self._pmid is not None and self._pmid != "n/a":
            mdown = f"{mdown} [PMID:{self._pmid}](https://pubmed.ncbi.nlm.nih.gov/{self._pmid}/)"
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






fh = open("../docs/publications.md", "wt")
fh.write("# Publications\n\n")

years = sorted(list(pub_d.keys()), reverse=True)

citation_i = 0
for year in years:
    publist = pub_d.get(year)
    fh.write(f"## {year} Publications\n\n")
    for pub in publist:
        citation_i += 1
        fh.write(f"{citation_i}. {pub.get_markdown()}\n")
fh.close()

print(f"We output {citation_i} publications.")



