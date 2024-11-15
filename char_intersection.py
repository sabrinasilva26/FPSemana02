palavra1 = set((input()))


palavra2 = set((input()))




intersection = palavra1 & palavra2

result = []

for char in palavra1:
    if char in intersection and char not in result:
        result.append(char)

result.sort()        
print(''.join(result))
