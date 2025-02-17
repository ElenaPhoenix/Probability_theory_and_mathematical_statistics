# Вероятность события А в каждом независимом испытании 0.0015. Какова вероятность того, что при 2000 испытаниях событие А появится 3 раза.
# Распределение Пуассона
import math

lamb = 0.0015 * 2000
P = math.pow(lamb, 3) * math.exp(-lamb) / math.factorial(3)
print(P)