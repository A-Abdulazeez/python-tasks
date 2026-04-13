numberone = input("input your first number: ")
numberone = int(numberone)
numbertwo = input("input your second number: ")
numbertwo = int(numbertwo)
numberthree = input("input your third number: ")
numberthree = int(numberthree)

print("The sum is; ", numberone+numbertwo+numberthree)
print("The average is: ", (numberone+numbertwo+numberthree)/3)
print("The product is: ", numberone*numbertwo*numberthree)

if numberone > numbertwo:
    print("the largest number is: ", numberone)
elif numbertwo > numberthree:
    print("the largest number is: ", numbertwo)
elif numberthree > numbertwo:
    print("the largest number is: ", numberthree)

if numberone < numbertwo:
    print("the smallest number is: ", numberone)
elif numbertwo < numberthree:
    print("the smallest number is: ", numbertwo)
elif numberthree < numbertwo:
    print("the smallest number is: ", numberthree)
