from kurs import kurs
import konverter
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

data_tabel = [[kode, nilai] for kode, nilai in kurs.items()]

print(tabulate(data_tabel, headers=["Mata Uang", "Kurs (IDR)"], tablefmt="fancy_grid"))

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
nominal = float(input("Nominal: "))

hasil = konverter.konversi(dari, ke, nominal)

print(f"\nResult: {nominal:,.0f} {dari} = {hasil:,.2f} {ke}")