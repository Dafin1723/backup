def hitung_luas_persegi_panjang(p, l):
    """Menghitung luas persegi panjang dengan validasi ketat"""
    assert isinstance(p, (int, float)), "Panjang harus angka (int/float)"
    assert isinstance(l, (int, float)), "Lebar harus angka (int/float)"
    
    assert p > 0, "Panjang harus lebih dari nol bang!"
    assert l > 0, "Lebar ga boleh nol atau minus ya!"
    
    return p * l


print("=== Kalkulator Luas Persegi Panjang (Versi Anti-Copas) ===")

try:
    panjang = float(input("Panjang sisi (cm): "))
    lebar   = float(input("Lebar sisi (cm): "))
    
    # Tambah validasi kreatif biar beda
    assert panjang != lebar, "Wah ini jadi persegi dong, bukan persegi panjang!"
    
    hasil = hitung_luas_persegi_panjang(panjang, lebar)
    
    print(f"\nLuasnya adalah → {hasil:.2f} cm²")
    print(f"({panjang} × {lebar} = {hasil})")

except AssertionError as err:
    print("\nYahh ketahuan errornya:")
    print("→", str(err))
    print("Coba input ulang dengan benar !")

except ValueError:
    print("\nInputnya harus angka dong bang, bukan huruf/kata!")

except Exception as apa:
    print("\nAda yang aneh nih:", str(apa))

finally:
    print("\n=== Program abisss. Makasih udah nyoba! ===")