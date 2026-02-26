stok_barang = [15, 40, 30, 10, 25]

stok_barang[3] = 50
stok_barang.insert(5,5)
stok_barang.sort(reverse=True)

jumlah_stok = sum(stok_barang)
rata_rata = jumlah_stok / len(stok_barang)
print(stok_barang)
print("Jumlah stok barang: {}".format(jumlah_stok))
print("Rata-rata stok barang: {:.2f}".format(rata_rata))


status = "Stok aman" if rata_rata > 20 else "Stok kurang"
print(status)