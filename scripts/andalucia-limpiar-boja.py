from pathlib import Path
from bs4 import BeautifulSoup
import re


SOURCE_FOLDER = Path("documentos/España/Andalucia/normativa") 
files = [f for f in SOURCE_FOLDER.iterdir() if f.suffix == ".html"]


for f in files:
    b = BeautifulSoup(f.read_bytes(), features="html.parser")
    votos = b.find_all(string=re.compile("votos"))
    for s in votos:
        s.replace_with("(votos reemplazados)")
    f.write_bytes(b.encode("utf8", formatter="html5"))