#question 1

#variable inputs
n = int(input("How many different numbers are possible? : "))
r = int(input("How many numbers are used? : "))
a = str(input("Is the order important? y/n : "))
b = str(input("Can you repeat a number? y/n  : "))

#basevalues
ans = 0
num = 0
eq = ("")
fin = 0

#first condition
if a == ("y"):
    if b == ("y"):
        fin = n**r
        eq = "a**b"
        
#second condition
if a == ("y"):
    if b == ("n"):
        
        #tophalf of equation
        inserttop = 0
        factorial = 1

        for i in range(1,n + 1):
            factorial = factorial*i
        inserttop = factorial
        print(inserttop)
        
        #bottomhalf of equation
        insertbottom = 0
        num = (n-r)
        factorial = 1

        for i in range(1,num + 1):
            factorial = factorial*i
        insertbottom = factorial
        print(insertbottom)
            
        fin = inserttop / insertbottom
        eq = "a!/(a-b)!"

#third condition
if a == ("n"):
    if b == ("y"):
        
        #tophalf of equation
        inserttop = 0
        num = r+n-1
        factorial = 1

        for i in range(1,num + 1):
            factorial = factorial*i
        inserttop = factorial
        print(inserttop)
        
        #bottemleft
        bottomleft = 0
        factorial = 1

        for i in range(1,r + 1):
            factorial = factorial*i
        bottomleft = factorial
        print(bottomleft)
        
        #bottomright
        bottomright = 0
        num = n-1
        factorial = 1
        
        for i in range(1,num + 1):
            factorial = factorial*i
        bottomright = factorial
        print(bottomright)
        
        fin = inserttop/(bottomleft*bottomright)
        eq = "(b+a-1)!/b!(a-1)!"
        
#fourth condition
if a == ("n"):
    if b == ("n"):
        
        #tophalf
        tophalf = 0
        factorial = 1
        
        for i in range(1,n + 1):
            factorial = factorial*i
        tophalf = factorial
        print(tophalf)
        
        #bottomright
        right = 0
        factorial = 1
        num = n-r
        
        for i in range(1,num + 1):
            factorial = factorial*i
        right = factorial
        print(right)
        
        #bottomleft
        left = 0
        factorial = 1
        
        for i in range(1,r + 1):
            factorial = factorial*i
        left = factorial
        print(left)
        
        fin = tophalf/(right*left)
        eq = "a!/b!(a-b)!"
        
#endpoint
print(fin)
print(eq)
