""" Limpieza de archivos descargados de la Comunitat Valenciana
Creamos un HTML bonito donde se ven los cambios
Quitamos el bloque de scripts de Liferay de la cabecera que
cambia en cada descarga
"""
from pathlib import Path
from bs4 import BeautifulSoup

SOURCE_FILE = Path("documentos/España/Comunitat Valenciana/normativa/")
SOURCE_FILE /= "covid-19.html"

b = BeautifulSoup(SOURCE_FILE.read_bytes(), features="html.parser")

# El bloque de scripts tiene un parametro "authToken" que cambia
# en cada descarga.
# Esto hace que salga un commit cada vez que se actualiza el fichero
scripts = [s for s in b.find_all("script") if "authToken" in s.next]
assert len(scripts) == 1

# No necesitamos el bloque de scripts, por lo que borramos el interior
s = scripts[0]
s.next.replace_with("/* Reemplazado */")

# tambien hay una serie de links a cosas minificadas con un timestamp
links = [link for link in b.find_all("link") if "&t=" in link["href"]]
for link in links:
    links["href"] = "#reemplazado"

scripts = [s for s in b.find_all("script") if "&t=" in s.get("src", "")]
for s in scripts:
    s["src"] = "#reemplazado"


SOURCE_FILE.write_text(b.prettify(), encoding="utf8")
