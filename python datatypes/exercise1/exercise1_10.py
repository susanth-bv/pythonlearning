def prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

if __name__ =="__main__":

    for number in range(1, 101):
        if prime(number):
            print(number)