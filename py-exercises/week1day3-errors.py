#error handling
def error1():
    while True:
      try:
        x = int(input("Please enter a number: "))
        break
      except ValueError:
        print("Oops!  That was no valid number.  Try again...")
# error1()

#exception: an error that occurs at runtime
#handle an exception: to prevent an exception from terminating a program by wrapping the block of code in a try/except construct

#try/except statements
def error2():
    try: #your normal code goes here
      x = int(input("enter a number:"))
    except ValueError: #if exception (aka error) is raised, then execute this block
      print ("Oops, no valid number, try again")
    except MemoryError:
      print("sorry this computer sucks! Close your facebook!")
    else: #if there was no exception then execute this block
        x += 10
        print(x)
    finally: #This block of code will always be executed, even if there are exceptions raised
      print("always_execute()")
# error2()

#create your own error message
#you're catching the error and putting your custom message in it.
def error3():
    raise NameError('Hi There') #raise: to cause an exception
    raise ValueError
    class MyError(Exception):
      pass
error3()

# mymodule.py
def test ():
    name = "Narf"
    print(name[10])
    print("done")
    if __name__ == '__main__':
        test()
