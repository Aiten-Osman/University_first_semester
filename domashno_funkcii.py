# зад.1 Напишете Python функция, която подканва потребителя да въведе число.
# След това, при наличие на това число, тя отпечатва 
# изречението „Здравей, Python!“ определен брой пъти.


# def congrat(number):
#     for i in range(number):
#         print("Здравей, Python!")

# n = int(input("Въведи число: ")) 

# congrat(n)


# Напишете Python функция, която приема низ като вход и връща речник,
# съдържащ броя на главните и малките букви в низа. Всички символи,
# които не могат да бъдат категоризирани като главни или малки букви (напр. символи), 
# трябва да се броят като „други“.

# def count_letters(niz:str) -> dict:
#     result = {"главни":0, "малки":0, "други":0}
#     for char in niz:
#         if char.isupper():
#             result["главни"] += 1
#         elif char.islower():
#             result["малки"] += 1
#         else:
#             result["други"] += 1
#     return result

# niz = input("Въведи низ: ")
# print(count_letters(niz))





# зад.3 Намиране на най-късите и най-дългите думи
# Напишете Python функция, която приема списък с низове като вход и връща кортеж, 
# съдържащ най-късата и най-дългата дума от списъка, в този ред.
# Ако има няколко думи с еднаква най-къса или най-дълга дължина, 
# връща първата намерена най-къса/най-дълга дума.

# def find_shortest_and_longest(words:list) -> tuple:
#     if not words:
#         return ("", "")
    
#     shortest = longest = words[0]
    
#     for word in words:
#         if len(word) < len(shortest):
#             shortest = word
#         elif len(word) > len(longest):
#             longest = word
            
#     return (shortest, longest)

# niz = input("Въведи думи, разделени с интервал: ")
# list = niz.split()
# print(f"Най- късата и най- дългата дума са {find_shortest_and_longest(list)}.")



# зад.4 Проверка преди добавяне
# Напишете Python функция, която приема списък и елемент като вход. 
# Функцията трябва да добави елемента към списъка само ако той вече не е наличен в него.

def add_if_not_exists(lst:list, element) -> list:
    if element not in lst:
        lst.append(element)
    return lst
element = input("Въведи елемент: ")
list = [input("Въведи елемент за списъка: ")]
print(list)
print(f"Новият вид приема вида: {add_if_not_exists(list, element)}")




# зад.5 Премахване на дубликати и сортиране
# Напишете Python функция, която приема списък с низове като вход и връща друг списък,
# съдържащ уникалните елементи от входния списък, сортирани по азбучен ред.

# def remove_duplicates_and_sort(strings:list) -> list:
#     unique_strings = list(set(strings))
#     unique_strings.sort()
#     return unique_strings

# user_input = input("Въведи елементите, разделени с интервали: ")
# list_niz = user_input.split()  # разделя по интервали и прави списък
# print(f"Новият списък приема вида: {remove_duplicates_and_sort(list_niz)}")


