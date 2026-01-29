siswa = [] 

while True:
    print("1. Masukan data siswa")
    print("2. Tampilkan data siswa")
    print("3. Hapus data siswa")
    print("0. Keluar")
    print("====================")
    
    pilihan = input("Masukan pilihan kamu : ")
    
    if pilihan == "1":
        while True:
            nis = input("masukan nis : ").strip()
            
            nis_sudah_ada = False
            for data in siswa:
                if data["nis"] == nis:
                    nis_sudah_ada = True
                    break
            
            if nis_sudah_ada:
                print("Error: NIS sudah terdaftar! Silakan masukkan NIS yang lain.\n")
            else:
                nama = input("masukan nama : ").strip()
                asal = input("masukan asal : ").strip()
                
                data_siswa = {"nis": nis, "nama": nama, "asal": asal}
                siswa.append(data_siswa)
                
                print("Data siswa berhasil ditambahkan!\n")
                break  
    
    elif pilihan == "2":
        if len(siswa) == 0:
            print("Belum ada data siswa yang dimasukkan.\n")
        else:
            print("Daftar Data Siswa:")
            for data in siswa:
                print(f"NIS: {data['nis']}, Nama: {data['nama']}, Asal: {data['asal']}")
            print()  
    
    elif pilihan == "3":
        if len(siswa) == 0:
            print("Tidak ada data siswa untuk dihapus.\n")
        else:
            nis_hapus = input("masukan nis : ")
            ditemukan = False
            for data in siswa:
                if data["nis"] == nis_hapus:
                    siswa.remove(data)  
                    print("Data siswa berhasil dihapus!\n")
                    ditemukan = True
                    break
            if not ditemukan:
                print("NIS tidak ditemukan.\n")
    
    elif pilihan == "0":
        print("Terima kasih, program selesai.")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")