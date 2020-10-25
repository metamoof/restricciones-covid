import json
import requests
from pathlib import Path

URL_LIST = Path("datos/nacional/boe/normas/para-descargar/codigos.json")
DESTINATION_DIR = Path("documentos/nacional/boe/normativa")

laws = json.loads(URL_LIST.read_text(encoding="utf8"))
for url in laws:
    _, filename = url.split("id=")
    r = requests.get(url)
    fpath = DESTINATION_DIR / (filename + ".html")
    fpath.write_bytes(r.content)
