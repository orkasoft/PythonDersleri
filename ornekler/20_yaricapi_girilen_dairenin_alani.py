#Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python örneği:

def daireAlan(yaricap):
    alan = float(yaricap) * float(yaricap)*3.14
    print ("Alan :",alan)
    return alan
 
r = input("Yarıçapı Gir :")
 
daireAlan(r)