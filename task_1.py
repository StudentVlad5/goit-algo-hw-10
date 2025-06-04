import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Total_Production", pulp.LpMaximize)

# Змінні: кількість вироблених напоїв
lemonade = pulp.LpVariable('Лимонад', lowBound=0, cat='Integer')
juice = pulp.LpVariable('Фруктовий_сік', lowBound=0, cat='Integer')

# Функція цілі: максимізація загальної кількості напоїв
model += lemonade + juice, "Загальна_кількість_напоїв"

# Обмеження ресурсів:
# Вода: лимонад (2 од.) + сік (1 од.) <= 100
model += 2 * lemonade + 1 * juice <= 100, "Обмеження_води"

# Цукор: тільки для лимонаду
model += 1 * lemonade <= 50, "Обмеження_цукру"

# Лимонний сік: тільки для лимонаду
model += 1 * lemonade <= 30, "Обмеження_лимонного_соку"

# Фруктове пюре: тільки для соку
model += 2 * juice <= 40, "Обмеження_фруктового_пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Статус розв'язання:", pulp.LpStatus[model.status])
print("Виробляти Лимонаду:", int(lemonade.varValue))
print("Виробляти Фруктового соку:", int(juice.varValue))
print("Максимальна кількість напоїв:", int(pulp.value(model.objective)))
