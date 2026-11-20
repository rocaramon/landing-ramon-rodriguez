from html.parser import HTMLParser
from pathlib import Path


class Portfolio(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.languages = set()
        self.empty_translations = 0

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        if tag == "button" and "data-language" in attributes:
            self.languages.add(attributes["data-language"])
        if "data-en" in attributes and not attributes["data-en"].strip():
            self.empty_translations += 1


page = Portfolio()
page.feed((Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8"))
page.close()
errors = []
if len(set(page.ids)) != len(page.ids):
    errors.append("Hay identificadores HTML duplicados.")
for link in page.links:
    if link.startswith("#") and link[1:] not in page.ids:
        errors.append(f"No existe el destino {link}.")
if "https://www.linkedin.com/in/ramon-roca/" not in page.links:
    errors.append("Falta el enlace al perfil de LinkedIn.")
if page.languages != {"es", "en"} or page.empty_translations:
    errors.append("Revisa los idiomas y las traducciones vacías.")
if errors:
    raise SystemExit("\n".join(errors))
print("Portafolio verificado: navegación, LinkedIn y controles de idioma.")
