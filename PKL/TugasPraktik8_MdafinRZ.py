def fungsi_total_nilai(var_harian, var_uts, var_uas):
    """
    Menghitung total nilai akhir berdasarkan bobot:
    - Harian: 30%
    - UTS: 30%
    - UAS: 40%
    """
    harian = int(var_harian) * 0.3
    uts = int(var_uts) * 0.3
    uas = int(var_uas) * 0.4
    
    total = harian + uts + uas
    return total


def fungsi_cek_nilai(nilai_angka):
    """
    Mengonversi nilai angka menjadi nilai huruf
    Ketentuan:
    85 - 100 : A
    70 - 84  : B
    55 - 69  : C
    40 - 54  : D
    < 40     : E
    """
    if nilai_angka >= 85:
        return 'A'
    elif nilai_angka >= 70:
        return 'B'
    elif nilai_angka >= 55:
        return 'C'
    elif nilai_angka >= 40:
        return 'D'
    else:
        return 'E'


def fungsi_nilai_ke():
    """
    Fungsi utama: meminta input nilai sebanyak 2 kali,
    menampilkan hasil per input, lalu rata-rata akhir.
    """
    daftar_total = []  

    print("Program Hitung Nilai dengan Fungsi")
    print("=" * 30)

    for i in range(1, 3):
        print(f"\n--- Nilai Ke {i} ---")
        try:
            harian = input("Nilai Harian : ")
            uts = input("Nilai UTS    : ")
            uas = input("Nilai UAS    : ")

            total = fungsi_total_nilai(harian, uts, uas)
            daftar_total.append(total)

            huruf = fungsi_cek_nilai(total)
            print(f"Total nilai ke-{i}: {total:.1f}")
            print(f"Nilai huruf ke-{i}: {huruf}")

        except ValueError:
            print("Error: Pastikan input berupa angka bulat!")
            daftar_total.append(0)  

    if len(daftar_total) >= 2:
        rata_rata = sum(daftar_total) / 2
        huruf_akhir = fungsi_cek_nilai(rata_rata)

        print("\n" + "=" * 30)
        print("Total nilai yang didapat : {:.1f}".format(rata_rata))
        print("Total nilai dalam huruf  : {}".format(huruf_akhir))
    else:
        print("Tidak ada data nilai yang valid.")


if __name__ == "__main__":
    fungsi_nilai_ke()