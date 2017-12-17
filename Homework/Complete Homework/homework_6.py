import time
class Car():
    def __init__(self, max_speed, acceleration, total_gas):
        self.max_speed = max_speed 
        self.acceleration = acceleration
        self.total_gas = total_gas
        self.current_speed = 0
        self.distance = 0
        self.old_gas = total_gas
        

    def speedup(self, time):
        self.current_speed = self.current_speed + self.acceleration * time
        if self.current_speed > self.max_speed:
            print ("Warning!!! The current speed is faster or the same as the max. speed.")
            self.current_speed = self.max_speed
        if self.current_speed <= 0:
            self.current_speed = 0
        return self.current_speed
    
    
    def speeddown(self, time):
        self.current_speed = self.current_speed - time * self.acceleration
        return self.current_speed


    def check_gas(self, distance):
         current_gas = self.old_gas - distance
         print ("You have " + str (current_gas) + " gas out of " + str (self.total_gas) + " after you arrived")
         self.old_gas = current_gas
         if current_gas <= 50 and current_gas > 0:
             print("Warning low on gas!!")
         if current_gas <= 0:
             print ("No more gas. 😢 ")
         return current_gas

class electronic_car(Car):
    def __init__(self, battery_life, max_speed, acceleration):
#        self.battery_life = battery_life
#        self.max_speed = max_speed
#        self.acceleration = acceleration
#        self.current_speed = 0       
#        self.old_battery = battery_life
        
        super().__init__(max_speed, acceleration,0)
        self.old_battery = battery_life
        self.battery_life = battery_life
    
    def check_gas(self):
        print("Gas is not available in electronic_car.")


        
#    
#tesla_model_s = electronic_car (450, 345, 20)
#print (str (tesla_model_s.max_speed)  +' '+ str ( tesla_model_s.acceleration))
#print(str(tesla_model_s.speedup(5))) 
#tesla_model_s.check_gas()  
#print(str(tesla_model_s.old_gas)) 
#    
    
    
def GPS ():
    lamborghini_asterion = Car(650, 40, 500)
    lamborghini_asterion.speedup(13)
    print ("Type exit to exit")
    print ("Please only type in lowercase!")
    print ("Type the numbers not the words!")
    while True:  
        old_barn = 1
        vancouver_airport = 41
        usa_border = 124
        sir_willam_osler_elementary_school = 12
        science_world = 32
        gas_station = 10
        destination = input (""" Choose from: 
        1: Old barn 1km away  
        2: Vancouver Airport 41km away 
        3: USA Border 124km away 
        4: Sir William Osler Elementary School 12km away 
        5: Science World 34km away 
        6: Gas station 10km away: """)
        if destination == ("exit"):
            break
        if destination == ("1"):
            oldbarn = old_barn /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(1) 
            lamborghini_asterion.check_gas(1)
            print ("You arrived in " + str (oldbarn) + " hours.")
        if destination == ("2"):
            vancouverairport = vancouver_airport /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(7) 
            lamborghini_asterion.check_gas(41)
            print ("You arrived in " + str (vancouverairport) + " hours.")
        if destination == ("3"):
            usaborder = usa_border /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(12) 
            lamborghini_asterion.check_gas(124)
            print ("You arrived in " + str (usaborder) + " hours.")
        if destination == ("4"):
            sirwillamoslerelementaryschool = sir_willam_osler_elementary_school /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(4) 
            lamborghini_asterion.check_gas(12)
            print ("You arrived in " + str (sirwillamoslerelementaryschool) + " hours.")
        if destination == ("5"):
            scienceworld = science_world /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(6) 
            lamborghini_asterion.check_gas(32)
            print ("You arrived in " + str (scienceworld) + " hours.")
        if destination == ("6"):
            gasstation = gas_station /  lamborghini_asterion.current_speed
            print ("You are traveling at the speed of " +  str (lamborghini_asterion.current_speed) + (" km per hr"))
            time.sleep(5) 
            lamborghini_asterion.check_gas(10)
            print ("You arrived in " + str (gasstation) + " hours.")
            lamborghini_asterion.old_gas=lamborghini_asterion.total_gas
            lamborghini_asterion.current_gas = lamborghini_asterion.total_gas
            print ("You refilled you gas tank to 500")