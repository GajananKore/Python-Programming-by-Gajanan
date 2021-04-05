


def additionEven(brr):
	sum=0
	for i in range(len(brr)):
		if(brr[i]%2==0):
			sum=sum+brr[i]
	return sum

def main():
	arr=[]
	no=int(input("Enter no of elements"))
	
	for i in range(no):
		value=int(input("Enter no: "))
		arr.append(value)
		
	print("Entered array is:",arr)
	ret=additionEven(arr)
	print("Summetion of even elements is:",ret)
if __name__=="__main__":
	main()