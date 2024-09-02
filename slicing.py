
#slicing is???
"""object = "nabil"
print(type(object))  # string
reversed=object[::-1]
print(type(reversed))
print(reversed)
"""

#trying out slicing

name= "karim"
guitar=["ibanez","gibson","fender","soloking","schecter","musicman"]

print(guitar[0:0])
print(guitar[0:1])
print(guitar[0:2])
print(guitar[0:3])
print(guitar[0:4])
print("hello")
print(guitar[1:0]) # 0
print(guitar[1:1]) # gibson
print(guitar[1:2]) # gibson ,fender
print(guitar[1:3]) # gibson,fender,soloking
print(guitar[1:4]) #gibson,fender,soloking
print(guitar[1:5])
print("----------------------------------------------")
bands = ["efek rumah kaca","fourtwnty","Nadin","feby putri","radiohead"]

print(bands[1:-0])
print(bands[:-1])
print(bands[:-2])
print("------------------")

print(bands[1:-1])
print(bands[1:-2])
print(bands[1:-3])
print(bands[1:-4])

print("______________________________________----------------")
print(bands[::1])
print(bands[::-1])
print(bands[::2])
print(bands[::-2])
print("******************try***************************")
for band in bands[::-1]:
    #band is empty
    # range of bands. len will return int
     newband = list(band) 
     print(newband)
    



    
    