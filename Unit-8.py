# unit 8 - Undian Hadiah Ulang Tahun -

import random

# tuple dafta nama peserta
nama_peserta = ("zohir","anggil","yosa","jack","ali")

# fungsi menampilkan seluruh peserta
def tampilkan_peserta(data):
    ''' menggunakan perulangan loop untuk mengambil '''
    peserta = ""
    for tup in data:
        peserta += f"-{tup}\n"
    return peserta

# fungsi menampilkan pemenang
def tampilkan_pemenang(data):
    ''' menggunaka perulangan loop untuk mengakses indeks didalam tuple'''
    hasil = ""
    pemenang = random.choices(data, k=2) # pemilihan tuple hanya sekali
    for item in pemenang:
        hasil += f"-{item}\n"
    return hasil
    

print("\n === Unit 8 ===") 
print(f"--- Daftar Peserta ---\n{tampilkan_peserta(nama_peserta)}")
print(f"=== Daftar Pemenang ===\n{tampilkan_pemenang(nama_peserta)}\n")