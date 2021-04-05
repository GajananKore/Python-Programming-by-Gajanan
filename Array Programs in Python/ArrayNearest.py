def nearestNo(brr,no):
	diff=0
		
	Nearest=0
	minDiff=brr[0]-no
	secNearest=0	
	
	if (minDiff<0):
		minDiff=-minDiff
		
			
	for i in range(len(brr)):
		
		diff=brr[i]-no
		
		
		if (diff<0):
			diff=-diff
		if(diff==0):
			Nearest=brr[i]
			break
		else:
			if(diff<=minDiff):
				minDiff=diff				
				Nearest=brr[i]
				print(i)
			if(diff>=secNearest and Nearest!=secNearest):
				secNearest=diff
				
	print("Nearest no is..",Nearest)
	print("secNearest is .",secNearest)
	
def main():
	arr=list()
	no=int(input("Enter no of elemeents...."))
	
	for i in range(no):
		value=int(input())
		arr.append(value)
	print("Entered array is...",arr)
	
	value=int(input("ENter no you want to search....."))
	nearestNo(arr,value)
	

if __name__=="__main__":
	main()
	
