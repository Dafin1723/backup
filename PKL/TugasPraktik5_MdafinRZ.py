print("Program Hitung Bilangan habis dibagi 3 dan 5 [1-100]")
print("----------------------------------------------------------")

hitung = 0
jumlah = 0

for bil in range(1, 101):
    if bil % 3 == 0 and bil % 5 == 0:
        print(f"Bilangan pada index ke- {bil-1} habis dibagi 3 dan 5 adalah {bil}")
        hitung += 1
        jumlah += bil

print("----------------------------------------------------------")
print(f"Banyak Bilangan yang habis dibagi 3 dan 5 adalah {hitung}")
print(f"Jumlah dari semua bilangan habis dibagi 3 dan 5 adalah {jumlah}")