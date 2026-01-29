import sqlite3
import os

if os.path.exists('inventaris.db'):
    os.remove('inventaris.db')

print("-----membuka koneksi ke database sqlite-----")
koneksi = sqlite3.connect('inventaris.db')
kursor = koneksi.cursor()
print("koneksi berhasil")

print("-----membuat tabel inventaris-----")
kursor.execute('''
    CREATE TABLE IF NOT EXISTS barang (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_barang TEXT NOT NULL,
        kategori TEXT,
        stok INTEGER,
        harga REAL
    )
''')

koneksi.commit()
print("tabel inventaris berhasil dibuat")
data_awal = [
    ('Laptop', 'Elektronik', 10, 750.00),
    ('Meja', 'Furnitur', 5, 150.00),
    ('Kursi', 'Furnitur', 20, 85.00),
    ('Smartphone', 'Elektronik', 15, 500.00),
    ('kebel rusak ', 'sampah', 0, 0)
]

kursor.executemany('''
    INSERT INTO barang (nama_barang, kategori, stok, harga)
    VALUES (?, ?, ?, ?)
''', data_awal) 
koneksi.commit()
print("data awal berhasil dimasukkan ke tabel inventaris")

print("-----READ Data-----")
kursor.execute('SELECT * FROM barang')
semua_barang = kursor.fetchall()
for barang in semua_barang:
    print(barang)


print("\n-----UPDATE Data-----")
kursor.execute('''
    UPDATE barang
    SET stok = 12, harga = 700.00
    WHERE nama_barang = 'Laptop'
''')
koneksi.commit()
print("data berhasil diupdate")


print("\n-----DELETE Data-----")
kursor.execute('delete from barang WHERE stok = 0')
koneksi.commit()
print("data dengan stok 0 berhasil dihapus")

print("\n-----Data akhir-----")
kursor.execute('SELECT * FROM barang')
final_barang = kursor.fetchall()
for barang in final_barang:
    print(barang)


kursor.close()
koneksi.close()
print("koneksi ke database ditutup")