#Gunting batu kertas oop ngawur
from random import randrange


tbrdm = {1:'G',2:'B',3:'K'}#tuple Pilihan G B K(Gunting Batu Kertas)
tb={}
tb[('G','B')]=-1 #Tuple Semua kemungkinan G B K, jika menang nilai 1, kalah -1 dan draw 0
tb[('G','K')]=1
tb[('G','G')]= 0
tb[('B','G')]= 1
tb[('B','B')]=0
tb[('B','K')]=-1
tb[('K','G')]=-1
tb[('K','B')]= 1
tb[('K','K')]=0

class Bermain():
	#global variabel untuk nilai dan permainan ke X
	nilaiku = 0
	#draw = 0
	nilaikom = 0
	permainanke = 0
	def __init__(self):
		#inisiasi nilai permainan ke X
		Bermain.permainanke +=1
		self.mainkan() #panggil method mainkan
	def mainkan(self):
		rdm = randrange(1,4) #ambil angka acak untuk komputer

		print ("Permainan ke "+ str(Bermain.permainanke) +"\n")
		pil = input("Pilihan Anda, Gunting, Batu, Kertas (G,B,K)? ") #inputan anda
		cr = (pil.upper(),tbrdm[rdm]) #cari pilihan di tupple tbrdm
		#if cr in tb: #pencarian di tupple tb
		banding = int(tb[cr]) #ambil nilai di tupple tb. jika 1 menang 0 draw. -1 kalah
		if banding == 1 :		
				print ("Sesi ini Anda Menang")
				Bermain.nilaiku +=1 #tambah 1 nilai

		elif banding == -1:
				print ("Sesi ini Anda Kalah ")
				Bermain.nilaikom +=1 #nilai dikurangi 1

		else:
				print ("Draw")
				#Bermain.draw +=1 #nilai ditambah 0

		print ("Pilihan komputer adalah " + str(tbrdm[rdm])+"\n") #tampilkan pilihan random komputer

def main():
	berapax = int(input("Anda ingin main berapa kali? ")) #input untuk perulangan berapa X permainan
	for _ in range(berapax): #perulangan
		a = Bermain() #panggil class Bermain

	print("Nilai AKhir Dari " + str(berapax) + " Pertandingan Adalah \n\nNilai Anda     : "+str(Bermain.nilaiku)+"\nNilai Komputer : "+str(Bermain.nilaikom)+"\nDraw            : " + str(berapax-(Bermain.nilaiku+Bermain.nilaikom))+"\n\n") #cetak nilai akhir
	if Bermain.nilaiku > Bermain.nilaikom:
		print("Selamat Anda Menang Di Game ini")
	elif Bermain.nilaiku < Bermain.nilaikom:
		print("Maaf Anda Kalah Di Game ini ")
	else:
		print("Anda Draw / Seri di Game ini")

if __name__ == '__main__':
	main()















