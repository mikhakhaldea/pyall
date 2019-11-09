#iseng di termux android + vim                
from random import randrange
tbrdm = {1:'G',2:'B',3:'K'}
tb ={}
tb[('G','G')]= 0
tb[('B','B')]= 0
tb[('K','K')]= 0
tb[('G','B')]= -1
tb[('G','K')]= 1
tb[('B','G')]= 1                                
tb[('B','K')]= -1
tb[('K','G')]= 1
tb[('K','B')]= 1
rdm = randrange(1,4)
#if rdm in tbrdm:
   # ip2 = tbrdm[rdm]
ip1 = input('Pilihan Anda. Gunting batu kertas (G,B,K)? ')
#ip2 = input('pil kedua? ')
cr = (ip1,tbrdm[rdm])
if cr in tb:
   # print(tb[cr])
    nilai = int(tb[cr])
    if nilai == 1:
        print ("Anda Menang")
    elif nilai == 0:
        print ("Draw Impas")
    else:
        print ("Anda Kalah")

print ("Pilihan komputer Adalah "+tbrdm[rdm])
