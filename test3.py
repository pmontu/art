evensize = 6

i=0;
a = [i]
s = 1
j=evensize;

a+=[j]
s=0
i+=1

k=a[len(a)-2]

print k,a[len(a)-2],a[len(a)-1],a[len(a)-2]<a[len(a)-1]

while(i<=evensize/2):

    if a[len(a)-2]<a[len(a)-1]:
        k+=1
    else:
        k-=1

    print k,a[len(a)-2],a[len(a)-1],a[len(a)-2]<a[len(a)-1]

    if k == a[len(a)-1]:
        if s==1:
            a+=[j]
            s=0
            i+=1
        else:
            a+= [i]
            s=1
            j-=1
        if (i==j):
            break