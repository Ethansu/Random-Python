i = 1
print("Enter yes to start a conversarion with me 😄")
start = input ("Do you want to chat? ")
if start == 'yes':
    print ("Hi I'm Hello Bot 😄")
    print ("Type bye to exit")
    while i == 0:
        i -= 1
        name = input ("What's your name? ")
        if name.title() == 'Bye':
            print('See you next time. 👋')
            break
        if name != '':
            print ("Hello " + name + "!")
     while   
        lol = input ("Do you want to hear a joke? " )
        if lol.title() == 'Yes':
            print ("Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all. Ha Ha Ha Ha Ha Ha Ha.")
        if lol.title() == "bye":
            print ('See you next time. 👋')
        else:
            print ("😞")
else:
    print ("Nooooooo 😞 ")