import requests
from ebooklib import epub
import tempfile
from pathlib import Path
import os

CODE_URL = "https://boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=355_COVID-19_Derecho_Europeo_Estatal_y_Autonomico_.epub"
DOC_OUTPUT = Path("documentos/nacional/boe/codigos/normativa-ue-y-autonomica.xhtml")

r = requests.get(CODE_URL)

(f, fname) = tempfile.mkstemp("epub")
f = os.fdopen(f, "wb")
f.write(r.content)
f.close()

book = epub.read_epub(fname)
doc = book.get_item_with_href("nota-autor.xhtml")

DOC_OUTPUT.write_bytes(doc.get_content())

os.remove(fname)
