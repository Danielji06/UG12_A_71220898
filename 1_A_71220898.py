awal = int(input("Masukkan awal deret: "))
akhir = int(input("Masukkan akhir deret: "))
for i in range(awal,akhir):
    if i%2==0 and i%6>>0 and i%3>>0:
        print(i, end="\t")
        continue
       