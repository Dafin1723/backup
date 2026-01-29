print("################################################")
print("PROGRAM HITUNG NILAI MATA PELAJARAN DENGAN PYTHON")
print("################################################\n")

NIS = int(input("Masukkan NIS milikmu: "))
Nama_siswa = input("Masukkan Nama Siswa: ")
Mata_pelajaran = input("Masukkan Nama Mata Pelajaran: ")
Nilai_absensi = int(input("Masukkan Nilai Absensi: "))
Nilai_tugas = int(input("Masukkan Nilai Tugas: "))
Nilai_UTS = int(input("Masukkan Nilai UTS: "))
Nilai_UAS = int(input("Masukkan Nilai UAS: "))

# Hitung nilai akhir
nilai_akhir = (Nilai_absensi + Nilai_tugas + Nilai_UTS + Nilai_UAS) / 4

# Tentukan keterangan (logika benar: dari tertinggi)
if nilai_akhir > 90:
    keterangan = "Sangat Memuaskan"
elif nilai_akhir > 80:
    keterangan = "Cukup"
elif nilai_akhir > 70:
    keterangan = "Baik"
else:
    keterangan = "Kurang"

# Output hasil
print("\n___________________________________")
print(f"NIS             : {NIS}")
print(f"Nama Siswa      : {Nama_siswa}")
print(f"Mata Pelajaran  : {Mata_pelajaran}")
print(f"Nilai Akhir     : {nilai_akhir:.2f}")  # dibulatkan 2 desimal
print(f"Keterangan      : {keterangan}")