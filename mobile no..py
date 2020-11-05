import re
def num(number):
    regex = re.compile("(91)?[7-9][0-9]{9}")
    return regex.match(number)

number = input('Enter mobile number :')
while True:
    if(num(number)):
        print('Valid')
        break
    else:
        number = input('Enter number :')











