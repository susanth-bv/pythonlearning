def arithematic(a,b):
    add = a+b
    subtract = a-b
    divide = a/b
    multiply = a*b

    return add, subtract, divide , multiply

if __name__ == "__main__":
    x ,y ,z ,w =arithematic(10,25)
    print(f"addition value {x}")
    print(f"subtraction value {y}")
    print(f"division value {z}")
    print(f"multiplication value {w}")

