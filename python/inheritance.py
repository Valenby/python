# object oriented programing - inheritance 

class Students:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def greeting(self):
        return f'hello! i am {self.first_name} {self.last_name}'
    

class CollegeStudent(Students): 
    def __init__(self, first_name, last_name, major ):
        super().__init__(first_name, last_name) 
        self.major = major
        
    def greeting(self):
        return f'{self.first_name} is a college student!' 

class NoCollegesStudent(Students):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__( first_name, last_name)
        self.future_adult_job = future_adult_job
    
    def grow_up(self):
        return f'when i grow up, i want to be ' \
               f'a {self.future_adult_job}'


studen_2 =  Students('elizabeth','jijijij')
studen_1 =  CollegeStudent('victoria', 'jejeje', "required proffesion xd")
studen_3 = NoCollegesStudent('carlos', 'learning UWU', 'Seller')

print(studen_1.greeting())
print(studen_2.greeting())
print(studen_1.major)
print(studen_3.future_adult_job)
print(studen_3.grow_up())

    
    
    
    
    