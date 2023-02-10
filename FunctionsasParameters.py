def toplama (a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpim(a,b):
    return a*b
def bolme (a,b):
    return a/b

def islem(f1,f2,f3,f4, islem_adi):
    if islem_adi=="toplama":
        print(f1(2,3))
    elif islem_adi=="cikarma":
        print(f2(5,3))
    elif islem_adi=="carpim":
        print(f3(3,2))
    elif islem_adi=="bolme":
        print(f4(8,2))

islem(toplama, cikarma, carpim, bolme, "carpim")