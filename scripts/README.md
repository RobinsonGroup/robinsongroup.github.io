# README

This repository generates the Robinson Lab home page
using mkdocs. We use a script to generate the publications
page.


## Documentation

These pages are generated with mkdocs.

To set things up, perform the following steps (substitute name of venv if needed).

```
python3 -m venv venvhpoo
source venvhpo/bin/activate
pip install --upgrade pip
pip install --upgrade mkdocs
pip install --upgrade mkdocs-material
pip install --upgrade mkdocs-material[imaging]
pip install --upgrade pymdown-extensions
pip install --upgrade pillow cairosvg
pip install --upgrade mkdocs-badges
pip install --upgrade mkdocstrings[python]
```

To start a local server, enter:
```
mkdocs serve
```
 