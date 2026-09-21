# Чете от конзолата две стойности - a и b
# Преобразува ги в тип float
# Пресмята с всички действия a+b, a-b, a*b, a/b
# Да използваме Try Except за следните случаи:
# Ако подаде невалидно число - да принтира "Invalid input. Please enter a valid number."
# Ако дели на нула - да принтира "Division by zero is not allowed."
# Ако мине успешно - да принтира "Operations completed successfully."
# Finally - End of calculations
 
try:
    a = float(input())
    b = float(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Operations completed successfully.")
finally:
    print("End of calculations")
 
 
# TASK 2
# Функция read_positive_int()
# Чете от конзолата число
# Ако не е цяло число - принтира ValueError (Invalid integer: {number})
# Ако е негативно число - exception с "Number must be positive."
# Ако е валидно число - връща числото (You entered a valid number: {number})
 
 
def read_positive_int():
    try:
        number = input("Въведи цяло число: ")
        if not isinstance(number, int):
            raise ValueError("Number must be integer.")
        if number < 0:
            raise ValueError(f"Number must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        print(f"You entered a valid number: {number}")
        return number
 
 
read_positive_int()
 
 
 
 
# TASK 3
class PasswordError(Exception):
    def __init__(self, message):
        self.message = message
 
 
def validate_password(password):
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise PasswordError("Password must contain at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        raise PasswordError("Password must contain at least one digit.")
    return True
 
 
try:
    validate_password(input("Enter password: "))
except PasswordError as e:
    print("Invalid password:", e.message)
else:
    print("Password is valid.")
 