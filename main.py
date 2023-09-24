#var = 10

#array = ["Math", "Info", "Physics", "General Culture"]
#array.append("English")
#sorted(array)
#array.sort()
#print(array)

#int_array = [1, 2, 3, 4, 5]
#float_array = [1.2, -3, 3.14, 4.23, -5]
#bool_array = [True, False, True, False]

#array.append("English")
#array = sorted(array)
#array.sort()
#int_array.sort(reverse=True)
#print(int_array)
#print(sorted(int_array))

#array = []
#array_length = int(input("Enter array length"))

#for i in range(0, array_length) :
    #element = int(input("Enter Element\n"))
    #array.append(element)

#print(array)
#array.sort()
#print(array)
#array.sort(reverse=True)
#print(array)

#list = ["12", "56", "2456", "547", "245", "876"]
#print(list) #print list
#for i in range(0, len(list)):
    #print(list[i]) #print list dupa index
#for e in list:
    #print(e) #print list by element

#if 12 in list :
    #print(True)
#else:
    #print(False)

#tuple = ("A", "B", "C", "D")
#print(tuple + ("E", "Finish"))

#int_array = [1, 2, 3, 1, 5, 2, 4, 5, 6, 7]
#int_array = set(int_array)
#set_array = {1, 2, 5}
#print(set_array)
#print(int_array)

dex = {"Cod": "Python", "Extend": ".py", "Less": "3"}
print(dex.get("Cod")) #use key to display
dex.update({"Less": 3}) # update value where key is less
print(dex)

for i in dex:
    print(i) #display key
    print(dex.get(i)) #display value with key(i)