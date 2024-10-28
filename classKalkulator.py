class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, pertama, kedua):
        self.pertama = pertama
        self.kedua = kedua        
    def tambah(self): 
        return self.pertama + self.kedua
    def kurang(self):
        return self.pertama - self.kedua
    def kali(self):
        return self.pertama * self.kedua
    def bagi(self):
        return self.pertama / self.kedua
    
hasilnya = Kalkulator(4, 5)
hasilnya1 = Kalkulator(4, 5)
hasilnya2 = Kalkulator(4, 5)
hasilnya3 = Kalkulator(4, 5)

print('Jawabannya :',  hasilnya.tambah())
print('Jawabannya :',  hasilnya1.kurang())
print('Jawabannya :',  hasilnya2.kali())
print('Jawabannya :',  hasilnya3.kali())

