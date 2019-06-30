###First project: Basic calculator project

words = ['cat', 'window', 'defenestrate']

vec = [[1,2,3], [4,5,6], [7,8,9]]

matrix = [[11, 32, 13, 24], [15, 6, 67, 78], [49, 3410, 2311, 1212],]

# Transpose output  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

 

#[[0][0], [1][0], [2][0]], [[0][1], [1][1], [2][1]]

'''

k=[]

 

new_matrix=[]

new_row=[]

 

for row in matrix:

    for item in row:

        new_row.append(item)

    #print(r'here it is', new_row)

    new_matrix.append(new_row)

    new_row=[]

print(new_matrix)

# Python code to demonstrate the working of

# zip()

 

# initializing lists

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]

roll_no = [ 4, 1, 3, 2 ]

marks = [ 40, 50, 60, 70 ]

 

# using zip() to map values

mapped = list(zip(name, roll_no, marks))

 

# converting values to print as set

#mapped = set(mapped)

 

# printing resultant values

#print ("The zipped result is : ",end="")

print (mapped)

  ''' 

 

 

def add(x,y):

    return x+y

 

def sub(x,y):

    return x-y 

 

def mul(x,y):

    return x*y

   

def div(x,y):

    return x/y

 

s='y'

while(s=='y'):

    t = int(input(''' Choose any operation as listed below

            to add press 1

            to sub press 2

            to mul press 3

            to div press 4: ''' ))

    if t<=0 or t>4:

        print("incorrect value so breaking out")

        break

       

    print("Enter the 2 values")

   

    n = int(input("1st no: "))

    m = int(input("2nd no: "))

   

    #print(type(n),type(m))

    if t ==1:

        value =add(n,m)

    elif t ==2:

        value =sub(n,m)

    elif t == 3:

        value =mul(n,m)

    elif t == 4:

        value =div(n,m)

 

    print("The answer is", value)

    s = input("DO you want to continue?: ")
 
