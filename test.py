evenvibrations = 6

i=0
a = [i]
s = 1
j=evenvibrations;

a+=[j]
s=0
i+=1

k=a[len(a)-2]

print k,a[len(a)-2],a[len(a)-1],a[len(a)-2]<a[len(a)-1]

for z in range(100):

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
            if i==6:
                print "Top"

                i=0
                a = [i]
                s = 1
                j=evenvibrations;

                a+=[j]
                s=0
                i+=1

                k=a[len(a)-2]

                print k,a[len(a)-2],a[len(a)-1],a[len(a)-2]<a[len(a)-1]

        if (i==j):
            s = 1
            j=i-1
            a+=[j]
            k-=1
            print k,a[len(a)-2],a[len(a)-1],a[len(a)-2]<a[len(a)-1]
            print "Mid"
            s=0
            i+=1