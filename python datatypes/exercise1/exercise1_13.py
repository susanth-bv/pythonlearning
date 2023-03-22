def evenindexelemenets(list):
    k = len(list)
    for i in range(0,k):
        if i % 2 == 0:
            print(list[i])

programmingLangs = ["Python", "Java", "Scala", "Go-Lang", "Ruby"]

evenindexelemenets(programmingLangs)

