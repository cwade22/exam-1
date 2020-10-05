#ask user for weight

weight_input = input('Please enter the package weight: ')
weight = float(weight_input)
rate_1= 3.00
rate_2 = 4.00
rate_3 = 5.00
rate_4 = 6.00
shipping_price = 0
#calc shipping price

if weight <= 3:
   shipping_price= weight*rate_1
elif weight > 3 and weight <6 :    
        shipping_price= ((weight-3 )*rate_2)+(3*rate_1)
elif weight >=6 and weight <10 :
        shipping_price= ((weight-6 )*rate_3)+(3*rate_1)+(3*rate_2)
elif weight >=10 :
        shipping_price= ((weight-10 )*rate_4)+(3*rate_1)+(3*rate_2)+(4*rate_3)
print(f'The shipping price for a',weight,'lb package is $', shipping_price,'.')
        

