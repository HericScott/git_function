#What happens when you run the following program? Why do we get that result?
#solution

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

#This code results in a NameError: name 'foo' is not defined because the variable foo created inside the set_foo() function is local to that function and does not exist in the global scope when print(foo) runs.
