from pathlib import Path
from bs4 import BeautifulSoup
import re


SOURCE_FOLDER = Path("documentos/España/Catalunya/interior") 
files = [f for f in SOURCE_FOLDER.iterdir() if f.suffix == ".html"] 

for f in files:
    b = BeautifulSoup(f.read_bytes(), features="html.parser")
    tag = b.find(property="og:url")
    tag["content"] = "#reemplazado"
    s = b.find(string=re.compile("GEOATX"))
    s.replace_with("#reemplazado")
    # un script que van poniendo y quitando constantemente
    s = b.find(text=re.compile("mozPerformance"))
    if s:
        s.parent.decompose()
    f.write_text(b.prettify(), encoding="utf8")
