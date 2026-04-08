class college:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def student_details(name, age):
        return f"Student details : {name} : {age}"
    
    def get_teachers_details(self):
        return f"teacher name - {self.name}"
    
class instrument:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(college.student_details(self.name, self.age))
        clsIns = college("Sohan", 23)
        print(clsIns.get_teachers_details())


insIns = instrument("Rohan", "Age")
