data_aktivitas = [("Diki",88),("Aqul",45),("Abid",92),("Rehan",70)]

for nama, nilai in data_aktivitas:
    if nilai > 80:
        print(f"{nama} mendapatkan predikat gold")
    elif nilai == 50 | nilai < 80:
        print(f"{nama} mendapatkan predikat silver")
    else:
        print(f"{nama} mendapatkan predikat bronze")
