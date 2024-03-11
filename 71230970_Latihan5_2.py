def ganjil(bawah,atas):
    if bawah < atas:    # Ketika parameter bawah lebih kecil dari atas maka perulangan i ke atas
        for i in range (bawah,atas+1):  # Batas atas ditambah 1 karena perulangan for akan berhenti sebelumnya 
            if i % 2 != 0:
                if i != atas and i != atas-1: 
                    print (i, end=", ") # Angka diberi koma ketika belum sama dengan batas atas (untuk angka ganjil) atau batas atas-1 (untuk angka genap)
                else:
                    print (i, end=".")  # Angka diberi titik ketika sudah mencapai batas
    else:   # Ketika parameter bawah lebih besar dari atas maka perulangan i ke bawah
        for i in range (bawah,atas-1,-1): # Batas bawah dikurangi 1 karena perulangan for akan berhenti sebelumnya 
            if i % 2 != 0:
                if i != atas and i != atas+1: # Angka diberi koma ketika belum sama dengan batas atas (untuk angka ganjil) atau batas atas-1 (untuk angka genap)
                    print (i, end=", ")
                else:
                    print (i, end=".")

masukan1 = int(input("Masukkan Batas Bawah: "))
masukan2 = int(input("Masukkan Batas Atas: "))
ganjil(masukan1,masukan2)

