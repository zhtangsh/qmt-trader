import os
import string
import random


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_env(key, default_val=None):
    val = os.getenv(key)
    if val is None:
        return default_val
    return val


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
