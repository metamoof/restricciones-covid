from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# este archivo se corre despues de actualizar el documento general de boe
# crea el fichero datos/nacional/boe/codigos/codigos.json


BASE_URL = "https://www.boe.es/"
TAB_2 = "&tab=2"

items = []
result = {
    "Nombre": "Códigos Electrónicos relacionados con COVID-19",
    "Documentos": items
    }


with open("documentos/nacional/boe/codigos/codigos.html",
          encoding="utf8") as f:
    b = BeautifulSoup(f, features="html.parser")
    anchor = b.find(id="COVID-19")
    shelf = anchor.parent
    links = [link for link in shelf.find_all("a") if link.has_attr("href")]
    for link in links:
        url = urljoin(BASE_URL, link["href"] + TAB_2)
        nombre = link.img["alt"]
        item = {
            "Nombre": nombre,
            "url": url
        }
        items.append(item)

with open("datos/nacional/boe/codigos/codigos.json", "w",
          encoding="utf8") as out:
    out.write(json.dumps(result, indent=4))
