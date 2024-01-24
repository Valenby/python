# object oriented programing

'''
# class Student:
#     pass

# student_1 = Student()
# student_2 = Student()

# student_1.first_name = 'Erik'
# student_1.last_name = 'Roby'
# student_1.major = 'Computer Science'

# student_2.first_name = 'Valentina'
# student_2.last_name = 'Pulgarin'
# student_2.major = 'Math'

# print(student_1.major)
# print(student_2.last_name)
'''

class Students:
    
    number_of_students = 0
    school = 'Online School'
    
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        
        Students.number_of_students += 1
    
    # metodos students:
    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} major!'
     
    def  fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} going to {self.school}' 
    
    #Metodos de class:
    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school   
    
    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)    
               
#object 
student_1 = Students('vale','pulga','nose')
student_2 = Students('peto','restre','nosex2')

new_student = 'Adil.yutzy.English'
student_3 = Students.split_students(new_student)
print(student_3.first_name)





# print(student_1.school)
# print(student_2.school)
# Students.set_online_school('I use google hangouts for class')
# print(student_1.school)
# print(student_2.school)




# print(f'Number of students = {Students.number_of_students}')

# print(student_1.fullname_major_school())
#print(Students.fullname_with_major(student_2))

# print(student_2.fullname_major_school())

#print(student_1.school)





