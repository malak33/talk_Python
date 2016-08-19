def print_header():
    print('----------------------------------')
    print('         Birthday App   ')
    print('----------------------------------')
    print()

def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = input('Year [YYYY]: ')
    month = input('Month [MM]: ')
    day = input('Day [DD]: ')


def compute_days_between_dates():
    pass

def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)
