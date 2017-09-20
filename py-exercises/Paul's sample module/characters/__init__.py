#from characters.werewolf import WereWolf

__all__ = ['blob', 'werewolf'] #does the same as #from characters.werewolf import WereWolf
#now in the terminal if we type in "from characters import *", you will find a werewolf

#circular dependencies: two files referencing each other
#how to avoid: try to be specific, import only the module(or variable) that you need, or place the import statement only in the method.
