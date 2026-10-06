import os
import time
import pwinput

os.system('cls' if os.name == 'nt' else 'clear')

database_akun = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "abc", "role": "user"}
}

daftar_tanaman = {
    "1": {"nama": "Anggrek", "jenis": "Indoor", "status": "Sudah disiram"},
    "2": {"nama": "Mawar", "jenis": "Outdoor", "status": "Belum disiram"},
    "3": {"nama": "Melati", "jenis": "Outdoor", "status": "Sudah disiram"},
    "4": {"nama": "Lavender", "jenis": "Outdoor", "status": "Sudah disiram"},
    "5": {"nama": "Peace Lily", "jenis": "Indoor", "status": "Belum disiram"}
}

def rapihkan_id_tanaman(data_lama):
    daftar_baru = {}
    nomor = 1
    
    for key in data_lama:
        daftar_baru[str(nomor)] = data_lama[key]
        nomor = nomor + 1
        
    return daftar_baru

def lihat_tanaman():
    print("\n========== DAFTAR TANAMAN ==========")
    if len(daftar_tanaman) == 0:
        print("Daftar tanaman masih kosong!")
        return False

    for id_tanaman in daftar_tanaman:
        info = daftar_tanaman[id_tanaman]
        print("[" + id_tanaman + "] Nama: " + info["nama"] + " | Jenis: " + info["jenis"] + " | Status: " + info["status"])
    return True

def tambah_tanaman():
    print("\n========== TAMBAH DATA TANAMAN ==========")
    nama = input("Masukkan nama tanaman baru: ")
    jenis = input("Masukkan jenis tanaman baru (Indoor/Outdoor): ")

    if nama == "" or jenis == "":
        print("Data tidak boleh kosong! Penambahan dibatalkan.")
        return
    
    if jenis != "Indoor" and jenis != "Outdoor":
        print("Jenis tanaman harus bertuliskan 'Indoor' atau 'Outdoor'!")
        return

    id_tanaman = str(len(daftar_tanaman) + 1)

    daftar_tanaman[id_tanaman] = {"nama": nama, "jenis": jenis, "status": "Belum disiram"}
    print(f"Tanaman '{nama}' berhasil ditambahkan dengan ID {id_tanaman}!")

def update_status_tanaman():
    if lihat_tanaman() == False:
        return

    print("\n========== UPDATE STATUS SIRAM TANAMAN ==========")
    pilihan_id = input("Masukkan nomor tanaman yang ingin diupdate: ")

    if pilihan_id in daftar_tanaman:
        if daftar_tanaman[pilihan_id]["status"] == "Sudah disiram":
            daftar_tanaman[pilihan_id]["status"] = "Belum disiram"
            print(f"Status '{daftar_tanaman[pilihan_id]['nama']}' berhasil diperbarui.")
        else:
            daftar_tanaman[pilihan_id]["status"] = "Sudah disiram"
            print("Status '" + daftar_tanaman[pilihan_id]["nama"] + "' berhasil diperbarui!")
    else:
        print("Nomor/ID tidak tersedia di dalam daftar!")

def hapus_tanaman():
    if lihat_tanaman() == False:
        return daftar_tanaman

    print("\n========== HAPUS TANAMAN ==========")
    pilihan_id = input("Masukkan nomor/ID tanaman yang ingin dihapus: ")

    if pilihan_id in daftar_tanaman:
        tanaman_dihapus = daftar_tanaman.pop(pilihan_id)
        print(f"Tanaman '{tanaman_dihapus['nama']}' berhasil dihapus dari daftar!")
        
        data_rapi = rapihkan_id_tanaman(daftar_tanaman)
        return data_rapi
    
    else:
        print("Nomor/ID tidak tersedia di dalam daftar!")
        return daftar_tanaman

def halaman_admin(username):
    while True:
        print("\n========== HALAMAN ADMIN ==========")
        print(f"Selamat datang, {username}!")
        print("1. Lihat daftar tanaman")
        print("2. Tambah data tanaman baru")
        print("3. Hapus tanaman")
        print("4. Update status siram tanaman")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == "1":
            lihat_tanaman()
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "2":
            tambah_tanaman()
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "3":
            hasil = hapus_tanaman()
            daftar_tanaman.clear()
            daftar_tanaman.update(hasil)
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "4":
            update_status_tanaman()
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "5":
            print("Keluar dari halaman admin.")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid! Silakan pilih antara 1-5.")
            input("\nTekan Enter untuk mengulangi")

def halaman_user(username):
    while True:
        print("\n========== HALAMAN USER ==========")
        print(f"Selamat datang, {username}!")
        print("1. Lihat daftar tanaman")
        print("2. Update status siram tanaman")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-3): ")

        if pilihan == "":
            print("Pilihan menu tidak boleh dikosongkan!")
            input("\nTekan Enter untuk mengulangi")
        elif pilihan == "1":
            lihat_tanaman()
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "2":
            update_status_tanaman()
            input("\nTekan Enter untuk melanjutkan")
        elif pilihan == "3":
            print("Keluar dari halaman user.")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid! Silakan pilih antara 1-3.")
            input("\nTekan Enter untuk mengulangi")

def halaman_login():
    while True:
        print("\n=====================================")
        print("SISTEM MANAJEMEN SIRAM TANAMAN")
        print("1. Login")
        print("2. Keluar")
        print("=====================================")

        pilihan = input("Masukkan pilihan Anda (1-2): ")

        if pilihan == "1":
            username_input = input("Masukkan username: ")
            password_input = pwinput.pwinput("Masukkan password: ")

            if username_input == "" or password_input == "":
                print("Username dan Password login tidak boleh dikosongkan!")
                input("Tekan Enter untuk mencoba lagi")
            elif username_input in database_akun:
                if database_akun[username_input]["password"] == password_input:
                    print(f"\nLogin berhasil! Selamat datang, {username_input}!")
                    role = database_akun[username_input]["role"]
                    if role == "admin":
                        halaman_admin(username_input)
                    elif role == "user":
                        halaman_user(username_input)
                else:
                    print("Password salah!")
                    input("Tekan Enter untuk mencoba lagi")
            else:
                print("Username tidak terdaftar di sistem!")
                input("Tekan Enter untuk mencoba lagi")

        elif pilihan == "2":
            print("Mematikan sistem siram tanaman...")
            time.sleep(2.51)
            break

        else:
            print("Pilihan tidak valid! Silakan pilih antara 1-2.")
            input("Tekan Enter untuk mengulangi")

if __name__ == "__main__":
    halaman_login()