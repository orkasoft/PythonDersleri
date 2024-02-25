#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız.

print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI 💪")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks  = kilo/(boy*boy)
 
if endeks <=18:
    print("\n zayıf VKİ:",endeks)
elif endeks > 18 and endeks <=25 :
    print("\n kilolu VKİ:",endeks)
elif endeks > 25 and endeks <=30:
    print("\n obez VKİ:",endeks)
elif endeks > 30:
    print("\n ciddi obez VKİ:",endeks)