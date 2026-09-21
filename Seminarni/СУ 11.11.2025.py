#зад 1
# a = int(input()) 
# a = str(a)   
# b = int(input())    
# b = str(b)

# a = list(a)
# b = list(b)
# for char in a:
#     if char in b:
#         print(char)
       



# # зад 2 

# M = int(input("Въведи M: "))
# N = int(input("Въведи N: ")) 
# list = []   

# for i in range (M, N): 
#      if i % 3 == 0 or i % 4 == 0:
#          if not ( i % 3 == 0 and i % 4 == 0):
#             list.append(i)
# print(list)

# # зад.3
# m = input()
# set()
# dictionary = {} 




# # #зад 4

# text = input("Въведи текст: ")
# text_tuple = tuple(text) 
# new_text_tuple = text_tuple[::2] 
# print(text_tuple)
# print(new_text_tuple)

# #зад 5   намиране на втория по големина елемент и неговия индекс в списъка
# n = int(input("Въведи n: "))
# list = []
# list_2 = [] 
# list_3 = []

# for i in range(n):
#     value = int(input("Въведи елемент: "))
#     list.append(value)

# list_2 = list.copy()
# list_2.sort(reverse = True) 
# element = list_2[1]  # вземане на втория по големина елемент
# index = list.index(element)      
# list_3 = [element, index]
# print(list)
# print(list_3)


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


#зад8

n = int(input())
matrix = [] 
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("Matrix:")
print(matrix)
for row in matrix:
    print(row)


#зад9




