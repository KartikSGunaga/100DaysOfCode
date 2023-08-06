import random
import string

length = int(input('Enter the length of your password: '))
#password_list = []

password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(length)])

print(password)



