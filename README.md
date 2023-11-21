# BTC-Puzzle
BTC Puzzle üzerine yaptığım çalışmalar

# Puzzle1.py
Rastgele aldığı bir sayıyı ECC ile koordinatlarını hesaplayıp, bunları parçalara bölerek denemeler yapar.	

Örnek: 

Rastgele(Random) fonksiyonu ile bir sayı alır => 63637343750687453568793823633539557033132131772799798257422903207884653281588

Bu sayının X ve Y koordinatlarını hesaplar => 

X = 8afff22d1ed43d7921b92742caa53a37f17eb3e97e038e4de6960e2504dee00c

Y = 8885a9159157417b462becc2a30b5e24082c8a60f707e9fe52c8f3f357b591a5

Bu iki sayı ile sondan 17 basamağından başlayarak sondan 39. basamağına kadar çözülmemiş bulmacalar için özel anahtar oluşturup, adresler ile eşleşme olup olmadığını denetler.

Eğer eşleşme olursa, eşleşme olan özel anahtarı yazdırır ve programdan çıkış yapar.

Gereksinimler:

secp256k1.py, ice_secp256k1.dll (Windows için) veya ice_secp256k1.so (Linux için) aynı klasörde olmalı veya yeri belirtilmelidir.

