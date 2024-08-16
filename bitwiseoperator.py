

#truth table for 


x= 7 # 1 1 1
y = 4 #1 0 0

print(x&y)
print(x|y)

x=7
y=4
print(x^y)


x=7
print(~x)

x=85 
key=51

encryptedvalue = x^ key
print("Encrypted value:",encryptedvalue)

#decryption

decryptedvalue=encryptedvalue^key
print("Decrypted value:",decryptedvalue)


#not operator can be used to find the next divisivble by n number
x=19
#find the next number whic is dibisible by 7
print((x+6) & ~ 6)