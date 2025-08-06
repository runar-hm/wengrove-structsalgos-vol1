
def is_prime(number):
    for i in range(2,number):
        if number % 2 == 0:
            return False
    return True
    
p = is_prime(1009)
print(p)