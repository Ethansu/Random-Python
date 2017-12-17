import time
class restuarant ():
    def __init__ (self, driver = "James", resturantimformer = "Lisa"):
        self.driver = driver
        self.resturantimformer = resturantimformer            
            
restuaranttwo = restuarant ()
while True:
    ask = input ("My name is " + self.driver + ". What kind of of restuarant do you want to go to, chinese or japanese? ")
    if ask.upper() == "CHINESE":
        print ("Sure. It'll be a 7 min ride.")
        time.sleep(5)
        money = input ("We arrived. Can you pay me $3.50, yes or no? ")
        if money.upper() == "YES" :
            print ("Thanks.")
            time.sleep(3)
            greeting = input ("你好我的名字是" + self.resturantimformer + "你想在这里吃午餐吗？ / Hello my name is " + self.resturantimformer +  ", do you want to eat lunch here? ")
            if greeting.upper() == "YES":
                menu = input ("""好的，这里是你的菜单： / Okay here is your menu:
            NOODLES / 面条                          
--------------------------------------------|                               
| 1. Banmian / 拌面	$9.60	         
| 2. Beef noodle soup / 牛肉面条汤 $8.75	
| 3. Cart noodle / 车面条 $10.30              		
| 4. Chow mein / 炒面	$14.50		
| 5. Hokkien mee / 福建面 $10.32			
| 6. Hot dry noodles / 热干面条 $9.65
| 7. Lanzhou beef lamian / 兰州牛肉拉面 $9.80   		

                
What do you want :) ? Write here: """)
                if menu == " " or menu == "" or menu == "  ":
                    drink = input ("What? Do you want some drinks instead? ")
                    if drink.upper() == "YES":
                        dmenu = input ("""Here's you drink menu:
      Drinks / 饮料
-------------------------------|
| 1. Orange Juice / 橙汁 $3.00
| 2. Apple Juice / 苹果汁 $3.00
| 3. Coca cola / 可口可乐 $2.50    
| 4. Red Tea / 红茶 $1.00
| 5. Green Tea / 绿茶 $1.00
| 6. Water / 水 $0.50


Write here: """)
                        if dmenu == "" or dmenu == " " or dmenu == "  ":
                            print ("We don't have anything else. You can leave. / 我们没有别的。 你可以走了。")
                            time.sleep(3)
                        else:
                            print ("So you want " + dmenu + "right? Okay coming in 5 mins.")
                            time.sleep(4)
                            print ("Here you go. / 干得好")
                            time.sleep(4)
                            print ("$45.67.")
                            print ("Thanks / 谢谢")
                            print ("Bye / 再见")
                            byea = input("Do you want to go home or keep eating?")
                            if byea.upper() == "GO HOME":
                                print("Okay")
                                break
                            else:
                                print("Okay")
                else:
                    menud = input("""当然，所以你想要的权利？""" + menu + """这里是你的饮料菜单：/ Sure so you want """ + menu + """ right? Here is you drink menu: 
        Drinks / 饮料
-------------------------------|
| 1. Orange Juice / 橙汁 $3.00
| 2. Apple Juice / 苹果汁 $3.00
| 3. Coca cola / 可口可乐 $2.50    
| 4. Red Tea / 红茶 $1.00
| 5. Green Tea / 绿茶 $1.00
| 6. Water / 水 $0.50


Write here: """)
                    if menud == "" or menud == " " or menud == "  ":
                        print ("You don't want drinks? Okay the food is coming in 25 min.")
                        time.sleep(5)
                        print ("Here you go. / 干得好")
                        time.sleep(5)
                        print ("""Thanks, here's your receipt / 谢谢，这是你的收据:
    RECEIPT                                    
--------------- 
Total $50.75""")
                        print ("Bye / 再见")
                        time.sleep(3)
                        bye = input ("Do you want to go home or keep eating?")
                        if bye.upper() == "GO HOME":
                            print("Okay")
                            break
                        else:
                            print ("Okay")                                    
            else:
                print ("你在做什么？ 你为什么在这？ 你在监视我们吗？ 我正在打电话给警察。 你受够了！ / What are you doing? Why are you here? Are you spying on us? I am calling the police. YOU GOT ARRESTED!")
                break
        else:
            print ("I'm calling the police")
            time.sleep
            time.sleep(3)
            print ("YOU GOT ARRESTED!!!")
            break