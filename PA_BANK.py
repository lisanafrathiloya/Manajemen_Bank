import json
import os
from prettytable import PrettyTable
import pwinput
os.system("cls")




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        setengah_kiri = arr[:mid]
        setengah_kanan = arr[mid:]

        merge_sort(setengah_kiri)
        merge_sort(setengah_kanan)

        i = j = k = 0

        while i < len(setengah_kiri) and j < len(setengah_kanan):
            if setengah_kiri[i] < setengah_kanan[j]:
                arr[k] = setengah_kiri[i]
                i += 1
            else:
                arr[k] = setengah_kanan[j]
                j += 1
            k += 1

        while i < len(setengah_kiri):
            arr[k] = setengah_kiri[i]
            i += 1
            k += 1

        while j < len(setengah_kanan):
            arr[k] = setengah_kanan[j]
            j += 1
            k += 1




# Fungsi untuk menampilkan invoice
def generate_invoice(nama_pengguna, jumlah, jenis_transaksi, penerima=None, saldo_sisa=None):
    print("\n")
    invoice = f"=========================================\n"
    invoice += f"|             Bank Sisfor Union         |\n"
    invoice += f"=========================================\n"
    invoice += f"Nama Nasabah: {nama_pengguna}\n"
    invoice += f"Jenis Transaksi: {jenis_transaksi}\n"
    invoice += f"Jumlah: Rp. {jumlah:,.2f}\n"
    if jenis_transaksi == "Deposit" and saldo_sisa is not None:
        invoice += f"Saldo Sekarang: Rp. {saldo_sisa:,.2f}\n"
    if jenis_transaksi == "Penarikan" and saldo_sisa is not None:
        invoice += f"Saldo Sisa: Rp. {saldo_sisa:,.2f}\n"
    if penerima:
        invoice += f"Transfer ke: {penerima}\n"
    invoice += f"=========================================\n"
    return invoice





# Fungsi untuk menampilkan saldo dengan tampilan rapi
def display_saldo(nama_pengguna):
    print("\n")
    print("=========================================")
    print("|             Bank Sisfor Union         |")
    print("=========================================")
    print(f"Nama Nasabah: {nama_pengguna}      ")
    t = PrettyTable(['Rekening', 'Saldo (Rp)'])
    t.add_row(['Pribadi', f"Rp. {rekenings[nama_pengguna]:,.2f}"])
    print(t)
    print("Diatas adalah saldo anda")





# Fungsi untuk login dengan maksimal 3 kali percobaan
def login(max_attempts=3):
    attempts = 0  # Menginisialisasi hitungan percobaan
    while attempts < max_attempts:
        try:
            print("\n")
            print("=========================================")
            print("|                                       |")
            print("|  Selamat datang di Bank Sisfor Union  |")
            print("|                                       |")
            print("=========================================")
            print("\n")
            print("===================================")
            print("Silahkan Memilih Role bagian anda")
            print("===================================")
            print("=========================================")
            print("|1. Admin                               |")
            print("|2. Nasabah                             |")
            print("|3. Keluar                              |")
            print("=========================================")

            role = input("Pilih role sesuai dengan nomor (1, 2, 3): ").strip()

            if role == "1":
                print("==================================")
                print("Warning! batas percobaan adalah 3!")
                print("==================================")
                username = input("Masukkan username admin (Alphabet): ")
                username = username.lower().strip()
                password = pwinput.pwinput("Masukkan password admin (4 Digit): ")
                password = password.replace(" ", "").strip()
                if username == "farhan" and password == "2005":
                    print("==============================")
                    print("Selamat datang interface Admin")
                    print("==============================")
                    return role, username
                else:
                    print("=============================")
                    print("Username  Passoword salah")
                    print("=============================")
                    attempts += 1
            elif role == "2":
                print("==================================")
                print("Warning! batas percobaan adalah 3!")
                print("==================================")
                username = input("Masukkan Username (Alphabet): ")
                username = username.lower().strip()
                password = pwinput.pwinput("Masukkan PIN (4 digit): ")
                password = password.replace(" ", "").strip()
                if username in pengguna and pengguna[username]["kata_sandi"] == password:
                    print("=====================")
                    print("Login nasabah sukses.")
                    print("=====================")
                    return role, username
                else:
                    print("===============================")
                    print("Login nasabah gagal. Coba lagi.")
                    print("===============================")
                    attempts += 1
            elif role == "3":
                print("\n")
                print("===================================")
                print("|                                 |")
                print("|  Terimakasih telah berkunjung   |")
                print("|                                 |")
                print("===================================")
                exit()
            else:
                print("\n")
                print("===================================")
                print("|      pilihan tidak valid        |")
                print("===================================")
                
        except KeyboardInterrupt:
            print("\n")
            print("=======================")
            print("Jangan menekan ctrl + c")
            print("=======================")
        

    print("\n")
    print("===================================")
    print("|   Melebihi batas percobaan login  |")
    print("===================================")
    exit()





# Fungsi untuk melakukan login sebagai nasabah
def login_sebagai_nasabah(username):
    while True:
        try:
            print("=======================================")
            print("  Apa yang ingin anda lakukan hari ini?")
            print("=======================================")
            print("\n")
            print(f"Anda Login sebagai Nasabah: {username}")
            print("=============Menu Nasabah=============")
            print("|  1. Cek Saldo                      |")
            print("|  2. Deposit                        |")
            print("|  3. Tarik Tunai                    |")
            print("|  4. Transfer                       |")
            print("|  5. Logout                         |")
            print("======================================")
            opsi = input("Pilih aksi yang ingin dilakukan: ") .strip()

            if opsi == "1":
                display_saldo(username)
            elif opsi == "2":
                deposit(username)
            elif opsi == "3":
                tarik_tunai(username)
            elif opsi == "4":
                transfer(username)
            elif opsi == "5":
                break
            else:
                print("\n")
                print("===================================")
                print("|      pilihan tidak valid        |")
                print("===================================")
        except KeyboardInterrupt:
            print("\n")
            print("=======================")
            print("Jangan menekan ctrl + c")
            print("=======================")





# Fungsi untuk menampilkan daftar rekening (CRUD) oleh admin
def admin_show_accounts():
    print("\n")
    t = PrettyTable(['No', 'Nama Pengguna', 'Saldo (Rp)'])
    for i, (username, balance) in enumerate(rekenings.items(), start=1):
        t.add_row([i, username, f"Rp. {balance:,.2f}"])
    print(t)





# Fungsi untuk menambahkan rekening (CRUD) oleh admin
def admin_create_account():
    try:
        username = input("Masukkan nama rekening baru: ")
        username = username.lower().strip()
        if not username.isalpha():
            print("\n")
            print("=====================================")
            print("Username harus berupa huruf alfabet.")
            print("=====================================")
            return

        if username in rekenings:
            print("\n")
            print("====================")
            print("|Rekening sudah ada|")
            print("====================")
            return

        # Meminta admin untuk mengatur PIN untuk nasabah
        pin = input("Masukkan PIN untuk akun ini : ")
        pin = pin.replace(" ", "").strip()  # Menghapus spasi dari PIN pakai replace
        if pin == 1234 or pin == 0000 or pin == 1111 or pin == 2222 or pin == 3333 or pin == 4444 or pin == 5555 or pin == 6666 or pin == 7777 or pin == 8888 or pin == 9999:
            print("\n")
            print("======================")
            print(" pin anda kurang aman ")
            print("=======================")
            return
        if not pin.isdigit() or len(pin) != 4:
            print("\n")
            print("====================================")
            print("    PIN harus berupa 4 digit angka  ")
            print("====================================")
            return

        # Membuat akun dengan saldo awal 0 dan PIN yang diberikan
        rekenings[username] = 0
        pengguna[username] = {"kata_sandi": pin}
        simpan_data()
        simpan_data_pengguna()  # Menyimpan data pengguna termasuk PIN
        print("\n")
        print("=========================================================================")
        print(f"Rekening untuk {username} berhasil dibuat dengan PIN {pin}.")
        print("=========================================================================")
    except KeyboardInterrupt:
        print("\n")
        print("=======================")
        print("Jangan menekan ctrl + c")
        print("=======================")





# Fungsi untuk menghapus rekening (CRUD) oleh admin
def admin_delete_account():
    try:
        username = input("Masukkan nama pengguna yang akan dihapus: ")
        username = username.lower().strip()
        if username in rekenings:
            del rekenings[username]
            simpan_data()
            simpan_data_pengguna()
            print("\n")
            print("========================================================")
            print(f"Rekening untuk {username} berhasil dihapus.")
            print("========================================================")
        else:
            print("=========================")
            print("Rekening tidak ditemukan.")
            print("=========================")
    except KeyboardInterrupt:
        print("\n")
        print("=======================")
        print("Jangan menekan ctrl + c")
        print("=======================")





# Fungsi untuk mencari rekening (CRUD) oleh admin
def admin_search_account():
    try:
        search_username = input("Masukkan nama pengguna yang ingin dicari: ")
        search_username = search_username.lower().strip()
        
        if search_username in rekenings:
            t = PrettyTable(['Nama Pengguna', 'Saldo (Rp)'])
            t.add_row([search_username, f"Rp. {rekenings[search_username]:,.2f}"])
            print("\nRekening ditemukan:")
            print(t)
        else:
            print("\n")
            print("=========================")
            print("Rekening tidak ditemukan.")
            print("=========================")
    except KeyboardInterrupt:
        print("\n")
        print("=======================")
        print("Jangan menekan ctrl + c")
        print("=======================")





# Fungsi untuk pembaruan PIN (CRUD) oleh admin
def admin_update_pin():
    try:
        username = input("Masukkan nama pengguna yang akan diperbarui PIN-nya: ")
        username = username.lower().strip()
        if username in pengguna:
            new_pin = pwinput.pwinput("Masukkan PIN baru: ")
            new_pin = new_pin.replace(" ", "").strip  # Menghapus spasi dari PIN
            pengguna[username]["kata_sandi"] = new_pin
            simpan_data_pengguna()  # Menyimpan data pengguna dengan PIN baru
            print("\n")
            print("========================================================")
            print(f"PIN untuk {username} berhasil diperbarui.")
            print("========================================================")
        else:
            print("\n")
            print("=========================")
            print("Rekening tidak ditemukan.")
            print("=========================")
    except KeyboardInterrupt:
        print("\n")
        print("=======================")
        print("Jangan menekan ctrl + c")
        print("=======================")





# Fungsi untuk deposit
def deposit(nama_pengguna):
    while True:
        try:
            jumlah = float(input("Masukkan jumlah yang akan Anda deposit (Rp): "))
            if jumlah < 0:
                print("\n")
                print("=============================")
                print("Jumlah deposit harus positif.")
                print("=============================")
                print("\n")
            elif jumlah > 10000000:
                print("\n")
                print("===========================================")
                print("Batas Maksimal Deposit adalah Rp.10.000.000")
                print("===========================================")
                print("\n")
            else:
                rekenings[nama_pengguna] += jumlah
                simpan_data()
                saldo_sekarang = rekenings[nama_pengguna]
                print("\n")
                print(f"Berhasil menambahkan Rp. {jumlah:,.2f} ke rekening Anda.")
                invoice = generate_invoice(nama_pengguna, jumlah, "Deposit", saldo_sisa=saldo_sekarang)
                print(invoice)
                break
        except ValueError:
            print("\n")
            print("===========================================================")
            print("Harap masukkan nominal hanya berupa angka tanpa elemen lain")
            print("===========================================================")
            print("\n")
        except KeyboardInterrupt:
            print("\n")
            print("=======================")
            print("Jangan menekan ctrl + c")
            print("=======================")
            print("\n")





# Fungsi untuk penarikan
def tarik_tunai(nama_pengguna):
    display_saldo(nama_pengguna)
    while True:
        try:
            if rekenings[nama_pengguna] == 0:
                    print("====================")
                    print("  Saldo anda = 0    ")
                    print("====================")
                    print("  Harap isi dahulu  ")
                    print("====================")
                    break
            jumlah = float(input("Masukkan jumlah yang akan Anda tarik (Rp): "))
            if jumlah < 0:
                print("\n")
                print("=================================")
                print("Jumlah tarik tunai harus positif.")
                print("=================================")
                print("\n")
            elif jumlah > 10000000:
                print("\n")
                print("===============================================")
                print("Batas Maksimal tarik tunai adalah Rp.10.000.000")
                print("===============================================")
                print("\n")
            elif rekenings[nama_pengguna] < jumlah:
                print("======================")
                print("Saldo tidak mencukupi.")
                print("======================")
            else:
                rekenings[nama_pengguna] -= jumlah
                simpan_data()
                saldo_sisa = rekenings[nama_pengguna]
                print("\n")
                print(f"Berhasil menarik Rp. {jumlah:,.2f} dari rekening Anda.")
                invoice = generate_invoice(nama_pengguna, jumlah, "Penarikan", saldo_sisa=saldo_sisa)
                print(invoice)
                break
        except ValueError:
            print("\n")
            print("===========================================")
            print("Masukkan hanya angka dan tanpa elemen lain.")
            print("===========================================")
            print("\n")
        except KeyboardInterrupt:
            print("\n")
            print("=======================")
            print("Jangan menekan ctrl + c")
            print("=======================")
            print("\n")





# Fungsi untuk mentransfer uang ke rekening lain
def transfer(nama_pengguna):
    print("\n")
    tujuan = input("Masukkan nama pengguna yang akan ditransfer: ")
    tujuan = tujuan.lower().strip()
    if tujuan in rekenings:
        display_saldo(nama_pengguna)
        while True:
            try:
                if rekenings[nama_pengguna] == 0:
                    print("====================")
                    print("  Saldo anda = 0    ")
                    print("====================")
                    print("  Harap isi dahulu  ")
                    print("====================")
                    break
                jumlah = float(input(f"Masukkan jumlah yang akan Anda transfer ke {tujuan} (Rp): "))
                if jumlah <= 0:
                    print("\n")
                    print("===================================")
                    print("Jumlah transfer harus lebih dari 0.")
                    print("===================================")
                    print("\n")
                elif jumlah > 10000000:
                    print("\n")
                    print("============================================")
                    print("Batas Maksimal Transfer adalah Rp.10.000.000")
                    print("============================================")
                    print("\n")
                elif rekenings[nama_pengguna] < jumlah:
                    print("======================")
                    print("Saldo tidak mencukupi.")
                    print("======================")
                else:
                    rekenings[nama_pengguna] -= jumlah
                    rekenings[tujuan] += jumlah
                    simpan_data()
                    print(f"Berhasil mentransfer Rp. {jumlah:,.2f} ke {tujuan}.")
                    invoice = generate_invoice(nama_pengguna, jumlah, "Transfer", penerima=tujuan)
                    print(invoice)
                    break
            except ValueError:
                print("\n")
                print("===========================================")
                print("Masukkan hanya angka dan tanpa elemen lain.")
                print("===========================================")
                print("\n")
            except KeyboardInterrupt:
                print("\n")
                print("=======================")
                print("Jangan menekan ctrl + c")
                print("=======================")
                print("\n")

    else:
        print("\n")
        print("================================")
        print("Rekening tujuan tidak ditemukan.")
        print("================================")
        print("\n")





# Fungsi untuk menyimpan data rekening ke file JSON
def simpan_data():
    with open("data_bank.json", "w") as file:
        json.dump(rekenings, file, indent=4)




# Inisialisasi data rekening
try:
    with open("data_bank.json", "r") as file:
        rekenings = json.load(file)
except FileNotFoundError:
    rekenings = {}




# Fungsi untuk menyimpan data pengguna ke file JSON
def simpan_data_pengguna():
    with open("pengguna.json", "w") as file:
        json.dump(pengguna, file, indent=4)




# Inisialisasi data pengguna
try:
    with open("pengguna.json", "r") as file:
        pengguna = json.load(file)
except FileNotFoundError:
    pengguna = {}





# Main Program
while True:
    role, username = login()
    try:
        if role == "1":
                while True:
                    print("\n")
                    print("=========================================")
                    print("|                                       |")
                    print("|         SELAMAT DATANG ADMIN          |")
                    print("|                                       |")
                    print("=========================================")
                    print("\n")
                    print("===========MENU ADMIN===============")
                    print("|  1. Tampilkan Rekening            |")
                    print("|  2. Tambah Rekening               |")
                    print("|  3. Hapus Rekening                |")
                    print("|  4. Update PIN                    |")
                    print("|  5. Cari Rekening                 |")  
                    print("|  6. sorting (menurut abjad nama)  |")
                    print("|  7. Logout                        |")
                    print("====================================")
                    print("\n")
                    opsi = input("Pilih opsi: ") .strip()
                    
                    # Dalam loop menu admin
                    if opsi == "1":
                        admin_show_accounts()
                    elif opsi == "2":
                        admin_create_account()
                    elif opsi == "3":
                        admin_delete_account()
                    elif opsi == "4":
                        admin_update_pin()  
                    elif opsi == "5":
                        admin_search_account()
                    elif opsi == "6":
                        sorted_accounts = sorted(rekenings.items(), key=lambda x: x[0])  # Mengurutkan berdasarkan nama akun
                        merge_sort(sorted_accounts)  # Mengurutkan daftar akun yang sudah diurutkan menggunakan Merge Sort
                        print("Daftar Rekening (Setelah Diurutkan):")
                        for i, (username, balance) in enumerate(sorted_accounts, start=1):
                            print(f"{i}. Nama Pengguna: {username}, Saldo: Rp. {balance:,.2f}")
                    elif opsi == "7":
                        break
                    else:
                        print("\n")
                        print("===================================")
                        print("|    Pilihan admin tidak valid    |")
                        print("===================================")
        else:
            login_sebagai_nasabah(username)
    except KeyboardInterrupt:
        print("\n")
        print("=======================")
        print("Jangan menekan ctrl + c")
        print("=======================")


