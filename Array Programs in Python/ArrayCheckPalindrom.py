#Program statemet:
#		Accept 'N' no from user and check whether that array is palindrom or not


def checkPalindrom(brr):
	for i in range(int(len(brr)/2+1)):
		if(brr[i]!=brr[len(brr)-1-i]):
			return False
	
	return True
	
	#iCnt=0
	#while(iCnt<=int(len(brr)/2+1)):
	#	if(brr[iCnt]!=brr[len(brr)-1-iCnt]):
		#	return False
		#iCnt=iCnt+1
	#return True
	
def main():
	arr=list();
	iLength=int(input('Enter no of elements: '));
	
	print('Enter elements...');
	for i in range(iLength):
		arr.append(int(input()));
	
	print(arr);
	
	iRet=checkPalindrom(arr);
	if iRet==True:
		print('Array is palindrom')
	else:
		print('Array is not palindrom')
	
	
	
if __name__=="__main__":
	main();
