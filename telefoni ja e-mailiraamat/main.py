from funktsioonid import * # RU: Импорт всех функций из файла funktsioonid.py
# ET: Impordime kõik funktsioonid failist funktsioonid.py

# RU: Бесконечный цикл — программа будет выполняться до тех пор, пока пользователь не введет "0"
# ET: Lõputu tsükkel — programm töötab seni, kuni kasutaja valib "0"
while True:
    print("\n TELEFONIRAAMAT") # RU: Заголовок — "Телефонная книга"
# ET: Pealkiri — "Telefoniraamat"

# RU: Выводим варианты действий для пользователя
# ET: Kuvame kasutajale valikud
    print("1 - Lisa kontakt") # RU: Добавить контакт / ET: Lisa uus kontakt
    print("2 - Kuva kõik kontaktid") # RU: Показать все контакты / ET: Näita kõiki kontakte
    print("3 - Otsi kontakti nime järgi") # RU: Поиск по имени / ET: Otsi kontakti nime järgi
    print("4 - Kustuta kontakt") # RU: Удалить контакт / ET: Kustuta kontakt
    print("5 - Muuda kontakti") # RU: Редактировать контакт / ET: Muuda kontakti andmeid
    print("6 - Sorteeri kontaktid") # RU: Сортировка контактов / ET: Sorteeri kontaktid
    print("0 - Välju") # RU: Выйти / ET: Välju programmist

    valik = input("Vali tegevus: ") # RU: Запрос ввода от пользователя / ET: Küsime kasutajalt valiku

# RU: if — условие. Если valik равен "1", выполнить следующий блок
# ET: if — tingimus. Kui valik on "1", täida järgmine plokk
    if valik == "1":
        nimi = input("Sisesta nimi: ") # RU: Ввод имени / ET: Sisesta kontakti nimi
        telefon = input("Sisesta telefon: ") # RU: Ввод телефона / ET: Sisesta telefoninumber
        email = input("Sisesta e-post: ") # RU: Ввод email / ET: Sisesta e-posti aadress

# RU: Вызываем функцию из модуля для добавления контакта
# ET: Kutsub välja funktsiooni kontakti lisamiseks
        lisa_kontakt(nimi, telefon, email)

        print("Kontakt lisatud!") # RU: Подтверждение / ET: Kinnitame lisamise

# RU: elif — "иначе если". Проверяется, если предыдущий if не сработал
# ET: elif — "muidu kui". Kontrollib, kui eelmine tingimus polnud tõene
    elif valik == "2":
        kuva_kontaktid() # RU: Показываем список всех контактов / ET: Kuvame kõik kontaktid

    elif valik == "3":
        nimi = input("Sisesta otsitava nimi: ") # RU: Запрашиваем имя для поиска / ET: Sisesta otsitava nimi
        tulemused = otsi_kontakti(nimi) # RU: Функция поиска возвращает список совпадений / ET: Funktsioon tagastab otsingutulemused
        if tulemused:
# RU: Если найдены контакты, выводим каждый
# ET: Kui tulemused on leitud, kuvame need
            for k in tulemused:
                    print(f"{k['nimi']} | {k['telefon']} | {k['email']}")
        else:
            print("Kontakti ei leitud.") # RU: Сообщаем, что ничего не найдено / ET: Teavitame, et kontakti ei leitud

    elif valik == "4":
        nimi = input("Sisesta kustutatava nimi: ") # RU: Имя контакта, который хотим удалить / ET: Sisesta kontakti nimi, mida soovid kustutada
        kustuta_kontakt(nimi) # RU: Удаление контакта по имени / ET: Kustutab kontakti nime järgi
        print("Kontakt kustutatud!") # RU: Подтверждение / ET: Kinnitame kustutamise

    elif valik == "5":
        vana_nimi = input("Sisesta kontakti vana nimi: ") # RU: Сначала спрашиваем старое имя / ET: Esmalt vana nimi
        uus_nimi = input("Uus nimi: ") # RU: Новое имя / ET: Uus nimi
        uus_telefon = input("Uus telefon: ") # RU: Новый номер / ET: Uus telefoninumber
        uus_email = input("Uus e-post: ") # RU: Новый email / ET: Uus e-posti aadress

# RU: Вызываем функцию для обновления информации о контакте
# ET: Kutsub välja funktsiooni kontakti uuendamiseks
        muuda_kontakti(vana_nimi, uus_nimi, uus_telefon, uus_email)
        print("Kontakt muudetud!") # RU: Подтверждение / ET: Kinnitame muutmise

    elif valik == "6":
# RU: Запрашиваем по какому полю сортировать (имя, телефон или email)
# ET: Küsime, mille järgi sorteerida (nimi, telefon või email)
        kriteerium = input("Sorteeri mille järgi (nimi / telefon / email): ").lower()
        kontaktid = sorteeri_kontaktid(kriteerium) # RU: Функция возвращает отсортированный список / ET: Funktsioon tagastab sorteeritud nimekirja
        for k in kontaktid:
            print(f"{k['nimi']} | {k['telefon']} | {k['email']}") # RU: Выводим каждый контакт / ET: Kuvame iga kontakti

    elif valik == "0":
        print("Head aega!") # RU: Сообщаем о завершении / ET: Hüvastijätt
        break # RU: break — выход из цикла while / ET: break — katkestab tsükli

    else:
# RU: Если введено что-то кроме 0–6, выводим сообщение об ошибке
# ET: Kui sisestati midagi muud kui 0–6, näitame veateadet
        print("Vale valik, proovi uuesti!") # RU: Неверный ввод / ET: Vale sisend