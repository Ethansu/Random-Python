import unittest
from Homework_9 import Employee
class test_Employee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee()
    
    def test_give_default_raise(self):
         actual_value = self.employee.give_raise()
         self.assertEqual (actual_value, 1005000)
         
    def test_give_custom_raise(self):
         self.Employee2 = Employee(annual_salary = 10000)
         actual_value = self.Employee2.give_raise(1000) 
         self.assertEqual (actual_value, 11000) 
        

unittest.main()