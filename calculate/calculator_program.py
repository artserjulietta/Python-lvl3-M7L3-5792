def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Ошибка: Введите числа."

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: Деление на ноль."
    else:
        return "Ошибка: Неизвестная операция."

def main():
    print("Простой калькулятор. Введите два числа и выберите операцию.")
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /): ")
    result = calculate(num1)
