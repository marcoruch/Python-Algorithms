N=int(input("Wo beginnen wir?"))
print()
print("Wir beginnen bei: " + str(N))
pos = ['?' for i in range(N)]
player=1

for i in range(N):
    if (pos[N-i-1]=='?'):
        steps =int(float(input("How many steps?")))
        steps = steps*steps
        for y in range(steps):
            pos[N-i-y-1]=player
            print(str(player)+" --> "+ str(N-i-y) + " --> ["+str(N-i-y-1)+"]")
        player = 2 if (player==1) else 1

print("Spieler " + str(pos[0]) + " hat gewonnen :^)")
print(pos)