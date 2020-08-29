n = int(input("Enter the number: "))# input of the outer boundary of the numbers

num = list(range(2,n+1))# range of numbers in between which the program runs



start = 2 # start from 2 as mentioned

end = n +1 # and continues upto n

lst = list()

for i in range(start,end): 
    for j in range(2,i): 
        if(i % j==0):     
            break           #The idea is to find no. of prime numbers in the given range bcoz every composite number can be writen as a product of its prime factors """
    else:
        
        lst.append(i) #storing all of them in a list
       
        
lis1 = []

for i in num:
    for j in lst :              #finding all the numbers which when divided by prime numbers gives zero
        if i%j == 0:            #numbers having same prime factor are co-prime to each other
            lis1.append(i)
            
listt = []
for i in lis1:
    for j in lst:               # finally finding how many prime numbers are there in the lis1
        if i == j:
            listt.append(i)     # how many we have that many distinct colors we can assign
           

x = len(listt) # x gives no. of distinct colors

y = x**2 + x  # since sum of all no. is to be calculated, we can use , the formula of first n natural numbers " (n(n+1))/2 "

print(y//2) # so to get a int value


"""
    TIME COMPLEXITY:
                    3*(N^2)
                    = O(n^2)
    SPACE COMPLEXITY:
                    since a single int input and few int variables
                    == O(1), constanr"""
