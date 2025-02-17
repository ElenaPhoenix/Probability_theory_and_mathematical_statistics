# Было проведено исследование научных статей на количество авторов в разные годы. 
# Построить 90% и 95% интервалы 
# Рисунок
# Доверительный интервал для средних арифметических
# 95%: Zт = 1.96
# 90%: Zт = 1.645
print(f'[{round(2 - 1.645*1.4/np.sqrt(151), 2)}; {round(2 + 1.645*1.4/np.sqrt(151), 2)}]') # 1946г. 90% [1.81; 2.19]
print(f'[{round(2 - 1.96*1.4/np.sqrt(151), 2)}; {round(2 + 1.96*1.4/np.sqrt(151), 2)}]') # 1946г.95% [1.78; 2.22]

print(f'[{round(2.3 - 1.645*1.6/np.sqrt(149), 2)}; {round(2.3 + 1.645*1.6/np.sqrt(149), 2)}]') # 1956г. 90% [2.08; 2.52]
print(f'[{round(2.3 - 1.96*1.6/np.sqrt(149), 2)}; {round(2.3 + 1.96*1.6/np.sqrt(149), 2)}]') # 1956г.95% [2.04; 2.56]