def encrypt(x,y,z,n):
    for k in range(y, len(x),z):
        if x[k].isalpha(): 
            tmp = ord(x[k])+(n-97)
            if x[k].isupper():
                if tmp <= ord("Z"): x[k] = chr(tmp)
                else: x[k] = chr(tmp-26)
            else:
                if tmp <= ord("z"): x[k] = chr(tmp)
                else: x[k] = chr(tmp-26)
def decrypt(x,y,z,n):
    for k in range(y, len(x),z):
        if x[k].isalpha(): 
            tmp = ord(x[k])-(n-97)
            if x[k].isupper():
                if tmp >= ord("A"): x[k] = chr(tmp)
                else: x[k] = chr(tmp + 26)
            else:
                if tmp >= ord("a"): x[k] = chr(tmp)
                else: x[k] = chr(tmp + 26)
def vigenere_encrypt(text, keyword):
    textl = list(text)
    a = 0
    lst = []
    for i in keyword:
        lst.append(ord(i))
    for j in lst:
        encrypt(textl,a,len(lst),j)
        a += 1
    return "".join(textl)
def vigenere_decrypt(text, keyword):
    textl = list(text)
    a = 0
    lst = []
    for i in keyword:
        lst.append(ord(i))
    for j in lst:
        decrypt(textl,a,len(lst),j)
        a += 1
    return "".join(textl)