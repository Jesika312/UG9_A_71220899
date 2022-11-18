#TEST CASE 2
import math
p=int(input("masukan panjang: "))
l=int(input("masukan lebar: "))
r=int(input("masukan tinggi: "))
luaslingkaran=float(((math.pi)*(r**2))/2)
luaspp=float(p*l)
jumlahkaleng=float(((luaslingkaran+luaspp)/15))
print ("Area tersebut membutuhkan",math.ceil(jumlahkaleng),"kalengcat")
