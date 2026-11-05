#===============SISTEM PERULANGAN MAHASISIWA====================== 
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa(5-10): "))
if 5 <= jumlah_mahasiswa <= 10:
    total = 10

    for i in range(1 , jumlah_mahasiswa + 1):
        print("\nMahasiswa ke-", i)
        nama= input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))

        total += nilai
    
        if nilai >=91:
            predikat = "A - sangat bagus"
        elif nilai >= 81:
             predikat = "B - bagus"
        elif nilai >= 71:
             predikat = "C - cukup" 
        elif nilai >= 51:
            predikat = "D -buruk"
        else:
            predikat = "E - sangat buruk"
        print("nama :", nama)
        print("predikat :", predikat)

    rata = total / jumlah_mahasiswa

    print("jumlah mahasiswa :",jumlah_mahasiswa)
    print("rata-rata nilai :",total)
    print("rata-rata nilai :",rata)

    if rata >=75:
        print("status kelas : memuaskan")
    else:
        print("status kelas : tingkat lagi")
else:
    print("jumlah mahasiswa harus antara 5 sampai 10")