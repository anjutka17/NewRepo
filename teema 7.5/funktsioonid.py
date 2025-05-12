import json
import os

faili_nimi="kontaktid.json"

def loe_failist():
    if not os.path.exists(faili_nimi):
        return[]
    with open(faili_nimi,'r',encoding="utf-8-sig") as f:
        return json.load(f)

def salvesta_kontaktid(kontaktid):
    with open(faili_nimi,'r',encoding="utf-8-sig") as f:
        json.dump(kontaktid, f, ensure_ascii=False, indent=4)

def lisa_kontakt(kontaktid, nimi, telefon,email):
    kontaktid.append({'nimi':nimi, "telefon": telefon,"email":email})

def otsi_kontakt(kontaktid , nimi):
    return [k for k in kontaktid if nimi.lower() in k["nimi"].lower()]
def kustuta_kontakt(kontaktid, nimi):
    leitud= [k for k in kontaktid if k["nimi"].lower() == nimi.lower()]
    if leitud:
        kontaktid.remove(leitud[0])
        return True
    return False

def soorteeri_kontaktid(kontaktid, vaike):
    return sorted(kontaktid, key=lambda x: x[vaike].lower())

def muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email):
    for k in kontaktid:
        if k["nimi"].lower()==vana_nimi.lower():
            k["nimi"]=uus_nimi
            k["telefon"]=uus_telefon
            k["email"]=uus_email
            return True
    return False
# Kontrollib, kas nimi, telefon ja email on õiged
def kontrolli_andmed(nimi, telefon, email):
    nimi_okei = nimi.replace(" ", "").isalpha()
    telefon_okei = telefon.isdigit() and 7 <= len(telefon) <= 15
    email_okei = bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))
    return nimi_okei and telefon_okei and email_okei

# Kontrollib, kas kontakt on juba olemas
def on_unikaalne(kontaktid, nimi, telefon, email):
    for kontakt in kontaktid:
        if (kontakt['nimi'].lower() == nimi.lower() or
            kontakt['telefon'] == telefon or
            kontakt['email'].lower() == email.lower()):
            return False
    return True

# Leiab kontakti kõige pikema nimega
def leia_pikim_nimi(kontaktid):
    if not kontaktid:
        return None
    return max(kontaktid, key=lambda x: len(x['nimi']))

# Grupeerib kontaktid domeeni järgi
def grupeeritud_emaili_domeenid(kontaktid):
    domeenid = defaultdict(list)
    for k in kontaktid:
        osa = k['email'].split("@")[-1]
        domeenid[osa].append(k)
    return domeenid
