import hashlib #Library to Generate Hashes
import quantumrandom as qrand 
# System Randomness is not random enough, so we use a server in MIT 
# That generates random strings based on the fluctuations of quantum particles 
# within a vaccuum. Seriously. Even then, it's barely random enough for this purpose.
# We'll need to find a more sustainable solution.
import sys #System Libraries, for taking user arguments
mcycle = int(sys.argv[1]) #Set how many keys to generate from user input
while mcycle >= 1: #As long as we haven't generated all the codes requested, loop
	hexx = qrand.hex() #Take a random string from the Quantum Generator
	meow = hashlib.sha256(str(hexx).encode('utf-8')).hexdigest()[:8] 
	#Encode it as a SHA256 Hash, Take only the first eight characters.
	flow = str("Meow States The Crow, Unaware of his Own Unusualness") + str(meow)
	# Salt the Hash
	crow = hashlib.md5(str(flow).encode('utf-8')).hexdigest()[:5] #Hash the Salted Hash, take the first 5 characters
	print (meow,"-",crow)    #Code = RandomHash - RandomHash+Salt
	mcycle = mcycle - 1    # One code has been generated, subtract it from mcycle
