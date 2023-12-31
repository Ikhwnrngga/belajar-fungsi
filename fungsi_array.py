nilai_berhitung = [["Upin",80,90],["Jarjit",70,75],["Ipin",94,90],["Mail",88,96],["Ehsan",92,80]]
print(nilai_berhitung[1][2])

def cari_maks(l_nilai):
    nilai_maks = 0
    siswa_maks = ''
    for nil_siswa in l_nilai:
        siswa = nil_siswa[0]
        nilai = (nil_siswa[1] + nil_siswa[2])/2
        if nilai > nilai_maks:
            nilai_maks = nilai
            siswa_maks = siswa

    return [siswa_maks,nilai_maks]

print(cari_maks(nilai_berhitung))