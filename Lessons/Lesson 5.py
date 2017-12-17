import unittest
#from  lol import lol
#class TestLol(unittest.TestCase):
#    def test_lol(self):
#        acutal_value = lol(7)
#        self.assertEqual(acutal_value,2)
#               
#unittest.main()

from homework_6 import Car
class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.Honda_Civic_Type_R = Car(650,20,750) 
    
    def test_Car_speedup(self):
         actual_value = self.Honda_Civic_Type_R.speedup(16)
         self.assertEqual (actual_value,320)
         actual_value = self.Honda_Civic_Type_R.speedup(16)
         self.assertEqual (actual_value,640)
         
         
    def test_Car_infinte_time_speedup(self):
         actual_value = self.Honda_Civic_Type_R.speedup(31684)
         self.assertEqual (actual_value,650)
         
    def test_Car_negative_time_speedup(self):
         actual_value = self.Honda_Civic_Type_R.speedup(-63634)
         self.assertEqual (actual_value,0)     
         
unittest.main()