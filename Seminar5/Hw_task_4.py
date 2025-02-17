# Решать с помощью функции. Есть ли статистически значимые различия в росте дочерей и матерей?
# 4) Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
import numpy as np
import scipy.stats as stats

x = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])
# Двухвыборочный тест с зависимыми выборками. Выборки зависимые, т.к. родители и дети имеют генетическую связь
print(stats.ttest_rel(x, y)) # TtestResult(statistic=0.559522990335608, pvalue=0.5911212354055175, df=8)
print('pvalue=0.5911 > 𝛼=0.05 => нулевая гипотеза подтверждается - статистически значимых различий в росте дочерей и матерей нет')