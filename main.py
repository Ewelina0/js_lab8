f = open('plik1.txt', 'w')
f.write('xxxxxxxxxx\nyyyyyyyyyyyy')
f = open('plik1.txt', 'r')
print(f.read())
f.close()