# # направи функция, която приема quantity, item и price като аргументи, 
# # # и връща с ключове "item" и "price", съдържащи съответните стойности

# def producti(quantity, item, price):
#    smetki = quantity * price 
#    print(f"{item} e na edinichna cena {price}, a za dadenoto kolichestvo {quantity} struva {smetki}.")

# quantity1 = int(input("enter quantity: "))
# item1 = input("enter item: ")
# price1 = float(input("enter price: "))
# producti(quantity1, item1, price1)





# # напишете потребителска функция, която проверява дали числото е полиндром. Функцията получава като
# # аргумент число и връща 1 ако числото е палиндрон и 0 ако не е 

# def polindrom(number):
#     reversed_number = number[::-1]
#     if reversed_number == number:
#         return 1
#     else:
#         return 0

       
# num = int(input())
# str_num = str(num)
# print(polindrom(str_num))




# СУ 
# зад 2 

# M = int(input("Въведи M: "))
# N = int(input("Въведи N: ")) 
# list = []   

# for i in range (M, N): # ако искаме включително => N +1
#      if i % 3 == 0 or i % 4 == 0:
#          if not ( i % 3 == 0 and i % 4 == 0):
#             list.append(i)
# print(list)






# зад 4

# text = input("Въведи текст: ")
# text_tuple = tuple(text) # превръщане на стринг в кОртеж
# new_text_tuple = text_tuple[::2] # вземане на всеки втори елемент от кортежа
# print(text_tuple)
# print(new_text_tuple)



# # зад 6
# import random
# count = int(input("Enter number of elements: "))
# list = []
# new_list_chetna = []
# new_list_nechetna = []


# for i in range(count):  
#     value = random.randint(1, 100)
#     list.append(value)
 

# for i in range(count):
#     if i % 2 == 0: # ако е на четна позиция
#         new_list_chetna.append(list[i])
        
#     else:          # ако е на нечетна позиция
#         new_list_nechetna.append(list[i])

# print (list)
# print (new_list_chetna)
# new_list_chetna.sort()
# print (new_list_chetna)
# print (new_list_nechetna)     
# new_list_nechetna.sort(reverse=True) #обръщане на реда на сортирането или
# print (new_list_nechetna) 




# # зад 5   намиране на втория по големина елемент и неговия индекс в списъка
# n = int(input("Въведи n: "))
# list = []
# list_2 = [] 
# list_3 = []

# for i in range(n):
#     value = int(input("Въведи елемент: "))
#     list.append(value)

# list_2 = list.copy()
# list_2.sort(reverse = True) # сортиране на списъка в низходящ ред
# element = list_2[1]  # вземане на втория по големина елемент
# index = list.index(element)  # намиране на индекса на втория по големина елемент    
# list_3 = [element, index]
# print(list)
# print(list_3)





