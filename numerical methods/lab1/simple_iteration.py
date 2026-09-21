from scipy.optimize import fixed_point

def simple_iteration(phi_func, x0: float, eps: float):
    """
    Власна реалізація методу простої ітерації.
    phi_func - функція phi(x)
    x0 - початкове наближення (стартова точка)
    eps - задана точність (у нашому випадку 0.001)
    """
    x_prev = x0
    iters = 0
    max_iters = 1000

    while iters < max_iters:
        # 1. Знаходимо нове значення x
        x_next = phi_func(x_prev)
        iters += 1
        
        # 2. Перевіряємо, чи досягли ми потрібної точності
        if abs(x_next - x_prev) < eps:
            return x_next, iters
            
        # 3. Якщо ні, рухаємось далі (новий ікс стає старим)
        x_prev = x_next
        
    raise RuntimeError("Метод простої ітерації не зійшовся за 1000 ітерацій")

def check_simple_iteration_scipy(phi_func, x0: float, eps: float):
    """
    Перевірка за допомогою бібліотеки SciPy (функція fixed_point).
    """
    return fixed_point(phi_func, x0, xtol=eps)




if __name__ == "__main__":
    from equations import phi_alg, phi_trans

    EPSILON = 0.001
    
    print("АЛГЕБРАЇЧНЕ РІВНЯННЯ")
    x0_alg = -1.5  # Стартуємо посередині відрізка [-1, 0]
    
    root_alg, iters_alg = simple_iteration(phi_alg, x0_alg, EPSILON)
    scipy_root_alg = check_simple_iteration_scipy(phi_alg, x0_alg, EPSILON)
    
    print(f"Початкова точка: x0 = {x0_alg}")
    print(f"Власний код (МПІ): Корінь = {root_alg:.5f}, Ітерацій = {iters_alg}")
    print(f"Перевірка SciPy  : Корінь = {scipy_root_alg:.5f}")
    
    
    print("\nТРАНСЦЕНДЕНТНЕ РІВНЯННЯ ")
    x0_trans = 1.5  # Стартуємо посередині відрізка [1, 2]
    
    root_trans, iters_trans = simple_iteration(phi_trans, x0_trans, EPSILON)
    scipy_root_trans = check_simple_iteration_scipy(phi_trans, x0_trans, EPSILON)
    
    print(f"Початкова точка: x0 = {x0_trans}")
    print(f"Власний код (МПІ): Корінь = {root_trans:.5f}, Ітерацій = {iters_trans}")
    print(f"Перевірка SciPy  : Корінь = {scipy_root_trans:.5f}")