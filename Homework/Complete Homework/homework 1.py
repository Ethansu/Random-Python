def even_number (list):
    list = input ("Give me a list, I'll show the even numbers: ")
    a = (list)
    print({x for x in a if x % 2 == 0})

even_number (list)