from datetime import datetime 

t=datetime.now() 

girilenTarih= input("doğum tarihinizi 0.0.0000 şeklinde giriniz : ")
girilenTarih=girilenTarih.split(".") 

birthday=datetime(int(girilenTarih[2]),int(girilenTarih[1]),int(girilenTarih[0])) 

differences=t-birthday 

year= int(differences.days/365) 

month= int((differences.days-(year*365))/30) 

day=differences.days-((year*365)+(month*30)) 

print("{} yıl {} ay {} gündür yaşıyorsunuz...".format(year,month,day))

