size = input("Input the size of the number list: ")
number_list = []

for index in range(0, int(size)):
  value = input("Enter the value at index " + str(index) + ": ") 
  number_list.append(int(value))

# print("The list is: ", number_list)
print("____________________________________________")

search_value = input("Enter the value to search: ")
found = -1
for index in range(0, int(size)):
   if number_list[index] == int(search_value):
     found = index
     break

print("Index of the value is: " + str(found))