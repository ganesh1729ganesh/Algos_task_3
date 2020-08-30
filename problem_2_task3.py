        
n = int(input("Enter the no. of units of length of the wall either 1 or 2: "))

m = int(input("Enter the number of bricks: "))

arr = list(map(int, input("Enter the strengths of  "+ str(m)+ " brick lines: ").split()))


if  n == 1:# if n is 1 s0 the sum is the sum of all the strengths of tthe bricks
    suum = 0
    for i in arr:
        suum += i # adding the strength in every loop

    print(suum)


if n == 2:
    def possibleLists(lst): 
  
    # If lst is empty then there are no possible lists
        if len(lst) == 0: 
            return [] 
  
    # If there is only one element in lst then, only 
    # one possible list exists
        if len(lst) == 1: 
            return [lst] 
  
    # Finding the possible lists for lst if there are 
    # more than 1 characters 
  
        l = [] # empty list that will store current possible list 
  
    # Iterate the input(lst) and calculate the possible lists 
        for i in range(len(lst)): 
           m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
           remLst = lst[:i] + lst[i+1:] 
  
       # Generating all possible lists  where m is first 
       # element 
           for p in possibleLists(remLst): # again using same function such that it might end up with len(lst) == 1 case, sort of recursion
               l.append([m] + p) 
        return l 
  
    data = arr
    last = []
    final = []
    for p in possibleLists(data):#  Iterating over all the possible lists 
       
        temp = 0
        tempsum = []
        for i in range(len(p)): # the logic is to sum value of strengths upto a point and compare it with sum of all remaining strengths after the point
            last.append(sum(p[0:i+1]))# storing all the sums upto a point p in a list 
        
        for i in p:
            temp += i #actual sum of all the strengths of brickss

        for j in range(len(last)): 
            tempsum.append(temp - last[j]) #deleting the sum of the strengths upto the point 
                                            #from the total sum to get remaining sum of strengths of bricks after that point 

    test_list1 = tempsum
    test_list2 = last

    res = [[i , j] for i, j in zip(test_list1, test_list2)]# concatenating element wise to compare , zip functions literally zips the lists
    mini = []
    for i in res:
        mini.append(min(i))# finally storing all the minimums in a list,  that is weakest brick in comparing every two
        y = max(mini) # finding the maximum possible minimum, that is mximum strength attainable

    print(y)
        



""" TIME COMPLEXITY:
                    = n^2+ n(3n) + n = 4n^2 + n

                    = O(n^2)

    SPACE COMPLEXITY:
                    it depends on two integers inputs + array of strengths

                    = O(n) """











        
