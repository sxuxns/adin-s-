print("======= Selamat Datang di Program Tanya Sapi =======")
print(" ")

print("- Daftar Sapi -")
print("1. Sapi Warrior")
print("2. Sapi Mage")
print("3. Sapi Assasin")
print("4. Sapi Nolep")
print(" ")

sapi = int(input("Berapa Jumlah Sapimu : "))
kodesapi = 1
kode = 0
total_waktu = 0
lamahari = 0

list_sapi = []

while kodesapi <= sapi:
    jenissapi = int(input(f"Kode sapimu yang ke-{kodesapi}: "))
    list_sapi.append(jenissapi)
    kodesapi += 1

    if jenissapi == 1:
        lamahari = 690

    elif jenissapi == 2:
        lamahari = 420

    elif jenissapi == 3:
        lamahari = 530
        
    elif jenissapi == 4:
        lamahari = 330

    total_waktu = total_waktu + lamahari
    kode += 1

tahun = total_waktu // 365
sisahari = total_waktu % 365
bulan = sisahari // 30
hari = sisahari % 30

print(" ")
print("Hasil :")
print("Jadi, sapi-sapimu akan dewasa dalam", tahun, "tahun",
bulan, "bulan", hari, "hari")
print(" ")