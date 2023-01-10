print("===== APP PEMESANAN FOOD CORNER BPI =====")
print("")

banyak = int(input("Mau Beli Berapa item? "))

i=1
for i in range (banyak):
    print(i+1)
    print("Pilihan Item")
    berat = print("1. Makanan Berat [Potongan rp. 2000 ALL Item!]")
    ringan = print("2. Makanan Ringan")
    minum = print("3. Minuman ")
    nomor = int(input("Pilih nomor: "))
    item = input("Nama item :")
    harga = int(input("Harga item :"))
    satu = 1

    diskon = 2000
    harganew = harga - diskon

    print("==================================")
    print("item 1 :", item)

    if nomor == satu :
        print("Potongan Harga: 2000")
    elif nomor != satu :
        print("Potongan Harga: 0")

    if nomor == satu :
        print("Harga(New) :", harganew)
    else:
        print("Harga(new):", harga)
    print("")

total = harga + harganew
print("Total yang harus di bayar adalah :",total)

#LELAH :)