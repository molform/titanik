# Функция сложения
def add(x, y):
    return x + y

# Функция вычитания
def subtract(x, y):
    return x - y

# Функция умножения
def multiply(x, y):
    return x * y

# Функция деления
def divide(x, y):
    if y == 0:
        return "Деление на ноль невозможно"
    return x / y

# Ввод операции и чисел
operation = input("Выберите операцию (+, -, *, /): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполнение операции
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Некорректная операция"

# Вывод результата
print("Результат:", result)