# ADINDA YECINTHYA NURLIYANTI (222410102025)

import random

print("=====" " "
"Game Tebak Angka" " "
"=====")

angka = random.randint(0,100)
putaran = 0

for i in range (10):
    number = int(input(f"[Percobaan {i + 1}] Masukkan angka : "))
    putaran += 1
    if number < angka:
        print("Angka terlalu kecil")
        print(" ")
    elif number > angka:
        print("Angka terlalu besar")
        print(" ")
    elif number == angka:
        print("Angka anda benar setelah menebak", str(putaran), "kali putaran")
        break

    if putaran == 10:
        print(" ")
        print("Your game is over!")

print(" ")
print("Sampai Jumpa Lagi :)")
print(" ")
