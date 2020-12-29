""" ** Password Picker **

Series   : 10 line projects
Language : Python3
Lines    : 5       (comments are not counted)

Pick secure and hard to guess password.
This program generates easy to remember
yet hard to crack passwords for you.

(c) author: ashraf minhaj
    mail  : ashraf_minhaj@yahoo.com
"""


# import library
import random

# set some names as you wish
adjectives = ['quick', 'slow', 'hot', 'sexy']
words      = ['jorina', 'cow', 'lip']

# now we generate new password randomly
password = random.choice(adjectives) + random.choice(words) + str(random.randint(0, 100))

print(password)
