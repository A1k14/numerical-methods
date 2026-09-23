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


def calc(f, df, d2f, a, b, eps=0.001):
    if f(a) * f(b) > 0:
        raise ValueError(f"Функція не змінює знак на кінцях відрізка [{a}, {b}].")

    if f(a) * d2f(a) > 0:
        x_prev = a
    elif f(b) * d2f(b) > 0:
        x_prev = b
    else:
        raise ValueError("Умова збіжності f(x)*f''(x) > 0 на кінцях відрізка не виконується.")

    iterations = 0
    history = []

    while True:
        iterations += 1
        x_curr = x_prev - (f(x_prev) / df(x_prev))

        # Записуємо точку (x, f(x)) в історію
        history.append((x_curr, f(x_curr)))

        if abs(x_curr - x_prev) < eps:
            break

        x_prev = x_curr

    return x_curr, iterations, history


def run_newton(f, df, d2f, a, b, eps=0.001):
    """Головна функція запуску Ньютона для виклика з main.py"""
    try:
        root, iters, history = calc(f, df, d2f, a, b, eps=eps)
        print("Ньютон")
        print(f"Корінь x* ≈ {root:.5f}")
        print(f"Перевірка f(x*) = {f(root):.12f}")
        print(f"Кількість ітерацій: {iters}\n")
        return root, history
    except Exception as ex:
        print(f"Помилка в Ньютоні: {ex}\n")
        return None, []


def run_with_test():
    from scipy.optimize import newton

    scipy_root1 = newton(f_alg, x0=-1.5)
    print(f"Корінь через SciPy: {scipy_root1:.5f}")


if __name__ == '__main__':
    run_with_test()