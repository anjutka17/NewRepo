import tkinter as tk
from tkinter import messagebox
from funktsioonid import *




kontaktid = loe_failist()

def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt_gui():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        lisa_kontakt(kontaktid, nimi,telefon,email)
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Edu","kontakt lisatud.")
        nimi_entry.delete(0,'end')
        telefon_entry.delete(0,'end')
        email_entry.delete(0,'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad","Täida kõik väljad")

def otsi_kontakt_gui():
    nimi = nimi_entry.get()
    tulemused=otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["nimi"])
        nimi_entry.delete(0,'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0,'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0,'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0",'end')
        tekstikast.insert("end", "Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")

def kustuta_kontakt_gui():
    nimi= nimi_entry.get()
    if kustuta_kontakt(kontaktid, nimi):
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Kustatud", "'{nimi}'kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")
def sorteeri_gui():
    kontaktid_sorted=soorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0","end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")
def muuda_kontakt_gui():
    vana_nimi = otsingu_viide.get()
    uus_nimi = nimi_entry.get()
    uus_telefon = telefon_entry.get()
    uus_email = email_entry.get()
    if vana_nimi and uus_email and uus_telefon and uus_email:
        õnnestus=muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            salvesta_kontaktid(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks.")
    else:
       messagebox.showwarning("Puuduvad andmed", "Palun täida kõik väljad.")
# Kontrollib andmete korrektsust ja unikaalsust enne lisamist
def kontrolli_ja_lisa_gui():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if not (nimi and telefon and email):
        messagebox.showwarning("Viga", "Kõik väljad peavad olema täidetud.")
        return

    if not kontrolli_andmed(nimi, telefon, email):
        messagebox.showwarning("Viga", "Andmevorming on vale.")
        return

    if not on_unikaalne(kontaktid, nimi, telefon, email):
        messagebox.showwarning("Viga", "See kontakt on juba olemas.")
        return

    lisa_kontakt(kontaktid, nimi, telefon, email)
    salvesta_kontaktid(kontaktid)
    messagebox.showinfo("Edukalt", "Kontakt lisatud.")
    kuva_kontaktid()

# Näitab kontakti kõige pikema nimega
def kuva_pikim_nimi_gui():
    pikim = leia_pikim_nimi(kontaktid)
    tekstikast.delete("1.0", "end")
    if pikim:
        tekstikast.insert("end", f"Pikim nimi: {pikim['nimi']} | {pikim['telefon']} | {pikim['email']}")
    else:
        tekstikast.insert("end", "Kontaktid puuduvad.")

# Kuvab kontaktid emaili domeeni kaupa
def kuva_domeenid_gui():
    grupeeritud = grupeeritud_emaili_domeenid(kontaktid)
    tekstikast.delete("1.0", "end")
    for domeen, inimesed in grupeeritud.items():
        tekstikast.insert("end", f"{domeen}:\n")
        for k in inimesed:
            tekstikast.insert("end", f" {k['nimi']} | {k['telefon']} | {k['email']}\n")
            tekstikast.insert("end", "\n")

aken = tk.Tk()
aken.title("Telefoniraamat")
aken.configure(bg="purple")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken, text="Nimi: ",font=("Arial",14, "bold"),fg="black").pack()
nimi_entry=tk.Entry(aken, font=("Comic Sans MS",12), fg="black", bg="white")
nimi_entry.pack()
tk.Label(aken, text="E-mail: ",font=("Arial",14, "bold"),fg="lightblue").pack()
email_entry=tk.Entry(aken, font=("Comic Sans MS",12), fg="black", bg="white")
email_entry.pack()
tk.Label(aken, text="Telefon: ",font=("Arial",14, "bold"),fg="darkblue").pack()
telefon_entry=tk.Entry(aken, font=("Comic Sans MS",12), fg="black", bg="white")
telefon_entry.pack()

nupude_rida=tk.Frame(aken)
nupude_rida.pack(pady=5)



tk.Button(nupude_rida, text="Kuva kontaktid", command=kuva_kontaktid,font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left",pady=2)
tk.Button(nupude_rida, text="Lisa kontakt", command=lisa_kontakt_gui,font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Otsi kontakt", command=otsi_kontakt_gui,font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Kustuta kontakt", command=kustuta_kontakt_gui, font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Soorteeri (nime järgi)", command=sorteeri_gui,font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Muuda kontakt", command=muuda_kontakt_gui,font=("Verdana", 12),fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Lisa (kontrollitud)", command=kontrolli_ja_lisa_gui, font=("Verdana", 12), fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Pikim nimi", command=kuva_pikim_nimi_gui, font=("Verdana", 12), fg="white", bg="lightblue").pack(side="left")
tk.Button(nupude_rida, text="Emaili domeenid", command=kuva_domeenid_gui, font=("Verdana", 12), fg="white", bg="lightblue").pack(side="left")
tekstikast = tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)



aken.mainloop()
