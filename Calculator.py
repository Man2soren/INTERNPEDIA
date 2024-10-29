# a simple console based calculator
def subtract(list1) :
    if len(list1) == 1 :
        print(list1[0])
    else :
        ans = list1[0]
        for i in range(1,len(list1)):
            ans -= list1[i]
        print("Ans :-",ans)

def multiply(list1) :
    if len(list1) == 1 :
        print(list1[0])
    else :
        ans = list1[0]
        i = 1
        for i in range(1,len(list1)) :
            ans *= list1[i]
        print("Ans :-",ans)

def divide(list1) :
    if len(list1) == 1 :
        print(list1[0])
    else :
        try :
            ans = list1[0]
            for i in range(1,len(list1)) :
                ans /= list1[i]
            print('Ans :-',ans)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")

def calculator() :
    print("---------- Welcome to the Console Calculator ------------- ")
    print()
    
    #Taking the input from the user 
    user_input = input("Enter numbers you want to perform operation(using space) :")
    list1 = list(map(int,user_input.split()))
    print()

    #Asking user for operation choice
    print("Select Operation :")
    print("1.Add(+)")
    print("2.Subtract(-)")
    print("3.Multiply(*)")
    print("4.Divide(/)")
    print()

    choice1 = int(input("Enter choice(1/2/3/4) :"))

    if choice1 == 1 :
        print(sum(list1))
    elif choice1 == 2 :
        subtract(list1)
    elif choice1 == 3 :
        multiply(list1)
    elif choice1 == 4 :
        divide(list1)
    else :
        print('Invalid input')

    choice2 = input(str("Do you want to continue(y/n) :"))
    print()
    if choice2 == 'y':
        calculator()
    else :
        print("Thank you !!!")
    print()
    
calculator()