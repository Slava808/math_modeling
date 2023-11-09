import numpy as np

Vo = 10 
Yo = 0
a = np.pi / 180 * 45
g = np.sqrt(9.8)

t = np.arange(0, 5.0, 0.1)  # создаем массив времени от 0 до 5 секунд с шагом 0,1

Vx = Vo * np.cos(a)  # вычисляем компоненты скорости
Vy = Vo * np.sin(a) - g * t  # вычисляем компоненту скорости по вертикали

x = Vx * t  # находим координаты по оси X
y = Yo + Vo * t - g*t**2 / 2  # находим координаты по оси Y

result = np.column_stack([t, x, y])
print(result)