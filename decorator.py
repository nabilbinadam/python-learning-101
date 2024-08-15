#decerator/annotator 

import datetime

def captureStartEndTime(func):

    def addCodeToCaptureStartEndTime(*arguments):
        now = datetime.datetime.now()
        print("Start Time:", now.time())
        result = func(*arguments)
        now = datetime.datetime.now()
        print("End Time", now.time())
        return result
    
    return addCodeToCaptureStartEndTime

@captureStartEndTime
def sayHello():
    print("Hello")

@captureStartEndTime
def simpleInterest(principle, period, rate):
    return (principle * period * rate) / 100

# sayHello()
# captureStartEndTime(sayHello)()
sayHello()
print(simpleInterest(1000, 1, 6))