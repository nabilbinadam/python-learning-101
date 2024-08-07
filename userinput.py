def keyboardInput(caption, datatype,errormessage):
    isErrorInput = True
    while (isErrorInput) :
        
    try:
         value =input(caption)
         value = datatype(value)
    except:
        print(errormessage)
        
    else:
        isErrorInput = False    
    return value    
        
princple = keyboardInput("Principle amount",int)

    
    