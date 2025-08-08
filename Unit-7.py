# unit 7 - Spesifikasi Sistem Data Pegawai - 

# Nama Pogram : Spesifikasi Sistem Data Pegawai Bank
# Tujuan      : Mempermudah mengelola data pegawai
# Input       : Nama , jabatan dan gaji
# Proses      : Menyimpan data pegawai dan menghitung rata rata gaji pegawai
# Output      : Menampilkan data pegawai dan rata rata gaji pegawai

data_pegawai = [{"nama" : "herry" , "divisi" : "Staff"   , "gaji" : 4000000},
                {"nama" : "lina"  , "divisi" : "Manager" , "gaji" : 16000000},
                {"nama" : "dede"  , "divisi" : "HRD"     , "gaji" : 8000000},
                {"nama" : "miro"  , "divisi" : "DA"      , "gaji" : 11000000},
                {"nama" : "gui"   , "divisi" : "IT "     , "gaji" : 9000000}
                ]

# fungsi menampilkan data pegawai 
def tampilkan_data_pegawai(data):
    '''menampilkan seluruh data pegawai dengan menggunakan perulangan loop '''
    pegawai = ""
    for person in data:
        pegawai += f"Nama : {person['nama']} Divisi : {person['divisi']} Gaji : {person['gaji']}\n"
    return pegawai

# fungsi menghitung gaji rata rata pegawai 
def rata_rata_gaji(data):
    '''menghitung rata rata dengan menjumlahkan seluruh gaji dan dibagi dengan banyaknya element data '''
    total = sum(gaji['gaji'] for gaji in data)
    return total / len(data)

print("\n === Unit 7 ===") 
print(f"Daftar seluruh pegawai :\n{tampilkan_data_pegawai(data_pegawai)}\n")
print(f"Rata rata gaji pegawai :\n{rata_rata_gaji(data_pegawai)}")