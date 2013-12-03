evenvibrations = 6

for k in range(2):

    i=0;
    a = [i]
    s = 1
    j=evenvibrations;

    a+=[j]
    s=0
    i+=1

    print a[len(a)-2],a[len(a)-1]

    while(i<evenvibrations):
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
            print "Mid"
            s = 1
            j=i-1
            a+=[j]
            s=0
            i+=1
            print a[len(a)-2],a[len(a)-1]

    a+= [i]
    print a[len(a)-2],a[len(a)-1]
    s=1
    j-=1
    print "Top"