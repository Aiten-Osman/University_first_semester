# # направи функция, която приема quantity, item и price като аргументи, 
# # # и връща речник с ключове "item" и "price", съдържащи съответните стойности

# def make_item(quantity = 1 , item = 11, price = 6.5):
    
#     total = round(quantity * price, 2)
#     return {"item": item, "price": total}
# print(make_item(3, "banana", 0.5))  



# print(make_item(2, "ябълка", 1.2))           
# print(make_item(item="мляко", price=0.95))   
# entry = make_item(price=2.5, item="шоколад") 
# print(entry)





#напишете програма, която намира лицето и периметъра на геометрична фигура , 
# като първо се въвежда вида на фигурата 1- квадрат,
# 2-правоъгълник, 3-правоъгълен триъгълник 
# # за пресмятане на лицето и периметъра да се напишат съответните функции,


# import math

# def area_square(a: float):
#     return a * a

# def perimeter_square(a: float):
#     return 4 * a

# def area_rectangle(a: float, b: float):
#     return a * b

# def perimeter_rectangle(a: float, b: float):
#     return 2 * (a + b)

# def area_right_triangle(a: float, b: float):
#     return a * b / 2

# def perimeter_right_triangle(a: float, b: float):
#     c = math.hypot(a, b)
#     return a + b + c

# choice = int(input())
   
# if choice == 1:
#     a = float(input("Въведи страна на квадрата: "))
#     print(f"Лице = {area_square(a):.2f}")
#     print(f"Периметър = {perimeter_square(a):.2f}")
# elif choice == 2:
#     a = float(input("Въведи страна a: "))
#     b = float(input("Въведи страна b: "))
#     print(f"Лице = {area_rectangle(a,b):.2f}")
#     print(f"Периметър = {perimeter_rectangle(a,b):.2f}")
# elif choice == 3:
#     a = float(input("Въведи катет a: "))
#     b = float(input("Въведи катет b: "))
#     print(f"Лице = {area_right_triangle(a,b):.2f}")
#     print(f"Периметър = {perimeter_right_triangle(a,b):.2f}")
# else:
#     print("Невалиден избор.")







# # напишете потребителска функция, която проверява дали числото е полиндром. Функцията получава като
# # аргумент число и връща 1 ако числото е палиндрон и 0 ако не е 


# def is_palindrome_number(n: int) :
#     s = str(n)
#     return 1 if s == s[::-1] else 0

# if __name__ == "__main__":
#     try:
#         num = int(input("Въведи число: "))
#     except ValueError:
#         print("Невалиден вход.")
#     else:
#         print(is_palindrome_number(num))







# програма която реализира калкулатор на цели числа. действията са събиране, 
# изваждане, умножение и деление. потребителят въвежда коя операция да бъде изпълнена и
# две цели числа. 
# реализирайте отделни функции за отделните операции.


# def add(a: int, b: int):
#     return a + b

# def sub(a: int, b: int):
#     return a - b

# def mul(a: int, b: int):
#     return a * b

# def div(a: int, b: int):
#     if b == 0:
#         print("Грешка: деление на 0.")
#         return None
#     return a / b


# operation = input("Въведи операция (+, -, *, /): ")
# if operation == "+":
#     a = int(input("Въведи първо число: "))
#     b = int(input("Въведи второ число: "))
#     print(f"Резултат: {add(a, b)}")
# elif operation == "-":
#     a = int(input("Въведи първо число: "))
#     b = int(input("Въведи второ число: "))
#     print(f"Резултат: {sub(a, b)}")
# elif operation == "*":
#     a = int(input("Въведи първо число: "))
#     b = int(input("Въведи второ число: "))
#     print(f"Резултат: {mul(a, b)}")
# elif operation == "/":
#     a = int(input("Въведи първо число: "))
#     b = int(input("Въведи второ число: "))
#     result = div(a, b)
#     if result is not None:
#         print(f"Резултат: {result}")
# else:
#     print("Невалидна операция.")    








# на функция се подават два аргумента първият е списък с числа, а вторият е число.
# променете всички елементи на списъка, със стойност по голяма от даденото число на 0.
# искаме резултатът да е като нов списък с променените стойности, без да се променя
#  оригиналния списък. листът да е поне три реда.


def replace_greater_with_zero(nums: list, threshold: float):
    new_list = []
    for v in nums:
        if v > threshold:
            new_list.append(0)
        else:
            new_list.append(v)
    return new_list

if __name__ == "__main__":
    original = []
    print("Original:", original)
    print("Modified:", replace_greater_with_zero(original, 10))




#ДОМАШНА упражнителни задачи: е- студент 


