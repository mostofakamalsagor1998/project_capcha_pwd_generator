import string
import random

def main():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s3))
    s.extend(list(s2))
    s.extend(list(s4))
    random.shuffle(s)
    plen =int(input('Enter password length: '))
    print("Your password is : "+"".join(s[0:plen]))

if __name__ == "__main__":
    main()