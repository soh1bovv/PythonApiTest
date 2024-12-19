# калькулятор с функциями деления и сложения
class Calculator:
        def divide(self, x: [int, float], y:[int, float]) -> int | float:
            if y == 0:
                raise ValueError("Cannot divide by zero") # ошибка деления на ноль
            return x / y

        def add(self, x: [int, float], y:[int, float]) -> int | float:
            if y == 0:
                raise ValueError("Cannot divide by zero") # ошибка деления на ноль
            return x + y


