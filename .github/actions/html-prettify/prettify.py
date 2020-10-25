import sys
from bs4 import BeautifulSoup
with open(sys.argv[1], 'rb') as f:
    b = BeautifulSoup(f, features="html.parser")
with open(sys.argv[1], 'w', encoding="utf8") as f:
    f.write(b.prettify())
