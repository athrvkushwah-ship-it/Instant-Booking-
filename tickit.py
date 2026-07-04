#booking tickit according to the choice 
from payment import Payment
print('Welcome to the PVR')
print('Choose your movie :')
# i=0
while True:
   print  ('1. Welcome back')
   print ('2.jungle book ')
   print('3.mirzapur')
#    i +=i
   break

Choice = int(input('Enter your choice :'))
if Choice == 1:
   print('review 5.2')

elif Choice == 2:
   print('review 6.2')

elif Choice == 3:
   print('review 7.2')

else: 
   print('invalid choice')

print('Enter your seat Type :') 
while True:
   print('1 . Reclinear  sliping')
   print('2 . Reclinear ')
   print('3 . Semi slipper')
   print('4 . Normal Sub class')
   break

Seat_type= int(input(' Seat Type :'))
if Seat_type == 1:
     print('1000 per person')

elif Seat_type ==2:
     print('750 per person')

elif Seat_type ==3:
     print('500 per person')

elif Seat_type == 4:
     print(' 300 per person')

else :
     print('invalid choice')
  

print('Enter payment timings')  
while True:
   print('Now')
   print('AT the time of check in ')
   break
payment_time = int(input('Payment type :'))
if payment_time ==1 :Payment()
elif payment_time ==2 :print('by cash')
else :
      print('Invalid option')




