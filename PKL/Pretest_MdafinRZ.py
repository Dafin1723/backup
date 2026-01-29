
print("=== PROGRAM HITUNG RATA-RATA 5 SEMESTER ===")
print("Masukkan nilai rapor tiap semester")

semester1 = float(input("Nilai Semester 1: "))
semester2 = float(input("Nilai Semester 2: "))
semester3 = float(input("Nilai Semester 3: "))
semester4 = float(input("Nilai Semester 4: "))
semester5 = float(input("Nilai Semester 5: "))

jumlah = semester1 + semester2 + semester3 + semester4 + semester5
rata_rata = jumlah / 5

print("\n=== HASIL ===")
print("Nilai Semester 1 :", semester1)
print("Nilai Semester 2 :", semester2)
print("Nilai Semester 3 :", semester3)
print("Nilai Semester 4 :", semester4)
print("Nilai Semester 5 :", semester5)
print("Jumlah semua nilai :", jumlah)
print("Rata-rata 5 semester :", rata_rata)
print("Yakin Mau SNBP?, klo nilai mu segini")