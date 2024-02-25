#Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python örneği:

def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print ("Alan :",alan)
    return alan
 
gen = input("Genişlik :")
 
yuk = input("Yükseklik : ")
 
dikdortgenAlan(gen, yuk)