#Linear Search Function
def Linear_Search(list):
	n = int(input('Enter the element you want to find:'))
	for i in range(len(list)):
		if n == list[i]:
			print('Found element at index',i)
			break

	else:
		print('Not Found the element')

#to make a List
def Make_List():
	z=int(input("How many elements do you want in list??"))
	x = []
	for i in range(z):
		x.append(int(input('Enter the element: ')))
	print(x)
	return x

#Store the list in a new variable
list1 = Make_List()

#Call the Linear Search Function
Linear_Search(list1)


#We can also pass the Make_List() Function directly inside the Linear_Search() Function
#Linear_Search(Make_List())
