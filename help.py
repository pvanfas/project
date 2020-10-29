python -c 'import random;import string; print("".join(random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(50)))'
