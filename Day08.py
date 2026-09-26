# try:
#     age = int(input("Enter your age  "))
# except:
#     print("Could you enter valid number")


# try:
#     number = int("hello")
# except ValueError as e:
#     print(e)


try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid Number")
else:
    #Below line work when try works
    print("This is the number : ", num)
    
finally:
    #Below line work everytime
    '''
    finally is all about cleanup
    ex:
    closing file
    closing database connections
    releasing resources
    cleanup operations
    '''
    
    print("I will work always")
    
    
    
    


users = {
    'tushar' : 'python123',
    'rahul' : 'django456'
}

username = input("Username: ")
password = input("Password: ")

try:
    correct_password = users[username]
    if password != correct_password:
        raise ValueError("Incorrect Password")
except KeyError:
    print("User doesn't exist ")
except ValueError as e:
    print(e)
    
else:
    print("Login successfully")
finally:
    print("Login system Completed")