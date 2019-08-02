from hashlib import sha256
code = input("Enter Product Code: ")

sec1 = code[:5]
print("Time Hash: ", sec1)
sec2 = code[-5:]
print ("Encode: ", sec2)
flow = str("Meow States The Crow, Unaware of his Own Unusualness") + str(sec1)
print ("Enode Verified: ", md5sum(str(flow).encode('utf-8')).hexdigest()[:5])
if md5sum(str(flow).encode('utf-8')).hexdigest()[:5] == str(sec2):
    print ("Code is Valid!")
else:
    print ("Invalid product Code.")
