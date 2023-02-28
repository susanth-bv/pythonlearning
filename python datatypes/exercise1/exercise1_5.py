def palindrome(x):
    numb = str(x)
    rev_numb = numb[::-1]
    if numb ==rev_numb :
        print("palindrome")
    else:
        print("not Palindrome" )

if __name__ == '__main__':

     a =1279721
     b= 16789643

     palindrome(a)
     palindrome(b)

