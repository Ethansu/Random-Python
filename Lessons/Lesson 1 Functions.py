import random
a = range(1,20)
for n in a:
   if n % 2 == 0:
      print (n)

print([x for x in a if x % 2 == 0])    
c = range (1,20)
a = random.randint(1,101)
print ("flag 1")
def check_even(jhkjhkj):
    print("Is " + str(jhkjhkj) + " even or odd number?")
    if jhkjhkj % 2 == 0:
        print ("even")
    else:
        print("odd")


check_even(a)
print("flag2")
b = 13224434    
check_even(b)

check_even (123)

s = ("Hello World")

def Hello():
    print ("Hello World")  
Hello ()
Hello()

def find_odd_from_a_list_of_numbers (l):
    print ([n for n in l if n % 2 == 0])
d = (1,2,3,4,5)
find_odd_from_a_list_of_numbers (c)

def lets (a) :
    for n in a:
        if n % 2 == 0 or n % 3 == 0 :
            print
        else:
            if n % 2 == 1 or n % 3 == 1 or n % 3 == 2:
                print (n)
lets (range(1,11))