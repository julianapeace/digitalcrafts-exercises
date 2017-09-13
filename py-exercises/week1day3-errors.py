#error handling
def error1():
    while True:
      try:
        x = int(input("Please enter a number: "))
        break
      except ValueError:
        print("Oops!  That was no valid number.  Try again...")
# error1()

#try/except statements
def error2():
    try:
      x = int(input("enter a number:"))
    except ValueError:
      print ("Oops, no valid number, try again")
    except MemoryError:
      print("sorry this computer sucks!")
    else:
        x = x + 10
        print(x)
        break
    finally:
      print("always_execute()")

#create your own error message
#you're catching the error and putting your custom message in it.
def error3():
    raise NameError('Hi There')
    raise ValueError
    class MyError(Exception):
      pass

# mymodule.py
def test ():
  name = "Narf"
  print(name[10])
  print("done")
if __name__ == '__main__':
  test()
