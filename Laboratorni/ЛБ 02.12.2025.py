# Работа с файлове в Python какви са режимите на отваряне 
# добре е да ги използваме с with open за да не забравим да затворим файла
# добре е да е с try except за да хванем грешки ако файла не съществува
# utf-8 е за да се четат и записват български букви правилно
# a+ - отваря файл за добавяне и четене, ако файла не съществува го създава
# + - добавя възможност за четене към всеки режим на отваряне


 #append - добавяне, w- write - запис, r - read - четене, a+ - добавяне и четене
# wb - write binary - запис в двоичен файл, rb - read binary - четене от двоичен файл
# wb+ - запис и четене в двоичен файл

# f = open ("my_file.txt", "w", encoding="utf-8")
# f.write("Тест123")
# f.close() # когато използваме горния начин с open трябва да затворим файла с close()
# # Програмата:
# f = open ("my_file.txt", "r", encoding="utf-8")
# # content = f.read()
# # print (content)



# f = open ("my_file.txt", "r", encoding="utf-8")
# # content = f.readlines()
# # print (content)


# f = open ("my_file.txt", "r", encoding="utf-8")
# for line in f:
#     print (line).strip()  # премахва празните редове при отпечатване
# f.close()
# # Програмата: прочита файла ред по ред и отпечатва всеки ред

# with open ("my_file.txt", "r", encoding="utf-8") as f:  
#     # автоматично затваря файла след приключване на блока
#     content = f.read()
#     print (content)   

# fruits = ["apple\n", "banana\n", "cherry"]
# with open("fruits.txt", "a", encoding="utf-8") as f:
#     f.writelines(fruits)  # записва елементите на списъка в нов файл без разделител



# with open ("my_file.txt", "a+", encoding="utf-8") as f:  
#     f.write("New Line\nНов ред добавен в края на файла.")
#     print(f"Текуща позиция на курсора: {f.tell()}")  # показва текущата позиция на курсора в файла
#     f.seek(5)  # връща курсора в началото на файла
#     for line in f:
#         print(line.strip())


# import json
# person={
#     "name": "John", 
#     "age": 30, 
#     "city": "New York"
# }

# with open("person.json", "w") as f:
#     json.dump(person, f, indent=4)  # записва речника в JSON файл




# import json
# person={
#     "name": "John", 
#     "age": 30, 
#     "city": "New York"
# }

# with open("person.json", "r") as f:
#     person = json.load(f)  # зарежда данните от JSON файла в речник
#     print(person["name"]) # отпечатва стойността на ключа "name"


# binary_file = open ("binary_file.bin", "wb+")  # отваря файл за запис в двоичен режим
# text = "Hello123"
# encoded = text.encode()  # кодира текста в байтове 
# #utf-8 може и да не го записваме в скобите, защото е по подразбиране
# binary_file.write (encoded)  # записва байтовете във файла
# binary_file.seek(0)  # връща курсора в началото на файла
# binary_data = binary_file.read()  # чете байтовете от файла
# print (binary_data)
# decoded = binary_data.decode()  # декодира байтовете обратно в текст
# print (decoded)
# # с encode и decode се преобразува текст в байтове и обратно


# зад1.
f = open ("hello.txt", "w", encoding="utf-8")
f.write("Hello, world!\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# зад.2
filename = "text.txt"

lines_count = 0
words_count = 0
chars_count = 0

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        lines_count += 1
        words = line.split()
        words_count += len(words)
        chars_count += len(line)

print("Брой редове:", lines_count)
print("Брой думи:", words_count)
print("Брой символи:", chars_count)

#зад.3
text = input("Въведете текст: ")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(text + "\n")

print("Текстът е добавен в log.txt")


# зад.4
filename = "data.txt"

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if "Python" in line:
            print(line, end="")


#зад.5 
filename = "data.txt"

N = int(input("Въведете N: "))

with open(filename, "r", encoding="utf-8") as f:
    text = f.read(N)   # прочита първите N символа

print("Първите", N, "символа са:")
print(text)
    



# зад.6
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Първи ред\n")
    f.write("Втори ред\n")
    f.write("Трети ред\n")

# seek 
