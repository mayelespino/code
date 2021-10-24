import itertools

x=1
y=1
z=1
out=2

xCoord =[i for i in range(x+1)]
yCoord =[i for i in range(y+1)]
zCoord =[i for i in range(z+1)]

#for combination in itertools.zip_longest(xCoord, yCoord, zCoord, fillvalue=0):
#    print(combination)

fullComboCoord = [ combo for combo in itertools.product(xCoord, yCoord, zCoord)]
print(fullComboCoord)

filteredComboCoord = [ list(combo) for combo in itertools.product(xCoord, yCoord, zCoord) if (combo[0] + combo[1] + combo[2]) != out]
print(filteredComboCoord)
