# -*- coding: utf-8 -*-
"""
@Mater : File Hnadling
@hari/tanggal : Senin,20211129
@nim : 065002100032
@author : Muhammad Danil Hidayat
"""

def edit():
    
    biodata = open("Biodata.txt",'w')
    biodata.write(str())
    biodata.close()
    
nama = str(input("masukkan nama mu: "))
umur = str(input("masukkan umur mu : "))
alamat = str(input("masukkan alamat mu : "))
email = str(input("masukkan email mu : "))
dosen = str(input("masukkan wali dosen mu : "))

def hasil():
    
    baca = open("Biodata.txt",'r')
    text = baca.read()
    print(text)
    baca.close()
    
print("\nberikut data kamu")
print(nama)
print(umur)
print(alamat)
print(email)
print(dosen)
