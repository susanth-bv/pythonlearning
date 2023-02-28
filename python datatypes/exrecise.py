if __name__ == '__main__':

    languages = ["python", "java", "scala"]
    n = len(languages)
    print(n)
    while n > 0:
        print(languages[n-1])
        if n < 0:
            break
        n -= 1
