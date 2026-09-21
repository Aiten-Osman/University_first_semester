



# a = int [input ( a )]
#b = int [ input (b  )]
#print ( a + b ) 

#a = 3
#b=4 
#s= "hey"

#print ("I am {a} old almost {b} and I say format ( s) .")

#a = float(input(""))
#b = float(input(""))
#h = float(input(""))

#formula = (a + b) / 2 * h   
#print(f" S = {formula:.2f}")
'''
import math

r = float(input(" "))

S = math.pi * r ** 2
P = 2 * math.pi * r

print(f"S = {S:.3f}")
print(f"P = { P:.3f}")
'''
'''
hours = float(input(""))
rate = float(input(" "))

gross_pay = hours * rate
netno = 0,1218 * gross_pay
print(f" Брутно заплатата е {gross_pay:.2f}")
print(f" Нетно заплатата е {(gross_pay - netno):.2f}")    

'''
'''
minutes = int(input(""))
days = minutes // 1440  
hours = minutes // 60
min  = minutes % 60
 
if days > 0:
    hours = hours % 24  
print(f"{minutes} минути са {hours} час(а) и {min} минути.")
print (days)
'''

number = int(input(""))

if number % 2 == 0:
    print("четно")
else:
    print("нечетно")

