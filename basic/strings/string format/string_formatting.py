age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))











quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."  # here number are used to get the location of a given string
print(myorder.format(quantity, itemno, price))