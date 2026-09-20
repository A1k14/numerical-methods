"""
chord.py
========
👤 СТЕПАН: Метод хорд (метод пропорційних частин / Regula Falsi)

Принцип методу:
Замість поділу відрізка навпіл, точки (a, f(a)) та (b, f(b)) сполучаються прямою (хордою).
Наближення кореня шукається як точка перетину цієї хорди з віссю Ox:
    x = a - f(a) * (b - a) / (f(b) - f(a))
"""

import numpy as np
from scipy.optimize import brentq
from equations import f_alg, d2f_alg, f_trans, d2f_trans


def calc(f, d2f, a, b, eps=0.001):
    """
    Знаходить корінь нелінійного рівняння методом хорд.
    Повертає: корінь, кількість ітерацій, масив похибок для побудови графіка.
    """
    if f(a) * f(b) > 0:
        raise ValueError(f"Функція не змінює знак на кінцях відрізка [{a}, {b}]. Корінь не ізольовано.")

    # Вибір нерухомого кінця за правилом: f(x) * f''(x) > 0
    if f(a) * d2f(a) > 0:
        fixed = a
        x_prev = b
    elif f(b) * d2f(b) > 0:
        fixed = b
        x_prev = a
    else:
        raise ValueError("Умова збіжності f(x)*f''(x) > 0 на кінцях відрізка не виконується.")

    iterations = 0
    errors = []

    while True:
        iterations += 1

        # Ітераційна формула
        x_curr = x_prev - f(x_prev) * (fixed - x_prev) / (f(fixed) - f(x_prev))

        # Зберігаємо поточну нев'язку (похибку) у масив
        current_error = abs(f(x_curr))
        errors.append(current_error)

        # Критерій зупинки: |x_n - x_{n-1}| < eps
        if abs(x_curr - x_prev) < eps:
            break

        x_prev = x_curr

    return x_curr, iterations, np.array(errors)


def run_first_func():
    """Запуск методу хорд для алгебраїчного рівняння"""
    a, b = -0.1, 0  # Межі ізоляції з equations.py
    try:
        root, iters, errors = calc(f_alg, d2f_alg, a, b, eps=0.001)
        res = f"\n[Метод хорд] Алгебраїчне рівняння:\n"
        res += f"Корінь: {root:.5f} (знайдено за {iters} ітерацій)\n"
        res += f"Похибки за ітераціями: {np.round(errors, 5)}"
        return res
    except Exception as ex:
        return f"Помилка в алгебраїчному рівнянні: {ex}"


def run_with_test():
    """Запуск для трансцендентного рівняння та перевірка через SciPy"""
    a, b = 1, 2  # Межі ізоляції з equations.py
    eps = 0.001

    try:
        # Власний розрахунок
        root, iters, errors = calc(f_trans, d2f_trans, a, b, eps)
        res = f"\n[Метод хорд] Трансцендентне рівняння:\n"
        res += f"Корінь (власний код): {root:.5f} (знайдено за {iters} ітерацій)\n"

        # Еталонний розрахунок через SciPy (аналог - brentq)[cite: 18, 19]
        scipy_root = brentq(f_trans, a, b, xtol=eps)
        res += f"Корінь (SciPy brentq): {scipy_root:.5f}\n"
        res += f"Різниця між методами: {abs(root - scipy_root):.7f}\n"
        res += f"Похибки за ітераціями: {np.round(errors, 5)}"

        return res
    except Exception as ex:
        return f"Помилка в трансцендентному рівнянні: {ex}"


if __name__ == '__main__':
    print(run_first_func())
    print(run_with_test())