waechterAmounts = [ 6,2,4,5,1,8,3,6,8,3,3,5,2,7,9,7,1,5,3,6 ]

waechterAdded = [waechterAmounts[0]]
print(waechterAdded[0])
l = len(waechterAmounts)
for i in range(1,l):
    waechterAdded.append(waechterAdded[i-1]+waechterAmounts[i])
    print(waechterAdded[i])

startPos = int(input("Gebe Anfang an: "))
endPos= int(input("Gebe Ende an: "))

print(waechterAdded[endPos]-waechterAdded[startPos-1])