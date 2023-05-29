import hashlib
import os
import time

password = input("Masukkan Password yang mau disimpan : ")
print("Password berhasil disimpan.")
os.system('cls')
md5 = hashlib.md5()
md5.update(password.encode("ascii"))
db_password = md5.hexdigest()
print("Untuk Login kamu harus masukkan Password")
while True:
    pwd = input("Masukkan Password : ")
    md5 = hashlib.md5()
    md5.update(pwd.encode("ascii"))
    db_pwd = md5.hexdigest()
    if db_pwd == db_password:
        print("Berhasil login")
        break
    else:
        print("Password salah, coba lagi")
        time.sleep(2)
        os.system('cls')
