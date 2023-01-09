import mysql.connector

def insertProduct(name,price,imageUrl,description): #tekli kayıt...
    connection=mysql.connector.connect(host="localhost",user="root",password="207259.Xx",database="node-app")
    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"

    values=(name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi...")
        print(f"son eklenen kaydın id : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı...")

def insertProducts(liste):
    connection=mysql.connector.connect(host="localhost",user="root",password="207259.Xx",database="node-app")
    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"

    values=(liste)

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi...")
        print(f"son eklenen kaydın id : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı...")
liste=[]

while True:
    name=input("ürün ismini giriniz : ")
    price=float(input("ürün fiyatını giriniz : "))
    imageUrl=input("ürün resmini giriniz : ")
    description=input("ürün bilgisi giriniz : ")

    liste.append((name,price,imageUrl,description))
    #insertProduct(name,price,imageUrl,description) çoklu kayıtta tekliya ihtiyaç yok...
    want=input("devam etmek istiyor musunuz? e/h")
    if want=="e":
        pass
    if want=="h":
        print("kayıtlanınız veri tabanına ekleniyor...")
        print(liste)
        insertProducts(liste)        
        break








