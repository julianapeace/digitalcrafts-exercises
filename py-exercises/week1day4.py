
def example():
    from matplotlib import pyplot

    def f(x):
        return 2 * x +1
    def g(x):
        return x + 1

    f_output = []
    g_output = []

    x_list = list(range(-3, 5))

    for x in x_list:
        f_output.append(f(x))
        g_output.append(g(x))
    pyplot.plot(x_list, f_output, x_list, g_output)
    pyplot.show()


def example1():
    def f(x):
        return 2 * x +1
    def g(x):
        return x + 1
    for x in range(-3,5):
        print("f({x}) = {y} \t g({x}) = {z}".format(x = x, y = f(x), z = g(x)))
# example1()

#a good way to code, and helps communicate with other developers is to do this
#arguments can be in any order, IF it is labelled
def hello(first_name=None, last_name=None):
    print(first_name, last_name)
# hello("paul", "bailey")
# hello(last_name="paul", first_name="bailey")

#eats all the arguments
def hello2(*args, **kwargs):
    print(*args)
    print(**kwargs)

# hello(1,2,4, name="paul", color="red")

def hello3(name, *args):
    print("Hello", name)
    for arg in args:
        print("Hello", arg)

# hello3('Julie')
# hello3('Julie', 'Paul', 'Pinky')

def examplegloballocalvariables():
    words = ['hello', 'world'] #this is a global variable
    def displaylist():
        words2 = ['hello']
        print(words)#see how you can reference a global variable
        print(words2) #this is a local variable
    displaylist()
    print(words2) #this will throw an error because it is a local variable. It's unaccessible outside of the function.

#The new python forces you to be more explicit. Cannot change global variables within functions unless specify GLOBAL
printed_hello = False
def display_hello():
    global printed_hello
    print('Hello')
    printed_hello = True
# print (printed_hello)
# display_hello()
# print(printed_hello)
#rule of thumb: try not to use global variables as much as possible
#you may use global variables for constants like pi or speed of light

def say_hello ():
    print("Hello World")
if __name__ == "__main__": #write this line all the time. the "__" double underscore is a special python code.
    say_hello()
