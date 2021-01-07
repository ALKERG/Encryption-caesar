#VARIABLES
dicc = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
        "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
maxCount = -999
mostRepeated = ""
key = 0

#DECRYPTION FUNCTION
def decodeText(mayus):
    ldecoded = len(dicc) - key
    newl = dicc[l.lower()] + ldecoded 
    if newl > 26:
        newl = dicc[l.lower()] - key
        for k in dicc.keys():
            if dicc[k] == newl and dicc:
                if mayus == True: print(k.upper(),end="")
                else: print(k,end="")
    else:
        for k in dicc.keys():
            if dicc[k] == newl:
                if mayus == True: print(k.upper(),end="")
                else: print(k,end="")

#MAIN RUN
text = input("Introduce un texto: \n")

for l in text:
    if text.count(l) > maxCount and l != " ":
        maxCount = text.count(l)
        mostRepeated = l
key = dicc[mostRepeated.lower()] - dicc["e"]
        
print("\nTEXTO DESCIFRADO")

for l in text:
    if not l.islower() and l != " " and l != "," and l != ".":
        decodeText(True)
    elif l.islower() == True and l != " " and l != "," and l != ".":
        decodeText(False)
    else:
        print(l,end="")

print("\nLLAVE DE CIFRADO: ",key)