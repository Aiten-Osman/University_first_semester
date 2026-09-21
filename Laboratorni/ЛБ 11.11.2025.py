# дефиниране на клас class MyClass:
#:obj = MyClass() обекта е инстанция от даден клас 
# __init__(self,name,age) - конструктор на класа
# self - референция към текущия обект ще въведем стойност на обекта атрибути на класа
# del obj.age - изтриване на атрибут
# del obj - изтриване на обект


# ?? навигиране в линукс: cd име_папка/име_папка/име_файл.py
# # ls - показва съдържанието на папката



# създаваме един клас, който да е person. искам на този клас да създам конструктор, който да
# включва име възраст, град. Искаме да създадем два обекта от този клас и да ги принтираме на екрана.

# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def print(self):
#         print(f"Name: {self.name}; City: {self.city}")


# person1 = Person("Ivan", 42, "Bulgarian")
# person1.print()

# person2 = Person("Aiten", 19, "Bulgarian")
# person2.print()




# class Person:   
#     def greetings(self):
#         print("Hey I am Georgi.")


# class MyCar:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# # print(MyCar.brand)  # Грешка: brand не е атрибут на класа MyCar
# # print(MyCar.year)   # Грешка: year не е атрибут на класа MyCar
# print(f"Car: {self.brand}; Year: {self.year};")    



# class Person:
#     def __init__(self):
#         self.name = name
        
#     def introduce(self):
#         print(f"Hello, my name is {self.name}.")

# class Student(Person):
#     def __init__(self, university):
#         self.university = university

# student = Student()
# student.introduce()  
# print(name.university)

#?? създаване на инстанция на нов клас; предефиниране на метод от базовия клас в наследения клас

 
# class Person:
#     def __init__(self, name, family, age, nationality):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.nationality = nationality

#     def print(self):
#         print(f"Name: {self.name} {self.family}; Nationality: {self.nationality}")


# class Student(Person):
#     def __init__(self, name, family, age, nationality, university, year_of_study):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.year_of_study = year_of_study


#     def print(self):
#         print(f"Name: {self.name} {self.family}; Age: {self.age}; Nationality: {self.nationality}; "
#               f"University: {self.university}; Year of study: {self.year_of_study}")
        
# student1 = Student("Aiten", "Osman", 19, "Bulgarian", "TU - Sofia", "First year")
# student1.print()

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Name: {self.name} {self.family}; Nationality: {self.nationality}")


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(f"Name: {self.name} {self.family}; Age: {self.age}; Nationality: {self.nationality}; "
              f"University: {self.university}; Year of study: {self.year_of_study}")

    def next_year(self):
        years = ["First year", "Second year", "Third year", "Fourth year", "Graduated"]
        if self.year_of_study in years and self.year_of_study != "Graduated":
            current_index = years.index(self.year_of_study)
            self.year_of_study = years[current_index + 1]
            print(f"{self.name} {self.family} е повишен/а в {self.year_of_study}.")
        else:
            print(f"{self.name} {self.family} вече е завършил/а.")

    def change_university(self):
        new_university = input(f"Въведи нов университет за {self.name} {self.family}: ")
        old_uni = self.university
        self.university = new_university
        print(f"{self.name} {self.family} се е преместил/а от {old_uni} в {new_university}.")




