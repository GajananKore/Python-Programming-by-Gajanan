def main():
	arr=[]
	no=int(input("Enter no of elements"))
	
	for i in range(no):
		value=int(input("Enter no: "))
		arr.append(value)
		
	print("Entered array is:",arr)
	
	sum=0
	for i in range(len(arr)):
		sum=sum+arr[i]
	
	print("Summetion of all entered elements in the array is:",sum)
if __name__=="__main__":
	main()