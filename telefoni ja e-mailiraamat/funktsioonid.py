faili_nimi = "kontaktid.txt" # RU: Имя файла для хранения контактов
# ET: Faili nimi, kuhu kontaktid salvestatakse

# RU: Функция для чтения контактов из файла
# ET: Funktsioon kontaktide lugemiseks failist
def loe_failist():
    kontaktid = [] # RU: Создаём пустой список контактов
    # ET: Loome tühja nimekirja kontaktide jaoks
    try: # RU: Пытаемся открыть файл
    # ET: Proovime faili avada
        with open(faili_nimi, "r", encoding="utf-8") as f:
            for rida in f: # RU: Проходимся по каждой строке
# ET: Käime läbi iga rea failis
                osad = rida.strip().split(";") # RU: Удаляем пробелы и разбиваем строку по ";"
# ET: Eemaldame tühikud ja jagame rea ";" järgi
                if len(osad) == 3: # RU: Проверяем, что строка содержит 3 элемента
# ET: Kontrollime, kas reas on 3 osa
                    kontaktid.append({
                    "nimi": osad[0], # RU: имя
                    "telefon": osad[1], # RU: телефон
                    "email": osad[2] # RU: email
                }) # ET: Lisame kontakti sõnastikuna
    except FileNotFoundError:
# RU: Если файл не существует, создаём новый пустой файл
# ET: Kui faili pole, loome uue tühja faili
           open(faili_nimi, "w", encoding="utf-8").close()
    return kontaktid # RU: Возвращаем список контактов / ET: Tagastame kontaktide nimekirja


# RU: Функция для записи всех контактов в файл
# ET: Funktsioon kõikide kontaktide faili kirjutamiseks
def kirjuta_failisse(kontaktid):
    with open(faili_nimi, "w", encoding="utf-8") as f: # RU: Открываем файл в режиме перезаписи
# ET: Avame faili kirjutamiseks ("w" tähendab, et vana sisu kustutatakse)
        for k in kontaktid:
# RU: Записываем контакт как строку, разделяя данные символом ";"
# ET: Kirjutame iga kontakti uuele reale, andmed eraldatud semikooloniga
            f.write(f"{k['nimi']};{k['telefon']};{k['email']}\n")


# RU: Функция для добавления нового контакта
# ET: Funktsioon uue kontakti lisamiseks
def lisa_kontakt(nimi, telefon, email):
    kontaktid = loe_failist() # RU: Сначала читаем существующие контакты
# ET: Loeme olemasolevad kontaktid failist
    kontaktid.append({
    "nimi": nimi,
    "telefon": telefon,
    "email": email
    }) # RU/ET: Добавляем новый словарь в список
    kirjuta_failisse(kontaktid) # RU/ET: Сохраняем обновлённый список в файл


# RU: Функция для отображения всех контактов
# ET: Funktsioon kõigi kontaktide kuvamiseks
def kuva_kontaktid():
    kontaktid = loe_failist()
    if kontaktid: # RU: Если список не пустой / ET: Kui kontaktide nimekiri ei ole tühi
        for k in kontaktid:
            print(f"{k['nimi']} | {k['telefon']} | {k['email']}") # RU/ET: Выводим построчно
    else:
        print("Kontaktid puuduvad.") # RU: Нет контактов / ET: Kontakte pole


# RU: Функция для поиска по имени (без учёта регистра)
# ET: Funktsioon kontakti otsimiseks nime järgi (tõstutundetu)
def otsi_kontakti(nimi):
    kontaktid = loe_failist()
# RU: Список всех контактов, чьё имя совпадает
# ET: Loome nimekirja kontaktidest, kelle nimi sobib
    tulemused = [k for k in kontaktid if k['nimi'].lower() == nimi.lower()]
    return tulemused # RU/ET: Возвращаем список совпадений (может быть пустым)


# RU: Функция для удаления контакта по имени
# ET: Funktsioon kontakti kustutamiseks nime järgi
def kustuta_kontakt(nimi):
    kontaktid = loe_failist()
# RU: Исключаем все контакты, чьё имя совпадает с введённым
# ET: Jätame alles ainult need kontaktid, kelle nimi ei sobi
    uus_list = [k for k in kontaktid if k['nimi'].lower() != nimi.lower()]
    kirjuta_failisse(uus_list) # RU/ET: Перезаписываем файл обновлённым списком


# RU: Функция для изменения данных существующего контакта
# ET: Funktsioon olemasoleva kontakti muutmiseks
def muuda_kontakti(vana_nimi, uus_nimi, uus_telefon, uus_email):
    kontaktid = loe_failist()
    for k in kontaktid:
        if k['nimi'].lower() == vana_nimi.lower(): # RU/ET: Если имя совпадает — обновляем поля
            k['nimi'] = uus_nimi
            k['telefon'] = uus_telefon
            k['email'] = uus_email
            kirjuta_failisse(kontaktid) # RU/ET: Сохраняем изменения


# RU: Функция для сортировки по выбранному полю: nimi, telefon или email
# ET: Funktsioon kontaktide sorteerimiseks nime, telefoni või e-posti järgi
def sorteeri_kontaktid(kriteerium):
    kontaktid = loe_failist()
# RU: Сортируем с помощью встроенной функции sorted() по заданному ключу
# ET: Sorteerime kontaktid vastavalt valitud võtmele
    if kriteerium in ["nimi", "telefon", "email"]:
        return sorted(kontaktid, key=lambda x: x[kriteerium].lower())
    else:
        return kontaktid # RU: Если ключ неправильный, возвращаем как есть / ET: Vale kriteeriumi korral tagastame muutmata
