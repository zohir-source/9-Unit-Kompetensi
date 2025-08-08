# unit 3 - Pengujian fungsi Konversi Pangjang -

# mengimpor unittest untuk menggunakan fitur unitest
import unittest

# kelas Konversi
class Konversi:
    ''' konversi m ke km dan m ke cm'''
    def meter_ke_kilometer(self, m,a):
        km = m / a
        return km
    
    def meter_ke_centimeter(self, m,b):
        cm = m * b
        return cm
    
# kelas Test konversi     
class TestKonversi(unittest.TestCase):
    ''' melakukan pengujian dengan menggunakan assertEqual dan assertRaises'''
    def test_m_ke_kilometer(self):
        km = Konversi()
        self.assertEqual(km.meter_ke_kilometer(5000,1000),5)
        
    def test_m_ke_kilometerType(self):
        km = Konversi()
        with self.assertRaises(TypeError):km.meter_ke_kilometer('a','b')
        # TypeError untuk mencegah user menginput string
    def test_m_ke_centiometer(self):
        km = Konversi()
        self.assertEqual(km.meter_ke_centimeter(2,100),200)
        
    def test_m_ke_centiometerType(self):
        km = Konversi()
        with self.assertRaises(TypeError):km.meter_ke_centimeter('b','a')
        # TypeError untuk mencegah user menginput string
        
print("\n === Unit 3 ===")          
unittest.main()