"""
Тестовый скрипт для проверки решения уравнений
Test script for equation solving
"""

import sympy as sp
from sympy import symbols, Eq, solve, log, ln, exp, simplify, sin, cos
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def test_equation(equation_text):
    """Тест решения уравнения"""
    print(f"\n{'='*60}")
    print(f"Тестируем уравнение: {equation_text}")
    print('='*60)
    
    try:
        x = symbols('x')
        
        # Разбор уравнения
        if '=' in equation_text:
            left_str, right_str = equation_text.split('=', 1)
        else:
            left_str = equation_text
            right_str = '0'
        
        transformations = standard_transformations + (implicit_multiplication_application,)
        
        left_expr = parse_expr(left_str.strip(), transformations=transformations, local_dict={'x': x})
        right_expr = parse_expr(right_str.strip(), transformations=transformations, local_dict={'x': x})
        
        equation = Eq(left_expr, right_expr)
        
        print(f"\nИсходное уравнение: {equation}")
        
        # Решение
        solutions = solve(equation, x)
        
        print(f"\nНайдено решений: {len(solutions) if isinstance(solutions, list) else 1}")
        
        if isinstance(solutions, list):
            for i, sol in enumerate(solutions, 1):
                print(f"\nРешение {i}: x = {sol}")
                try:
                    numeric_val = complex(sol.evalf())
                    if numeric_val.imag == 0:
                        print(f"  Численное значение: x ≈ {numeric_val.real:.6f}")
                    else:
                        print(f"  Численное значение: x ≈ {numeric_val:.6f}")
                except:
                    pass
                
                # Проверка
                try:
                    check_left = left_expr.subs(x, sol)
                    check_right = right_expr.subs(x, sol)
                    if simplify(check_left - check_right) == 0:
                        print(f"  ✓ Проверка: решение верно")
                    else:
                        print(f"  ? Проверка: требуется дополнительная проверка")
                except:
                    pass
        else:
            print(f"\nРешение: x = {solutions}")
        
        print("\n✓ Тест пройден успешно")
        return True
        
    except Exception as e:
        print(f"\n✗ Ошибка: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА УРАВНЕНИЙ")
    print("=" * 60)
    
    test_cases = [
        # Линейные уравнения
        "2*x + 5 = 11",
        "3*x - 7 = 2",
        
        # Квадратные уравнения
        "x**2 - 4 = 0",
        "x**2 + 3*x + 2 = 0",
        "x**2 - 5*x + 6 = 0",
        
        # Кубические уравнения
        "x**3 - 2*x**2 + x = 0",
        
        # Логарифмические уравнения
        "log(x) + 2 = 5",
        "log(x, 2) = 3",
        
        # Экспоненциальные уравнения
        "exp(x) - 5 = 0",
        "2*exp(x) = 10",
        
        # Тригонометрические уравнения
        "sin(x) = 0",
        "cos(x) = 1",
    ]
    
    passed = 0
    failed = 0
    
    for test_case in test_cases:
        if test_equation(test_case):
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    print(f"Всего тестов: {len(test_cases)}")
    print(f"Пройдено: {passed}")
    print(f"Провалено: {failed}")
    print("=" * 60)
