"""
bisection.py
============
👤 ТАРАС: Метод дихотомії (половинного ділення)

Принцип методу:
Послідовний поділ відрізка [a, b] навпіл. На кожному кроці обирається та
половина, на кінцях якої функція набуває значень протилежних знаків (f(a) * f(b) < 0).
"""

from scipy.optimize import bisect
from equations import f_alg

root, result = bisect(f_alg, a=-1, b=0, xtol=0.01, full_output=True)

print(f"Корінь x* ≈ {root:.2f}")
print(f"Перевірка f(x*) = {f_alg(root):.12f}")
print(f"Кількість ітерацій: {result.iterations}")