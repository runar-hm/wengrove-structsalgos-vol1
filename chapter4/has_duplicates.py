

# Array, each value is between 0-10
array = [1,5,3,9,1,4]

# O(N^2) Quadratic time
def has_duplicate_value_quadratic(array):
    steps = 0
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1
            if (i != j) and (array[i] == array[j]):
                print(f'Quadratic Algo - Steps: {steps}',end=' ')
                return True
    print(f'Quadratic Algo - Steps: {steps}',end=' ')
    return False

# O(N) Linear time
def has_duplicate_value_linear(array):
    steps = 0

    # Exploit the fact that numbers will always be within range 0-10
    number_index = [0] * 11

    for i in range(len(array)):
        steps += 1
        if number_index[array[i]] == 1:
            print(f'Linear Algo - Steps: {steps}',end=' ')
            return True
        else:
            number_index[array[i]] = 1

    print(f'Linear Algo - Steps: {steps}',end=' ')
    return False



print(f'Quadratic: {has_duplicate_value_quadratic(array)}')
print(f'Linear: {has_duplicate_value_linear(array)}')

