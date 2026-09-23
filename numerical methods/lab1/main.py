"""
main.py
=======
Головна точка входу.
  1. Метод дихотомії    (bisection.py)
  2. Метод хорд         (chord.py)
  3. Метод Ньютона      (newton.py)
  4. Проста ітерація    (simple_iteration.py)


"""
import numpy as np
import matplotlib.pyplot as plt

# Імпортуємо 4 різні файли з їхніми методами
from bisection import run_bisection
from equations import f_alg, df_alg, d2f_alg
from newton import run_newton  # Файл 3


def main():
    print("Оберіть рівняння для розрахунку 4 методами:")

    f, root_bisect, hist_bisect, title = run_bisection()

    # 2. Запускаємо інші 3 методи з відповідних файлів 
    root_newton, hist_newton = run_newton(f_alg, df_alg, d2f_alg, a=-2, b=-1)
    plt.figure(figsize=(9, 5))

    methods = {
        "Ділення навпіл": (hist_bisect, 'bo-'),
        "Метод Ньютона": (hist_newton, 'g^-.'),
    }

    for name, (history, fmt) in methods.items():
        fc_vals = [fc for _, fc in history]
        n_vals = np.arange(1, len(fc_vals) + 1)
        log_res = [np.log10(abs(fc)) if abs(fc) > 0 else -16 for fc in fc_vals]

        plt.plot(n_vals, log_res, fmt, label=name)

    plt.title(f"Порівняння 4 методів | {title}")
    plt.xlabel('Номер ітерації (n)')
    plt.ylabel(r'$\log_{10}|f(x_n)|$')
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
