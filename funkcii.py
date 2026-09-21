# zad 1
# def FindDayWinner(*winners):
#     team1 = 0
#     team2 = 0
#     for i in winners:
#        if i == "Team1":
#            team1 += 1
#        elif i == "Team2":
#            team2 += 1
#        else:
#            print("Enter team again")
   
#     if team1 > team2:
#         print("The winner is Team1")
#     elif team2 > team1:
#         print("The winner is Team2")
#     else:
#         print("Tie")  
   

# FindDayWinner("Team1", "Team2", "Team1")


# #zad2
# def checkPerfectNum(numbers):
#     sum = 0
#     for i in range(1, numbers):
#         if numbers % i == 0:
#             sum += i
#     if sum == numbers:
#         return True
#     else:
#         return False
    
# print(checkPerfectNum(int(input("Enter number: "))))



#zad4
# def fromTenToSec(n):
#     if n == 0:
#         return "0"
#     if n < 0:
#         return "-" + fromTenToSec(-n)
    
#     sum_ostataci = []

#     while n > 0:
#         sum_ostataci.append(str(n % 2))
#         n //= 2
#     rev = list(reversed(sum_ostataci))
#     result = "".join(rev)
#     return result

# print(fromTenToSec(int(input("Enter number: "))))


# #zad5
# import random

# def func(list1, list2):
#     max_len = max(len(list1), len(list2))
     
#     total = 0

#     for i in range(max_len):
#         a = list1[i % len(list1)]
#         b = list2[i % len(list2)]
#         total += a * b
    
#     return total

# n1 = int(input("Enter count in list1: "))
# l1 = []
# for i in range(n1):
#     num = random.randint(1,10)
#     l1.append(num)

# n2 = int(input("Enter count in list2: "))
# l2 = []
# for i in range(n2):
#     num = random.randint(1,10)
#     l2.append(num)

# print("List 1: ", l1)
# print("List 2: ", l2)

# result = func(l1, l2)
# print("Result: ", result)



#zad6

# def func(*argument):

#     average = sum(argument) / len(argument)
#     maximum = max(argument)
#     minimum = min(argument)

#     return [average, maximum, minimum]

# numbers = input("Enter numbers: ")
# num_list = [int(x) for x in numbers.split()]

# result = func(*num_list)

# print("Average: ", result[0])
# print("Maximum: ", result[1])
# print("Minimum: ", result[2])


# #zad 10
# def CheckPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Въведете число: "))

# found = False

# for p in range(2, num):
#     q = num - p
#     if CheckPrime(p) and CheckPrime(q):
#         print(f"{num} = {p} + {q}")
#         found = True
#         break

# if not found:
#     print("Не може .")


    
        






# #zad7
# def build_text(text, *indexes):
#     result = ""
#     for i in indexes:
#         if 0 <= i < len(text):
#             result += text[i]
#     return result
# text = input("Въведи текст: ")
# indexes_input = input("Въведете индексите (разделени с интервал): ")
# indexes = [int(x) for x in indexes_input.split()]
# result = build_text(text, *indexes)
# print("Резултат:", result)

#zad 9 

# def create_matrix(rows, cols):
#     matrix = []
#     print("Въвеждайте елементите ред по ред:")

#     for r in range(rows):
#         row = []
#         for c in range(cols):
#             value = int(input(f"Елемент [{r}][{c}]: "))
#             row.append(value)
#         matrix.append(row)

#     return matrix


# def print_matrix(matrix):
#     print("\nМатрицата е:")
#     for row in matrix:
#         for value in row:
#             print(value, end=" ")
#         print()


# def sum_columns(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     col_sums = [0] * cols

#     for r in range(rows):
#         for c in range(cols):
#             col_sums[c] += matrix[r][c]

#     print("\nСума по колони:")
#     for i, s in enumerate(col_sums):
#         print(f"Колона {i}: {s}")

# rows = int(input("Въведете брой редове: "))
# cols = int(input("Въведете брой колони: "))

# matrix = create_matrix(rows, cols)
# print_matrix(matrix)
# sum_columns(matrix)
















# #zad3
# def fromSecToTen(num):
#     decimetri = 0
#     stepen = 0 
#     for i in reversed(num):
#         if i != '0' and i != '1':
#             return "Error"
#         i = int(i)
#         decimetri += i * (2 ** stepen)
#         stepen += 1 
#     return decimetri

# print(fromSecToTen(input("Enter number: ")))

#zad8
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# # въвеждаме двете числа
# a = int(input("Въведете първото число: "))
# b = int(input("Въведете второто число: "))

# # намираме НОК чрез функцията
# result = lcm(a, b)

# print("НОК =", result)
# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)

# #1
# def FindDayWinner(results):
#     """
#     results: списък от стрингове – името на победителя във всеки мач
#     връща: "Team1", "Team2" или "Tie"
#     """
#     team1_wins = results.count("Team1")
#     team2_wins = results.count("Team2")

#     if team1_wins > team2_wins:
#         return "Team1"
#     elif team2_wins > team1_wins:
#         return "Team2"
#     else:
#         return "Tie"
# print(FindDayWinner(["Team1", "Team2", "Team1"]))
# # изход: Team1

# print(FindDayWinner(["Team1", "Team2", "Team2", "Team1", "Team2"]))
# # изход: Team2



# #zad2
# def checkPerfectNum(n):
#     if n <= 0:
#         return False

#     sum_divisors = 0

#     for i in range(1, n):
#         if n % i == 0:
#             sum_divisors += i

#     return sum_divisors == n
# numbers = [6, 10, 28, 12, 496, 20]

# for num in numbers:
#     if checkPerfectNum(num):
#         print(num)