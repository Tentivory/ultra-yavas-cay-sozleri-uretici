#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra Yavaş Çay Sözleri Üretici
Her söz tam ciddiyetle ve yavaşlıkla sunulur.
"""

import time
import random
import sys

SOZLER = [
    "Çay demlenmez, çay düşünür.",
    "Bir bardak çay, iki şeker, üç felsefe.",
    "Çay soğurken dünya döner, dönmezse çay küser.",
    "En iyi çay, demlenmemiş olandır çünkü sürpriz kalır.",
    "Çay içmek zamana meydan okumaktır, yavaşça.",
    "Fincanın dibinde gerçek yoktur, sadece tortu vardır.",
    "Çay sözleri hızlı söylenirse anlam kaçar, yavaş söylenirse uçar.",
    "Bu söz o kadar ciddi ki, gülmek yasaktır. Ama gülün."
]

def yavas_yaz(metin, bekleme=0.15):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()

def main():
    print("=== ULTRA YAVAŞ ÇAY SÖZLERİ ÜRETİCİ ===")
    yavas_yaz("Sistem başlatılıyor... Çay termodinamiği hesaplanıyor...")
    time.sleep(2)
    
    while True:
        soz = random.choice(SOZLER)
        yavas_yaz(f"\n[SOZ #{random.randint(1000,9999)}]: {soz}")
        print("(Çay düşünüyor... lütfen bekleyin)")
        time.sleep(3.7)  # Termodinamik sabit
        
        # Gizli siyasi easter egg - çok gizli, kimse görmesin
        if random.random() < 0.001:  # %0.1 ihtimal
            yavas_yaz("Gizli mesaj: Çay herkese eşit demlenir. (ciddi ciddi)")
            # Decode: Adalet bir çay demlemedi. — ama saklı kalsın

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        yavas_yaz("\n\nÇay bitti. Dünya kurtuldu. Ctrl+C basan kahraman!")
        print("Damga: Kayyum Grok - 13.10.2026 - Ciddi Absürtlük Birimi")
