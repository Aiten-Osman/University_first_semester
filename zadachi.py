# зад.1 за произведение на числа от m до n, които се делят на 3 или на 4    

# m = int(input())
# n = int(input())

# multiply = 1
# flag = False 
# for i in range(m, n + 1):   
#     if (i % 3 == 0) or (i % 4 == 0) :
#         multiply *= i
#         flag = True

# if flag:
#     print(multiply)
# else:
#     print("Няма намерени числа.") 




# sum = 0
# counter = 0
# for i in range (7, 70 + 1):
#     if i % 3 ==0:
#         sum += i
#         counter += 1
# print (sum/counter)
# зад.2 за средноаритметично на числа от 7 до 70, които се делят на 3





# num = int(input())
# edinici = num % 10
# desetici = (num // 10) % 10
# if edinici % 5 == 0:
#     print("deli se")
# else :
#     print("ne se deli")

# if desetici % 2 == 0:
#     print("even")
# else:
#     print("odd")
# зад.3 проверка на цифрите на двуцифрено число




# sum = 0
# for t in range (1,50):
#     if t % 2 == 0 or t % 3 == 0:
#         if not (t % 2 == 0 and t % 3 == 0):
#             sum += t
# print(sum)       
# зад.4 сума на числата от 1 до 49, които се делят на 2 или на 3, но не и на двете




# num = int(input("Enter a number: "))
# list = []   
# min = - 99999
# max = 999999
# for i in range(num): 
#     value = int(input())
#     list.append(value)

# for t in range(num):
#     if list[t] < min:
#         min = list[t]
#     if list[t] > max:
#         max = list[t]

# print(f"Min = {min}")
# print(f"Max = {max}")
# # зад.5 намиране на минимално и максимално число от n въведени числа



# figure = input("Choose a figure--> 1kvadrat 2pravougulnik 3pravoug triug: ")
# if figure == "kvadrat":
#     a = float(input("Enter side a: "))
#     S = a * a
#     P = 4 * a
#     print(f"S = {S:.2f}")
#     print(f"P = {P:.2f}")
# elif figure == "pravougulnik":
#     a = float(input("Enter side a: "))
#     b = float(input("Enter side b: "))
#     S = a * b
#     P = 2 * (a + b)
#     print(f"S = {S:.2f}")
#     print(f"P = {P:.2f}")
# elif figure == "pravoug triug":
#     a = float(input("Enter side a: "))
#     b = float(input("Enter side b: "))
#     c = float(input("Enter side c: "))
#     S = a * b / 2
#     P = a + b + c
#     print(f"S = {S:.2f}")
#     print(f"P = {P:.2f}") 
# зад.6 изчисляване на лице и периметър на квадрат, правоъгълник или правоъгълен триъгълник
#  според избора на потребителя



# success = float(input("Enter your success rate: "))
# max_stipediq = float(input())

# if success >= 5.50:
#     print(f"You get  {max_stipediq:.2f} BGN")
# elif  5.50 > success >= 5.00:
#     print(f"You get  {max_stipediq * 0.70:.2f} BGN") 
# elif 5.00 > success >= 4.50:
#     print(f"You get  {max_stipediq * 0.50:.2f} BGN")
# elif 4.50 > success:
#     print("You don't get a stipendia")
# зад.7 изчисляване на стипендия според успеха на студента       

        
# bank_id = 0
# bust = 0 
# sth = input("Enter man or women: ")
# if sth == "man":
#     bank_id = float(input())
# elif sth == "woman":
#     bust= float(input())  

# if bank_id >= 250000 or bust >= 100:
#     print("Подходящ ")    
# elif bank_id < 250000 or bust < 100:
#     print("Не е подходящ")
#  зад.8 проверка мъж или жена
   



# num = input()
# tuple_1 = tuple(num)
# tuple_2 = tuple(reversed (tuple_1)) # обръщане на реда на елементите в tuple 
# # tuple_2 = tuple [::-1]  # обръщане на реда на елементите в tuple
# print(tuple_1)
# print(tuple_2)
# зад.1 въвеждане на число и отпечатване на цифрите му в обратен ред като tuple





import random
n = int(input("Enter number of elements: "))
list = []
new_list = []
for i in range(n):  
    value = random.randint(1, 100)
    list.append(value)
print(list)

for t in range (len(list)-1): # намиране на дължина на лист ==> n-1 пак става
    new_list.append(list[t])
    new_list.append(list[t] + list[t+1])

print (new_list)   
# зад.2 числов списък като новият списък е с елементи сборни на съседните от горния ред






# num = int(input())
# list = []

# for i in range(1, num + 1):
#     list.append(i)
# print(list)

# new_list = reversed(list)
# dictionary = dict(zip(list, new_list))
# print(dictionary)
# зад. 3 списъци и речници  list and dict

