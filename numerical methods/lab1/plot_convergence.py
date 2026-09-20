import numpy as np
import matplotlib.pyplot as plt

#РІВНЯННЯ
# Алгебраїчне
f_alg = lambda x: 8 * x ** 4 - 8 * x ** 2 + 32 * x + 1
df_alg = lambda x: 32 * x ** 3 - 16 * x + 32
phi_alg = lambda x: (-8 * x ** 4 + 8 * x ** 2 - 1) / 32

# Трансцендентне
f_trans = lambda x: 2 - np.log10(x) - x
df_trans = lambda x: -1 / (x * np.log(10)) - 1
phi_trans = lambda x: 2 - np.log10(x)

EPS = 0.001


# СИМУЛЯТОРИ МЕТОДІВ
def track_bisection(f, a, b):
    errors = []
    while (b - a) >= EPS:
        c = (a + b) / 2
        errors.append(abs(f(c)))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return errors


def track_chord(f, a, b, fixed_end):
    errors = []
    x_prev = b if fixed_end == a else a
    while True:
        x_curr = x_prev - f(x_prev) * (fixed_end - x_prev) / (f(fixed_end) - f(x_prev))
        err = abs(f(x_curr))
        errors.append(err)
        if abs(x_curr - x_prev) < EPS: break
        x_prev = x_curr
    return errors


def track_newton(f, df, x0):
    errors = []
    x_prev = x0
    while True:
        x_curr = x_prev - f(x_prev) / df(x_prev)
        err = abs(f(x_curr))
        errors.append(err)
        if abs(x_curr - x_prev) < EPS: break
        x_prev = x_curr
    return errors


def track_mpi(f, phi, x0):
    errors = []
    x_prev = x0
    for _ in range(20):  # Запобіжник
        x_curr = phi(x_prev)
        err = abs(f(x_curr))
        errors.append(err)
        if abs(x_curr - x_prev) < EPS: break
        x_prev = x_curr
    return errors


# ЗБІР ДАНИХ
# Алгебраїчне (відрізок [-0.1, 0])
err_alg_bis = track_bisection(f_alg, -0.1, 0)
err_alg_cho = track_chord(f_alg, -0.1, 0, fixed_end=-0.1)
err_alg_newt = track_newton(f_alg, df_alg, x0=-0.1)
err_alg_mpi = track_mpi(f_alg, phi_alg, x0=-0.05)

# Трансцендентне (відрізок [1, 2])
err_tr_bis = track_bisection(f_trans, 1, 2)
err_tr_cho = track_chord(f_trans, 1, 2, fixed_end=1)
err_tr_newt = track_newton(f_trans, df_trans, x0=1)
err_tr_mpi = track_mpi(f_trans, phi_trans, x0=1.5)

# ПОБУДОВА ГРАФІКІВ
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


def setup_axis(ax, title, errors_dict):
    markers = ['o', 's', 'd', '^']
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

    for (name, errs), m, c in zip(errors_dict.items(), markers, colors):
        iters = np.arange(1, len(errs) + 1)
        ax.plot(iters, errs, marker=m, color=c, label=f"{name} ({len(errs)} іт.)")

    ax.axhline(EPS, color='r', linestyle='--', label=f"eps = {EPS}")
    ax.set_yscale('log')  # Логарифмічна шкала похибки
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Номер ітерації (k)', fontsize=12)
    ax.set_ylabel('Оцінка похибки |f(x)|', fontsize=12)
    ax.grid(True, which="both", ls="--", alpha=0.5)
    ax.legend(fontsize=11)


setup_axis(ax1, "Збіжність для алгебраїчного рівняння", {
    "Метод дихотомії": err_alg_bis,
    "Метод хорд": err_alg_cho,
    "Метод Ньютона": err_alg_newt,
    "Метод МПІ": err_alg_mpi
})

setup_axis(ax2, "Збіжність для трансцендентного рівняння", {
    "Метод дихотомії": err_tr_bis,
    "Метод хорд": err_tr_cho,
    "Метод Ньютона": err_tr_newt,
    "Метод МПІ": err_tr_mpi
})

plt.tight_layout()
plt.savefig("convergence_plot.png", dpi=300)
print("Графік успішно збережено у файл convergence_plot.png!")