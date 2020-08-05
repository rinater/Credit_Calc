import math

user_input = int(input())
contagent = math.cos(user_input * math.pi/180)/math.sin(user_input * math.pi/180)
print(round(contagent, 10))
