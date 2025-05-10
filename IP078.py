def caesar_cipher(text, k):
    t = ""
    for i in text:
        if i.islower(): t = t + chr((ord(i)+k-ord("a"))%26+ord("a"))
        else: t += i
    return t