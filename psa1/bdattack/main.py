from hashlib import md5
from random import choices
from string import ascii_letters, digits

passwords = {}

def generate_password(k=8):
    return ''.join(choices(ascii_letters + digits, k=k)).encode()

def find_collision(bits):
    while True:
        p = generate_password()
        h = md5(p).hexdigest()[:bits//4]
        if h in passwords:
            
            return h, p.decode(), passwords[h]
        passwords[h] = p.decode()



def main() :
    ...

if __name__ == "__main__":
    main()