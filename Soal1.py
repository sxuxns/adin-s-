print("===== Selamat Datang di Word Checker! =====")
print(" ")

kata = int(input("Jumlah kata : "))
listkata = 1

kata_kata = []

while listkata <= kata:
    word = input(f"Kata {listkata} : ")
    kata_kata.append(word)
    listkata += 1

print(" ")

for a in kata_kata:
    print("Ini hasilnya :")
    for i in range(0, len(a)):
        if i == 0:
            continue
        print(" ")
        huruf_sebelum = a[i-1]
        huruf_sesudah = a[i]

        selisih_huruf = ord(huruf_sebelum) - ord(huruf_sesudah)

        if selisih_huruf < 0:
            selisih_huruf2 = -(selisih_huruf)

        if ord(huruf_sebelum) < ord(huruf_sesudah):
            status = "itu sebelum"
            print(huruf_sebelum, status, huruf_sesudah, "dan selisihnya yaitu ", selisih_huruf2)
        elif ord(huruf_sebelum) > ord(huruf_sesudah):
            status = "itu sesudah"
            print(huruf_sebelum, status, huruf_sesudah, "dan selisihnya yaitu ", selisih_huruf)
        else:
            status = "sama dengan"
            print(huruf_sebelum, status, huruf_sesudah, "dan selisihnya yaitu ", selisih_huruf)
