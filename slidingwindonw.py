

data=[1,4,5,6,7,10]
target= 10


def slidingwindow(data,target):

    left=0
    right = len(data)-1
    ranging= range(left,right)

    while right<left:
        sum= data[left]=data[right]

        if target in ranging:
            return 
        elif target not in ranging:
            left+=1
        else:
            righ-=1    
