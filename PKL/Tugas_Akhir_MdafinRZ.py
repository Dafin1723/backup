def tampilkan_menu():
    print("\n" + "="*50)
    print("       APLIKASI DAFTAR BELANJA SEDERHANA ")
    print("="*50)
    print("1. Tambah barang ke daftar")
    print("2. Lihat daftar belanja")
    print("3. Hapus barang dari daftar")
    print("4. Hitung total estimasi harga")
    print("5. Kosongkan daftar belanja")
    print("0. Keluar dari program")
    print("="*50)


def tambah_barang(daftar_belanja):
    nama = input("Masukkan nama barang: ").strip().title()
    try:
        harga = float(input("Masukkan estimasi harga (Rp): "))
        jumlah = int(input("Jumlah barang: "))
        
        if harga < 0 or jumlah <= 0:
            print("Harga tidak boleh negatif & jumlah harus lebih dari 0!")
            return
        
        ditemukan = False
        for item in daftar_belanja:
            if item["nama"] == nama:
                item["jumlah"] += jumlah
                item["total"] = item["jumlah"] * item["harga"]
                print(f"→ {nama} sudah ada, jumlah ditambahkan!")
                ditemukan = True
                break
        
        if not ditemukan:
            daftar_belanja.append({
                "nama": nama,
                "harga": harga,
                "jumlah": jumlah,
                "total": harga * jumlah
            })
            print(f"→ {nama} berhasil ditambahkan!")
            
    except ValueError:
        print("Input harga/jumlah harus berupa angka!")


def tampilkan_daftar(daftar_belanja):
    if not daftar_belanja:
        print("\nDaftar belanja masih kosong... :(")
        return
    
    print("\n" + "-"*60)
    print(f"{'No':<4} {'Nama Barang':<25} {'Harga':>12} {'Jumlah':>8} {'Subtotal':>12}")
    print("-"*60)
    
    for i, item in enumerate(daftar_belanja, 1):
        print(f"{i:<4} {item['nama']:<25} {item['harga']:>12,.0f} {item['jumlah']:>8} {item['total']:>12,.0f}")
    
    print("-"*60)


def hapus_barang(daftar_belanja):
    if not daftar_belanja:
        print("\nDaftar masih kosong, tidak ada yang bisa dihapus.")
        return
    
    tampilkan_daftar(daftar_belanja)
    try:
        nomor = int(input("\nMasukkan nomor barang yang ingin dihapus: "))
        if 1 <= nomor <= len(daftar_belanja):
            barang = daftar_belanja.pop(nomor-1)
            print(f"→ {barang['nama']} berhasil dihapus dari daftar!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")


def hitung_total(daftar_belanja):
    if not daftar_belanja:
        print("\nTotal belanja: Rp 0")
        return
    
    total = sum(item["total"] for item in daftar_belanja)
    print(f"\nTotal estimasi belanja: Rp {total:,.0f}")
    print(f"Jumlah jenis barang: {len(daftar_belanja)}")


def kosongkan_daftar(daftar_belanja):
    konfirmasi = input("\nYakin ingin mengosongkan SEMUA daftar? (y/n): ").lower()
    if konfirmasi == 'y':
        daftar_belanja.clear()
        print("Daftar belanja telah dikosongkan!")
    else:
        print("Operasi dibatalkan.")


print("\n" + "="*60)
print("   SELAMAT DATANG DI APLIKASI DAFTAR BELANJA SEDERHANA")
print("="*60)

daftar_belanja = []

while True:
    tampilkan_menu()
    
    pilihan = input("\nPilih menu (0-5): ").strip()
    
    if pilihan == '1':
        tambah_barang(daftar_belanja)
    elif pilihan == '2':
        tampilkan_daftar(daftar_belanja)
    elif pilihan == '3':
        hapus_barang(daftar_belanja)
    elif pilihan == '4':
        hitung_total(daftar_belanja)
    elif pilihan == '5':
        kosongkan_daftar(daftar_belanja)
    elif pilihan == '0':
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih nomor 0-5.")