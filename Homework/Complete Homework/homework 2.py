def sum_of_numbers_in_a_list_that_cannot_be_divided_by_2_3_or_5 (list):
    c = 0
    for a in list:
        if a % 2 != 0 and a % 3 != 0 and a % 5 != 0:
            c = c + a
    return c

b = (range(1,10000))           
print(sum_of_numbers_in_a_list_that_cannot_be_divided_by_2_3_or_5 (b))