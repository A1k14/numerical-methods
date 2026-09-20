"""
main.py
=======
Головна точка входу.
  1. Метод дихотомії    (bisection.py)
  2. Метод хорд         (chord.py)
  3. Метод Ньютона      (newton.py)
  4. Проста ітерація    (simple_iteration.py)


"""

EPSILON = 0.001  # Задана точність


def main():
    print("\n\nПрогрма для запуска потрібного режиму виберіть його зі списку на напишіть потрібний номер")
    print("\n  1. Метод дихотомії    (bisection.py)\n  2. Метод хорд         (chord.py)\n  3. Метод Ньютона      (newton.py)\n  4. Проста ітерація    (simple_iteration.py)\n\n  0. вихід\n")


    while True:
        print("\n\nПрогрма для запуска потрібного режиму виберіть його зі списку на напишіть потрібний номер")
        print(
            "\n  1. Метод дихотомії    (bisection.py)\n  2. Метод хорд         (chord.py)\n  3. Метод Ньютона      (newton.py)\n  4. Проста ітерація    (simple_iteration.py)\n\n  0. вихід\n")
        numberr = input("---->")
        match numberr:
            case '1':
                pass #TODO вставте свої точки входа сюда з імпортом
            case '2':
                import chord
                do_test = input("\n\nвикликати функцію перевірки ? (t/f)\n--->")
                if do_test == 'f':
                    print(chord.run_first_func())
                else:
                    print(chord.run_with_test())
                _ = input()
            case '3':
                import newton
                do_test = input("\n\nвикликати функцію перевірки ? (t/f)\n--->")
                if do_test == 'f':print(newton.run_first_func())
                else: print(newton.run_with_test())
                _ = input()
            case '4':
                pass #TODO вставте свої точки входа сюда з імпортом
            case _:
                print("байбай")
                return 0

if __name__ == "__main__":
    main()
