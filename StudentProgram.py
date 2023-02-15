import StudentClass as sc

Haden = sc.Student(8936,'Haden','01/08/2001','senior')
Haden.calculate_age()
Haden.student_register()

print(f"\nStudent Age: {Haden.get_age()}\nRegistration Dates: {Haden.get_regis()}\n")