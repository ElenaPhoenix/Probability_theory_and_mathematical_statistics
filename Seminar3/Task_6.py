# В ящике 15 шаров, из которых 5 голубы и 10 красных. Из ящика последовательно вынимают 2 шара; первый шар в ящик не возвращают. 
# Найти вероятность, что первый вытащенный шар  - красный , а второй – голубой. 
import math

P1 = math.comb(10, 1) / math.comb(15, 1)
P2 = math.comb(5, 1) / math.comb(14, 1)
P = P1 * P2
# P = (10/15) * (5/14)
print(P1, P2, P)