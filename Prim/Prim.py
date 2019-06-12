import math

def checkifprim(possiblePrim):
    if (possiblePrim % 2 == 0):
        return False

    i=3
    while i <= math.sqrt(possiblePrim):
        if possiblePrim % i == 0:
            return False
        i+=2
    return True

prim = checkifprim(int(input()))

print("Ist Prim" if prim  else "Keine Prim")
    