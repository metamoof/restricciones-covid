import requests
from ebooklib import epub
import tempfile
from pathlib import Path
import os

EU_URL = "https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=355_COVID-19_Derecho_Europeo_y_Estatal__.epub"
EU_OUTPUT = Path("documentos/nacional/boe/codigos/normativa-ue.xhtml")

r = requests.get(EU_URL)

(f, fname) = tempfile.mkstemp("epub")
f = os.fdopen(f, "wb")
f.write(r.content)
f.close()

book = epub.read_epub(fname)
doc = book.get_item_with_href("nota-autor.xhtml")

EU_OUTPUT.write_bytes(doc.get_content())

AUTONOMY_URL = "https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?fich=396_COVID-19_Derecho_Autonomico.epub"
AUTONOMY_OUTPUT = Path("documentos/nacional/boe/codigos/normativa-autonómica.xhtml")

f = os.fdopen(f, "wb")
f.write(r.content)
f.close()

book = epub.read_epub(fname)
doc = book.get_item_with_href("nota-autor.xhtml")

AUTONOMY_OUTPUT.write_bytes(doc.get_content())


os.remove(fname)
