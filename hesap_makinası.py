birinci_sayı = int(input("İlk sayıyı giriniz: "))
ikinci_sayı = int(input("Diğer sayıyı giriniz: "))
işlem = input("Yapmak istediğiniz işlemi giriniz. (Toplama: + , Çıkartma: - , Çarpma: x , Bölme: /): ")

if işlem == "+":
    sonuç = birinci_sayı + ikinci_sayı
elif işlem == "-":
    sonuç = birinci_sayı - ikinci_sayı
elif işlem == "x":
    sonuç = birinci_sayı * ikinci_sayı
elif işlem == "/":
    if ikinci_sayı != 0:
        sonuç = birinci_sayı / ikinci_sayı  # istersen // yerine / de kullanabilirsin
    else:
        sonuç = "Bir sayı sıfıra bölünemez."
else:
    sonuç = "Geçersiz işlem."

print("Sonuç:", sonuç)