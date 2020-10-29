import requests
from ebooklib import epub
import tempfile
from pathlib import Path
import os


def extract_epub_page(url, href, outfile):

    print(f"Extrayendo {url} a {outfile}...")
    r = requests.get(url)
    (f, fname) = tempfile.mkstemp("epub")
    f = os.fdopen(f, "wb")
    f.write(r.content)
    f.close()

    book = epub.read_epub(fname)
    doc = book.get_item_with_href(href)

    outpath = Path(outfile)
    outpath.write_bytes(doc.get_content())

    os.remove(fname)


# Primero la normativa UE:
extract_epub_page(
    "https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?" +
    "fich=355_COVID-19_Derecho_Europeo_y_Estatal__.epub",
    "nota-autor.xhtml",
    "documentos/nacional/boe/codigos/normativa-ue.xhtml"
)

# Luego la normativa aotnómica
extract_epub_page(
    "https://www.boe.es/biblioteca_juridica/codigos/abrir_epub.php?" +
    "?fich=396_COVID-19_Derecho_Autonomico.epub",
    "nota-autor.xhtml",
    "documentos/nacional/boe/codigos/normativa-autonómica.xhtml"
)
