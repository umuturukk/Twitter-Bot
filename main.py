from twitter import Twitter
from time import sleep

kullaniciAdi = input("Twitter hesabınızın kullanıcı adı: ")
sifre = input("Twitter hesabınızın şifresi: ")
tw = Twitter(username = kullaniciAdi, password = sifre)
sleep(4)
print("\n")
print("***** Twitter Bot Uygulamasına Hoş Geldiniz *****")
print("Yapabileceğiniz İşlemler:\n1-) Giriş Yap\n2-) Girdiğin Keyword'e Göre Arama\n3-) Trendlerin Başlıklarını Göster\nÇıkmak için 'q' ya basınız.\n")

secim = input("Bir seçim yapınız: ")

def main():
    if secim == "1":
        tw.signIn()
    elif secim == "2":
        keyword1 = input("Arama yapmak istediğiniz keyword'u giriniz: ")
        tw.signIn()
        tw.keywordSearch(keyword = keyword1)
    elif secim == "3":
        tw.signIn()
        tw.getTrendTweetsTitle()
    else:
        print("Lütfen işlem numaranıza dikkat ediniz.")

    while True:
        kapamaSecimi = input("Tarayıcıyı kapatmak için 'q' tuşuna basın: ")
        if kapamaSecimi == "q":
            break

if __name__ == '__main__':
    main()