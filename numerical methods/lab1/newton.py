"""
newton.py
=========
Метод Ньютона (метод дотичних)

Принцип методу:
У точці поточного наближення x_k проводиться дотична до графіка функції y = f(x).
Наступне наближення x_{k+1} шукається як точка перетину цієї дотичної з віссю Ox:
    x_{k+1} = x_k - f(x_k) / f'(x_k)

    Загаєвський
"""
from equations import f_alg, df_alg, d2f_alg


# TODO використовувати лямбди з equations.py

def calc(f, df, d2f, a, b, eps=0.001) :
    """
    фнкція для знаходженя кореня нелінійного рівняння методом Ньютона.
    :param f: Цільова функція
    :param df: Перша
    :param d2f: Друга похідна
    :param a: ліва
    :param b: права межа відрізка ізоляції
    :param eps:  точность
    :return: корінь рівняння та кількість ітерацій
    """
    if f(a) * f(b) > 0: #п еревірка знаків функції на кінцях відрізка теорема БольцаноКоші
        raise ValueError(f"функція не змінює знак на кінцях відрізка [{a}, {b}]. Корінь не ізольовано.")


    if f(a) * d2f(a) > 0: # Вибір початкового наближення x0 де f(x) * f''(x) > 0
        x_prev = a
    elif f(b) * d2f(b) > 0:
        x_prev = b
    else:
        raise ValueError("Умова збіжності f(x)*f''(x) > 0 на кінцях відрізка не виконується.")
    iterations = 0

    while True:
        iterations += 1

        # щитаємо наступне наближення
        x_curr = x_prev - (f(x_prev) / df(x_prev))
        if abs(x_curr - x_prev) < eps:# Критерій зупинки
            break

        x_prev = x_curr

    return x_curr, iterations

def run_first_func():

    a1, b1 = -2, -1
    try:
        root1, iters1 = calc(f_alg, df_alg, d2f_alg, a1, b1, eps=0.001)
        print(f"Корінь: {root1:.5f} (знайдено за {iters1} ітерацій)")
        return root1, iters1
    except Exception as ex: print(ex)

def run_with_test():
    from scipy.optimize import newton

    scipy_root1 = newton(f_alg, x0=-1.5)
    print(f"Корінь через SciPy: {scipy_root1:.5f}")

if __name__ == '__main__':
    run_with_test()