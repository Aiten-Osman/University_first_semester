# #зад1
# class NumberList:
#     def __init__(self, values):
#         self.number = []
#         for i in values:
#             if isinstance(i, (int, float)):
#                 self.number.append(i)

#     def print(self):
#         print("List has:", self.number)

#     def average(self):
#         if not self.number:
#             return 0
#         return round(sum(self.number) / len(self.number), 2)


# values = [1, 2, 3.5, 4]
# obj = NumberList(values)
# obj.print()
# print("Average value:", obj.average())

# #зад2
# class Func:
#     def __init__(self, value):     
#         self.value = value

#     def __str__(self):            
#         return f"Func({self.value})"
    

# def obj_func(x):
#     object_list = []
#     number = 1
#     for i in range(x):
#         obj = Func(number)
#         object_list.append(obj)
#         number += 2
#     return object_list


# x = int(input("Enter number of objects: "))
# objects = obj_func(x)

# for obj in objects:
#     print(obj)



# #зад4
# class Shape:
#     def __init__(self,figura_type):
#         self.figura_type = figura_type
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, side):
#              super().__init__("square")
#              self.side = side
#     def area(self):
#              return self.side * self.side
        
# class Circle(Shape):
#     def __init__(self, radius):
#           super().__init__("circle")
#           self.radius = radius
#     def area(self):
#          import math
#          return math.pi * self.radius * self.radius
    


# try:
#     figura_type = input("Type of figure: ").lower()
    
#     if figura_type == "square":
#         side = float(input("Length of side: "))
#         if side <= 0:
#             raise ValueError("Side has to be a positive number")
#         shape = Square(side)
    
#     elif figura_type == "circle":
#         radius = float(input("Enter a radius: "))
#         if radius <= 0:
#             raise ValueError("Radius has to be a positive number")
#         shape = Circle(radius)
    
#     else:
#         raise ValueError(f"Invalid figure: {figura_type}")
    
#     print(f"Figure: {shape.figura_type}")
#     print(f"Shape: {shape.area():.2f}")

# except ValueError as e:
#     print(f"ValueError: {e}")
# except Exception as e:
#     print(f"Exception: {e}")

# #зад5
# class Func:
#     def __init__(self, *args):
#         texts = [a for a in args if isinstance(a, str)]
#         nums = [a for a in args if isinstance(a, int)]

#         if len(args) == 2:
#             if len(texts) == 2:
#                 self.text = texts[0] + texts[1]
#             elif len(nums) == 2:
#                 self.number = nums[0] + nums[1]
#             elif len(texts) == 1 and len(nums) == 1:
#                 self.text = texts[0]
#                 self.number = nums[0]

#     def __str__(self):
#         parts = []
#         if hasattr(self, "text"):
#             parts.append(f"text={self.text}")
#         if hasattr(self, "number"):
#             parts.append(f"number={self.number}")
#         return "Func(" + ", ".join(parts) + ")"
        

# obj1 = Func("hello", "world")  
# obj2 = Func(10, 20)              
# obj3 = Func("age", 15)           
# obj4 = Func(7, "days")           

# print(obj1)  
# print(obj2)  
# print(obj3)  
# print(obj4)


# #зад6
# class TriangleChecker:
#     def __init__(self, *arg):
#         self.sides = arg

#     def is_triangle(self):
#         for side in self.sides:
#             if not isinstance(side, (int, float)):
#                 return "Трябва да въведете само числа!"

#         for side in self.sides:
#             if side <= 0:
#                 return "Нищо няма да работи с отрицателни числа!"

#         if len(self.sides) != 3:
#             return "Enter exactly three numbers!"
        
#         a, b, c = self.sides

#         if a + b > c and a + c > b and b + c > a:
#             return "Ура можете да построите триъгълник!"
#         else:
#             return "Жалко не можете да направите триъгълник от това!"

#     def get_triagle_type(self):
#         result = self.is_triangle()
#         if result != "Ура можете да построите триъгълник!":
#             return "Не може да се определи тип (не е валиден триъгълник)"

#         a, b, c = self.sides

#         if a == b == c:
#             return 'равностранен'
#         elif a == b or a == c or b == c:
#             return "равнобедрен"
#         else:
#             return "разностранен"



# try:
#     a = float(input("Enter side a: "))
#     b = float(input("Enter side b: "))
#     c = float(input("Enter side c: "))

#     obj = TriangleChecker(a, b, c)

#     print(obj.is_triangle())
#     print("Вид на триъгълника:", obj.get_triagle_type())

# except ValueError:
#     print("Трябва да въведете валидни числа!")



#зад 7
class Phone:
    def __init__ (brand, model, price, quantity):
        brand_= input()
        model = input()
        price = input.float()
        quantity = input.int()



def create_phone_list:

def find_max_price_phone:
pass

def calculate_average_price:
pass

def filter_ by_brand:
pass
     
