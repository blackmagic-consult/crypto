import hashlib
import quantumrandom as qrand
import sys
mcycle = int(sys.argv[1])
while mcycle >= 1:
    hexx = qrand.hex()
    meow = hashlib.sha256(str(hexx).encode('utf-8')).hexdigest()[:8]
    flow = str("Meow States The Crow, Unaware of his Own Unusualness") + str(meow)
    crow = hashlib.md5(str(flow).encode('utf-8')).hexdigest()
    print (meow,"-",crow)
    mcycle = mcycle - 1
    # print ("Codes Left: ",mcycle)
