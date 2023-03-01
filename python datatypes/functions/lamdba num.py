if __name__ == "__main__":
    # # help= "no words"
    # # x = lambda num:num * len(help)
    # # print(x(10000))
    #
    # addition = lambda a, b ,c: a+b+c
    # print(addition(10,11,12))
    #
    # strconcat = lambda str1,str2,str3: str1 +" "+ str2 + " "  +str3
    # print(strconcat('windows', 'unix', 'linux'))
    #
    # numberList =[-19,27,38,-120,180,-39,-20000]
    #
    # positivenumberlist = list(filter(lambda number: number > 0 , numberList))
    #
    #
    # print("positive number  " ,positivenumberlist)

    numlist = [2, 3, 4, 5, 6, 7]
    squarelist = list(map(lambda number: number ** 2, numlist))
    print("square number  ", squarelist)

    nlist = [2,3,5,6,7,10]
    sortedlist = sorted(nlist, reverse=True)
    print("sorted list numbers are: ", sortedlist)

    minnumber = min(nlist)
    maxnumber = max(nlist)

    print("minimum number from list", minnumber)
    print("minimum number from list", maxnumber)

    multiplicationpower = pow(4, 5, 3)
    print("pow result", multiplicationpower)

    num1 = 7.96735
    roundnumber =round(num1, 3)
    print("ouput of round() function ", roundnumber)

    listsum = sum(nlist)
    print("sum of all num in the list ", listsum)
