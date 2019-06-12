
def biszu(k):
    if  k == 1:
        return [1]
    else:
        return biszu(k-1) + [k]

# print(biszu(10))


#l1
def woerter(n):
    
    if n == 1:
        return ['A', 'B']
    else:
        mid = woerter(n-1)
        result = []
        for midword in mid:
            result.append('A' + midword)
            result.append('B'+midword)
            # print(result)
        return result

# print(woerter(3))



# l2

def gute_woerter(n):
    
    if n == 1:
        return ['A', 'B']
    else:
        mid = gute_woerter(n-1)
        result = []
        for midword in mid:
            if (midword[0] != 'A'):
                result.append('A' + midword)
            result.append('B'+midword)
            # print(result)
        return result

# print(gute_woerter(3))


#l3

def schoene_woerter(n):
    
    if n == 1:
        return ['A', 'B']
    else:
        mid = schoene_woerter(n-1)
        result = []
        for midword in mid:
            if (midword[0:2] != 'AA'):
                result.append('A' + midword)
            
            if (midword[0:2] != 'BB'):
                result.append('B'+midword)
            # print(result)
        return result


# print(schoene_woerter(3))


#l4


def count_appearance(arr, char):
    cnt =0
    for i in range(0, len(arr)):
        if (arr[i]==char):
            cnt+=1
    return cnt





def untermengen(list):
    if len(list) == 0:
        return [[]]
    else:
        erstes = liste[0]
        rest = liste[1:]
        return [[erster] + u for u in untermengen(rest)] + untermengen(rest)


def damen(n, rows):
    if rows > n:
        return []
    else:
        for i in range(n):