def greet(name='Sasori'):
    return f"Hello Mr {name}"


print(greet())
print(greet("Tushar"))


def greet2(name="Tushar",age=25):
    return f"My name is {name} and my age is {age}"



print(greet2())
print(greet2("Noname",21))



# def scope():
#     name = "Tushar"
#     print(name)
    
# print(name)
# scope()

def scope():
    name = "Tushar"
    
    def scope2():
        name = "Uchiha"
        print(name)
        
    scope2()
    print(name)
    
    
scope()

def add(*num):
    #This *num is tuples
    print(sum(num))
    
    
add(1,2,3,4,5,6,7,8)


def arg(**detail):
    #This is dictionary
    print(detail)
    
    
    
arg(name="Tushar",age=25,Gender="M")


num = [1,2,3,4,5]
print(*num)

user = {
    'fname' : "Tushar",
    'age' : 25
}

arg(**user)


def fun1(**details):
    print(details)
    
    
    
    
    
fun1(name='tushar',age=15,country="India",location='delhhi')


def add(a,b,c):
    return a+b+c


l = [1,2,3]
print(add(*l))

data = {
    'name' : 'Tushar',
    'age' : 25,
    'city' : 'Delhi'
}

def register_user(name,age,city):
    print(name,age,city)
    
    
register_user(**data)



#If we writing a * it means when you are calling that function after the * you have to call the parameter explicity not by just providing the value itself and it applies to every values which comes after the *
def create_uesr(name,age,*,city,p):
    ...
    
    
create_uesr('Tushar',25,city='Delhi',p='Hari') # works
# create_uesr('Tushar',25,'Delhi') # not works



