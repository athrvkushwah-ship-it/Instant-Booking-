from pymongo  import MongoClient 

from payment import Payment
from pymongo import MongoClient

Client = MongoClient("mongodb://localhost:27017/")
db = Client['Booking_db']
box = db['office']
custom = db['Cart']
final = db['bill']

Movie= [
    {'movie name':'Goolmal 1','code' :1},
    {'movie name': 'Goolmal 2','code' :2},
    {'movie name': 'Goolmal 3','code' :3},
    {'movie name':'Goolmal 4','code' :4},
    {'movie name': 'Goolmal 5','code' :5},
]

# box.insert_many(Movie)
box.create_index("movie name",unique = True)
Price = [
    {1:'Reclinear  sliping', "Price" : 500},
    {2:' Semi slipper',"Price":400},
    {3:'Normal Sub class',"Price": 300},
]
# box.insert_many(Price)


for moive in box.find({}):
    print(moive,Price)

select = input('Select move type : ')
if not select:
    print('Pls fill the given field')
elif select  in  Movie:
    custom.insert_one({'Movie name' : select})
else:
    print('Movie not avilable')
    


type = input("select seat type")
if not type:
       print("Pls fill this field")

else:
  custom.insert_one({"seat_type" : type})

 
custom.find({})
quant = int(input('prople for tickit :'))
if quant<1:
    custom.insert_one({"people":quant})
else:
     print("pls provide valid number")

print("Pls pay")
Payment()

final.insert_one({
    {"name" : select,"seat_type" : type,'People' :quant,},           
})

for bi in final.find({}):
    print(bi)




