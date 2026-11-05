def count(a:list):
    letters = []
    for i in a:
        for l in set(i):
            if not letters.__contains__(l):
                letters.append(l)
    n=0
    for letter in letters:
        count = 0
        for i in a:
            if i.count(letter)>count:
                count = i.count(letter)
        n+=count
    
    
    return n

def manager(s:str):
    data = s.split("\n")
    classes = []
    for i in data:
        if i.isdigit():
            if not classes == []:
                print(count(classes))
            classes = []
        else :
            classes.append(i)
    if not classes == []:
        print(count(classes))

def __main__():
    x=""
    n = input()
    x+=n
    for i in  range(int(n)):
            s = input()
            x+="\n"
            x+= s
            for a in range (int(s)):
                x+="\n"
                w = input()
                x+=w

    manager(x)


if __name__ == "__main__":
    __main__()
