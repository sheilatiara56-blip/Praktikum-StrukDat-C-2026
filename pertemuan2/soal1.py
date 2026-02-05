stock = [15,50,30,25,40]
stock.append(100)
stock.insert(2,75)
stock.sort()
rata_rata = sum(stock) / len(stock)
print(stock)
print("Rata-rata stock: {:.2f}".format(rata_rata))