# Program Kalkulator Sederhana

def penjumlahan():
    return num1 + num2

def pengurangan():
    return num1 - num2

def pembagian():
    return num1 / num2

def perkalian():
    return num1 * num2

print("=== Selamat Datang di Program Kalkulator Sederhana ===")
print("=" * 54)
while True:
    try:
        num1 = float(input("Masukkan angka pertama\t: "))
    except ValueError:
        print("Error! Masukkan angka yang benar!")
        continue
    break

while True:
    try:
        num2 = float(input("Masukkan angka kedua\t: "))
    except ValueError:
        print("Error! Masukkan angka yang benar!")
        continue
    break

print("\nOperasi Hitung: \n\t1. Penjumlahan (+)\n\t2. Pengurangan (-)\n\t3. Pembagian (/)\n\t4. Perkalian (*)\n")
while True:
    try:
        pilihan = int(input("Masukkan pilihan anda (1/2/3/4): "))
    except ValueError:
        print("Masukkan pilihan dengan benar!")
        continue

    if pilihan == 1:
        print("Hasil penjumlahan =", num1, "+", num2, "=", penjumlahan())
    elif pilihan == 2:
        print("Hasil pengurangan =", num1, "-", num2, "=", pengurangan())
    elif pilihan == 3:
        print("Hasil pembagian =", num1, "/", num2, "=", pembagian())
    elif pilihan == 4:
        print("Hasil perkalian =", num1, "*", num2, "=", perkalian())
    else:
        print("Error! Pilihan anda tidak tersedia.")
        continue
    break