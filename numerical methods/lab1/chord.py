"""
chord.py
========
👤 СТЕПАН: Метод хорд (метод пропорційних частин / Regula Falsi)

Принцип методу:
Замість поділу відрізка навпіл, точки (a, f(a)) та (b, f(b)) сполучаються прямою (хордою).
Наближення кореня шукається як точка перетину цієї хорди з віссю Ox:
    x = a - f(a) * (b - a) / (f(b) - f(a))
"""

def calc(f, d2f, a, b, eps=0.001):
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
    history = []

    while True:
        iterations += 1

        # Ітераційна формула
        x_curr = x_prev - f(x_prev) * (fixed - x_prev) / (f(fixed) - f(x_prev))

        # Записуємо точку (x, f(x)) в історію
        history.append((x_curr, f(x_curr)))

        # Критерій зупинки
        if abs(x_curr - x_prev) < eps:
            break

        x_prev = x_curr

    return x_curr, iterations, history


def run_chord(f, d2f, a, b, eps=0.001):
    """Головна функція запуску методу хорд для виклика з main.py"""
    try:
        root, iters, history = calc(f, d2f, a, b, eps=eps)
        print("Хорди")
        print(f"Корінь x* ≈ {root:.5f}")
        print(f"Перевірка f(x*) = {f(root):.12f}")
        print(f"Кількість ітерацій: {iters}\n")
        return root, history
    except Exception as ex:
        print(f"Помилка в Хордах: {ex}\n")
        return None, []