import math

# АЛГЕБРАЇЧНЕ РІВНЯННЯ: 8x^4 - 8x^2 + 32x + 1 = 0
# Корінь лежить на відрізку [-1, 0]

f_alg = lambda x: 8 * x**4 - 8 * x**2 + 32 * x + 1

df_alg = lambda x: 32 * x**3 - 16 * x + 32

d2f_alg = lambda x: 96 * x**2 - 16

phi_alg = lambda x: (-8 * x**4 + 8 * x**2 - 1) / 32


# ТРАНСЦЕНДЕНТНЕ РІВНЯННЯ: 2 - lg(x) - x = 0
# Корінь лежить на відрізку [1, 2]

f_trans = lambda x: 2 - math.log10(x) - x

df_trans = lambda x: -1 / (x * math.log(10)) - 1.0

d2f_trans = lambda x: 1 / (x**2 * math.log(10))

phi_trans = lambda x: 2 - math.log10(x)
