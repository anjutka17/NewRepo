import matplotlib.pyplot as plt
import numpy as np

plt.figure(facecolor="lightblue")

# Верхняя часть зонта
x1 = np.linspace(-12, 12, 400)
y1 = -1/18 * x1**2 + 12
plt.plot(x1, y1, color="pink") # розовый цвет

x2 = np.linspace(-4, 4, 400)
y2 = -1/8 * x2**2 + 6
plt.plot(x2, y2, color="green")

x3 = np.linspace(-12, -4, 400)
y3 = -1/8 * (x3 + 8)**2 + 6
plt.plot(x3, y3, color="green")

x4 = np.linspace(4, 12, 400)
y4 = -1/8 * (x4 - 8)**2 + 6
plt.plot(x4, y4, color="green")

# Ручка зонта
x5 = np.linspace(-4, -0.3, 400)
y5 = 2*(x5 + 3)**2 - 9
plt.plot(x5, y5, color="purple")

x6 = np.linspace(-0.4, 0.2, 400)
y6 = 1.5*(x6 + 3)**2 - 10
plt.plot(x6, y6, color="purple")

plt.title("VIHMAVARI") # "Зонтик" по-эстонски
plt.grid(True)
plt.axis('equal')
plt.show()
