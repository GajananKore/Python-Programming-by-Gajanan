#Program statemet:
#		Accept 'N' no from user and findout largest subarray which is sorted increasing

def maxArray(brr):
	iMax=0
	iMin=0
	iStart=0
	iEnd=0;
	for i in range(len(brr)-1):
		if brr[i]<=brr[i+1]:
			iEnd=i+1;
			
		else:
			if(iMax-iMin)<(iEnd-iStart):
				iMin=iStart;
				iMax=iEnd;
			iStart=iEnd=i+1;
			
	if(iMax-iMin)<(iEnd-iStart):
		iMin=iStart;
		iMax=iEnd;
	print('Largest Sub array start at: ',iMin,iMax)				
			
	
	

def main():
	arr=list();
	iLength=int(input('Enter no of elements: '));
	
	print('Enter elements...');
	for i in range(iLength):
		iValue=int(input());
		arr.append(iValue);
	
	print(arr);
	
	iRet=maxArray(arr);
	
	
	
if __name__=="__main__":
	main();
