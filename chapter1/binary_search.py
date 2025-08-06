
def binary_search(array, search_value):
    lower_bound = 0 
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        
        midpoint = ( upper_bound + lower_bound ) // 2
        value_at_midpoint = array[midpoint]

        if value_at_midpoint == search_value:
            return midpoint
        if search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        if  search_value > value_at_midpoint:
            lower_bound = midpoint + 1

    return None
    

t = binary_search([3,17,75,22,80,202], 80)
print(f'result: {t}')


