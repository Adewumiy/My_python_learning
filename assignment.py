print('WE SELL BIKE AT AFFORDABLE PRICE HERE WITH GOOD DISCOUNT')
print('BUY ANY BIKE OF YOUR CHOICE WITH GOOD VARYING DISCOUNT')
      
bike=100_000
price=int(input('amount :'))
if price>bike:
    price_tax=15/100*bike
    print(price_tax)
elif price>50_000 and price<bike:
    price_tax=10/100*bike
    print(price_tax)

elif  price<=100_000:
    price_tax=20/100*bike
    print(price_tax)
        
    
    
