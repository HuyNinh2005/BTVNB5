n = input()
dict = {}
for char in n:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)