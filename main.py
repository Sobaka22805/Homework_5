print("Homework_5")

class Calculator:
    def convert_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            print("Помилка: неможливо конвертувати в тип float.")
            return None
        finally:
            print("Конвертація типу даних завершена.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Помилка: ділення на нуль неможливе.")
            return None
        finally:
            print("Операція ділення завершена.")
