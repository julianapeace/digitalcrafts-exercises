#week2 Friday Challenges

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        elif n % 2 == 1:
            n = n*3 +1
        print('Collatz Sequence: {} \n'.format(n))

# collatz(200)
def isPal(n):
    n = str(n)
    if n[:] == n[::-1]:
        return True

def palnum(n):#could be solved with math or programming way by manipulating strings
    #find if palindrome



palnum(9009)

def challenge3(counter):
    #divide from 1 to 10
    if counter < 2500:
        return hello
    else:
        for i in range (1,10):
            ans = counter % i
            if ans != 0:
                challenge3(counter-1)
    print(counter)

# challenge3(3000)
