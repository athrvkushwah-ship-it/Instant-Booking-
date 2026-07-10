# #booking tickit according to the choice 
from payment import Payment
from finalinfo import info
#select the seat 
def paytime():
  print('Enter payment timings')  
  while True:
   print(' 1. Now')
   print('2 .AT the time of check in ')
   payment_time = int(input('Payment type :'))
   if payment_time ==1 :
    seat_count = info()
    print(seat_count)
    # viewers_info()
    break
   elif payment_time ==2 :
    print('by cash')
   else :
      print('Invalid option')

def seat(): 
      print('Enter your seat Type :') 
      while True:
       print('1 . Reclinear  sliping')
       print('2 . Reclinear ')
       print('3 . Semi slipper')
       print('4 . Normal Sub class')
       Seat_type= int(input(' Seat Type :'))
       if Seat_type == 1:
        print('1000 per person')
        paytime()
        break

       elif Seat_type ==2:
        print('750 per person')
        paytime()
        break
 
       elif Seat_type ==3:
        print('500 per person')
        paytime()
        break

       elif Seat_type == 4:
        print(' 300 per person')
        paytime()
        break

       else :
        print('invalid choice')

print('Welcome to the PVR')
print('Choose your movie :')
while True:
   print  ('1. Welcome back')
   print ('2.jungle book ')
   print('3.mirzapur') 
   
   Choice = int(input('Enter your choice :'))
   if Choice == 1:
    seat()
    break
   
   elif Choice == 2:
    seat()
    break

   elif Choice == 3:
     seat()
     break

   else: 
     print('invalid choice')

# def seat():
#  print('Enter your seat Type :') 
#  while True:
#    print('1 . Reclinear  sliping')
#    print('2 . Reclinear ')
#    print('3 . Semi slipper')
#    print('4 . Normal Sub class')
#    break
#  Seat_type= int(input(' Seat Type :'))
#  if Seat_type == 1:
#      print('1000 per person')

#  elif Seat_type ==2:
#      print('750 per person')
 
#  elif Seat_type ==3:
#      print('500 per person')

#  elif Seat_type == 4:
#      print(' 300 per person')

#  else :
#      print('invalid choice')
     







