import random
import sys

def generate_password(p=None,n=14):
    # try to use uppercases and symbols
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '!@#$%^&*()'
    if p:
        result = ''
        for ch in p:
            if ch.isdigit():
                result += '!@#$%^&*()'[int(ch)]
            else:
                result += ch.upper()
        if len(result)<16:
            result += ''.join(random.sample(chars, 16-len(result)))
        return result
    else:
        
        return ''.join(random.sample(chars, n))
    
try:
    if len(sys.argv) == 1:
        password = generate_password()
    elif len(sys.argv) == 2:
        password = generate_password(sys.argv[1])
    elif len(sys.argv) == 3:
        password = generate_password(sys.argv[1], int(sys.argv[2]))
    print('Recommend Password:', password)
except:
    print('Wrong Usage!! (e.g. python generate_password.py password 10)')