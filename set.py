zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))

bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('\nSet:', bag, '\tLength', len(bag))
print (type(bag))

print('\nId Green in bag Set?:', 'Green' in bag)
print('\nIs Orange in bag set?:', 'Orange' in bag)

box = {'Red', 'Purple', 'Yellow'}
print('\nSet:', box, '\t\tLength:', len(box))
print('Common To Both Sets:', bag.intersection(box))