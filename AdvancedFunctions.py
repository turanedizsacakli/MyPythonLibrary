# def greeting(name):
#     print("hello " , name)

# sayHello=greeting
# print(greeting("turan"))
# print(sayHello("turan"))

#encapsulation (kapsülleme) denilmekte...
def outer(num1):
    print("dıştaki")
    if not isinstance(num1, int): #isinstance(obj, class_or_tuple) sayı mı str mi kontrol eder...
        raise TypeError("sayı olmalı...")

    def inner_increment(num1):
        print("içteki")
        return num1+1
    num2=inner_increment(num1)
    print(num1,num2)

outer(10)
