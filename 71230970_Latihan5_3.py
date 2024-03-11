def indeksSemester (jumlah):
    totalNilai = 0
    for i in range (1,jumlah+1):    # Mengulang input nilai matakuliah sebanyak jumlah yang diinput oleh user
        masukan1 = input(f"Nilai MK {i}: ") 
        if masukan1 == "A":
            totalNilai = totalNilai + 4
        elif masukan1 == "B":
            totalNilai = totalNilai + 3
        elif masukan1 == "C":
            totalNilai = totalNilai + 2
        else:
            totalNilai = totalNilai + 1
    nilaiIPS = totalNilai / jumlah
    return round(nilaiIPS,2)    # Melakukan pembulatan dua angka di belakang koma

masukan2 = int(input("Berapa jumlah mata kuliah? "))
print("Nilai IPS anda semester ini", indeksSemester(masukan2))
            
