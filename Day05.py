#Comprehensions

numbers = [1,2,3,4,5,5]
sqaures = [number ** 2 for number in numbers]
n = [number for number in numbers if number % 2 == 0]
print(sqaures)
print(n)

res = [number ** 2 for number in numbers if number % 2 == 0]
print(res)

print(True if 1 == 1 else False)
# below examples used when else is also added in structure Without else above code will be used or syntax will be used

ans = ["ODD" if number % 2 == 0 else "EVEN" for number in numbers]
print(ans)

word = "python123"

ans = [char for char in word if char.isdigit()]
print(ans)