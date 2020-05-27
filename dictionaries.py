sub_on_students = {'Arabic':3, 'English':3,'Math':2}
#print(sub_on_students)
students = {'Arabic':['ali','ahmad','yusuf'],'English':['jack','jay','eva']}
#print(students)
students['Math']=['mona','fatima']
#print(students)
students.update({'History':'fadi'})
#print(students)
sub_on_students.update({'History':1})
print( 'sub_on_students : ', sub_on_students)
print('students_name :' ,students)