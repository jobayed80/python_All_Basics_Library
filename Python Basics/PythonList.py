


# _____________ // Access List ///______________
print("\n")
print("....................... Access list ............................")
info = ["name: Jobayed", "age:25", "weight: 75kg", "height: 145", "Region: Camberwell"]
print(info)

print("1. ", info[1])  #Its working like as  Array because Array always start from [0] index , such as index[1] that means age data
print("2. ",info[-1]) # when I wrote index[-1] that means Array is working from the last part.
print("3. ",info[2:5]) # It's called Range. The array position will be counted [2] to [4] but I wrote [5] index, so [5] in Not included
print("4. ",info[:4])
print(info[-4:-1])


# Change List
print("\n")
print("....................... Change list ............................")
info = ["Orange", "Banana", "Apple", "cherry", "kiwi", "watermelon"]
print(info)
info[0] = "Mango" # info[0] that means we stored Mango because we have tro change the data , such as it was A Orange in 0 index
print(info)


# Change a rage of Item
print("\n")
print("....................... Change a rage of Item ............................")
info[1:3] = ["blackcurrant", "Orange"]
print(info)

#Append Items that means Items Add
print("\n")
print("....................... Append Items that means Items Add ............................")
info = ["cherry", "kiwi", "watermelon", "cherry"]
info.append("mango")
print(info)
info.insert(1,"lemons, Lime")
print(info)

info1= ["A", "B", "C", "D", "E"]
info2= ["a", "b", "c", "d", "e"]
info1.extend(info2)
print(info1)


# Python - Remove List Items
print("\n")
print("....................... Python - Remove List Items ............................")
vegitable = ["Tomato", "Lime", "Cucumber", "Cabbage", "Lettuce", "Spinach"]
vegitable.remove("Tomato") #It's mean that a specific Array index remove such as mention the items
print(vegitable)

vegitable.pop(1) #It's mean that a specific Array index remove except mention the items
print(vegitable)


