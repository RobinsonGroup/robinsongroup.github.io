# README

This repository generates the Robinson Lab homepage using some scripts and mkdocs.

To test this locally, perform the following steps:

```bash
python3 -m venv mkd_venv
source mkd_venv/bin/activate
pip install --upgrade pip
pip install mkdocs-material
pip install mkdocs-material[imaging]
pip install badges
pip install mkdocs-badges
mkdocs serve
```

This will start a server on localhost at http://127.0.0.1:8000/

## Troubleshooting

Depending on your set up, if you are on a Mac, you many need to install cairo and pango libraries, and then execute the following command:

```bash
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

