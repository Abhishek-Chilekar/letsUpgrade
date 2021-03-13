''' Linear Search '''

list1 = [int(i)for i in input("Enter your list of numbers :- ").split()]

while True:
    number = int(input(" Enter the item to be searched :- "))
    flag = False
    pos = 0
    for i in list1:
        if number == i:
            flag = True
            break
        pos+=1 
    if flag:
        print(str(number)+" is found at position "+str(pos+1))
    else:
        print(str(number)+" is not present in the list ")
    
    choice = input(" do you want to continue ?(y/n) :  ").lower()
    if(choice == 'n'):
        break