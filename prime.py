"""
prime.py -- Write the application code here
"""
#Python program to find prime factors

def generate_prime_factors(input_num):
    "Finds prime factors of a number - starts at 2"
    prime_list = []
    div = 2
    try:
        while input_num > 1:
            if(input_num % div == 0):
                prime_list.append(div)
                input_num = input_num / div
                div = div - 1
            div = div + 1
        return prime_list
    except:
        raise ValueError
