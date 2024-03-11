def perkalian(a,b):
    total = 0   
    hasilPerkalian = a*b    
    print(f"{a} x {b} =", end=" ")  # Digunakan untuk menampilkan hasil dalam satu baris
    while total < hasilPerkalian:   # Perulangan yang berlangsung selama total belum sama dengan hasil perkalian di atas
        total += b  # Perulangan dilakukan dengan menjumlahkan nilai disebelah kanan tanda perkalian
        if hasilPerkalian == total: 
            print(f"{b} =", end=" ")    # Jika hasilPerkalian sama dengan total maka tampilkan tanda "=" di sebelah angka
        else:
            print(f"{b} +", end=" ")    # Jika belum sama lanjutkan dengan menampilkan tanda "+" di sebelah angka
    print (f"{total}")

masukan1 = int(input("Masukkan Bilangan Pertama : "))
masukan2 = int(input("Masukkan Bilangan Kedua: "))
perkalian(masukan1, masukan2)


