evensize = 6

i=0;
a = [i]
s = 1
j=evensize;

a+=[j]
s=0
i+=1

print a[len(a)-2],a[len(a)-1]

while(i<=evensize/2):
    if s==1:
        a+=[j]
        print a[len(a)-2],a[len(a)-1]
        s=0
        i+=1
    else:
        a+= [i]
        print a[len(a)-2],a[len(a)-1]
        s=1
        j-=1
    if (i==j):
        break