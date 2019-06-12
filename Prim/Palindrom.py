
def palindrom(possiblePalindrom):
    possiblePalindromLastIndex= len(possiblePalindrom)-1;
    for i in range(0, int(len(possiblePalindrom) / 2)):
        if (not possiblePalindrom[i] == possiblePalindrom[possiblePalindromLastIndex]):
            return False;
        else:
            possiblePalindromLastIndex = possiblePalindromLastIndex-1;
    return True


def satzpalindrom(possiblePalindrom):
    possiblePalindromLastIndex= len(possiblePalindrom)-1;
    i = 0
    while (i < int(len(possiblePalindrom) / 2)):
        if (possiblePalindrom[i].isalpha()):
            if (possiblePalindrom[possiblePalindromLastIndex].isalpha()):
                if (not possiblePalindrom[i].lower() == possiblePalindrom[possiblePalindromLastIndex].lower()):
                    return False;
                else:
                    i +=1
                    possiblePalindromLastIndex = possiblePalindromLastIndex-1
            else:
                possiblePalindromLastIndex = possiblePalindromLastIndex-1
        else:
            i +=1
    return True


def satzpalindrom2(possiblePalindrom):
    palindromSentence =""
    for i in range(0, len(possiblePalindrom)):
        if (possiblePalindrom[i].isalpha()):
            palindromSentence+=possiblePalindrom[i].lower()


    return palindrom(palindromSentence)






palindromWort='SIEESSEEIS'
print(palindromWort +" => "+ str(palindrom(palindromWort)))

palindromSatz= 'Regal mit Sirup pur ist im Lager.'
print(palindromSatz +" => "+ str(satzpalindrom(palindromSatz)))

palindromSatz2= 'Regal mit Sirup pur ist im Lager.'
print(palindromSatz2 +" => "+ str(satzpalindrom2(palindromSatz2)))



