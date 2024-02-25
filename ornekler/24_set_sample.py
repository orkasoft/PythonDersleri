fruitSet = {"elma", "muz", "kiraz", "elma", "kiraz"}

print(fruitSet)  #  Tekrar eden kayıtları 1 er defa gösterir.

# print(fruitSet[1])    -->   Set ile index kullanımı yapılamaz. 
# fruitSet[1] = "üzüm"  -->   Set düzenli bir sıralama barındırmaz. Rasgele olarak elamanları tutar.

for x in fruitSet:
    print(x)