#//create a function that takes in three arguments name, 
#age and city and print their values

def my_self(name,age,city):
    print(name,age,city)
my_self("Emmily",20,"Nairobi")

#create a function with default arguments while assinging value to the salary
def student_sch(name,age=25):
    print("Name:",name,"age:",age)

student_sch("Stephanie",35)
student_sch("Esther")

 #Write a python function that takes in variables and calculate addition
 #and subtraction hence return both operations

def operations(a,b):
   addition = a + b
   subtraction = a - b
   return addition,subtraction


ans = operations(250,100)
print(ans)

#create a function that takes in arecusive function to calculate the sum of
# numbers from 1-20
def calculation(numbers):
    sum = 0
    for i in range (0,numbers+1):
        sum += i
        print(sum)
calculation(20)


#Generate a python list of all odd numbers between 1 - 20


    
