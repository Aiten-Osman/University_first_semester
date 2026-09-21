num = input()
tuple_1 = tuple(num)
tuple_2 = tuple(reversed (tuple_1)) # обръщане на реда на елементите в tuple 
tuple_2 = tuple [::-1]  # обръщане на реда на елементите в tuple
print(tuple_1)
print(tuple_2)






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






text = input("Въведете текст: ")
rechnik = ()
for char in text:
    if char == " ":
        continue
    if char not in rechnik:
        rechnik [char] = 1 
    else:
        rechnik [char] += 1 
print(rechnik)       
         






num = input()
tuple_1 = tuple(num)
tuple_2 = tuple(reversed (tuple_1)) # обръщане на реда на елементите в tuple 
# tuple_2 = tuple [::-1]  # обръщане на реда на елементите в tuple
print(tuple_1)
print(tuple_2)




# # Напишете програма, която приема цяло число, а програмата формира два tuple единият с цифрите в прав ред, а другият в обратен ред
n = int(input("Въведи n: "))
 
t1 = tuple(str(n))
t2 = tuple(str(n)[::-1])
 
print(t1, t2)
 
# # Напишете програма която създава числов списък, който се запълва със случайни числа, след това между всеки две числа се добавя елемент,
# # който е сума от съседните елементи
 
import random
 
n = int(input("Въведи n: "))
l = [random.randint(0, 100) for _ in range(n)]
print(l)
 
for i in range(0, len(l) + 1, 2):
    l.insert(i + 1, l[i] + l[i + 1])
print(l)
 
# # Програма която потребителя задава текст и на негова база се създава dictionary, ключовете са символите от текста,
# # а стойностите на ел е броят на съответните символи
 
text = input("Въведи текст: ")
rechnik = {}
 
for char in text:
    if char == " ":
        continue
    if char not in rechnik:
        rechnik[char] = 1
    else:
        rechnik[char] += 1
 
print(rechnik)
 
 
# # Искаме да разменим две стойности във вложен tuple. Искаме да изведем нов кортеж с разменените позиции
# # Искаме да разменим 2 и 5 примерно
 
t = ((1, 2, 3), (4, 5, 6))
my_list = [list(t[0]), list(t[1])]
print(my_list)
 
 
my_list[0][1], my_list[1][1] = my_list[1][1], my_list[0][1]
print(my_list)
 
reversed_tuple = (tuple(my_list[0]), tuple(my_list[1]))
print(reversed_tuple)
 
# Напишете програма, в която потребителя въвежда чяло число. От него се
# създава списък състоящ се от числата от 1 до това число . Въз основа на този
# списък се създава речник, в който елементите на списъка служат за ключове
# на елементите на речника , а стойностите на тези елементи в речника са
# елементите на списъка но в обратен ред.
# Пример : ако сме въвели числото 4 , създава се списъка [1,2,3,4 ] и на негова
# основа се създава речник с 4 елемента : {1:4, 2:3, 3:2, 4:1}
 
n = int(input("Въведи n: "))
 
l = [i for i in range(1, n + 1)]
print(l)
 
d = {l[i]: l[len(l) - i - 1] for i in range(len(l))}
# d = dict(zip(l, l[::-1]))
print(d)