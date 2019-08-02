from hashlib import md5 #Import MD5 Hash Function
code = input("Enter Product Code: ") #Take User Input

sec1 = code[:8] # Grab the first code, Eight Characters
print("Time Hash: ", sec1) # Print the first code
sec2 - code[-5:] # Grab the second code, last 5 characters
print("Encode: ", sec2) # Print the second code
flow = str("Meow States The Crow, Unaware of his Own Unusualness") + str(sec1) # Salt the first code
enc = md5sum(str(flow).encode('utf-8')).hexdigest()[:5]) #Hash the salted code
print("Verified Hash: ", enc) #Print the hashed salted code
if str(enc) == str(sec2): # Ensure the new hash matches the original product code
	print ("Code is Valid!")
else:
	print ("Invalid Product Code.")
