#Python Part 1 Exercise

def exercise1():
    name = input ('What is your name?')
    print ("Hello, ", name, "!")
exercise1()

def exercise2():
    name = (input ("What is your name?")).upper()
    print ("Hello".upper(), name)
exercise2()

def exercise3():
    name = input("What is the name?")
    subject = input("What is the subject?")
    print (name, "'s favorite subject in school is ", subject, ".")
exercise3()

def exercise4():
    day = int(input("Day (0-6)?"))
    if day == 0:
        print ("Sunday")
    elif day == 1:
        print ("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print ("Wednesday")
    elif day == 4:
        print ("Thursday")
    elif day == 5:
        print ("Friday")
    elif day == 6:
        print ("Saturday")
exercise4()

def exercise5():
        day = int(input("Day (0-6)?"))
        if day == 0 or day == 6:
            print ("Sleep in")
        else:
            print ("Go to work")
exercise5()

def exercise6():
    degree = float(input("What is the temperature in C?"))
    degree = degree * 1.8 + 32
    print ("That is", degree, "in Fahrenheit.")
exercise6()

def exercise7():
    bill = float(input("Total bill amount?"))
    service = input ("Level of service? Write 'good','fair', or 'bad'")
    service = service.lower()
    if service == "good":
        tip = bill * 0.20
    elif service == "fair":
        tip = bill * 0.15
    else:
        tip = bill * 0.10
    totalbill = bill + tip
    print ("Tip amount:", "\t", tip, "\n", "Total amount:", "\t" ,totalbill, "\n")
exercise7()

def exercise8():
    bill = float(input("Total bill amount?"))
    service = input ("Level of service? Write 'good','fair', or 'bad'")
    service = service.lower()
    if service == "good":
        tip = bill * 0.20
    elif service == "fair":
        tip = bill * 0.15
    else:
        tip = bill * 0.10
    people = int(input ("Split how many ways? Enter integer."))
    totalbill = bill + tip
    split = totalbill/people
    print ("Service was", service, "\n", "Tip amount:", "\t", tip, "\n", "Total amount:", "\t" ,totalbill, "\n", "Amount per person:","\t" ,split)
exercise8()

def exercise9():
    i = 0
    while i < 10:
        i = i + 1
        print (i)
exercise9()

def exercise10():
    coin = 0
    answer = ""
    while answer != "no":
        print ("You have", coin, " coins.")
        answer = input ("Do you want another?")
        answer = answer.lower()
        coin = coin + 1
    print ("Bye")
exercise10()
