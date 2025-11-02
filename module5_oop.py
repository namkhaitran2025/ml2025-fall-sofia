class List():
   def __init__(self):
     self.size = 0
     self.number_list = []

   def setSize(self):
     self.size = input("Input the size of the number list: ")

   def setList(self):
     for index in range(0, int(self.size)):
       value = input("Enter the value at index " + str(index) + ": ") 
       self.number_list.append(int(value))

   def searchValue(self):
      # print("The list is: ", self.number_list)
      print("____________________________________________")
      search_value = input("Enter the value to search: ")
      found = -1
      for index in range(0, int(self.size)):
         if self.number_list[index] == int(search_value):
            found = index
            break
      print("Index of the value is: " + str(found))

# main program
number_list = List()
number_list.setSize()
number_list.setList()
number_list.searchValue()