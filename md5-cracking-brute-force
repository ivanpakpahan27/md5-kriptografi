import hashlib
import time
counter = 1
md5_hash = input("Input MD5    : ")
pwdfile = input("Wordlist Path : ")
try:
    pwdfile = open(pwdfile, "r")
except:
    print("\nFile not found")
    quit()
for password in pwdfile:
    md5 = hashlib.md5()
    md5.update(password.strip().encode("ascii"))
    start = time.time()
    print("String %d : %s " % (counter, password.strip()))

    counter = counter + 1
    end = time.time()
    t_time = end-start

    if md5_hash.strip() == md5.hexdigest():
        print("\nPassword found!.\nPasswordnya : %s" %
              password.strip())
        print("Duration(s) : ", t_time)
    else:
        print("Password not found")
