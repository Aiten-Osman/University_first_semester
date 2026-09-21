# n = 30
# if n == 15:
#    print("n=15")

# elif n < 35:
#     print("n<35")

# else:
#     print("HI")

# year = int(input())

# if year >=  18:
#     print("You are adult")
#     if year >= 65:
#         print("You are pensioner")
#     else:
#         print("You are adult but not pensioner")

# else:
#     print ("You are kid") 


# sum = 0   
# for i in range(0,100):
#  sum = sum + i
# print(sum) 


# text = " PyThoN "
# for char in text:
#     if char >= 'a' and char <= 'z': # когато в кавичките е главна буква => само главни букви (ascii table) 
#      print(char)

# text = " PyThoN "
# for char in word:
#    if char.islower():  # .islower() - проверява дали е малка буква .isupper() - проверява дали е главна буква
#      print(char)


# text = " PyThoN "
# for char in reversed (text):
#      print(char)

# text = input()
# lenght = len(text)
# print(lenght)

# rows = int(input())

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print() 

# rows = int(input())

# k = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()


# n = int(input())
# for i in range(n + 1):

#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


n = int(input())
flag = True

if n >= 1:
    for i in range(2, n):
        if n % i == 0:
            flag = False

if flag:
    print("Prime ")
else:
    print("Not Prime")

#просто или сложно число