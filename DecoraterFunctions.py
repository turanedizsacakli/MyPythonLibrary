# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler...")
#         func(name)
#         print("fonksiyondan sonraki işlemler...")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello world... ",name)

# @my_decorator
# def sayGreeting():
#     print("greeting...")

# sayHello("turan")
# #sayGreeting()

# #bunun yerine sadece @ yeterli
# # sayHello=my_decorator(sayHello)
# # sayGreeting=my_decorator(sayGreeting)
# # sayHello()
# # sayGreeting()

import math
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish=time.time()
        print("fonksiyon "+func.__name__+" "+str(finish-start)+" saniyede sona erdi...")
    return wrapper

@calculate_time
def usalma(a,b):
    print(math.pow(a, b))


  
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    

usalma(2, 3)
faktoriyel(20)