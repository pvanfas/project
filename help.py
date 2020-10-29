from django.core.management.utils import get_random_secret_key

key = get_random_secret_key()
print('NEW SECRET_KEY IS\n' + key)
