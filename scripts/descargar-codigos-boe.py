from bs4 import BeautifulSoup
from urllib import parse
import json
import requests
from pathlib import Path


BASE_URL = "https://www.boe.es/"
DOCS_PATH = Path("documentos/nacional/boe/codigos")
DATA_PATH = Path("datos/nacional/boe/codigos")
LAWS_PATH = Path("datos/nacional/boe/normas/para-descargar/codigos.json")

codigos = []
normas = set()

with open("datos/nacional/boe/codigos/codigos.json", "r",
          encoding="utf8") as f:
    datos = json.loads(f.read())
    codigos = [item["url"] for item in datos["Documentos"]]

for url in codigos:
    filename = parse.parse_qs(parse.urlparse(url).query)["id"][0]
    r = requests.get(url)
    with open(DOCS_PATH / (filename + ".html"), "wb") as outdoc:
        outdoc.write(r.content)
    b = BeautifulSoup(r.text, features="html.parser")
    laws = set(
        parse.urljoin(BASE_URL, a["href"])
        for a in b.find(id="col-2").find_all("a")
        if a.has_attr("href") and "buscar" in a["href"]
        )
    title = b.find("h2").text
    normas.update(laws)
    data = {"Nombre": title, "Normas": sorted(list(laws))}
    with open(DATA_PATH / (filename + ".json"), "w",
              encoding="utf8") as outdata:
        outdata.write(json.dumps(data, sort_keys=True, indent=4))

with open(LAWS_PATH, "w", encoding="utf8") as f:
    f.write(json.dumps(sorted(list(normas)), sort_keys=True, indent=4))
