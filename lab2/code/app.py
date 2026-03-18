import random
import string
import time

def generate_password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "#[]().,!@&^%*"
    all_chars = lower + upper + digits + special

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    length = random.randint(8, 16)
    password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)
    return "".join(password)

def application(environ, start_response):
    password = generate_password()
    
    time.sleep(0.05)

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    
    return [password.encode('utf-8')]