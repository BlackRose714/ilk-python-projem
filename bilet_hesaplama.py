fiyat= 50
print ("İsminiz nedir?")
isim= input()
print ("Kaç yaşındasınız?")
yaş= int(input())
print ("Boyunuz kaç cm?")
boy= int(input())
if yaş >= 12 and boy >= 150:
    print("Öğrenci misiniz?")
    öğrenci= input()
    print("İndirim kuponunuz var mı?")
    kupon= input()
    if öğrenci.lower()== "evet":
        fiyat = fiyat-25
    if kupon.lower()== "evet":
        fiyat = fiyat-10
    print(f"{isim} adlı kişinin bileti {fiyat}TL.")
else:
	print("Bilet alamazsınız.")