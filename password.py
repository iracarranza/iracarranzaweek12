import random
from string import ascii_lowercase

# the join method will add to my currently empty string: 12 random lowercase letters #
randPassword = ''.join(random.choices(ascii_lowercase, k=12))

print("Generated password: ", randPassword)