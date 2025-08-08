# unit 6 - Kursus Online - 

# list data kursus
data_kursus = [{"nama kursus" : "matematika"     , "hari" : "senin"  , "durasi" : 4},
               {"nama kursus" : "bahasa inggris" , "hari" : "selasa" , "durasi" : 3},
               {"nama kursus" : "fisika"         , "hari" : "rabu"   , "durasi" : 2},
               {"nama kursus" : "kimia"          , "hari" : "kamis"  , "durasi" : 5},
               {"nama kursus" : "komputer"       , "hari" : "jumat"  , "durasi" : 1} 
              ]

# fungsi menampilkan seluruh jadwal khusus 
def tampilkan_jadwal_kursus(data):
    ''' menampilkan jadwal kursus dengan melakukan perulangan sebanyak nilai elemen yang ada didalam list '''
    jadwal = ""
    for kursus in data:
        jadwal += f"Nama kursus : {kursus['nama kursus']}, Hari : {kursus['hari']}, Durasi : {kursus['durasi']}\n"
    return jadwal
# fungsi menampilkan kursus pada hari tertentu
def kursus_hari_tertentu(data):
    '''menampilkan kursus pada hari tertentu dengan menggunakan percabangan if dan perulangan loop '''
    jadwal = ""
    for kursus in data:
        if kursus['hari'] == 'rabu' or kursus['hari'] == 'kamis' :
            jadwal += f"Nama kursus : {kursus['nama kursus']}, Hari : {kursus['hari']}, Durasi : {kursus['durasi']}\n"
    return jadwal
# fungssi untuk menampilkan total durasi kursus
def total_durasi(data):
    ''' meampilkan total durasi dengan menggunakan sum()'''
    total = sum(item['durasi'] for item in data)
    return total

print("\n === Unit 6 ===") 
print(f"Jadwal kursus :\n{tampilkan_jadwal_kursus(data_kursus)}\n")
print(f"Jadwal kursus hari tertentu:\n{kursus_hari_tertentu(data_kursus)}")
print(f"Total durasi :\n{total_durasi(data_kursus)}")