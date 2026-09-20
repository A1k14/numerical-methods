import matplotlib.pyplot as plt
import numpy as np

from equations import f_alg


def check_gua_theorem(coeffs):

    n = len(coeffs) - 1
    all_satisfied = True


    for k in range(1, n):
        a_k = coeffs[k]
        a_prev = coeffs[k - 1]
        a_next = coeffs[k + 1]

        lhs = a_k**2
        rhs = a_prev * a_next
        is_valid = lhs > rhs

        if not is_valid:
            all_satisfied = False

        print(
            f"{k:<3} | {a_k:<5} | {a_prev:<8} | {a_next:<8} | {lhs:<8} | {rhs:<15} | {is_valid}"
        )

    print("-" * 85)
    if all_satisfied:
        print(
            "умова Гюа виконується для всіх k."
        )
    else:
        print(
            "Умова не виконується. Рівняння має принаймні одну пару комплексних коренів."
        )


def count_sign_changes(coefficients):
    """Рахує кількість змін знаків у послідовності коефіцієнтів, ігноруючи нулі."""
    # Відфільтровуємо нульові коефіцієнти
    nonzero_coeffs = [c for c in coefficients if c != 0]

    changes = 0
    for i in range(len(nonzero_coeffs) - 1):
        # Якщо знаки сусідніх елементів різні, добуток буде від'ємним
        if nonzero_coeffs[i] * nonzero_coeffs[i + 1] < 0:
            changes += 1
    return changes


def descartes_rule_of_signs(coefficients):

    positive_changes = count_sign_changes(coefficients)
    n = len(coefficients)
    negative_coeffs = []
    for i, c in enumerate(coefficients):
        degree = n - 1 - i
        if degree % 2 != 0:
            negative_coeffs.append(-c)
        else:
            negative_coeffs.append(c)

    negative_changes = count_sign_changes(negative_coeffs)

    pos_possibilities = [positive_changes - 2 * k for k in range(positive_changes // 2 + 1)]
    neg_possibilities = [negative_changes - 2 * k for k in range(negative_changes // 2 + 1)]

    print(f"Можлива кількість додатних коренів: {pos_possibilities}")
    print(f"Можлива кількість від'ємних коренів: {neg_possibilities}")


def find_root_ring_bounds(coefficients):
    if coefficients[0] == 0 or coefficients[-1] == 0:
        raise ValueError("Старший коефіцієнт a_n та вільний член a_0 не повинні дорівнювати 0.")

    abs_coefs = [abs(c) for c in coefficients]

    abs_an = abs_coefs[0]
    abs_a0 = abs_coefs[-1]

    a = max(abs_coefs[1:])

    b = max(abs_coefs[:-1])

    lower_bound = abs_a0 / (abs_a0 + b)

    upper_bound = 1 + (a / abs_an)

    return lower_bound, upper_bound




coeffs = [8, 0, -8, 32, 1]
check_gua_theorem(coeffs)
descartes_rule_of_signs(coeffs)

r_min, r_max = find_root_ring_bounds(coeffs)

print("--- Результат локалізації за теоремою ---")
print(f"Всі корені (дійсні та комплексні) за модулем задовольняють нерівність:")
print(f"{r_min:.4f} <= |x| <= {r_max:.4f}")



x = np.linspace(-2.5, 1.5, 500)
y = f_alg(x)

all_roots = np.roots([8, 0, -8, 32, 1])
real_roots = all_roots[np.isreal(all_roots)].real

plt.figure(figsize=(10, 6))

plt.plot(x, y, label=r"$P_4(x) = 8x^4 - 8x^2 + 32x + 1$", color="navy", linewidth=2)

plt.axvspan(-2, -1, color="green", alpha=0.2, label="Інтервал ізоляції [-2, -1]")
plt.axvspan(-1, 0, color="dodgerblue", alpha=0.2, label="Інтервал ізоляції [-1, 0]")

plt.axhline(0, color="black", linewidth=1.2)
plt.axvline(0, color="black", linewidth=1.2)

plt.scatter(
    real_roots,
    [0] * len(real_roots),
    color="red",
    s=70,
    zorder=5,
    label="Дійсні корені",
)

plt.ylim(-60, 200)
plt.ylim(-60, 200)
plt.xlim(-2.5, 1.5)
plt.xlabel("x", fontsize=11)
plt.ylabel("$P_4(x)$", fontsize=11)
plt.title(
    "Графічний метод відокремлення коренів рівняння $8x^4 - 8x^2 + 32x + 1 = 0$",
    fontsize=12,
)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=10, loc="upper right")

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect


def f(x):
    return 2 - np.log10(x) - x


root = bisect(f, 1, 2, xtol=1e-5)
print(f"Знайдений дійсний корінь: x ≈ {root:.5f}")

x = np.linspace(0.1, 3.5, 500)
y = f(x)

plt.figure(figsize=(9, 5))

plt.plot(x, y, label=r"$f(x) = 2 - \lg(x) - x$", color="navy", linewidth=2)

plt.axvspan(1, 2, color="green", alpha=0.2, label="Інтервал ізоляції [1, 2]")

plt.axhline(0, color="black", linewidth=1.2)
plt.axvline(0, color="black", linewidth=1.2)

plt.scatter(
    [root], [0], color="red", s=70, zorder=5, label=f"Корінь x ≈ {root:.4f}"
)

# Налаштування вигляду
plt.xlim(0, 3.5)
plt.ylim(-2, 2)
plt.xlabel("x", fontsize=11)
plt.ylabel("$f(x)$", fontsize=11)
plt.title(
    "Відокремлення та знаходження кореня рівняння $2 - \lg(x) - x = 0$",
    fontsize=12,
)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=10, loc="upper right")

plt.tight_layout()
plt.show()