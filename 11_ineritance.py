# 
# class className:
#     pass


class grandpa:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    def _get_my_car(self):
        return "Drive my car : Grandpa"


    def __get_salary_details(self):
        return "my salary details"
    
class papa(grandpa):

    def __init__(self, car, grandpa_salary, papa_salary):
        self.papa_salary = papa_salary
        grandpa.__init__(self, car, grandpa_salary)

    def get_my_fathers_car(self):
        return self._get_my_car()
    
    def get_my_fathers_salary(self):
        return self.__get_salary_details()
    
class childson(papa):

    def __init__(self, car, grandpa_salary, papa_salary):
        papa.__init__(self, car, grandpa_salary, papa_salary)

    def access_my_father_car(self):
        return self.get_my_fathers_car()
    
    def access_my_grandpa_salary(self):
        return self.get_my_fathers_salary()

    
# grandpaIns = grandpa('Swift', 50000)
# print(grandpaIns._get_my_car())
# print(grandpaIns.__get_salary_details())

# papaIns = papa("Swift", 50000, 80000)
# print(papaIns.get_my_fathers_car())
# print(papaIns.get_my_fathers_salary())

childSonIns = childson("Swift", 50000, 80000)
print(childSonIns.access_my_father_car())
print(childSonIns.access_my_grandpa_salary())