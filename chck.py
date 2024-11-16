data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]



def check(data):

    sum = 0 

    for dates in data:

        if isinstance(dates,int):

            sum+=dates

        elif isinstance(dates,str) and dates.isdigit():
            sum=+int(dates) 

        elif isinstance(dates,list):

           sum+=check(dates)
    return sum 



      



print(check(data))