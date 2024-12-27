text = '123 321 228 1488'
dict = dict()
for i in range(len(text.split(' '))):
    print(i)
    for j in text.split(' '):
        print(j)
        dict[i] = j

print(dict)