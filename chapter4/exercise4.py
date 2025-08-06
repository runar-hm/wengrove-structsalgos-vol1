
array = [9,4,139,453,682,1234,6814,392]


# O(N^2)
def greatest_number_on2(array):
    if not array:
        return None
    for i in array:
        # Assume for now that i is the greatest:
        is_i_the_greatest = True

        for j in array:
            if j > i:
                is_i_the_greatest = False

        if is_i_the_greatest:
            return i
        

print(f'O(N^2): {greatest_number_on2(array)}')

# Linear Solution O(N)
def greatest_number_on(array):
    greatest = 0

    for i in array:
        if i > greatest:
            greatest = i

    return greatest

print(f'O(N): {greatest_number_on(array)}')