import math
print('Welcome to the Pizza Calculator (Weekend Only)')


Total_Charge = 0

def friday():
    global Total_Charge 
    global total1
    global tax1
    global delivery1
    global total1
    global pizzas_needed1
    global output1
    people1 = int(input("How many people on friday? "))
    print("                 ")
    slices1 = float(input("How many slices each person need on friday? "))
    print("                 ")
    price1 = float(input("How much is the pizza on friday?  "))
    print("                 ")
    slices1 = int(slices1.__ceil__())
    pizzas_needed1 = (slices1*people1) / 8
    pizzas_needed1 = pizzas_needed1.__ceil__()

    output1 = pizzas_needed1 * price1
    tax1 = 0.07 * output1
    delivery1 = (tax1 + output1) * 0.2

    total1 = delivery1 + tax1 + output1

    Total_Charge = total1


def saturday():
    global Total_Charge
    global total2
    global tax2
    global delivery2
    global total2
    global pizzas_needed2
    global output2
    people2 = int(input("How many people on saturday? "))
    print("                 ")
    slices2 = float(input("How many slices each person need on saturday? "))
    print("                 ")
    price2 = float(input("How much is the pizza on saturday?  "))
    print("                 ")

    slices2 = int(slices2.__ceil__())
    pizzas_needed2 = (slices2*people2) / 8
    pizzas_needed2 = pizzas_needed2.__ceil__()

    output2 = pizzas_needed2 * price2
    tax2 = 0.07 * output2
    delivery2 = (tax2 + output2) * 0.2

    total2 = delivery2 + tax2 + output2

    Total_Charge = total2


def sunday():
    global Total_Charge
    global total3
    global tax3
    global delivery3
    global total3
    global pizzas_needed3
    global output3
    people3 = int(input("How many people on sunday? "))
    print("                 ")
    slices3 = float(input("How many slices each person need on sunday? "))
    print("                 ")
    price3 = float(input("How much is the pizza on sunday?  "))
    print("                 ")
    slices3 = int(slices3.__ceil__())
    pizzas_needed3 = (slices3*people3) / 8
    pizzas_needed3 = pizzas_needed3.__ceil__()

    output3 = pizzas_needed3 * price3
    tax3 = 0.07 * output3
    delivery3 = (tax3 + output3) * 0.2

    total3 = delivery3 + tax3 + output3

    Total_Charge = total3


def listingsun():
    print("                 ")
    print("Friday's Total")
    print(f'{pizzas_needed1} Pizzas: ${output1:.2f}')
    print(f'Tax: ${tax1:.2f}')
    print(f'Delivery: ${delivery1:.2f}')
    print(f'Total: ${total1:.2f}')
    print("                 ")
    print("Saturday's Total")
    print(f'{pizzas_needed2} Pizzas: ${output2:.2f}')
    print(f'Tax: ${tax2:.2f}')
    print(f'Delivery: ${delivery2:.2f}')
    print(f'Total: ${total2:.2f}')
    print("                 ")
    print("Sunday's Total")
    print(f'{pizzas_needed3} Pizzas: ${output3:.2f}')
    print(f'Tax: ${tax3:.2f}')
    print(f'Delivery: ${delivery3:.2f}')
    print(f'Total: ${total3:.2f}')

def listingsat():
    print("                 ")
    print("Friday's Total")
    print(f'{pizzas_needed1} Pizzas: ${output1:.2f}')
    print(f'Tax: ${tax1:.2f}')
    print(f'Delivery: ${delivery1:.2f}')
    print(f'Total: ${total1:.2f}')
    print("                 ")
    print("Saturday's Total")
    print(f'{pizzas_needed2} Pizzas: ${output2:.2f}')
    print(f'Tax: ${tax2:.2f}')
    print(f'Delivery: ${delivery2:.2f}')
    print(f'Total: ${total2:.2f}')
    print("                 ")

def listingfri():
    print("                 ")
    print("Friday's Total")
    print(f'{pizzas_needed1} Pizzas: ${output1:.2f}')
    print(f'Tax: ${tax1:.2f}')
    print(f'Delivery: ${delivery1:.2f}')
    print(f'Total: ${total1:.2f}')


days = int(input('How many days you need pizza? (1-3)? '))
print("                 ")


if days == 3:
    friday()
    saturday()
    sunday()
    final = total1 + total2 + total3
    listingsun()
    print("                 ")
    print(f'Weekend TotalL: ${final:.2f} now pay up..')

if days == 2:
    friday()
    saturday()
    final = total1 + total2
    listingsat()
    print("                 ")
    print(f'Weekend TotalL: ${final:.2f} now pay up..')

if days == 1:
    friday()
    final = total1
    listingfri()
    print("                 ")
    print(f'Weekend Total: ${final:.2f} now pay up..')
    print("                 ")










