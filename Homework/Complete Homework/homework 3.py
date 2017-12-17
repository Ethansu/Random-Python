def delete_all_duplicated_numbers_in_a_list (list):
    print (set(list)) 
list = [int(x) for x in input ("Tell me a list of numbers, I'll remove the duplicated numbers: ").split(',')]

delete_all_duplicated_numbers_in_a_list (list)