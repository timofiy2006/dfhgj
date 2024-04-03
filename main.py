import random
import string
letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(10)) )
letters = string.ascii_uppercase
print ( ''.join(random.choice(letters) for i in range(10)) )
letters = string.digits
print ( ''.join(random.choice(letters) for i in range(10)) )