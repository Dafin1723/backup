from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Data login lo
EMAIL = "muhamaddafinrifatzulfaqqar@smkithsanulfikri.sch.id"
PASSWORD = "crushsayaa6"  # Ganti kalau udah berubah!

# Setup browser biar mirip manusia
options = Options()
# options.add_argument("--headless")  # JANGAN aktifkan dulu, biar bisa solve captcha
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)  # Tunggu lebih lama kalau lambat

try:
    print("1. Membuka halaman login Gamelab...")
    driver.get("https://www.gamelab.id/login")
    time.sleep(3)  # Biar page full load

    print("2. Mengisi email dan password otomatis...")
    # Isi email
    email_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='email'], input[name='email'], input[placeholder*='email']")
    ))
    email_field.clear()
    email_field.send_keys(EMAIL)

    # Isi password
    password_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='password'], input[placeholder*='kata sandi']")
    ))
    password_field.clear()
    password_field.send_keys(PASSWORD)

    print("\n=== MANUAL STEP SEKARANG ===")
    print("→ Solve CAPTCHA: ketik ulang angka yang muncul di gambar")
    print("→ Kalau ada cookie banner muncul sekarang → klik 'Terima' / 'Izinkan' dulu")
    print("→ Lalu klik tombol 'Masuk' / 'Login'")
    print("→ Tunggu sampai masuk dashboard (lihat 'Selamat Pagi' atau progres magang)")
    print("Setelah login BERHASIL dan dashboard muncul → kembali ke terminal & tekan ENTER")
    input("Tekan ENTER setelah login sukses...")

    # Setelah lo konfirm login OK, cek cookie lagi (kalau muncul pas redirect)
    print("\nCek cookie banner setelah login...")
    try:
        cookie_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'terima') or contains(text(),'Accept') or contains(text(),'Izinkan') or contains(text(),'OK') or contains(@class,'cookie')][1]")
        ))
        cookie_button.click()
        print("Cookie consent diterima setelah login!")
        time.sleep(2)
    except:
        print("Tidak ada cookie banner setelah login (sudah di-handle atau tidak muncul).")

    # Lanjut ke dashboard / halaman absen
    print("Menuju dashboard...")
    driver.get("https://www.gamelab.id/dashboard")  # Ganti kalau URL absen khusus (misal /magang/presensi)

    time.sleep(4)

    # Klik tombol absen (Absen Pulang / Masuk)
    print("Mencari tombol absen...")
    try:
        absen_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Absen Pulang') or contains(text(),'Absen Masuk') or contains(text(),'Absen') or contains(@class,'absen-pulang') or contains(@class,'green')][1]")
        ))
        absen_button.click()
        print("✅ Absen berhasil diklik! Cek konfirmasi di browser.")
        time.sleep(5)  # Tunggu popup sukses kalau ada
    except:
        print("❌ Tombol absen tidak ketemu otomatis.")
        print("Manual fix:")
        print("1. Di browser, klik kanan tombol absen hijau → Inspect")
        print("2. Copy teks tombol atau XPath (contoh: //button[text()='Absen Pulang'] )")
        print("3. Ganti di script bagian XPath di atas, lalu run ulang.")
        print("Browser tetap terbuka untuk dicek.")

    print("\nProses hampir selesai. Browser terbuka 15 detik lagi buat verifikasi...")
    time.sleep(15)

except Exception as e:
    print(f"\nError terjadi: {str(e)}")
    print("Browser tetap terbuka untuk debug. Tutup sendiri setelah selesai cek.")

finally:
    print("\nScript selesai dijalankan. Semua step done!")
    # driver.quit()  # Uncomment kalau mau auto tutup browser