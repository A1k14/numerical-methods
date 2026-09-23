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

from equations import f_alg, df_alg, d2f_alg, phi_alg
from equations import f_trans, df_trans, d2f_trans, phi_trans

from bisection import run_bisection
from newton import run_newton
from chord import run_chord
from simple_iteration import run_simple_iteration


def main():
    print("Оберіть рівняння для розрахунку 4 методами:")

    # 1. Запускаємо меню, яке повертає обране рівняння
    f, root_bisect, hist_bisect, title = run_bisection()

    # Розподіл параметрів залежно від вибору
    if title == "Алгебраїчне":
        df, d2f, phi = df_alg, d2f_alg, phi_alg
        a, b = -2, -1
        x0_newton = -2
        x0_mpi = -1.5
    else:
        df, d2f, phi = df_trans, d2f_trans, phi_trans
        a, b = 1, 2
        x0_newton = 2
        x0_mpi = 1.5

    # 2. Запускаємо інші 3 методи з відповідних файлів
    root_newton, hist_newton = run_newton(f, df, d2f, a, b)
    root_chord, hist_chord = run_chord(f, d2f, a, b)
    root_mpi, hist_mpi = run_simple_iteration(f, phi, x0_mpi)

    # 3. Побудова графіків
    plt.figure(figsize=(9, 5))

    methods = {
        "Ділення навпіл": (hist_bisect, 'bo-'),
        "Метод хорд": (hist_chord, 'rs--'),
        "Метод Ньютона": (hist_newton, 'g^-.'),
        "Проста ітерація": (hist_mpi, 'md:')
    }

    for name, (history, fmt) in methods.items():
        if not history:  # Пропускаємо, якщо метод впав з помилкою
            continue

        fc_vals = [fc for _, fc in history]
        n_vals = np.arange(1, len(fc_vals) + 1)

        # Уникаємо логарифма від чистого нуля, якщо точність ідеальна
        log_res = [np.log10(abs(fc)) if abs(fc) > 1e-16 else -16 for fc in fc_vals]

        plt.plot(n_vals, log_res, fmt, label=f"{name} ({len(n_vals)} іт.)")

    plt.axhline(-3, color='r', linestyle='--', label="eps = 0.001 (10^-3)")

    plt.title(f"Порівняння 4 методів | {title}")
    plt.xlabel('Номер ітерації (n)')
    plt.ylabel(r'$\log_{10}|f(x_n)|$')
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()