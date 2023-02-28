def check_first_last(numbers):
    if numbers[0] == numbers[-1]:
        print(True)
    else:
        print(False)

if __name__ == '__main__':

    num = [10, 20, 30, 40, 10]
    num_2 =  [75, 65, 35, 75, 30]

    check_first_last(num)
    check_first_last(num_2)


