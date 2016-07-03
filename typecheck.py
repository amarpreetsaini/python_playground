
  """  First, def a function called distance_from_zero, with one argument (choose any argument name you like).
    If the type of the argument is either int or float, the function should return the absolute value of the function input.
    Otherwise, the function should return "Nope" """
    
    def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Nope"
    
