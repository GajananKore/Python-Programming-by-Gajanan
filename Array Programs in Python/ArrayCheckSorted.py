#Program statemet:
#		Accept 'N' no from user and check whether array is sorted in increasing order or not

def checkSorted(brr):
	
	for i in range(len(brr)-1):
		if brr[i]>=brr[i+1]:
			break;			
			
	print('value of i is: ',i)
	if i==len(brr)-2:
		return True;
	else:
		return False;
	

def main():
	arr=list();
	iLength=int(input('Enter no of elements: '));
	
	print('Enter elements...');
	for i in range(iLength):
		iValue=int(input());
		arr.append(iValue);
	
	print(arr);
	
	iRet=checkSorted(arr);
	if iRet==True:
		print('Array is Sorted');
	else:
		print('Array is not Sorted');
	
	
if __name__=="__main__":
	main();
