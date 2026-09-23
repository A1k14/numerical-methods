"""
simple_iteration.py
===================
👤 ДАНІК: Метод простої ітерації
"""


def calc(f, phi_func, x0: float, eps: float = 0.001):
    x_prev = x0
    iters = 0
    max_iters = 1000
    history = []

    while iters < max_iters:
        x_next = phi_func(x_prev)
        iters += 1

        # Записуємо точку (x, f(x)) в історію
        history.append((x_next, f(x_next)))

        if abs(x_next - x_prev) < eps:
            return x_next, iters, history

        x_prev = x_next

    raise RuntimeError("Метод простої ітерації не зійшовся за 1000 ітерацій")


def run_simple_iteration(f, phi, x0, eps=0.001):
    """Головна функція запуску МПІ для виклика з main.py"""
    try:
        root, iters, history = calc(f, phi, x0, eps=eps)
        print("МПІ")
        print(f"Корінь x* ≈ {root:.5f}")
        print(f"Перевірка f(x*) = {f(root):.12f}")
        print(f"Кількість ітерацій: {iters}\n")
        return root, history
    except Exception as ex:
        print(f"Помилка в МПІ: {ex}\n")
        return None, []