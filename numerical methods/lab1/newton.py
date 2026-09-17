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
    """функция запуска метода нютона за першою формулою сьомого варіанту """
    f1 = lambda x: 8 * x ** 4 - 8 * x ** 2 + 32 * x + 1
    df1 = lambda x: 32 * x ** 3 - 16 * x + 32
    d2f1 = lambda x: 96 * x ** 2 - 16
    a1, b1 = -0.1, 0
    try:
        root1, iters1 = calc(f1, df1, d2f1, a1, b1, eps=0.001)
        print(f"Корінь: {root1:.5f} (знайдено за {iters1} ітерацій)")
        return root1, iters1
    except Exception as ex: print(ex)

def run_with_test():
    """для теста правильності написання перевірямо з еталоном"""
    from scipy.optimize import newton

    f1 = lambda x: 8 * x ** 4 - 8 * x ** 2 + 32 * x + 1

    scipy_root1 = newton(f1, x0=-0.5)
    print(f"Корінь через SciPy: {scipy_root1:.5f}")
    print(f"Різниця між методами: {abs(run_first_func()[0] - scipy_root1)}")

if __name__ == '__main__':
    run_with_test()