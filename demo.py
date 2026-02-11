#!/usr/bin/env python3
"""
Демонстрационный скрипт решения уравнений без GUI
Demo script for equation solving without GUI
"""

import sympy as sp
from sympy import symbols, Eq, solve, log, exp, simplify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def solve_equation_detailed(equation_text):
    """
    Решение уравнения с подробным выводом
    Solve equation with detailed output
    """
    print(f"\n{'='*70}")
    print(f"Решение уравнения / Solving equation: {equation_text}")
    print('='*70)
    
    try:
        x = symbols('x')
        
        # Разбор уравнения / Parse equation
        if '=' in equation_text:
            left_str, right_str = equation_text.split('=', 1)
        else:
            left_str = equation_text
            right_str = '0'
        
        # Парсинг с поддержкой неявного умножения
        # Parsing with implicit multiplication support
        transformations = standard_transformations + (implicit_multiplication_application,)
        
        left_expr = parse_expr(left_str.strip(), transformations=transformations, local_dict={'x': x})
        right_expr = parse_expr(right_str.strip(), transformations=transformations, local_dict={'x': x})
        
        # Формирование уравнения / Create equation
        equation = Eq(left_expr, right_expr)
        
        print(f"\nИсходное уравнение / Original equation:")
        print(f"  {equation}")
        
        # Приведение к стандартному виду / Convert to standard form
        standard_form = left_expr - right_expr
        print(f"\nСтандартный вид / Standard form:")
        print(f"  {standard_form} = 0")
        
        # Упрощение / Simplification
        simplified = simplify(standard_form)
        if simplified != standard_form:
            print(f"\nУпрощенный вид / Simplified form:")
            print(f"  {simplified} = 0")
        
        # Решение уравнения / Solve equation
        print(f"\nРешение / Solution:")
        solutions = solve(equation, x)
        
        if not solutions:
            print("  Уравнение не имеет действительных решений")
            print("  No real solutions")
        elif isinstance(solutions, list):
            print(f"  Найдено решений: {len(solutions)} / Found {len(solutions)} solution(s)")
            print()
            
            for i, sol in enumerate(solutions, 1):
                print(f"  Решение {i} / Solution {i}:")
                print(f"    x = {sol}")
                
                # Численное значение / Numerical value
                try:
                    numeric_val = complex(sol.evalf())
                    if numeric_val.imag == 0:
                        print(f"    x ≈ {numeric_val.real:.8f}")
                    else:
                        print(f"    x ≈ {numeric_val:.8f}")
                except:
                    pass
                
                # Проверка / Verification
                try:
                    check_left = left_expr.subs(x, sol)
                    check_right = right_expr.subs(x, sol)
                    if simplify(check_left - check_right) == 0:
                        print(f"    ✓ Проверка: решение верно / Verification: correct")
                    else:
                        print(f"    ? Проверка: требуется дополнительная проверка")
                        print(f"      ? Verification: additional check needed")
                except:
                    pass
                print()
        else:
            print(f"  x = {solutions}")
        
        print("="*70)
        return True
        
    except Exception as e:
        print(f"\n✗ Ошибка / Error: {str(e)}")
        print("="*70)
        return False


if __name__ == '__main__':
    print("\n" + "="*70)
    print("КАЛЬКУЛЯТОР УРАВНЕНИЙ / EQUATION CALCULATOR")
    print("Демонстрация / Demo")
    print("="*70)
    
    examples = [
        ("Линейное / Linear", "2*x + 5 = 11"),
        ("Квадратное / Quadratic", "x**2 - 4 = 0"),
        ("Полиномиальное / Polynomial", "x**3 - 2*x**2 + x = 0"),
        ("Логарифмическое / Logarithmic", "log(x) + 2 = 5"),
        ("Логарифм по основанию / Log with base", "log(x, 2) = 3"),
        ("Экспоненциальное / Exponential", "exp(x) - 5 = 0"),
        ("Сложное квадратное / Complex quadratic", "x**2 + 3*x + 2 = 0"),
    ]
    
    for category, equation in examples:
        print(f"\n[{category}]")
        solve_equation_detailed(equation)
    
    print("\n" + "="*70)
    print("Демонстрация завершена / Demo completed")
    print("="*70 + "\n")
