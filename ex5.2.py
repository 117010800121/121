def isOdd(num):
    if num%2 ==1:
        return True
    else:
        return False
while True:
    s = input("Plese enter an Integer:")   
    if not s.isdigit():
        print("Please enter again!")
        continue
    n = eval(s)
