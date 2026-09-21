"""
bisection.py
============
👤 ТАРАС: Метод дихотомії (половинного ділення)

Принцип методу:
Послідовний поділ відрізка [a, b] навпіл. На кожному кроці обирається та
половина, на кінцях якої функція набуває значень протилежних знаків (f(a) * f(b) < 0).
"""

from scipy.optimize import bisect
from equations import f_alg, f_trans

def run_bisection():
    root, result = bisect(f_alg, a=-2, b=-1, xtol=0.01, full_output=True)

    root1 = bisect(f_trans, 1, 2, xtol=1e-5)
    print(f"Знайдений дійсний корінь: x ≈ {root1:.5f}")

    print(f"Корінь x* ≈ {root:.2f}")
    print(f"Перевірка f(x*) = {f_alg(root):.12f}")
    print(f"Кількість ітерацій: {result.iterations}")
