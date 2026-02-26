gudang_pc = [

{"item": "Laptop", "harga": 1500000, "stok": 5 },
{"item": "Mouse", "harga": 250000, "stok": 12},
{"item": "Keyboard", "harga": 400000 , "stok":5 },

]

#tambahkan satu key baru "kategori" dengan valeu aksesoris untuk produk keyboard
gudang_pc[2]["kategori"] = "aksesoris"
print(gudang_pc)

gudang_pc.append({"item": "headset", "harga": 3500000, "stok": 8, })
print(gudang_pc)

for x in range(len(gudang_pc)):
    print(f"item: {gudang_pc[x]['item']}, total_aset: {gudang_pc[x]['harga'] * gudang_pc[x]['stok']}")
