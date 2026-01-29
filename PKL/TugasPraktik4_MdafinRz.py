NIS = int(input("Masukkan NIS milikmu: "))
Nama_siswa = (input("Masukkan Nama Siswa: "))
Mata_pelajaran = input("Masukkan Nama Mata Pelajaran: ")
Nilai_absensi = int(input("Masukkan Nilai Absensi: "))
Nilai_tugas = int(input("Masukkan Nilai Tugas: "))
Nilai_UTS = int(input("Masukkan Nilai UTS: "))
Nilai_UAS = int(input("Masukkan Nilai UAS: "))

nilai_akhir = (0.20 * Nilai_absensi) + (0.25 * Nilai_tugas) + (0.25 * Nilai_UTS) + (0.30 * Nilai_UAS)

if nilai_akhir > 90:
    keterangan = "Sangat Memuaskan"
elif nilai_akhir > 80:
    keterangan = "Memuaskan"
elif nilai_akhir > 70:
    keterangan = "Cukup"
else:
    keterangan = "Kurang"

print("################################################")
print("PROGRAM HITUNG NILAI MATA PELAJARAN DENGAN PYTHON")
print("################################################\n")
print(f"NIS             : {NIS}")
print(f"Nama Siswa      : {Nama_siswa}")
print(f"Mata Pelajaran  : {Mata_pelajaran}")
print(f"Nilai Akhir     : {nilai_akhir:.2f}")
print(f"Keterangan      : {keterangan}")