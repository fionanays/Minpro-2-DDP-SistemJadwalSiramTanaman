# MINI_PROJECT_2


## Nama: Fiona Deandra Liani
## Nim: 2609116053


# DESKRIPSI

Sistem Siram Tanaman adalah program yang saya buat untuk mengecek atau mengetahui tentang tanaman yang sudah disiram atau belum. Sistem Siram Tanaman ini mencakup metode login dengan 2 role dengan akses yang berbeda (admin dan user), admin memiliki akses CRUD yang lengkap sedangkan user hanya bisa melihat daftar tanaman dan update status tanaman. Di dalam sistem ini saya memasukkan 3 jenis data seperti "nama tanaman", "jenis tanaman (Indoor/OUtdoor)", dan "status tanaman (sudah/belum disiram)". Sistem Siram Tanaman ini sudah memiliki 5 data tanaman yang bisa diakses datanya.

# FLOWCHART

## Gambar Flowchart
<img width="1491" height="1172" alt="minpro_2 drawio" src="https://github.com/user-attachments/assets/382000eb-840b-4874-8aed-e544106df549" />


## Penjelasan Flowchart
1.Program akan menampilkan tampilan login

2.Lalu program akan menyuruh input untuk 1 (login), 2 (keluar), dan jika menginput angka selain 1 dan 2 maka program akan kembali ke tampilan login 

3.Jika menginput 1 maka kita diarahkan ke menu login dan harus menginput username dan password, jika menginput kosong pada keduanya program akan mengatakan input data tidak vald dan silahkan coba lagi. Data akan mengecek kesesuaian data dan akan mengarahkan ke role yang sesuai dengan inputan username dan password.

4.Ketika mengetik username dan password yang sesuai dengan admin, maka akan masuk ke tampilan menu sebagai admin, lalu kita perlu menginput pilihan antara 1 (lihat daftar tanaman), 2(tambah data), 3(hapus data tanaman ), 4(update status siram), dan 5(keluar). Jika input 1 maka program akan menampilkan daftar tanaman dan akan kembali ke menu sebagai admin. Lalu jika input 2 maka program akan menyuruh menginput nama tanaman dan jenis tanaman, outputnya berisi data yang berhasil ditambahkan, lalu akan kembali ke menu sebagai admin. Jika input 3 maka akan menampilkan output daftar tanaman, lalu menginput nomor/id tanaman yang ada di list daftar tanaman ouputnya tanaman berhasil dihapus, lalu program akan kembali ke tampilan menu sebagai admin . Jika input 4 maka akan menampilkan ouput daftar tanaman, memilih tanaman mana yang mau diubah dengan memasukkan id/nomor yang sesuai lalu menu akan kembali ke tampilan menu sebagai admin. Jika input 5 maka program akan keluar dan kembali ke menu login awal. Terakhir jika input selain 1-5 maka ouputnya tidak valid dan program akan kembali ke tampilan menu sebagai admin.

5.Ketika mengetik username dan password yang sesuai dengan user, maka akan masuk ke tampilan menu sebagai user, lalu kita perlu menginput pilihan antara 1 (lihat daftar tanaman), 2(update status siram), dan 3(keluar). Jika input 1 maka program akan menampilkan daftar tanaman dan akan kembali ke menu sebagai user. Jika input 2 maka akan menampilkan ouput daftar tanaman, memilih tanaman mana yang mau diubah dengan memasukkan id/nomor yang sesuai lalu menu akan kembali ke tampilan menu sebagai user. Jika input 3 maka program akan keluar dan kembali ke menu sebagai user. Terakhir jika input selain 1-3 maka ouputnya tidak valid dan program akan kembali ke tampilan menu sebagai user.


# PROGRAM

## Gambar Program
<img width="957" height="558" alt="Screenshot 2026-10-06 171534" src="https://github.com/user-attachments/assets/272cb073-ce2a-4d03-8fbd-848c861e8587" />
<img width="959" height="566" alt="Screenshot 2026-10-06 171638" src="https://github.com/user-attachments/assets/8ba10c4c-276e-49cb-8c8f-0263cffab06c" />
<img width="959" height="599" alt="Screenshot 2026-10-06 171719" src="https://github.com/user-attachments/assets/733e6ce6-b22d-4611-b270-5722b6db94f8" />
<img width="959" height="599" alt="Screenshot 2026-10-06 171731" src="https://github.com/user-attachments/assets/78f6d32e-b622-42fb-bffb-74b7b8316751" />
<img width="959" height="536" alt="Screenshot 2026-10-06 172208" src="https://github.com/user-attachments/assets/4cbc0e30-86c5-42e4-9de5-dd66179d499b" />
<img width="959" height="563" alt="Screenshot 2026-10-06 172227" src="https://github.com/user-attachments/assets/fc9ff10b-2a1e-4036-8f53-e83b46794ae9" />
<img width="959" height="164" alt="Screenshot 2026-10-06 172249" src="https://github.com/user-attachments/assets/b62ea750-3bae-4ab1-afaa-fb002e3b8f8c" />

## Penjelasan Program

1.<img width="959" height="65" alt="image" src="https://github.com/user-attachments/assets/5ace8181-2507-4ce7-ad66-081bbc03beae" />
Tambahkan tuple yang berisi data dari admin dan user, saya memakai tuple karena ingin datanya tidak diubah. Masukkan username dan passwordnya

2.<img width="959" height="122" alt="Screenshot 2026-10-06 173706" src="https://github.com/user-attachments/assets/896086b3-91b7-4f45-928f-67c3828e3400" />
Masukkan data dari tanaman yang terdiri dari "nama", "jenis", dan "status" tanaman, lalu saya menambahkan id/nomor agar lebih memudahkan saya ketika ingin melihat, menghapus, dan menambah data dari tanaman dengan hanya mengetikkan angkanya saja.

3.<img width="959" height="135" alt="image" src="https://github.com/user-attachments/assets/6b19f431-c820-4d59-b684-eb5ef229cae2" />
Def rapihkan id tanaman digunakan untuk merapikan id dari tanaman dengan menambahkan fungsi data lama, penggunaan daftar_baru = {} bertujuan sebagai dictionary kosong sementara untuk menampung data yang ID-nya sedang dirapikan satu per satu. Lalu for key in data_lama untuk melalkukan looping yang dimana dia akan melakukan pengecekan jika ada tambahan data dalam id baru. Lalu penggunaan data string pada nomor agar sesuai dengan isi daftar tanaman yang menggunakan id/nomor

4.<img width="959" height="165" alt="Screenshot 2026-10-06 191539" src="https://github.com/user-attachments/assets/ec9e4fee-eef6-4639-a55d-5e8eff973a7f" />
Def tambah_tanaman berfungsi untuk memudahkan program ketika ingin melakukan kode pada program tidak double dan tinggal memanggil fungsi yang telah dibuat tadi. Di bagia ini berisi if yang jika inputannya kosong maka akan memberikan peringatan "Daftar tanaman ini masih kosong". Lalu for id_tanaman in daftar-tanaman bertujuan sebagai hasil dari daftar tanaman yang sudah tersedia

5.<img width="959" height="260" alt="Screenshot 2026-10-06 192303" src="https://github.com/user-attachments/assets/dbaac155-cf33-486f-b133-616a830c3921" />
Pengguna/admin akan diminta input jenis dan nama tanaman. Jika mengisi data ksong maka penambahan data dibatalkan dan kembali ke menu halaman admin/user lagi. Jika jenis tanamannya tidak sama denfan Indoor atau Outdoor maka outputnya akan mengharuskan user/admin bertuliskan sama persis. Lalu setiap penambahan data baru maka idnya akan bertambah 1, dan akan menampilkan bahwa data tersebut berhasil ditambahkan

6.<img width="959" height="238" alt="Screenshot 2026-10-06 192315" src="https://github.com/user-attachments/assets/fbdcf310-3fe8-4621-b9d5-25233570e434" />
Pengguna/admin menginput id tanaman yang ingin diubah status siramnya. Jika mereka memilih status tanaman yang belum disiram maka akan terganti menjadi sudah disiram begitupun sebaliknya.

7.<img width="959" height="254" alt="Screenshot 2026-10-06 192329" src="https://github.com/user-attachments/assets/a15304ec-077f-46c1-b9c2-db1267ac3c12" />
Sebelum menghapus sistem memanggil fungsi lihat_tanaman(). Jika daftar ternyata kosong (len == 0), fungsi langsung berhenti (return daftar_tanaman) tanpa meminta input ID dari pengguna. Pengguna diminta memasukkan nomor/ID tanaman yang hendak dihapus. Lalu sistem mengecek id. Pengecekan ini berguna sebagai Error Handling untuk mencegah KeyError. Lalu pengguaan pop(pilihan_id) untuk menghapus elemen tersebut sekaligus mengambil datanya lalu menyimpannya di variabel tanaman_dihapus. Untuk fungsi rapihkan_id_tanaman(daftar_tanaman) dipanggil untuk menyusun ulang ID yang tersisa agar kembali berurutan, lalu mengembalikan data ke data_rapi. Jika menginput selain dari itu maka datanya tidak akan berubah dan akan kembali ke menu awal.

8.<img width="959" height="170" alt="Screenshot 2026-10-06 192339" src="https://github.com/user-attachments/assets/ce9325ef-5e86-4646-9b45-7823000b5c75" />
Masuk ke halaman_admin yang berisi beberapa list dengan akses CRUD lengkap. 1(Lihat daftar tanaman READ), 2(Tambah data UPDATE), 3(Hapus data DELETE), 4(Update data tanaman UPDATE), dan 5(keluar) dari program. Lalu diberikan sebuah pilihan untuk menginput akses yang sesuai.


9.<img width="959" height="310" alt="Screenshot 2026-10-06 192352" src="https://github.com/user-attachments/assets/330e98ef-7f04-430a-a7d8-2c4fdf05526e" />
Pilihan 1 akan memanggil fungsi lihat_tanaman dan menginput enter untuk melanjutkan ke menu user. Pilihan 2 akan memanggil fungsi tambah_tanaman dan menginput enter untuk melanjutkan ke menu user. Pilihan 3, di bagian hasil akan menampung dictionary baru yang dikembalikan oleh fungsi, daftar_tanaman.clear untuk mengosongkan data lama di daftar_tanaman utama, daftar_tanaman.update untuk menambah data aaru di daftar_tanaman utama dan input enter untuk melanjutkan ke menu user. Pilihan 4 akan memanggil fungsi update_status_tanaman dan menginput enter untuk melanjutkan ke menu user. Pilihan 5 untuk keluar dari halaman admin dan masuk ke halaman utama. Jika menginput selain itu maka outputnya akan tidak valid

10.<img width="959" height="143" alt="Screenshot 2026-10-06 192405" src="https://github.com/user-attachments/assets/a0260fc8-dea2-419a-8378-2b7137cabc0b" />
Masuk ke halaman_user yang berisi beberapa list dengan akses yang tidak selengkap admin . 1(Lihat daftar tanaman READ), 2(Update data tanaman UPDATE), dan 3(keluar) dari program. Lalu diberikan sebuah pilihan untuk menginput akses yang sesuai.

11.<img width="959" height="274" alt="Screenshot 2026-10-06 192416" src="https://github.com/user-attachments/assets/b85cc15e-12f6-4ad5-9a0a-eabc1111aa26" />
Pilihan 1 akan memanggil fungsi lihat_tanaman dan menginput enter untuk melanjutkan ke menu user. Pilihan 2 akan memanggil fungsi update_status_tanaman dan menginput enter untuk melanjutkan ke menu user. Pilihan 3 untuk keluar dari halaman admin dan masuk ke halaman utama. Jika menginput selain itu maka outputnya akan tidak valid.

12.<img width="959" height="136" alt="Screenshot 2026-10-06 192429" src="https://github.com/user-attachments/assets/63c20533-41ad-4e22-af70-152092fc0ff8" />
Halaman login  utama, atau program tampilan login. Berisi 2 pilihan yaitu login dan keluar, tetapi jika memilih selain dari 2 angka itu maka akan mengembalikan ke tampilan login lagi.

13.<img width="959" height="53" alt="Screenshot 2026-10-06 192540" src="https://github.com/user-attachments/assets/26ace4db-e979-494f-8ce1-c21485e8c3fa" />
Jika memilih akses pertama (login) maka user/admin harus menginput sesuai dengan data mereka

14.<img width="959" height="277" alt="Screenshot 2026-10-06 192554" src="https://github.com/user-attachments/assets/70abffbd-4548-4967-9249-448604a5fe95" />
Jika username dan passwordnya kosong maka outputnya akan invalid dan kembali ke menu tampilan login lagi. Jika menginputksn sesuai dengan role maka akan masuk ke halaman role yang sesuai dengan yang diinput. Mengetik selain dari username dan password admin/user maka akan menampilkan output invalid

15.<img width="959" height="104" alt="Screenshot 2026-10-06 192603" src="https://github.com/user-attachments/assets/f2842178-a0df-4029-b8aa-bfcdd2d8733f" />
Saat admin/user input pilihan 2 maka program akan berhenti dan tidak akan melakukan looping lagi

16.<img width="959" height="111" alt="Screenshot 2026-10-06 203245" src="https://github.com/user-attachments/assets/3eb5536e-70f7-437d-a8bb-c930efce86df" />
Jika menginput selain dari 1 atau 2 maka outputnya akan mengalami error

# Output program
1.<img width="923" height="149" alt="Screenshot 2026-10-06 193607" src="https://github.com/user-attachments/assets/75b8eda0-19e0-41f3-bb92-c400c0d9d011" />
Pilihan login dan login sebagai admin

2.<img width="959" height="140" alt="Screenshot 2026-10-06 193621" src="https://github.com/user-attachments/assets/4063df69-3184-4893-aaab-3b4785f96dea" />
Halaman admin

3.<img width="959" height="118" alt="Screenshot 2026-10-062 193621" src="https://github.com/user-attachments/assets/2a45895e-fc7d-4321-8369-33824eabedc9" />
Tampilan akses dari input 1 untuk melihat tanaman

4.<img width="959" height="205" alt="Screenshot 2026-10-06 194037" src="https://github.com/user-attachments/assets/b93a64a3-e3aa-43a5-a3ba-7c18289a73c8" />

Tampilan akses dari input 2 untuk menambah data tanaman baru

5.<img width="959" height="299" alt="Screenshot 2026-10-06 194057" src="https://github.com/user-attachments/assets/61956a98-5e7a-49a3-94b8-50ff37733d10" />
Tampilan akses dari input 3 untuk hapus

6.<img width="959" height="235" alt="Screenshot 2026-10-06 194110" src="https://github.com/user-attachments/assets/af1141e5-44df-4726-b96f-9eb6237e2e05" />
Tampilan setelah data ditambah dan dihapus

7.<img width="959" height="287" alt="Screenshot 2026-10-06 194121" src="https://github.com/user-attachments/assets/bc2f76fc-ac32-4a2d-a36f-84a1fabf1d91" />
Tampilan akses dari input 4 untuk update status siram

8.<img width="959" height="122" alt="Screenshot 2026-10-06 194136" src="https://github.com/user-attachments/assets/0b37c3c0-b272-4e9c-96c3-9c94e6d2ccff" />
Tampilan keluar dari halaman admin

9.<img width="959" height="350" alt="image" src="https://github.com/user-attachments/assets/49e2136e-4dc2-467e-9b5d-3f6320f94a10" />
Tampilan login dengan user, halaman user, dan daftar tanaman

10.<img width="959" height="227" alt="image" src="https://github.com/user-attachments/assets/7b878561-ab01-4511-8838-b8e50274c6e3" />
Tampilan keluar dari halaman user dan keluar dari sistem

# Penerapan Tambahan

## Error-handling

<img width="959" height="56" alt="Screenshot 2026-10-06 205344" src="https://github.com/user-attachments/assets/87526a1a-d2f2-4ff3-9cd9-747fc9d03779" />
Mencegah operasi pada data kosong pada lihat tanaman

<img width="959" height="111" alt="Screenshot 2026-10-06 205226" src="https://github.com/user-attachments/assets/f761f36d-7295-4297-a3d5-c830151ca052" />
Mencegah pengisian yang kosong pada nama dan jenis tanaman. Dan juga mencegah jika penulisannya tidak sama dengan Indoor dan Outdor

<img width="946" height="51" alt="Screenshot 2026-10-06 205705" src="https://github.com/user-attachments/assets/40c23318-8a8f-4e6c-b278-cece3d1e6152" />
Terjadi jika  mencoba mengakses atau menghapus key dictionary yang tidak pernah ada (misalnya pengguna mengetik ID 99 atau huruf abc)

<img width="956" height="196" alt="Screenshot 2026-10-06 205013" src="https://github.com/user-attachments/assets/5a06c8fd-14b9-4d06-a948-4fcc65435c43" />
Mencoba mengecek password dari username yang tidak ada di database_akun.


## 3 library

### os
<img width="959" height="23" alt="image" src="https://github.com/user-attachments/assets/89047153-8a24-4a98-a6f2-3c66e02b8d08" />
Penggunaan os di sini adalah untuk merapikan folder agar tidak muncul saat menjalankan program, tempat foldernya berada akan kosong dan hanya akan menampilkan kode

### time
<img width="959" height="31" alt="Screenshot 2026-10-06 204014" src="https://github.com/user-attachments/assets/a3a9ad72-258a-4d2d-89b3-6149e6bc1387" />

<img width="956" height="32" alt="Screenshot 2026-10-06 203949" src="https://github.com/user-attachments/assets/4c94bd07-5ef1-4ec2-85ea-164d41ac888a" />
Penggunaan time untuk menjeda waktu saat admin/user ingin keluar, agar terlihat seperti program sedang loading untuk mematikan/keluar dari sistem

### pwinput
<img width="959" height="50" alt="image" src="https://github.com/user-attachments/assets/f39e9365-0c43-40a3-affb-784304b6be89" />
Penggunaan pwinput untuk menyembunyikan password dengan tanda *(bintang) untuk menghindari terjadi pembocoran password atau merahasiakan password yang diinput
