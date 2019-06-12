""" queue => first in first out """
""" stack => last in last out """
""" pop() letztes element wird entfernt und zurückgegeben """
""" pop(index) entfernt element at index und gibt zurück """

def klammerungAllChars(myString):
    stack = []
    for currChar in myString:
        if (currChar == '('):
            stack.append('(')
        elif (currChar == ')'):
            if len(stack) ==0:
                return False
            stack.pop()
    return (len(stack) ==0)
     
def klammerung(myString):
    stack= []
    for currChar in myString:
        if (currChar == '('):
            stack.append('(')
        else:
            if len(stack) ==0:
                return False
            stack.pop()
    return len(stack)== 0


stringtocheck = input()
if stringtocheck != "":
    print("Only () returns: " + str(klammerung(list(stringtocheck))))
    print("All Chars returns: " + str(klammerungAllChars(list(stringtocheck))))
else:
    print("nothing in there..")