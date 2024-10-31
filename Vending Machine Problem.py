def process_payment(price):
    attempt = 2
    print("1) CASH")
    print("2) QRIS")
    ment = input("Pilihlah metode pembayaran anda diantara 2 pilihan di atas (1/2): ")

    if ment == "1":
        try:
            pay = int(input(f"Silahkan memasukkan cash sesuai dengan harga Rp {price}: "))
            while pay < price and attempt > 0:
                attempt -= 1
                if attempt > 0:
                    print(f"Maaf, uang anda tidak mencukupi! Percobaan anda tersisa {attempt} lagi!")
                    pay = int(input(f"Silahkan memasukkan cash sesuai dengan harga Rp {price}: "))
                else:
                    print("Maaf, percobaan Anda sudah habis. Silahkan ulangi transaksi baru.")
                    return False
            if pay == price:
                print("Uang pas! Terima kasih karena telah membeli. Produk anda akan segera dijatuhkan!")
            elif pay > price:
                print(f"Uang anda berlebih! Kembalian uang anda adalah Rp {pay - price}")
                print("Terima kasih karena telah membeli. Produk anda akan segera dijatuhkan beserta uang kembalian anda!")
        except ValueError:
            print("Input tidak valid! Silahkan memasukkan jumlah uang yang benar.")
            return False

    elif ment == "2":
        print("Scan QR code berikut! Transaksi anda akan langsung selesai setelah memasukkan PIN.")
        import time
        time.sleep(10)
        print("Transaksi berhasil! Terima kasih karena telah membeli.")
    else:
        print("Pilihan metode pembayaran tidak valid.")
        return False
    return True

def vending_machine():
    print("Selamat datang di Vending Machine YumYum! Dimana harga terjangkau!")
    import time; time.sleep(2)
    
    # Main Menu
    print("A: Beli makanan")
    print("B: Beli minuman")
    coba = 3
    fitur = input("Pilih fitur yang anda inginkan diantara opsi di atas (A/B): ").upper()

    # Makanan
    if fitur == "A":
        print("Makanan apa yang ingin kamu beli?")
        print("a. Popmie (Rp 9000)")
        print("b. Dairy Milk Coklat (Rp 8200)")
        print("c. Chitato Rasa Sapi Panggang (Rp 10500)")
        yum = input("Pilih antara (a/b/c): ").lower()

        if yum == "a":
            if process_payment(9000):
                print("Popmie akan segera dijatuhkan.")
        elif yum == "b":
            if process_payment(8200):
                print("Dairy Milk akan segera dijatuhkan.")
        elif yum == "c":
            if process_payment(10500):
                print("Chitato akan segera dijatuhkan.")
        else:
            print("Maaf, pilihan tidak tersedia.")

    # Minuman
    elif fitur == "B":
        print("Minuman apa yang ingin kamu beli?")
        print("a. Pocari Sweat (Rp 8500)")
        print("b. Ultra Milk Fresh Milk (Rp 5000)")
        print("c. Air Le Mineral (Rp 3500)")
        print("d. Coca Cola (Rp 7800)")
        print("e. Teh Pucuk (Rp 6000)")
        yumm = input("Pilih antara (a/b/c/d/e): ").lower()

        if yumm == "a":
            if process_payment(8500):
                print("Pocari Sweat akan segera dijatuhkan.")
        elif yumm == "b":
            if process_payment(5000):
                print("Ultra Milk akan segera dijatuhkan.")
        elif yumm == "c":
            if process_payment(3500):
                print("Air Le Mineral akan segera dijatuhkan.")
        elif yumm == "d":
            if process_payment(7800):
                print("Coca Cola akan segera dijatuhkan.")
        elif yumm == "e":
            if process_payment(6000):
                print("Teh Pucuk akan segera dijatuhkan.")
        else:
            print("Maaf, pilihan tidak tersedia.")

    # Invalid Input
    else:
        while coba > 0:
            coba -= 1
            print(f"Tolong pilih salah satu fitur! Percobaan tersisa {coba}.")
            fitur = input("Pilih fitur yang anda inginkan diantara opsi di atas (A/B): ").upper()
            if fitur in ["A", "B"]:
                vending_machine()  # Re-run the main logic if valid input is given
                return
        print("Maaf, percobaan Anda sudah habis. Silahkan ulangi transaksi yang baru.")

# Run the vending machine program
vending_machine()
