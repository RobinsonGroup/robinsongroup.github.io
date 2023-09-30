import yaml
import re
from collections import defaultdict

class Publication:

    def __init__(self, dict):
        self._pmid = dict.get('pmid', 'n/a')
        self._authors = dict.get('authors', 'n/a')
        self._year = int(dict.get('year', 'n/a'))
        self._title = dict.get('title', 'n/a')
        self._journal = dict.get('journal', 'n/a')
        self._volume = dict.get('volume', 'n/a')
        self._pages = dict.get('pages', 'n/a')


    @property
    def year(self):
        return self._year


    def get_markdown(self):
        authors = self._authors
        authors = re.sub(r"\.\s?", "", authors)
        authors = authors.replace("Robinson, PN", "**Robinson, PN**")
        mdown = f"{authors}. {self._year} {self._title} *{self._journal}* **{self._volume}**:{self._pages}"
        if self._pmid is not None:
            mdown = f"{mdown}\n[PMID:{self._pmid}](https://pubmed.ncbi.nlm.nih.gov/{self._pmid}/)"
        return mdown






publication_file = "../data/citations.yml"

pub_d = defaultdict(list)

with open(publication_file, 'r') as fh:
    publications = yaml.safe_load(fh)
    for p in publications:
        pub = Publication(dict=p)
        year = pub.year
        pub_d[year].append(pub)

for k, v in pub_d.items():
    for item in v:
        print(item.get_markdown())



