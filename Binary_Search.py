def Binary_Search(list1):
	n = int(input("Enter the search Element: "))
	low = 0
	high = len(list1)-1
	Flag = False

	while low<=high and not Flag:
		mid  = (low+high)//2
		if n==list1[mid]:
			Flag = True
		elif n>list1[mid]:
			low = mid+1
		else:
			high = mid-1
	if Flag==True:
		print("Element Found: ")
	else:
		print("Element Not Found")

num = int(input("How many Element?: "))
list1 = sorted([int(input('Enter: ')) for i in range(num)])

print(list1)
Binary_Search(list1)