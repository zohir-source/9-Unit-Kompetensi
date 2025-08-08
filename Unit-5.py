# unit 5 - Analisis Data Buku Perpustakaan -

# list data buku 
data_buku = [{"judul" : "pemanah sakti"       , "penulis" : "bibi lung" , "jumlah halaman" : 134},
             {"judul" : "kenangan rumah itu"  , "penulis" : "jeniffer"  , "jumlah halaman" : 104},
             {"judul" : "hari biasa"          , "penulis" : "andre"     , "jumlah halaman" : 78},
             {"judul" : "pelukis terindah"    , "penulis" : "fiona"     , "jumlah halaman" : 68},
             {"judul" : "pemain terbaik"      , "penulis" : "yura"      , "jumlah halaman" : 56} 
             ]

# fungsi menampilkan data buku 
def tampilkan_data_buku(data):
    ''' menyimpan dan menampilkan seluruh data buku'''
    hasil = ""
    for buku in data:
        hasil += f"Judul : {buku['judul']}, Penulis : {buku['penulis']}, Jumlah halaman : {buku['jumlah halaman']}\n"
    return hasil

# fungsi menampilkan buku dengan halaman terbanyak
def halaman_terbanyak(data):
    ''' menghitung jumlah halaman terbanyak '''
    tertinggi = max(data, key=lambda item:item['jumlah halaman'])
    return f"Judul : {tertinggi['judul']}, Penulis : {tertinggi['penulis']}, Jumlah halaman : {tertinggi['jumlah halaman']}" 
    
# fungsi menghitung rata rata jumlah halaman
def rata_rata_halaman(data):
    ''' menghitung jumlah rata rata halaman '''     
    total_halaman = sum(item['jumlah halaman'] for item in data)
    return total_halaman / len(data)

print("\n === Unit 5 ===")   
print(f"Semua data buku :\n{tampilkan_data_buku(data_buku)}")
print(f"Halaman terbanyak :\n{halaman_terbanyak(data_buku)}\n")
print(f"Rata rata halaman :\n{rata_rata_halaman(data_buku)}")