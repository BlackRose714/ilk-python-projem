print("Kaç yaşındasınız?")
yaş= int(input())
if yaş >= 18:
	print("Okuyormusunuz?")
	cevap= input()
	if cevap.lower() == "evet":
		print("Okulunuzu tamamladıktan sonra askere gideceksiniz.")
	elif cevap.lower() == "hayır":
		print("Askere gitme yaşınız geldi.")
elif yaş < 18:
	print("Askere gitme yaşınız gelmedi.")