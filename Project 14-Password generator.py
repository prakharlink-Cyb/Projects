import string
import random


if __name__ == "__main__":
    s1 = string.digits
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    s4 = string.punctuation

    plen = int(input("Enter password length \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    print("".join (s[0:plen]))