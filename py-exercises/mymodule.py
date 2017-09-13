#use pdb to debug
#import pdb.run('mymodule.py')
# or python3 -m pdb mymodule.py
#break into the debugger by adding "pdb.set_trace()" anywhere in the code where you are not getting the answer you want
def test ():
  name = "Narf"
  print(name[10])
  print("done")
if __name__ == '__main__':
  test()
