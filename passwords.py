import random
import string

length = 12

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

all_chars = lower + upper + digits
password = random.sample(all_chars, length)
random.shuffle(password)
final_password = ''.join(password)

print("Generated Password:", final_password)
