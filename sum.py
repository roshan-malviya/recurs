def sumof(n):
	if n==1:
		return 1
	return (sumof(n-1)+n)

b=int(input())
print(sumof(b))