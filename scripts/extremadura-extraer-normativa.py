from pdfreader import PDFDocument
from pathlib import Path
from collections import OrderedDict
import json

PDF_FILE = Path("documentos/España/Extremadura/normativa/covid.pdf")
OUT_FILE = Path("datos/España/Extremadura/normativa/pdf_DOE.json")

links = []

with PDF_FILE.open("rb") as fd:
    doc = PDFDocument(fd)
    for page in doc.pages():
        links += [annot.A.URI.decode("utf8") for annot in page.Annots]


links = list(OrderedDict.fromkeys(links))

OUT_FILE.write_text(json.dumps(links, sort_keys=True, indent=4))
