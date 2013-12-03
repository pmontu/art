evensize = 6
for k in range(1):
	i=0;
	j=evensize;
	a = [i]
	s = 1
	while(i<=evensize/2):
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
print a
