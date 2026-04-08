from abc import ABC, abstractmethod

class college(ABC):

    def __init__(self, student_name, enrollment_status):
        self.student_name = student_name
        self.enrollment_status = enrollment_status

    @abstractmethod
    def pay_fees(self):
        return "Fees paid/ abstract method implemented"
    
class student(college):

    def __init__(self, name, enrollment_status):
        college.__init__(self, name, enrollment_status)

    def pay_fees(self):
        return "Fees paid"

studentIns = student("Rohan", True)
print(studentIns.pay_fees())

