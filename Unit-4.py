# unit 4 - Debug Program Penilaian - 

# 1. kode program yang salah
''' 
total_nilai = []

# fungsi nilai tugas
def nilai_tugas(data):
    ' menghitung nilai tugas '
    total = data * 0.3
    return total_nilai.append(total)
# fungsi nilai uts
def nilai_uts(data):
    ' menghitung nilai uts '
    total = data * 0.3
    return total_nilai.append(total)
# fungsi nilai uas
def nilai_uas(data):
    ' menghitung nilai uas '
    total = data * 0.4
    return total_nilai.append(total)

# fungsi nilai akhir
def nilai_akhir(data):
    '99 menghitung nilai akhir '
    total  = 0     
    total = sum(data) 
    return total


# perulangan untuk memasukan jumlah siswa
while True:
    try:
        jmlh = int(input("masukan jumlah siswa :"))
        break
    except ValueError: # pesan error jika yang di masukan bukan angka
        print("Input yang ada masukan bukan angka")

# perulangan untuk memasukan nilai siswa sebanyak jumlah siswa
for i in range(jmlh):
    nama_siswa = input("masukan nama siswa :")
    while True:
        try: 
            nilaitugas = int(input("masukan nilai Tugas :"))
            nilaiuts = int(input("masukan nilai UTS :"))
            nilaiuas = int(input("masukan nilai UAS :"))
            break
        except ValueError:
            print("Input yang ada masukan bukan angka")
    
    nilai_tugas(nilaitugas)
    nilai_uts(nilaiuts)
    nilai_uas(nilaiuas)
    print(f"nama siswa :{nama_siswa} dengan nilai akhir {nilai_akhir(total_nilai)}")


'''

# 2.terdapat 6 kesalahan 3 kesalahan syntax, 2 kesalahan indentasi dan 1 kesalahan logika
# 3. kesalahan syntax terjadi karena penulisan kode program yang tidak sesuai dengan struktur python
# kesalahan indentasi terjadi karena penulisan kode program yang tidak sesuai dengan struktur blok
# kesalahan logika terjadi kode program tetap berjalan tetapi tidak megnhasilkan hasil yang diinginkan


# 4  berikut perbaikan kodingan 

# fungsi nilai tugas
def nilai_tugas(a):
    ''' menghitung nilai tugas '''
    total = a * 0.3
    return total
 
# fungsi nilai uts
def nilai_uts(b):
    ''' menghitung nilai uts '''
    total = b * 0.3
    return total
      
# fungsi nilai uas
def nilai_uas(c):
    ''' menghitung nilai uas '''
    total = c * 0.4
    return total

# fungsi nilai akhir
def nilai_akhir(a,b,c):
    ''' menghitung nilai akhir '''   
    return nilai_tugas(a) + nilai_uts(b) + nilai_uas(c) 
    
print("\n === Unit 4 ===")   
# perulangan untuk memasukan jumlah siswa
while True:
    try:
        jmlh = int(input("masukan jumlah siswa :"))
        break
    except ValueError: # pesan error jika yang di masukan bukan angka
        print("Input yang ada masukan bukan angka")

# perulangan untuk memasukan nilai siswa sebanyak jumlah siswa
for i in range(jmlh):
    nama_siswa = input("masukan nama siswa :")
    while True:
        try: 
            nilaitugas = int(input("masukan nilai Tugas :"))
            nilaiuts = int(input("masukan nilai UTS :"))
            nilaiuas = int(input("masukan nilai UAS :"))
            break
        except ValueError:
            print("Input yang anda masukan bukan angka")
            
    hasil = nilai_akhir(nilaitugas,nilaiuts,nilaiuas)  
    print(f"nama siswa :{nama_siswa} dengan nilai akhir {hasil}")