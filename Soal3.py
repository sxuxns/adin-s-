print("===== Pembuktian Kenyamanan String =====")
print(" ")

kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

Entr_str = input("Enter a String : ")

urutanhuruf = []
result = True

for huruf_1 in Entr_str:
    if huruf_1 in kiri:
        urutanhuruf.append(1)
    elif huruf_1 in kanan:
        urutanhuruf.append(2)

for huruf_2 in range(len(urutanhuruf)-1):
    if urutanhuruf[huruf_2] == urutanhuruf[huruf_2+1]:
        result = False

print('Result : ', result)
