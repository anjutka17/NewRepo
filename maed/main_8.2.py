import numpy as np
import matplotlib.pyplot as plt


with open("maeed.txt", encoding="utf-8") as f:
    sisu = f.readlines()

tipunimed = [] 
korgused = [] 


# Обрабатываем каждую строку, разделяя имя и высоту
for rida in sisu:
    tükid = rida.strip().split() # del пробелы 
    tipp = ' '.join(tükid[:-1]) # кроме последнего —название горы
    väärtus = int(tükid[-1]) # last элемент — это высота
    tipunimed.append(tipp) # имя 
    korgused.append(väärtus) # высоту 

#  Преобразуем список высот в массив NumPy
korgused_arr = np.array(korgused)

# статистика
keskmine_korgus = korgused_arr.mean() 
maksimum_korgus = korgused_arr.max() 
minimaalne_korgus = korgused_arr.min() 
summa_korgus = korgused_arr.sum() 


korgeim = tipunimed[np.argmax(korgused_arr)] 
madalaim = tipunimed[np.argmin(korgused_arr)] 

# результаты 
print("Mägede keskmine kõrgus:", keskmine_korgus, "m") 
print("Kõige kõrgem mägi:", korgeim, "-", maksimum_korgus, "m") 
print("Kõige madalam mägi:", madalaim, "-", minimaalne_korgus, "m")
print("Kõrguste summa kokku:", summa_korgus, "m") 

# график
plt.figure(figsize=(10, 6))
plt.bar(tipunimed, korgused, color="cornflowerblue") 
plt.title("Maailma kõrgeimad tipud") 
plt.xlabel("Mäed") 
plt.ylabel("Kõrgus (m)") 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.savefig("maed_graafik.png") #Сохраняем 
plt.show() # показ

# Объединяем высоты и имена для сортировки
andmepaarid = list(zip(korgused, tipunimed)) # (kõrgus, nimi)

#  Сортировка по убыванию вручную
for i in range(len(andmepaarid)):
    for j in range(i + 1, len(andmepaarid)):
        if andmepaarid[i][0] < andmepaarid[j][0]: #  Если высота меньше — меняем местами
            andmepaarid[i], andmepaarid[j] = andmepaarid[j], andmepaarid[i]

# Разделяем обратно имена и высоты
sorteeritud_korgused = [paar[0] for paar in andmepaarid]
sorteeritud_nimed = [paar[1] for paar in andmepaarid]

#  Строим отсортированную диаграмму
plt.figure(figsize=(10, 6))
plt.bar(sorteeritud_nimed, sorteeritud_korgused, color="darkslateblue")
plt.title("Mäed kõrguse järgi (kahanevalt)") 
plt.xlabel("Mäetipud") 
plt.ylabel("Kõrgus (m)") 
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik_sorted.png") #  Сохраняем как файл
plt.show()
