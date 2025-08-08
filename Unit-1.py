# unit 1 - Validasi dan Klasifikasi Nilai Akademik -

# list untuk menyimpan nilai
hasil= []
# fungsi klasifikasi nilai
def klasifikasi_nilai(nilai):
    ''' melakukan percabangan if untuk mengklasifikasi range nilai '''
    if  90 <= nilai <= 100:
        hasil.append(f"{nilai} Sangat baik")
    elif 75 <= nilai <= 89: 
        hasil.append(f"{nilai} Baik")
    elif 60 <= nilai <= 74: 
        hasil.append(f"{nilai} Cukup")
    elif 0 <= nilai <= 59: 
        hasil.append(f"{nilai} Kurang")
    # return digunakan untuk mengembalikan nilai ke fungsi klasifikasi nilai

print("\n === Unit 1 ===")
# melakukan perulangan untuk menginput nilai sebanyak 3 kali    
for i in range(3):
    angka = int(input(f"masukan nilai ke-{i+1} :"))
    klasifikasi_nilai(angka) # pemanggilan fungsi dengan mengisi paramater angka

# melakukan perulangan cetak sebanyak isi dari list
for i in hasil:   
    print(f"{i}")