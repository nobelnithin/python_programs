r,c=map(int,input().strip().split())

l=[input().strip().split() for i in range(r)]
k=int(input().strip())

m=[input().strip().split() for i in range(k)]

for i in range(k):
    for j in range(i,k):
        m[i][j],m[j][i]= m[j][i],m[i][j]

for i in range(r-k+1):
    for j in range(c-k+1):
        if l[i][j]==m[0][0]:
            x,y,ch=i,j,1
            for a in range(k):
                y=j
                for b in range(k): 
                    if not l[x][y]==m[a][b]:
                        ch=0
                        break
                    y+=1
                if ch==0:
                    break
                x+=1
            if x==i+k and y==j+k:
                for i in range(k):
                    for j in range(i,k):
                        m[i][j],m[j][i]=m[j][i],m[i][j]
                for s in m:
                    print(*s,sep=' ')
print(-1)