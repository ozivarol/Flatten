def flatten(aList):
    newList = []
    for item in aList:
        if type(item) != type([]):
            newList.append(item)
            print(newList)
        else:
            newList.extend(flatten(item))
            print(newList)
    return newList
    

    
aList=([[1,'a',['cat'],2],[[[3]],'dog'],4,5]) 

flatten(aList)    
