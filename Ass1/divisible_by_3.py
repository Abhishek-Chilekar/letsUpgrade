list1 = [int(i) for i in input("Enter the numbers in the list ").split(" ")]
result = []
for i in list1:
    if(i % 3 == 0):
        result.append(i)
print("Numbers divisible by 3 are :- ",result)