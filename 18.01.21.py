for line in open('file1', 'r'):
    print(line.upper().strip())

L = [1, 2, 3]
for i in range(len(L)):
    L[i] +=10
print(L)

L = [element + 10 for element in L]
print(L)

f = open('file1', 'r')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
f.close()

lines = [line.rstrip() for line in open('file1', 'r')]
print(lines)

s = ['house', 'pet', 'python', 'sky', 'Petro']
print(lines)
lines = [line for line in lines if line.lower().startswith('p')]
print(lines)

l = [x + y for x in 'abc' for y in 'lmn']
print(l)

res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)
print(res)

with open('file1', 'r') as f:
    for (count, item) in enumerate(f):
        print(count, item)


colors = ['black', 'white', 'yellow']
print(enumerate(colors))
print(list(enumerate(colors)))
print(list(enumerate(colors, 5)))


for color in enumerate(colors, 20):
    print(color, end=' ')
print()

lines = list(map(str.upper, s))
print(lines)


print(sorted([5, 2, 3, 1, 4], reverse=True))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
print(tuple(x))

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)



