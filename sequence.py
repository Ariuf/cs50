#strings
name = 'Ariuf'
print(name[0])

#list
names = ['Aria', 'Rosha', 'Leila']
names.append('Ali')
names.sort()
print(names)

#tuple : mostly for saving cordinates of a point or obj ...
point = (12.5, 25)
print(point)

#set : Only unique values
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(7)
s.add(5)
s.add(4)
s.add(1)
print(s)

#dict : collection of key-valus pairs
person = {
    'name' : 'Aria',
    'age' : 20,
    'loc' : 'iran'
}

print(person)