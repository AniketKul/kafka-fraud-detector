from string import ascii_letters, digits
from random import choices, randint

account_chars: str = digits + ascii_letters

"""Return a random account number which consists of 15 characters"""
def create_random_account_id():
    return ''.join(choices(account_chars, k=15))

"""Return a random amount between 1.00 and 5000.00 USD"""
def create_random_amount():
    return randint(100, 500000) / 100

"""Creates a faux random transaction"""
def generate_random_transaction():
    return {
        'source_acc': create_random_account_id(),
        'target_acc': create_random_account_id(),
        'amount': create_random_amount(),
        'currency': 'USD',
    }
