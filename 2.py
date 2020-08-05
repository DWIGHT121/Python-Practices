# to find maximum pairwose product

liste = []
length = int(input("Enter the number of elements for the list"))
for i in range(0, length):
    element = int(input("Enter the element number {}".format(i+1)))
    liste.append(element)

total_len = len(liste)
half = total_len//2
product1 = 0
for j in range(0, total_len):
    for k in range(j+1, total_len):
        product2 = liste[j]*liste[k]
        if product2 > product1:
            elements = "{}, {}".format(liste[j], liste[k])
            product1 = product2

print(elements)
