menu = {
    "gorengan": 2000,
    "mie ayam": 10000
}

print("Selamat datang di kantin!")
print("Menu yang tersedia:")
for i, (nama, harga) in enumerate(menu.items(), start=1):
    print(f"{i}. {nama} - Rp{harga}")

pilih = input("Silakan pilih menu (ketik nama menu): ").lower()
jumlah = int(input("Masukkan jumlah pesanan: "))

item = list(menu.keys())[list(menu.keys()).index(pilih)]
harga = menu[item]
total_harga = harga * jumlah

print(f"total harga untuk {jumlah} porsi {item} adalah Rp{total_harga}")


while True:
    uang = int(input("Masukkan uang pembayaran: Rp"))
    if uang < total_harga:
        kekurangan = total_harga - uang
        print(f"Uang Anda kurang Rp{kekurangan}. Silakan masukkan jumlah yang cukup.")
    else:
        kembalian = uang - total_harga
        print(f"Pembayaran berhasil! Kembalian Anda: Rp{kembalian}")
        break

    