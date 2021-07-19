from tabulate import tabulate 
import itertools as it
# genConverter bertujuan untuk menghasilkan sebuah list tahap - tahap konversi yang nantinya akan kita masukkan ke fungsi tabulate utuk outputnya
def genConverter(angka, pembilang): # param "pembilang" yg akan menjadi pembagi untuk menentukan kita akan menkonversi bil. apa
    res = []
    hasilAngka = ""
    loop = True
    while loop:
        if angka >= pembilang:
            res.append(angka) # menggabungkan nilai "angka" ke akhir "res"
            sisa = angka % pembilang # hasil dari angka sisa bagi pembilang
            angka //= pembilang
            if sisa > 9:  # dlm kondisi loop(True), if sisa > 9, dan angka >= pembilang, dan dalam kondisi loop/True, maka huruf = libChar(sisa)
                huruf = libChar(sisa)
                hasilAngka += huruf
                sisa = "{0} = {1}".format(sisa, huruf) # {0} sebagai sisa, {1} sebagai huruf, maka sisa adalah huruf
            else: # klo sisanya ternyata di < 9 maka, "hasilAngka += str(sisa)"
                hasilAngka += str(sisa)
            divid = "{0}------  {1}".format(pembilang, sisa) # ini di luar else, tp masih d dlm "if angka % pembilang" maka {0} = pembilang, {1} = sisa
            res.append(divid) # "if angka >= pembilang" maka menggabungkan nilai "divid" ke akhir "res"
        else:
            if angka > 9: # dlm kondisi loop(True), if angka <= pembilang, dan angka > 9, maka "angka = libChar(angka)"
                angka = libChar(angka)
            hasilAngka += str(angka) # "if angka ternyata <= pembilang" maka, "hasilAngka += str(angka)"
            res.append(angka) # lalu menambahkan nilai "angka" ke akhir "res"
            loop = False # "if angka ternyata <= pembilang" maka, "loop = False"
            break # stop
        res.append("") # dalam kondisi loop(True) di akhir "res" ditambahkan kutip dua("")
    hasilAngka = "".join(reversed(hasilAngka)) # reversed # pada fungsi "genConverter",  "hasilAngka = "".join(reversed(hasilAngka))

    return (res, hasilAngka) # lalu ketika yg diatas sudah smua maka mereturn "res", "hasilAngka"
    
def libChar(angka): # ini untuk aturan hexadesimal
    if angka == 10:
        return "A"
    elif angka == 11:
        return "B"
    elif angka == 12:
        return "C"
    elif angka == 13:
        return "D"
    elif angka == 14:
        return "E"
    elif angka == 15:
        return "F"
    elif angka == 16:
        return "G"
# lalu setelah semua fungsi dibuat, kita panggil fungsi "genConverter" dgn parameter bilangan 2 = biner, 8 = octal, 16 = hexa
angka = int(input("Masukkan bilangan untuk dikonversi: "))

biner, hasilBiner = genConverter(angka, 2)
octal, hasilOctal = genConverter(angka, 8)
hexa, hasilHexa = genConverter(angka, 16)

table = list(it.zip_longest(biner, octal, hexa))

# ini utnuk header table
header = ("Binary", "Octal", "Hexadecimal")

print(tabulate(table, header, tablefmt="plain"))
print("")
print("====================================================")
print("Binary : ", hasilBiner)
print("Octal  : ", hasilOctal)
print("Hexa   : ", hasilHexa)

output:
Masukkan bilangan untuk dikonversi: 50
Binary      Octal       Hexadecimal
50          50          50
2------  0  8------  2  16------  2

25          6           3
2------  1

12
2------  0

6
2------  0

3
2------  1

1

====================================================
Binary :  110010
Octal  :  62
Hexa   :  32



        