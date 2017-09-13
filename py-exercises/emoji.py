#play with emoji unicode
palm = u"\U0001F334"
ok = u"\U0001F44C"
flower = u"\U0001F33A"

emoji = [palm, ok, flower]

def emoji():
    ans = str(input("Which emoji do you want? Type in palm/ok/flower or type 'quit' to stop playing"))
    while ans != "quit":
        if ans == "palm":
            print (palm)
        if ans == "ok":
            print(ok)
        if ans =="flower":
            print(flower)
        ans = str(input("Which emoji do you want? Type in palm/ok/flower or type 'quit' to stop playing"))
    print("bye")

#random emoji function
