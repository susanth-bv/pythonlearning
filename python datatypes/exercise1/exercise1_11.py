def fibonacii(number):
    if number <= 0 :
        print("not true")
    elif number ==1 or number==2:
        return 1
    else:
        return fibonacii(number-1) + fibonacii(number-2)
for i in range(1,11):
 print (fibonacii(i))


