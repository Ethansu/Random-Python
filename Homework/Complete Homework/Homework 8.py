import unittest
from homework_6 import Car
class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.Honda_Civic_Type_R = Car(650,20,750) 
    
    def test_Car_speedup(self):
         actual_value = self.Honda_Civic_Type_R.speedup(16)
         self.assertEqual (actual_value,320)
         actual_value = self.Honda_Civic_Type_R.speedup(16)
         self.assertEqual (actual_value,640)
         
    def test_Car_speeddown(self):
        actual_value = self.Honda_Civic_Type_R.speedup(15)
        self.assertEqual (actual_value,300)
        actual_value = self.Honda_Civic_Type_R.speeddown(5)
        self.assertEqual (actual_value,200)
        
    def test_Car_check_gas(self):
        actual_value = self.Honda_Civic_Type_R.check_gas(416)
        self.assertEqual (actual_value, 334)
        actual_value = self.Honda_Civic_Type_R.check_gas(45)
        self.assertEqual (actual_value, 289)

         
unittest.main()