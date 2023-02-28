def check_number(list):
    i=-1
    while i < len(list):
        i += 1
        if list[i]>500:
            break
        elif list[i] % 5 == 0:
            print(list[i])
        elif list[i] >150:
            continue

if __name__ == "__main__":

    numbers =[10,28,157,267,25,29,45,500,30,505,35]
    check_number(numbers)