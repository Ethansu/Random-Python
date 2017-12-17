class Car(object):
    def __init__(self, max_speed, acceleration):
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.current_speed = 0
        
        
    def speedup(self, time):
        self.current_speed = self.current_speed + self.acceleration * time
        if self.current_speed > self.max_speed:
            print ("Warning!!! The current is faster than the max. speed.")
            self.current_speed = self.max_speed
        return self.current_speed


    def comparing_car(self, car2):
        return self.current_speed - car2.current_speed

    
my_car = Car(100,5)        
print(my_car.speedup(3))

print(my_car.speedup(2))

my_slow_car = Car(60,2)
print(my_slow_car.speedup(60))

lamborghini_asterion = Car(400, 40)
print("The max. speed of my lamborghini asterion is: " + str(lamborghini_asterion.max_speed))
lamborghini_asterion.speedup(10)

print (lamborghini_asterion.comparing_car(my_slow_car))