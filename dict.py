dict = {'name' : 'Bob', 'ref' : 'Python', 'Sys' : 'Win'}
print('Dictionary:', dict)
print('\nReference:', dict['ref'])
print('\nKeys:', dict.keys())
del dict['name']
dict['user'] = 'Tom'
print('\nDictionary:', dict)
print('\nIs there A Name Key?:', 'name' in dict)