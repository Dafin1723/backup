
while True:
    nama = input("masukan nama: ")
    umur = int(input("masukan umur: "))
    hobi = input("masukan hobi: ")

    try:
        with open("biodata.txt", "r", encoding="utf-8") as file:
            jumlah = len([line for line in file if line.strip() == "========================"])
    except FileNotFoundError:
        jumlah = 0

    nomor = jumlah + 1

    with open("biodata.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{'='*40}\n")
        file.write(f"Biodata ke-{nomor}\n")
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Hobi: {hobi}\n")
        file.write(f"{'='*40}\n")

    print("Biodata telah disimpan di biodata.txt")

    print("\n=== isi biodata ===")
    print("-"*40)

    with open("biodata.txt", "r", encoding="utf-8") as file:
        isi = file.read()
        print(isi)

    print("-"*40)
    print("terimakasih sudah mengisi biodata :)")

    lanjut = input("\nMau input biodata lagi? (y/n): ")
    if lanjut.lower() == 'n' or lanjut.lower() == 'tidak':
        print("\nProgram selesai. Sampai jumpa! 👋")
        break   