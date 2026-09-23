#What does the following code print?
#def scream(words): words = words + '!!!!' return print(words) scream('Yipeee')

#solution

def scream(words):
     words = words + '!!!!' 
     return 
     print(words) 
     scream('Yipeee')

#the code prints 'yipeee' but since their is 'return' showing the closure of the function body so
#the code prints none if you try to run it on a terminal      
