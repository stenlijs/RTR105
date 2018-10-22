n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

print('-----------------------')

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

print('-----------------------')

friends = ['a', 'b', 'c']
for friend in friends :
    print('hny', friend)
print('done!')

print('-----------------------')

for i in [5, 4, 3, 2, 1] :
    print(i)
print('blastoff!')

print('-----------------------')

print('before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('after')

print('-----------------------')

x = 34
print('before', x)
for y in [9, 41, 12, 3, 74, 15]:
    if y > x :
        x = y
        print(x, y)

    print('after', x)

print('-----------------------')

x = 0
print('before', x)
for thing in [9, 41, 12, 3, 74, 15, 34, 71, 18, 16, 46, 87, 76, 97, 98]:
    x = x + 1
    print(x, thing)
print('after', x)

print('-----------------------')

x = 0
print('before', x)
for thing in [9, 41, 12, 3, 74, 15]:
    x = x + thing
    print(x, thing)
print('after', x)

print('-----------------------')

count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)

print('-----------------------')

print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('large number', value)
        print('after')

print('-----------------------')

found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('after', found)

print('-----------------------')

lsf = -1
print('before', lsf)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > lsf :
        lsf = the_num
        print(lsf, the_num)

        print('after', lsf)

print('-----------------------')

ssf = -1
print('before', ssf)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < ssf :
        ssf = the_num
        print(ssf, the_num)

        print('after', ssf)

print('-----------------------')

smallest = None
print('before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)

print('-----------------------')

while True:
    line = input('>')
    if line == 'done' :
        break
    print(line)
    print('done!')

