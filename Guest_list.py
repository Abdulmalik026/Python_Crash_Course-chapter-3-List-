guest = ['Abu-hanifah', 'Abulqaasim', 'Abu Ahmad']
print(guest)
print(f'{guest[0]} is hereby invited to our quaterly award wining & dinner!')
print(f"{guest[1]} is hereby invited to our quaterly award wining & dinner!")
print(f'{guest[2]} is hereby invited to our quarterly award wining & dinner!')

abs_1 = guest.pop( )
print(guest)
print(f'{abs_1} will be unavoidably absent')
guest.append('Idris')
print(guest)
print(f'{guest} are all invited')

guest.insert(0, 'Umar')
print(guest)
guest.insert(3, 'Hamza')
print(guest)
guest.append('Shauib')
print(guest)
print(f'We now have a big dinner table {guest[0]}, your presence will be highly appreciated!!')
print(f'We now have a big dinner table {guest[1]}, your presence will be highly appreciated!!!')
print(f'We now have a big dinner table {guest[2]}, your presence will be highly appreciated!!!')
print(f'We now have a big dinner table {guest[3]}, your presence will be highly appreciated!!!')
print(f'We now have a big dinner table {guest[4]}, your presence will be highly appreciated!!!')
print(f'We now have a big dinner table {guest[5]}, your presence will be highly appreciated!!!')

print('\033[36m Unfortunately our new dinner tables wont arrive on time!\033[0m')
print(guest)
popped1 = guest.pop()
print(f'hello {popped1}! we are sorry to cancel your invitation')
popped2 = guest.pop()
print(f'hello {popped2}! we are sorry to cancel your invitation')
popped3 = guest.pop()
print(f'hello {popped3}! we are sorry to cancel your invitation')
popped4 = guest.pop()
print(f'hello {popped4} we are sorry to cancel your invitation')
print(guest)
print(f'Hello {guest[0]} your invitation is still valid and we are expecting you')
print(f'Hello {guest[-1]} your invitation still valid and we hope to meet at the dinner')
print (guest)
del guest[0]
print(guest)
del guest[0]
print(guest)