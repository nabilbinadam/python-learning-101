product = "Ibanez GIO"
quantity = 1000
price = 20000
isAvailabe = True 


statement = "Aku ada %s padu boh  %d tapi harga %f" % (product,quantity,price)

print(statement)

result= f"{product:>10s}{quantity:>10d}{price:^10.2f}"

print(result)