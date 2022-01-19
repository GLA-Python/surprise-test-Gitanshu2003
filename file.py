def listing(num):
    lst=[]
    i = 0
    while i < len(num):
        count = 1
        while i+1 < len(num) and num[i]==num[i+1]:
            i += 1 
            count += 1 
        lst.append(str(count)+num[i])
        i += 1 
    return ''.join(lst)
z=1
n=int(input())
for i in range(n):
    print(z)
    z=listing(str(z))
