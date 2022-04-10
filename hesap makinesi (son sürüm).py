sayi1 = int(input("1.sayı => "))
sayi2 = int(input("2.sayı => "))
islem = input("Yapmak istediğiniz işlemi giriniz (+,-,*,/) => ")

if islem == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
elif islem == "/" and sayi2 != 0:
    sonuc = sayi1 / sayi2
    print(sonuc)
else :
    print("Yanlış işlem girdiniz.. ")