# unit 9 - CRUD Data Mahasiswa -

# mengimpor mysql.connector untuk menggunak fitur fitur yang ada didalamnya
import mysql.connector


# variabel db untuk menyambungkan database 
db = mysql.connector.connect (
    host = "your-localhost",
    user = "your-root",
    password = "your-password",
    database = "your-database"
)

cursor = db.cursor() # membuat objek untuk menggunakan method cursor


# fungsi menambah data mahasiswa
def tambahkan_data(mhs): 
    ''' menggunakan try dan except untuk menentukan benar dan pengecualian '''
    try: 
        for i in range(mhs): # untuk melakukan perulangan
            nama = input(f"masukan nama mahasiswa ke-{i+1} :") # menginput nama
            jurusan = input("masukan jurusan :") # menginput juruasan
            query = "INSERT INTO mahasiswa (nama,jurusan) VALUES (%s, %s)" # query untuk menambahkan data mahasiswa 
            data = (nama,jurusan) # membuat variabel baru untuk menampung nilai nama dan jurusan
            cursor.execute(query,data) # untuk mengeksekusi query dan variabel data
            db.commit() # untuk menyimpan perubahan data ke database
            print(f"Data mahasiswa ke-{i+1} berhasil ditambahkan")
        return nama # untuk mengembalikan nilai ke fungsi tambhakan data
    except mysql.connector.Error as e: # untuk melakukan pengecualian jika terjadi error
        print(f"Terjadi kesalahan {e}")

# fungsi perbarui data mahasiswa
def update_data(mhs):
    ''' menggunakan try dan except untuk menentukan benar dan pengecualian '''
    try: 
        for i in range(mhs): # untuk melakukan perulangan
            id_mhs = int(input(f"masukan id mahasiswa ke-{i+1}:")) # menginput id mahasiswa
            nama_baru = input("masukan nama baru mahasiswa :") # menginput nama baru
            jurusan_baru = input("masukan jurusan :") # menginput jurusan baru
            query = "UPDATE mahasiswa SET nama = %s , jurusan = %s WHERE id = %s" # query untuk memperbarui data mahasiswa 
            data = (nama_baru,jurusan_baru,id_mhs) # membuat variabel baru untuk menampung nilai nama jurusan baru melalui pemganggilan id mhs
            cursor.execute(query,data) # untuk mengeksekusi query dan variabel data
            db.commit() # untuk menyimpan perubahan data ke database
            print(f"Data mahasiswa ke-{i+1} berhasil diperbarui")
        return id_mhs # untuk mengembalikan nilai ke fungsi update data
    except mysql.connector.Error as e: # untuk melakukan pengecualian jika terjadi error
        print(f" Terjadi kesalahan {e}")
    
# fungsi menghapus data mahasiswa
def hapus_data(mhs):
    ''' menggunakan try dan except untuk menentukan benar dan pengecualian '''
    try: 
        for i in range(mhs): # untuk melakukan perulangan
            id_mhs = int(input(f"masukan id mahasiswa ke-{i+1}:")) # menginput id mahasiswa
            query = "DELETE FROM mahasiswa WHERE id = %s" # query untuk menghapus data mahasiswa melalui pemanggilan id mhs 
            data = (id_mhs,) # membuat variabel baru untuk menampung nilai dengan menggunakan id mhs
            cursor.execute(query,data) # untuk mengeksekusi query dan variabel data
            db.commit() # untuk menyimpan perubahan data ke database        
            print(f"data mahasiswa ke-{i+1} berhasil dihapus")
        return id_mhs # untuk mengembalikan nilai ke fungsi hapus data
    except mysql.connector.Error as e: # untuk melakukan pengecualian jika terjadi error
        print(f" Terjadi kesalahan {e}")
    
# fungsi menampilkan seluruh data mahasiswa
def tampilkan_data():
    ''' menggunakan try dan except untuk menentukan benar dan pengecualian '''
    try:
        query = "SELECT * FROM mahasiswa " # query untuk menampilkan seluruh data mahasiswa
        cursor.execute(query) # untuk mengeksekusi query 
        mhs = cursor.fetchall() # untuk mengambil data yang ada di tabel mahasiswa
        for baris in mhs: # untuk melakukan perulangan didalam mhs 
            print(baris)
        print("data mahasiswa berhasil ditampilkan")
        return mhs # untuk mengembalikan nilai ke fungsi tampilkan data
    except mysql.connector.Error as e: # untuk melakukan pengecualian jika terjadi error
        print(" Terjadi kesalahan ", e)
        
        
 # melaukan perulangan didalam menu pilihan       
while True :
    print("=== Menu Pilihan ===")
    print("1. Tambahkan data")
    print("2. Update data")
    print("3. Delete data")
    print("4. Tampilkan data")
    print("5. keluar")
    
    pilihan = input("pilih menu :") # menginput pilihan untuk percabangan      
    if pilihan == "1" : # percbangan untuk pilihan 1
        while True: # melakukan perulangan untuk exception Error 
            try :
                jumlah = int(input("masukan berapa data mahasiswa yang ingin ditambah :"))
                break
            except ValueError:
                print("data yang dimasukan tidak valid")
        tambahkan_data(jumlah)
    elif pilihan == "2": # percbangan untuk pilihan 2
        while True:
            try :
                jumlah = int(input("masukan berapa data mahasiswa yang ingin diperbarui :"))
                break
            except ValueError:
                print("data yang dimasukan tidak valid")
        update_data(jumlah)
    elif pilihan == "3": # percbangan untuk pilihan 3
        while True:
            try :
                jumlah = int(input("masukan berapa data mahasiswa yang ingin dihapus :"))
                break
            except ValueError:
                print("data yang dimasukan tidak valid")
        hapus_data(jumlah)
    elif pilihan == "4": # percbangan untuk pilihan 4
        tampilkan_data()
    elif pilihan == "5": # percbangan untuk pilihan 5
        break
    else: # percbangan untuk pilihan yang lain
        print("data yang anda masukan tidak tersedia di pilihan")
        
    
        
        