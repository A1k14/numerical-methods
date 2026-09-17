import math

<<<<<<< HEAD
# АЛГЕБРАЇЧНЕ РІВНЯННЯ: 8x^4 - 8x^2 + 32x + 1 = 0
# Корінь лежить на відрізку [-1, 0]

f_alg = lambda x: 8 * x**4 - 8 * x**2 + 32 * x + 1

df_alg = lambda x: 32 * x**3 - 16 * x + 32

d2f_alg = lambda x: 96 * x**2 - 16

phi_alg = lambda x: (-8 * x**4 + 8 * x**2 - 1) / 32
=======
# TODO: переписати возврат на лямбди для удобства Тарас подивись на це !! дивись в мене в файлі
>>>>>>> dc96c4a0dcdadaea5aadd9d14cd02d373e97af89


# ТРАНСЦЕНДЕНТНЕ РІВНЯННЯ: 2 - lg(x) - x = 0
# Корінь лежить на відрізку [1, 2]

<<<<<<< HEAD
f_trans = lambda x: 2 - math.log10(x) - x

df_trans = lambda x: -1 / (x * math.log(10)) - 1.0

d2f_trans = lambda x: 1 / (x**2 * math.log(10))

phi_trans = lambda x: 2 - math.log10(x)
=======
def f_alg(x: float) -> float:
    return 8 * x**4 - 8 * x**2 + 32 * x + 1

def df_alg(x: float) -> float:
    return 32 * x**3 - 16 * x + 32

def d2f_alg(x: float) -> float:
    # Виправлено похідну
    return 96 * x**2 - 16

def phi_alg(x: float) -> float:
    # Функція для методу простої ітерації: x = phi(x)
    return (-8 * x**4 + 8 * x**2 - 1) / 32


# ТРАНСЦЕНДЕНТНЕ РІВНЯННЯ: 2 - lg(x) - x = 0
# Корінь лежить на відрізку [1, 2]

def f_trans(x: float) -> float:
    """ f(x) = 2 - lgx - x"""
    return 2 - math.log10(x) - x

def df_trans(x: float) -> float:
    """Перша похідна f'(x) = -1/(x*ln(10)) - 1 """
    return -1 / (x * math.log(10)) - 1.0

def d2f_trans(x: float) -> float:
    """Друга похідна f''(x) = 1/(x^2 * ln(10)) """
    return 1 / (x ** 2 * math.log(10))

def phi_trans(x: float) -> float:
    """ Функція для методу простої ітерації: x = 2 - lg(x) """
    return 2 - math.log10(x)
>>>>>>> 8f53a654236a92366a5ac6b137a4912e838c619b
