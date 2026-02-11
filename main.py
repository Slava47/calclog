"""
Калькулятор для решения логарифмических, обычных и нелинейных уравнений
Calculator for solving logarithmic, regular, and nonlinear equations
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
import sympy as sp
from sympy import symbols, Eq, solve, log, ln, exp, simplify, expand
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import traceback


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # Основной контейнер
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Заголовок
        title = Label(
            text='Калькулятор Уравнений',
            size_hint_y=None,
            height=dp(50),
            font_size=dp(24),
            color=(0.2, 0.2, 0.2, 1),
            bold=True
        )
        main_layout.add_widget(title)
        
        # Инструкция
        instruction = Label(
            text='Введите уравнение (используйте x как переменную)\nПримеры: x**2 - 4 = 0, log(x) + 2 = 5, sin(x) = 0.5',
            size_hint_y=None,
            height=dp(60),
            font_size=dp(14),
            color=(0.3, 0.3, 0.3, 1)
        )
        main_layout.add_widget(instruction)
        
        # Поле ввода уравнения
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))
        
        input_label = Label(
            text='Уравнение:',
            size_hint_x=0.25,
            font_size=dp(16),
            color=(0.2, 0.2, 0.2, 1)
        )
        input_layout.add_widget(input_label)
        
        self.equation_input = TextInput(
            multiline=False,
            font_size=dp(16),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[dp(10), dp(10)]
        )
        input_layout.add_widget(self.equation_input)
        
        main_layout.add_widget(input_layout)
        
        # Кнопки
        button_layout = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(10))
        
        solve_btn = Button(
            text='Решить',
            font_size=dp(16),
            background_color=(0.2, 0.6, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        solve_btn.bind(on_press=self.solve_equation)
        button_layout.add_widget(solve_btn)
        
        clear_btn = Button(
            text='Очистить',
            font_size=dp(16),
            background_color=(0.6, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        clear_btn.bind(on_press=self.clear_all)
        button_layout.add_widget(clear_btn)
        
        example_btn = Button(
            text='Пример',
            font_size=dp(16),
            background_color=(0.2, 0.4, 0.6, 1),
            color=(1, 1, 1, 1)
        )
        example_btn.bind(on_press=self.load_example)
        button_layout.add_widget(example_btn)
        
        main_layout.add_widget(button_layout)
        
        # Область вывода решения
        solution_label = Label(
            text='Решение:',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(18),
            color=(0.2, 0.2, 0.2, 1),
            bold=True
        )
        main_layout.add_widget(solution_label)
        
        # ScrollView для решения
        scroll_view = ScrollView(size_hint=(1, 1))
        
        self.solution_output = Label(
            text='',
            size_hint_y=None,
            font_size=dp(14),
            color=(0, 0, 0, 1),
            markup=True,
            padding=(dp(10), dp(10))
        )
        self.solution_output.bind(texture_size=self.solution_output.setter('size'))
        
        scroll_view.add_widget(self.solution_output)
        main_layout.add_widget(scroll_view)
        
        return main_layout
    
    def solve_equation(self, instance):
        """Решение уравнения с подробным выводом"""
        equation_text = self.equation_input.text.strip()
        
        if not equation_text:
            self.solution_output.text = '[color=#FF0000]Ошибка: Введите уравнение[/color]'
            return
        
        try:
            x = symbols('x')
            
            # Разбор уравнения
            if '=' in equation_text:
                left_str, right_str = equation_text.split('=', 1)
            else:
                left_str = equation_text
                right_str = '0'
            
            # Парсинг с поддержкой неявного умножения
            transformations = standard_transformations + (implicit_multiplication_application,)
            
            left_expr = parse_expr(left_str.strip(), transformations=transformations, local_dict={'x': x})
            right_expr = parse_expr(right_str.strip(), transformations=transformations, local_dict={'x': x})
            
            # Формирование уравнения
            equation = Eq(left_expr, right_expr)
            
            # Начало решения
            solution_steps = []
            solution_steps.append('[b]Исходное уравнение:[/b]')
            solution_steps.append(f'{sp.latex(equation)}')
            solution_steps.append('')
            
            # Приведение к стандартному виду
            standard_form = left_expr - right_expr
            solution_steps.append('[b]Шаг 1: Приведение к стандартному виду[/b]')
            solution_steps.append(f'{sp.latex(standard_form)} = 0')
            solution_steps.append('')
            
            # Упрощение
            simplified = simplify(standard_form)
            if simplified != standard_form:
                solution_steps.append('[b]Шаг 2: Упрощение[/b]')
                solution_steps.append(f'{sp.latex(simplified)} = 0')
                solution_steps.append('')
            
            # Решение уравнения
            solution_steps.append('[b]Шаг 3: Решение уравнения[/b]')
            solutions = solve(equation, x)
            
            if not solutions:
                solution_steps.append('[color=#FF6600]Уравнение не имеет действительных решений[/color]')
            elif isinstance(solutions, list):
                solution_steps.append(f'Найдено решений: {len(solutions)}')
                solution_steps.append('')
                for i, sol in enumerate(solutions, 1):
                    solution_steps.append(f'[b]Решение {i}:[/b]')
                    solution_steps.append(f'x = {sp.latex(sol)}')
                    
                    # Численное значение если возможно
                    try:
                        numeric_val = complex(sol.evalf())
                        if numeric_val.imag == 0:
                            solution_steps.append(f'x ≈ {numeric_val.real:.6f}')
                        else:
                            solution_steps.append(f'x ≈ {numeric_val:.6f}')
                    except:
                        pass
                    solution_steps.append('')
            else:
                solution_steps.append(f'x = {sp.latex(solutions)}')
            
            # Проверка решений
            if solutions and isinstance(solutions, list):
                solution_steps.append('[b]Шаг 4: Проверка решений[/b]')
                for i, sol in enumerate(solutions, 1):
                    try:
                        check_left = left_expr.subs(x, sol)
                        check_right = right_expr.subs(x, sol)
                        solution_steps.append(f'Проверка решения {i}:')
                        solution_steps.append(f'Левая часть: {sp.latex(check_left)}')
                        solution_steps.append(f'Правая часть: {sp.latex(check_right)}')
                        
                        if simplify(check_left - check_right) == 0:
                            solution_steps.append('[color=#00AA00]Решение верно[/color]')
                        else:
                            solution_steps.append('[color=#FF6600]Требуется дополнительная проверка[/color]')
                        solution_steps.append('')
                    except:
                        pass
            
            self.solution_output.text = '\n'.join(solution_steps)
            
        except Exception as e:
            error_msg = f'[color=#FF0000]Ошибка при решении:[/color]\n{str(e)}\n\n'
            error_msg += '[color=#666666]Проверьте правильность ввода уравнения[/color]'
            self.solution_output.text = error_msg
    
    def clear_all(self, instance):
        """Очистка всех полей"""
        self.equation_input.text = ''
        self.solution_output.text = ''
    
    def load_example(self, instance):
        """Загрузка примера уравнения"""
        examples = [
            'x**2 - 4 = 0',
            'log(x) + 2 = 5',
            'log(x, 2) = 3',
            'x**3 - 2*x**2 + x = 0',
            'exp(x) - 5 = 0',
            'sin(x) = 0.5',
            'x**2 + 3*x + 2 = 0'
        ]
        import random
        self.equation_input.text = random.choice(examples)


if __name__ == '__main__':
    CalculatorApp().run()
