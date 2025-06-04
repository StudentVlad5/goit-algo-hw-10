import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# 1. Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість точок для методу Монте-Карло
N = 100000

# 2. Метод Монте-Карло
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

# Обчислення середнього значення f(x)
mean_fx = np.mean(y_rand)

# Площа прямокутника (b - a)
monte_carlo_result = (b - a) * mean_fx

print("Метод Монте-Карло:", monte_carlo_result)

# 3. Точне обчислення інтеграла через SciPy
quad_result, quad_error = spi.quad(f, a, b)
print("Точне значення (quad):", quad_result)
print("Абсолютна похибка:", abs(monte_carlo_result - quad_result))

# 4. Побудова графіка функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x² від 0 до 2')
plt.grid()
plt.show()

# Метод Монте-Карло: 2.661952772147002
# Точне значення (quad): 2.666666666666667
# Абсолютна похибка: 0.004713894519664752

'''
Метод Монте-Карло надає наближене значення інтеграла.
При великій кількості точок (N = 100000) результат дуже близький до точного.
Основна перевага Монте-Карло — простота реалізації і застосування до складних багатовимірних задач.
Основний недолік — повільна збіжність: потрібно дуже багато точок для високої точності.
'''