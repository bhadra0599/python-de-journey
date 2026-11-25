# comparisions:
# Equal:                ==
# Not Equal:            !=
# Greater than:         >
# Less than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object identity:      is

language = 'Java'

# if language == 'Python':
#     print('True')

# if language == 'Python':
#     print('Language is Python')
# else:
#     print('No match')

# if language == 'Pyhton':
#     print('Laanguage is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'Javascript':
#     print('Language is Javascript')
# else:
#     print('No match')

# and
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' and not logged_in:     #here logged_in = false, so not logged_in changes it to True
    print('Admin Page')
else:
    print('Bad Creds')