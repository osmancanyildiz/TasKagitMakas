import random

class TasKagitMakas:
    def __init__(self):
        self.secenekler = ["taş", "kağıt", "makas"]
        self.oyuncu_galibiyetleri = 0
        self.bilgisayar_galibiyetleri = 0
        self.oyun_sayaci = 0

    def oyunu_baslat(self):
        print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
        print("Oyun kuralları basit:")
        print("1. Taş, kağıdı yener.")
        print("2. Kağıt, makası yener.")
        print("3. Makas, taşı yener.")
        print("İlk iki turu kazanan oyunu kazanır.")
        print("Çıkmak için 'q' tuşuna basabilirsiniz.")

        while True:
            oyuncu_tur_sayaci = 0
            bilgisayar_tur_sayaci = 0
            self.oyun_sayaci += 1
            
            print(f"\nOyun {self.oyun_sayaci} başlıyor!")
            
            while oyuncu_tur_sayaci < 2 and bilgisayar_tur_sayaci < 2:
                oyuncu_secimi = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q'): ").lower()
                if oyuncu_secimi == 'q':
                    print("Oyundan çıkılıyor...")
                    return

                if oyuncu_secimi not in self.secenekler:
                    print("Geçersiz bir seçenek! Lütfen tekrar deneyin.")
                    continue
                
                bilgisayar_secimi = random.choice(self.secenekler)
                print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
                
                if oyuncu_secimi == bilgisayar_secimi:
                    print("Berabere!")
                elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                     (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                     (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                    print("Turunu kazandınız!")
                    oyuncu_tur_sayaci += 1
                else:
                    print("Bilgisayar turu kazandı!")
                    bilgisayar_tur_sayaci += 1

            if oyuncu_tur_sayaci == 2:
                print("Tebrikler, oyunu kazandınız!")
                self.oyuncu_galibiyetleri += 1
            else:
                print("Bilgisayar oyunu kazandı!")
                self.bilgisayar_galibiyetleri += 1
            
            while True:
                devam_etmek = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
                if devam_etmek == 'e' or devam_etmek == 'h':
                    break
                else:
                    print("Geçersiz bir seçenek! Lütfen 'e' veya 'h' girin.")

            if devam_etmek != 'e':
                print("Oyun sona erdi. Tekrar görüşmek üzere!")
                break

            print("Başka bir oyun oynamak ister misin Bilgisayar?")

            bilgisayar_devam = random.choice(['e', 'h'])
            if bilgisayar_devam == 'h':
                print("Bilgisayar devam etmek istemiyor. Oyun sona erdi.")
                break
            else:
                print("Bilgisayar da devam etmek istiyor. Yeni oyun başlıyor!")

def tas_kagit_makas_Osman_Can_YILDIZ():
    oyun = TasKagitMakas()
    oyun.oyunu_baslat()

# Oyunu başlatmak için:
tas_kagit_makas_Osman_Can_YILDIZ()
