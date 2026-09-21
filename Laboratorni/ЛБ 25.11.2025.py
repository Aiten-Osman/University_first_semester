# #напишете код на метод който приема като параметър име на тектов файл
# прочита съдържанието на файла и го връща като стринг 

# def read_text_file(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             return file.read()

#     except FileNotFoundError:
#         print(f"Грешка: Файлът '{filename}' не е намерен.")

#     except PermissionError:
#         print(f"Грешка: Нямате права за достъп до файла '{filename}'.")

#     except EOFError:
#         print(f"Грешка: Неочакван край на файла '{filename}' (EOFError).")

#     except Exception as e:
#         print(f"Неочаквана грешка: {e}")
#         text = read_text_file("example.txt")
# text = read_text_file("example.txt")
# print(text)


# Напишете програма, която прочита от конзолата цяло положително число
# и отпечатва на конзоата корен квадратен от това число. Ако числото е отрицателно или невалидно
# да се изпише invalid number и във всички случаи да изписма good bye.
# try:
#     number = int(input("Въведи цпч: "))

#     if number < 0:
#         print("invalid number")
#     else:
#         print(f"{number ** 0.5 :.2f}")  

# except ValueError:
#     print("invalid number")

# finally:
#     print("Good bye!")




# програма която чете две стойности може да са числа или текст чете оператор плюс
# минус умножение деление и се опитва 
# да изпълни операция 
# a = input("Въведи първо число a= : ")
# b = input("Въведи второ число b= : ")
# operation = input(" Избери операция(+, -, *, /): ")

# try:
#     aNum = float(a)
#     bNum = float(b)
#     isNumber = True
# except ValueError:
#     isNumber = False

# try:
#     if operation == "+":
#         if isNumber:
#             print(aNum + bNum)
#         else:
#             print("Не може да се изпълни операцията.") 

#     elif operation == "-":
#         if isNumber:
#             print(aNum - bNum)
#         else:
#             print("Не може да се изпълни операцията.")

#     elif operation == "*":
#         if isNumber:
#             print(aNum * bNum)
#         else:
#             print("Операцията '*' е възможна само число * текст.")

#     elif operation == "/":
#         if isNumber:
#             if bNum == 0:
#                 print("ZeroDivisionError")
#             else:
#                 print(aNum / bNum)
#         else:
#             print("Не може да се изпълни операцията '/'.")

#     else:
#         print("Невалиден оператор!")

# except Exception as e:
#     print("Невалидна грешка:", e)




a = input("Въведи число a= : ")
b = input("Въведи число b= : ")
operation = input("Избери оператор (+, -, *, /): ")

try:
    # Опитваме да преобразуваме входа към числа
    aNum = float(a)
    bNum = float(b)

    # Изпълняваме операцията
    if operation == "+":
        result = aNum + bNum
    elif operation == "-":
        result = aNum - bNum
    elif operation == "*":
        result = aNum * bNum
    elif operation == "/":
        result = aNum / bNum
    else:
        raise ValueError("Невалиден оператор!")

except ValueError as ve:
    print("Не е въведено число!!!", ve)

except ZeroDivisionError:
    print("Грешка: Деление на нула!")

except TypeError:
    print("Грешка: Не може да се изпълни операцията!")

except Exception as e:
    print("Невалидна грешка:", e)

else:
    print("Result=:", result)
