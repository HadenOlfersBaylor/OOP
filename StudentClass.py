from datetime import date

class Student:

    def __init__(self,id,n,dob,c):
        self.__student_id = id
        self.__name = n
        self.__dob = dob
        self.__classif = c 
        self.__age = None
        self.___register = None

    def calculate_age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_year = dob[2]
        self.__age = today.year - int(dob_year) 

    def student_register(self):
        if self.__classif == 'senior':
            self.___register = '4/1 thru 4/3'
        elif self.__classif == 'junior':
            self.___register = '4/4 thru 4/6'
        elif self.__classif == 'sophomore':
            self.___register = '4/7 thru 4/9'
        elif self.__classif == 'freshmen':
            self.___register = '4/10 thru 4/12'  
        else:
            self.___register = 'classification not found'         

    def get_age(self):
        return self.__age

    def get_regis(self):
        return self.___register