def divisible_five(list):
    for x in list :
        if x % 5 == 0:
            print(x)

if __name__ == '__main__':

    numb =[1,3,5,10,20,28]


    divisible_five(numb)