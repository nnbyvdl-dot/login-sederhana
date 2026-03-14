kesempatan = 3

while kesempatan > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "Michelle" and password == "01234*#":
        print("Login berhasil")
        break
    else:
        kesempatan -= 1
        print("Login gagal. Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("Akun diblokir")