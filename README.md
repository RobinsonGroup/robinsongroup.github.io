# README

This repository generates the Robinson Lab homepage using some scripts and mkdocs.

To test this locally, perform the following steps:

```bash
python3 -m venv mkd_venv
source mkd_venv/bin/activate
pip install --upgrade pip
pip install mkdocs-material
pip install mkdocs-material[imaging]
mkdocs serve
```

This will start a server on localhost at http://127.0.0.1:8000/