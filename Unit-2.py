# unit 2 - Katalog Kendaraan - 

# kelas Kendaraan
class Kendaraan:
    ''' menggunaka artibut nama dan kendaraan '''
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

# sub kelas Mobil
class Mobil(Kendaraan):
    ''' fungsi menampilkan nama dan jenis kendaraan '''
    def tampilkan_info(self):
        print("nama kendaraan mobil",self.nama,"dengan jenis",self.jenis,"memiliki keunikan desain sporty,irit,populer sejak lama")        

# sub kelas Motor
class Motor(Kendaraan):
    ''' fungsi menampilkan nama dan jenis kendaraan '''
    def tampilkan_info(self):
        print("\nnama kendaraan motor",self.nama,"dengan jenis",self.jenis,"memiliki keunikan Motor sport 250cc paling populer,tampang garang") 
 
# membuat objek dari kelas Mobil dan Motor       
mobil = Mobil("Honda Civic","Mobil Sedan")   
motor = Motor("Kawasaki Ninja 250","Motor Sport")
       
# menggunakan objek untuk menjalankan method tampilkan info
print("\n === Unit 2 ===")   
mobil.tampilkan_info()
motor.tampilkan_info()  