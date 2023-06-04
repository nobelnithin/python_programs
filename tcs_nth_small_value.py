def find_small(x):
    small = x[0]
    for i in range(len(x)):
       if x[0]>x[i]:
          small=x[i]
    x.remove(small)
    return small
def main():
    list = [8, 6, 4, 12, 2, 0, 14, 16, 11]
    new_list = []
    n=0
    while n<len(list):
        find_small(list)
        new_list.append(find_small(list))
        print(new_list)
        print(list)
        n+=1


if __name__=='__main__':
    main()