car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
}
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

malibus = []
for n in range(10):
  new_car = {
    'model':'malibu',
    'rang':None, # rangi noaniq
    'yil':2020,
    'narh':None, # narhi belgilanmagan
    'km':0,
    'korobka':'avto'
  }
  malibus.append(new_car)
for malibu in malibus[:3]:
  malibu['rang'] = 'qora'

for malibu in malibus[3:6]:
  malibu['rang'] = 'oq'
  
for malibu in malibus[6:]:
  malibu['rang'] = 'oq'
  malibu['korobka'] = 'mexanika'

for malibu in malibus:
  if malibu['korobka'] == 'avto':
    malibu['narh'] = 40000
  else:
    malibu['narh'] = 35000
print(malibus)

print(malibu['rang'])