print("#"*55)
print("Program Hitung Jumlah Kata dan Karakter dengan Python")
print("#"*55)

input_kata = input("Masukkan Sebuah Kata: ")

kata = input_kata.split()

jumlah_kata = len(kata)
jumlah_karakter = len(input_kata)

dibalik = " ".join(reversed(kata))

print(f"Jumlah Kata: {jumlah_kata}")
print(f"Jumlah Karakter: {jumlah_karakter}")
print(f"Jika dibalik akan menampilkan kata : {dibalik}")
print("#"*55)
