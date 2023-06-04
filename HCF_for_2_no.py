num1=int(input('Enter your number: '))

num2=int(input("Enter your number: "))
        

def main(num1,num2):
    if num1>num2:
        ans=num1%num2
        if ans==0:
            print(num2)
            pass
        else:
            main(num2,ans)
    else:
        ans=num2%num1
        if ans==0:
            print(num1)
            pass
        else:
            main(num1,ans)

main(num1,num2)
