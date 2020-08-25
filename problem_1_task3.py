
n = input("Enter the number: ")
#Taking input in the form of string

  
   
sumTemp = 0
count = 0
  
   
while (len(n) > 1): #only we need to find sum of digits only when it is a non-single digit number
      
    sumTemp = 0
  

    for i in range(len(n)): 
        sumTemp +=  (ord(n[ i ]) - ord('0'))  #If the character is a digit, ord(ch) - ord("0") returns the numeric value of the digit - "0" becomes 0, "1" becomes 1
                                                    # simply to convert the digit in the form of character to int form in each iteration
  
                              
        # converting temporary_sum into  
        # string str again . 
    n = str(sumTemp)# for loop to continue AND FOR  len method to work 
  
        # increase the count  for each loop and that gives finally the least no. of times we need to add
    count += 1

print(count)


""" TIME COMPLEXITY:
                    2 loops 1 loop inside another loop , so O(n^2)

    SPACE COMPLEXITY:
                    SINCE  onnly one int input and few constant space taking integers

                    overall space complexity is O(1) """
                    
