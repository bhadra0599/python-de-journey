#mutable

courses = ['History','Math','Physics','Comp']
print(courses)

print(courses[0])
print(courses[3])    #or print(courses[-1]) to get the last item

print(courses[0:2])
print(courses[:3])
print(courses[1:])
print(courses[::-1])      #reverse list

# courses[0] = 'Art'        #to change the value of specf position
# print(courses)

# courses.append('Art')
# print(courses)              #will add 'Art' at the last

# courses.insert(0,'Art')     #will be inserted at specified position, 0 is the position
# print(courses)

courses_2 = ['Art','Economics']

# courses.insert(0,courses_2)
# print(courses)                    #will add courses_2 to courses as a list like [['Art', 'Economics'], 'History', 'Math', 'Physics', 'Comp'], append also does the same

# courses.extend(courses_2)        #adds 2 lists like ['History', 'Math', 'Physics', 'Comp', 'Art', 'Economics']
# print(courses)

# courses.remove('Math')        #removes the specified item 
# print(courses)    

# courses.pop()                #removes last item
# print(courses)

# courses.reverse()           #to reverse a list
# print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)      #to reverse the sorted list
print(courses)

# nums = [1,6,8,3,5]
# print(max(nums))
# print(min(nums))
# print(sum(nums))

# print(courses.index('Comp'))         #to get the index of any value
# print(courses.index('Art'))          #throws error if the value is not in list

# print('Math' in courses)             #to get true or false result
# print('Art' in courses)

# course_str = ', '.join(courses)       #to convert list to string
# print(course_str)

# new_list = course_str.split(', ')        #to convert back string to list
# print(new_list)


print('-----------Tuples------------')

#immutable

# tuple_1 = ('History', 'Math', 'Physics', 'Comp')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'        #tuple dese not support obj assig

# print(tuple_1)
# print(tuple_2)


print('-------------Sets-------------')

#unordered and no duplicates

cs_courses = {'History', 'Math', 'Physics', 'Comp', 'Math'}        #dups will be removed
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print(art_courses)

# print('Math' in cs_courses)               #sets are better optimized to check if a value(membership test) is in set

print(cs_courses.intersection(art_courses))      #common
print(cs_courses.difference(art_courses))        #diffe
print(cs_courses.union(art_courses))              #combined


#empty lists
empty_list = []
print(empty_list)

#empty tuple
empty_tuple = ()
print(empty_tuple)

#empty set
# empty_set = {}    #this is for empty dict not for empty set
empty_set = set()
print(empty_set)



print('-------------dict------------')

#mutable 

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp']}      # name is key and John is value
print(student)

print(student['name'])       #to access a value of a key

print(student.get('age'))
print(student.get('phone','Not Found'))     #if the key is not in the set, it will return not found


student.update({'name': 'Jane', 'age': 26, 'phone': 2345664537})    #to add or update multiple keys at the same time
print(student)

# del student['age']       #to delete a key and its value
# print(student)

# age = student.pop('age')      #similar to del
# print(age)

print(len(student))             #len = 4, because we have 4 keys

print(student.keys())           #gives all keys in a dict
print(student.values())         #gives all values in a dict
print(student.items())          #gives key and value pair

# for key, value in student.items():
#     print(key, value)