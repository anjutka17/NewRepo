import numpy as np
import matplotlib.pyplot as plt

# Loeme tekstifaili sisu / Читаем содержимое текстового файла
with open("maeed.txt", encoding="utf-8") as f:
    sisu = f.readlines()

tipunimed = [] # Mäetippude nimed / Названия горных вершин
korgused = [] # Vastavad kõrgused / Соответствующие высоты

# Töötleme iga rida, jagades nime ja kõrguse
# Обрабатываем каждую строку, разделяя имя и высоту
for rida in sisu:
    tükid = rida.strip().split() # Eemaldame tühikud ja jagame sõnadeks / Удаляем пробелы и разделяем по словам
    tipp = ' '.join(tükid[:-1]) # Kõik peale viimase on mäe nimi / Всё, кроме последнего — название горы
    väärtus = int(tükid[-1]) # Viimane element on kõrgus / Последний элемент — это высота
    tipunimed.append(tipp) # Lisame nime loendisse / Добавляем имя в список
    korgused.append(väärtus) # Lisame kõrguse loendisse / Добавляем высоту в список

# Teisendame kõrgused NumPy massiiviks / Преобразуем список высот в массив NumPy
korgused_arr = np.array(korgused)

# Arvutame statistika / Вычисляем статистику
keskmine_korgus = korgused_arr.mean() # Keskmine kõrgus / Средняя высота
maksimum_korgus = korgused_arr.max() # Kõrgeim tipp / Максимальная высота
minimaalne_korgus = korgused_arr.min() # Madalaim tipp / Минимальная высота
summa_korgus = korgused_arr.sum() # Kõrguste summa / Сумма всех высот

# Leiame vastavad mäetipud / Находим названия самой высокой и низкой гор
korgeim = tipunimed[np.argmax(korgused_arr)] # Kõrgeim mägi / Самая высокая гора
madalaim = tipunimed[np.argmin(korgused_arr)] # Madalaim mägi / Самая низкая гора

# Kuvame tulemused / Выводим результаты в терминал
print("Mägede keskmine kõrgus:", keskmine_korgus, "m") # Средняя высота гор
print("Kõige kõrgem mägi:", korgeim, "-", maksimum_korgus, "m") # Самая высокая гора
print("Kõige madalam mägi:", madalaim, "-", minimaalne_korgus, "m") # Самая низкая гора
print("Kõrguste summa kokku:", summa_korgus, "m") # Общая сумма всех высот

# Joonistame algse graafiku / Строим исходный график
plt.figure(figsize=(10, 6))
plt.bar(tipunimed, korgused, color="cornflowerblue") # Tulpdiagramm / Столбчатая диаграмма
plt.title("Maailma kõrgeimad tipud") # Заголовок
plt.xlabel("Mäed") # Подпись оси X
plt.ylabel("Kõrgus (m)") # Подпись оси Y
plt.xticks(rotation=45) # Поворот подписей X-тели
plt.tight_layout() # Автонастройка отступов
plt.savefig("maed_graafik.png") # Salvestame pildina / Сохраняем как изображение
plt.show() # Kuvame graafiku / Показываем график

# Kombineerime nime ja kõrguse sorteerimiseks / Объединяем высоты и имена для сортировки
andmepaarid = list(zip(korgused, tipunimed)) # (kõrgus, nimi)

# Sorteerime kahanevalt / Сортировка по убыванию (вручную, без sort())
for i in range(len(andmepaarid)):
    for j in range(i + 1, len(andmepaarid)):
        if andmepaarid[i][0] < andmepaarid[j][0]: # Kui kõrgus on väiksem, vahetame / Если высота меньше — меняем местами
            andmepaarid[i], andmepaarid[j] = andmepaarid[j], andmepaarid[i]

# Eraldame uuesti nimekirjad / Разделяем обратно имена и высоты
sorteeritud_korgused = [paar[0] for paar in andmepaarid]
sorteeritud_nimed = [paar[1] for paar in andmepaarid]

# Joonistame sorteeritud graafiku / Строим отсортированную диаграмму
plt.figure(figsize=(10, 6))
plt.bar(sorteeritud_nimed, sorteeritud_korgused, color="darkslateblue")
plt.title("Mäed kõrguse järgi (kahanevalt)") # Заголовок
plt.xlabel("Mäetipud") # Подпись оси X
plt.ylabel("Kõrgus (m)") # Подпись оси Y
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik_sorted.png") # Salvestame pildina / Сохраняем как файл
plt.show()