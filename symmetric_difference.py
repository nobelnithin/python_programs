def fun(x,y):
    soln=[]
    for i in range(len(x)):
        if x[i] in y:
            pass
        else:
            soln.append(x[i])
    for i in range(len(y)):
        if y[i] in x:
            pass
        else:
            soln.append(y[i])
    return soln


def main():
    sym_diff=fun([1,2,3], [2,3,4])
    print("Symmetric difference=",sym_diff)
if __name__=="__main__":
    main()