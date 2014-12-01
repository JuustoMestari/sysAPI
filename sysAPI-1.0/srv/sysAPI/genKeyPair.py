from random import choice
from string import ascii_letters

authfile = 'authfile.conf'
n = 32

secretkey = "".join(choice(ascii_letters) for i in range(n))
accesskey = "".join(choice(ascii_letters) for i in range(n))


with open(authfile, "a") as myfile:
    myfile.write(secretkey+'#'+accesskey+'\r\n')

print("KEY PAIR : %s#%s added to %s" % (secretkey,accesskey,authfile))