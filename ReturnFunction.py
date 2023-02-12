# def usalma(number):
#     #two=usalma(2)
#     #three=usalma(3)
#     def inner(power):
#         return number**power
    
#     return inner

# two=usalma(2)
# print(two(3))

# ***************************************************

# def yetki_sorgula(page):
#     def inner(role):
#         if role=="admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolünün {1} sayfasına ulaşamaz.".format(role,page)
#     return inner


# user1=yetki_sorgula("product edit")

# print(user1("admin"))

#*****************************************************

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            çarpim*=i
        return carpim
    if islem_adi=="toplama":
        return toplam
    elif islem_adi=="carpim":
        return carpma
    
yapilacak=islem("toplama")

print(yapilacak(2,5))