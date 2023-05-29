import hashlib
text = input("Nilai String : ")
md5 = hashlib.md5()
md5.update(text.encode("ascii"))
print(md5.hexdigest())
