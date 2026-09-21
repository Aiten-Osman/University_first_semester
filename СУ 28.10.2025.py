#зад1. произведение 
# m = int(input())
# n = int(input())

# multiply = 1
# flag = False 
# for i in range(m, n + 1):   
#     if (i % 3 == 0) and (i % 4 == 0) :
#         multiply *= i
#         flag = True

# if flag:
#     print(multiply)
# else:
#     print("Няма намерени числа.") 



#зад2 делят на 3 в интервал (7;70)
# count = 0
# sum = 0 
# for i in range(7,70):
#     if i % 3 == 0:
#         count +=1
#         sum = sum + i
#     continue
# print(sum/count)




#зад3 цифра на единици, стотици....
    
# num = int(input())
# edinici = num % 10
# desetici = (num // 10) % 10
# if edinici % 5 == 0:
#     print(f"Edinicite na chisloto {num} se delqt na 5")
# else :
#     print(f"Edinicite na chisloto {num} ne se delqt na 5")

# if desetici % 2 == 0:
#     print(f"Deseticite na chisloto {num} sa chetni")
# else:
#     print(f"Deseticite na chisloto {num} sa nechetni")





# #зад4 произведение на числата от 1 до 50, които се делят на 2 или 3
# sum = 0 

# for i in range(1,50):
#     if i % 3 == 0 or i % 2 == 0:
#         if not (i % 3 == 0 and i % 2 == 0):
#             sum += i
        
# print(sum)         





# #зад5 
# num = int(input()) # имената на ключовите думи да НЕ са имена на променливи!!!
# max = -999999
# min = 999999


# for i in range (num):
#     n = int(input())
#     if n < min:
#         min = n 
#     elif n > max:
#         max = n

# print(f" Най - малкото число е {min}")
# print(f" Най - голямото число е {max}")




# #зад6 лице и периметър на фигура
# name = input("Фигурата може да е квадрат, правоъгълник и правоъгълен триъгълник: ")
# a = int(input())



# if name == "квадрат":
#     S = a*a
#     P = 4*a 
# elif name == "правоъгълник":
#     b = int(input())
#     S = a*b 
#     P = 2*(a + b)    
# elif name == "правоъгълен триъгълник":
#     b = int(input())
#     c = int(input())
#     S = (a * b) / 2
#     P = a + b + c 

# print(f"Лицето е {S:.2f}")
# print(f"Периметърът е {P:.2f}")





# #зад7 
# success = float(input())
# max_stipendiaq = float(input())

# if success >= 5.50:
#     stipendiq = max_stipendiaq
# elif 5.00 <= success < 5.50:
#     stipendiq = max_stipendiaq * 0.70
# elif 4.50 <= success < 5.00:
#     stipendiq = max_stipendiaq * 0.50
# elif success < 4.50:
#     stipendiq = 0
# if stipendiq == 0:
#     print("You do not get sripendiq")
# else:
#     print(f"Your stipendiq is {stipendiq}")    




# 10 zad
# budget = float(input("Enter your budget: "))
# season = (input("Enter your season: "))
#
# destinations = ["Bulgaria", "Balkans", "Europe"]
# final_destination = ""
# price = 0
#
# if budget <= 100:
#     final_destination = destinations[0]
#     if season == "summer":
#         price = 0.3 * budget
#     elif season == "winter":
#         price = 0.7 * budget
# elif budget <= 1000:
#     final_destination = destinations[1]
#     if season == "summer":
#         price = 0.4 * budget
#     elif season == "winter":
#         price = 0.8 * budget
# elif budget > 1000:
#     final_destination = destinations[2]
#     price = 0.9 * budget
#
# print("Somewhere in", final_destination)
# if season == "summer":
#     print(f"Camp - {price:.2f}")
# elif season == "winter":
#     print(f"Hotel - {price:.2f}")


#11 zad

# skiors = int(input("Number of skiors: "))
# sum = 0
#
# for i in range(skiors):
#     print(f"{i+1} skior: ")
#     jackets = int(input("Number of jackets: "))
#     kasks = int(input("Number of kasks: "))
#     shoes = int(input("Number of shoes: "))
#
#     sum += jackets * 120 + kasks * 75 + shoes * 299.90
#     print()
#
# sum = sum + 0.2 * sum
#
# print(f"Total price:{sum:.2f}")

#12 zad
# import sympy
#
# sum_prime = 0
# sum_not_prime = 0
#
# while True:
#     n = input()
#     if n == "stop":
#         break
#     else:
#         n = int(n)
#         if n < 0:
#             continue
#         else:
#             if sympy.isprime(n):
#                 sum_prime += n
#             else:
#                 sum_not_prime += n
#
#
# print(f"Sum of all prime numbers: {sum_prime}")
# print(f"Sum of all non prime numbers: {sum_not_prime}")

#13 zad
# floors = int(input())
# rooms_for_one_floor = int(input())
#
# flat_name = ''
#
# for floor in range(floors, 0, -1):
#     for rooms in range(0, rooms_for_one_floor):
#         flat_name = f"{floor}{rooms}"
#
#         if floor == floors:
#             print(f"L{floor}{rooms}", end=' ')
#         elif floor % 2 != 0:
#             print(f"A{floor}{rooms}", end=' ')
#         elif floor % 2 == 0:
#             print(f"O{floor}{rooms}", end=' ')
#
#     print()