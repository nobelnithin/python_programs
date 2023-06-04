num1=1266
num2=1461
num3=1863

def compute(x,y):
    if x>y:
        ans=x%y
        if ans==0:
            return (y)
        else:
            compute(y,ans)
    else:
        ans=y%x
        if ans==0:
            return(x)
        else:
            compute(x,ans)

def main():
    print(compute(num1,num2))
    #hcf_3=compute(hcf_2,num3)
    #print(hcf_2)


main()
    
    
