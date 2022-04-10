sayi1 = int(input("1.sayı => "))
sayi2 = int(input("2.sayı => "))
islem = input("Sadece toplama işlemi yapınız (+) => ")

if islem == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
else :
    print("Yanlış işlem girdiniz.. ")