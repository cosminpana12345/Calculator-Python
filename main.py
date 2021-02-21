def doua_numere(x, semn, y):
    x = float(x)
    y = float(y)
    if semn == ":":
        return x / y
    elif semn == '*':
        return x * y
    elif semn == '+':
        return x + y
    elif semn == '-':
        return x - y;

def calculare(ecuatie):
    L = []
    y = ""
    for x in ecuatie:
        if x.isnumeric():
            y = y + str(x)
        else:
            L.append(y)
            L.append(x)
            y = ""
    L.append(y)
    #print(L)
    while "." in L:
        for i in range(0, len(L)):
            if L[i] == '.':
                L[i - 1] = L[i - 1] + L[i] + L[i + 1]
                del L[i]
                del L[i]
                break
    #print(L)
    while ':' in L:
        for i in range(0, len(L)):
            if L[i] == ':':
                x = doua_numere(L[i - 1], L[i], L[i + 1])
                del L[i - 1]
                del L[i]
                L[i - 1] = x
                break
    while '*' in L:
        for i in range(0, len(L)):
            if L[i] == '*':
                x = doua_numere(L[i - 1], L[i], L[i + 1])
                del L[i - 1]
                del L[i]
                L[i - 1] = x
                break
    while '+' in L:
        for i in range(0, len(L)):
            if L[i] == '+':
                x = doua_numere(L[i - 1], L[i], L[i + 1])
                del L[i - 1]
                del L[i]
                L[i - 1] = x
                break
    while '-' in L:
        for i in range(0, len(L)):
            if L[i] == '-':
                x = doua_numere(L[i - 1], L[i], L[i + 1])
                del L[i - 1]
                del L[i]
                L[i - 1] = x
                break
    if len(L) == 1:
        return L[0]
    else:
        return "What happened?"
    #print(L)

def calculare_totala(ecuatie):
    L = []
    s = ""
    for i in range(len(ecuatie)):
        x = ecuatie[i]
        if x == "(":
            if s != '':
                L.append(s)
                s = ""
            L.append(x)
        elif x == ")":
            if s != '':
                L.append(s)
                s = ""
            L.append(x)
        else:
            s = s + x
    if s != "":
        L.append(s)
    if L[0] == '(' and L[len(L) - 1] == ')':
        del L[0]
        del L[len(L) - 1]
    print(L)

    while "(" in L:
        ipd = -1  # ipd = indice paranteza deschisa
        for i in range(len(L)):
            if L[i] == "(":
                ipd = i
        if ipd != -1:
            val = calculare(L[ipd + 1])
            del L[ipd]
            del L[ipd]
            L[ipd] = val
            if ipd != 0:
                if L[ipd - 1] != "(" and L[ipd - 1] != ")":
                    L[ipd] = L[ipd - 1] + str(L[ipd])
                    del L[ipd - 1]
                    ipd -= 1
            if ipd < len(L) - 1:
                if L[ipd + 1] != "(" and L[ipd + 1] != ")":
                    L[ipd] = str(L[ipd]) + L[ipd + 1]
                    del L[ipd + 1]
                print(L)
    return calculare(L[0])

print("Operatori:\n+ = adunare;\n- = scadere;\n* = inmultire;\n;: = impartire.\nSe accepta si numere neintregi(Se va folosi . ca delimitator intre partea intreaga si partea fractionara.)\n")
ec = input()
ec = ec.replace(" ", "")
ec = ec.replace("\n", "")
print(ec)
print(calculare_totala(ec))