#writing the payment logic
def Payment():
    print('Enter your payment option ')
    print('1. Credit Card')
    print('2 .Debit Card')
    print('3 .UPI')
    payment_type = int(input('Enter payment option :'))
    if payment_type == 1:
      print('10% discount')
    elif payment_type == 2:
      print('5% discount')
    elif payment_type == 3:
     print('No discount')
    else:
     print('invalid option')