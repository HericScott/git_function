#Take a look at this code snippet:
#What does this program print? Why?

 #solution

foo = 'bar' 
def set_foo():
     foo = 'qux'

set_foo()
print(foo)

# The program prints 'bar' cause the foo at the top most part is a global variable which make it accessable 