evensize = 10
a = []
for k in range(1):
	i=0;
	j=evensize;
	while(i<=evensize/2):
		a += [i,j]
		i+=1
		j-=1
		if (i==j):
			j-=1
			while(i<=evensize):
				if j==-1:
					a += [i]
					break
				a += [i,j]
				i+=1
				j-=1
			break
print a
