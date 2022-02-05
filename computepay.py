#define the function
def computepay (hours, rate): 
    if (hours > 40): 
        return (rate * hours) * 1.5 
    else : 
        return rate * hours 


#take input from the user 
h = float(input("Enter hours: ")) 
r = float(input("Enter rate: "))

#print the result  
print(computepay(h, r)) 