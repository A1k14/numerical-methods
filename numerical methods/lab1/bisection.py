"""
bisection.py
============
👤 ТАРАС: Метод дихотомії (половинного ділення)

Принцип методу:
Послідовний поділ відрізка [a, b] навпіл. На кожному кроці обирається та
половина, на кінцях якої функція набуває значень протилежних знаків (f(a) * f(b) < 0).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from equations import f_alg, f_trans


def plot_and_bisect(f, a, b, xtol, title):
    history = []

    def tracker(x):
        y = f(x)
        history.append((x, y))
        return y

    # Запускаємо bisect SciPy
    root, res = bisect(tracker, a=a, b=b, xtol=xtol, full_output=True)

    # Історія ітерацій (пропускаємо перші 2 виклики для меж a та b)
    iterations = history[2:]

    # Графік залежності log10|f(xn)| для вашого файлу
    fc_vals = [fc for _, fc in iterations]
    n_vals = np.arange(1, len(fc_vals) + 1)
    log_residuals = [np.log10(abs(fc)) if abs(fc) > 0 else -16 for fc in fc_vals]

    plt.figure(figsize=(7, 4))
    plt.plot(n_vals, log_residuals, 'bo-', label=r'$\log_{10}|f(x_n)|$')
    plt.title(f"{title} (Метод ділення навпіл)")
    plt.xlabel('Номер ітерації (n)')
    plt.ylabel(r'$\log_{10}|f(x_n)|$')
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.show()

    # Повертаємо корінь, об'єкт res та історію для main.py
    return root, res, iterations


def run_bisection():
    while True:
        print("\n=== МЕНЮ ===")
        print("1 Алгебраїчне рівняння")
        print("2 Трансцендентне рівняння")

        choice = input("Оберіть варіант: ").strip()

        match choice:
            case "1":
                root_alg, res_alg, hist_alg = plot_and_bisect(f_alg, a=-2, b=-1, xtol=0.01, title="Алгебраїчне")
                print("А")
                print(f"Корінь x* ≈ {root_alg:.2f}")
                print(f"Перевірка f(x*) = {f_alg(root_alg):.12f}")
                print(f"Кількість ітерацій: {res_alg.iterations}\n")
                return f_alg, root_alg, hist_alg, "Алгебраїчне"

            case "2":
                root_trans, res_trans, hist_trans = plot_and_bisect(f_trans, a=1, b=2, xtol=0.01,
                                                                    title="Трансцендентне")
                print("Транс")
                print(f"Корінь x* ≈ {root_trans:.5f}")
                print(f"Перевірка f(x*) = {f_trans(root_trans):.8f}")
                print(f"Кількість ітерацій: {res_trans.iterations}\n")
                return f_trans, root_trans, hist_trans, "Трансцендентне"

            case _:
                print("Некоректний вибір! Введіть 1 або 2.")


if __name__ == "__main__":
    run_bisection()