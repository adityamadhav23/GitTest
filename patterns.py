n=int(input())
print(n)
# # for i in range(n):
# # 	for j in range(i):
# # 		print("*",end=" ")
# # 	print("\r")	

k=n
for i in range(n-1):
	for j in range(k):
		print("#",end="")
	print("\r")	
