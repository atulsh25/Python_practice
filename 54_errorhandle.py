def division(num1,num2):
    try:
        print(num1/num2)
    except:
        print("Error encountered")

num1=input("Enter Divisible ")
num2=input("Enter Divisor ")

division(int(num1),int(num2))