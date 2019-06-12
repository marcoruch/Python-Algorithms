n = 7
arrs = [[0 for x in range(n^2*2)] for y in range(n)] 


for i in range(n^2):
    for j in range(n):
        for k in range(2):
            arrs[i][j]=k
print(arrs)

