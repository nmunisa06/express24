import random

def sms_code_generate():
    rand_code = random.randint(100000, 999999)

    entered_code = int(input("Enter the verification code: "))

    if entered_code == rand_code:
        print('phone number is verified')
    else:
        print('code doesnt match')

sms_code_generate()