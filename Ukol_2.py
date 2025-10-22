import json
import requests

#Část1
#vyhledání podle IČO

dotaz_ico = input("Zadej IČO:")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{dotaz_ico}")
data = response.json()

nazev_spolecnosti = data.get("obchodniJmeno")
sidlo = data.get("textovaAdresa")

print(f"{nazev_spolecnosti}")
print(f"{sidlo}")

#Část2
#vyhledání dle názvu

import json
import requests

spolecnost = input("Zadej název společnosti: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{spolecnost}"}}'

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data.encode("utf=8"))

vypis = response.json()
subjekty = vypis.get("ekonomickeSubjekty", [])

print(f"Nalezeno subjektů: {len(subjekty)}")

for subjekt in subjekty:
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    pravni_forma = subjekt.get("pravniForma")
    print(f"{jmeno}, {ico}, {pravni_forma}")