import re

'''
This is a Magic calculatator with python
I wanna use the most simple code to do the 
mathematical expressions and this is can be saved automatically 
by sistem without lost information or back to menu.
'''

print("Magic Calculator")
print("Type 'quit' to exit\n")

previus = 0
run = True


def performMath():
    global run
    global previus

    if previus == 0:
        equation = input('Enter equation:')
    else:
        equation = input(str(previus))

    if equation == 'quit':
        print("GoodBye, see you later !")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()"]', "", equation)
        while equation == "" and equation != 'quit':
            performMath()
        if previus == 0:
            previus = eval(equation)
        else:
            previus = eval(str(previus)+equation)


while run:
    performMath()
