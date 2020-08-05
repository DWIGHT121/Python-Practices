# Write a Python program to sum all the items in a list

list = []
sum = 0
a = int(input("Enter number of elements in the list"))
for i in range(0, a):
    list1 = int(input("Enter the element {}".format(i)))
    sum += list1
    list.append(list1)


print(sum)
