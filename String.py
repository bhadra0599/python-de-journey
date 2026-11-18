name = ' sai teja '

word_with_single_cote = 'Sai Teja\'s Laptop'
print(word_with_single_cote)

sentence = 'The car was good but, ' \
'cost was too high'
print(sentence)

print(len(sentence))     #gives lenght
print(sentence[5])       #gives char at index 5, 1st char index will be 0

#slicing
print(sentence[0:8])     #or print(sentence[:8]) for same result
print(sentence[22:])      

#methods
print(name)
print(name.upper())    #converts to upper
print(name.lower())    #converts to lower
print(name.capitalize())     #1st to caps & rest small
print(name.title())       #every 1st word capitalized
print(name.swapcase())     #small to cap & cap to small

print(name.strip())      #remove spaces from both ends
print(name.lstrip())
print(name.rstrip())

a = name.strip().upper()

print(name.count('a'))      #gives no of 'a's repeated
print(name.find('teja'))    #gives index of t in teja

new_name = name.replace('teja','charan')
print(new_name)                           #also can assign to existing variable(name)

#string concatination
greeting = 'Hello Hi'
welcome_msg = 'Welcome to my Home'

message = '{}, {} and have lunch.'.format(greeting,welcome_msg)
#or message = f'{gretting}, {name} and have lunch'
print(message)


#additional
#print(dir(name))            #gives all functions that can be used on that string
#print(help(str))


