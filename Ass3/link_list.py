class Node:
    def __init__(self,movieName,release_date):
        self.movieName = movieName
        self.release_date = release_date
        self.next_pt = None 
    
class NetflixMovieList:
    def __init__(self):
        self.head = None
    
    def addMovie(self,movieName,release_date):
        new = Node(movieName,release_date)
        if(self.head == None):
            self.head = new
        else:
            new.next_pt = self.head
            self.head = new
        print("Your movie is added to the list")
    
    def deleteMovie(self):
        if(self.head == None):
            print("Linked list is empty")
            return
        else:
            temp = self.head
            while(temp.next_pt.next_pt != None):
                temp = temp.next_pt
            temp.next_pt = None
        print("Old movie is deleted from the list")
    def traverse(self):
        if(self.head == None):
            print("Linked list is empty")
            return
        else:
            temp = self.head
            while(temp.next_pt != None):
                print(temp.movieName+" "+temp.release_date+" -> ",end= " ")
                temp = temp.next_pt
            print(temp.movieName+" "+temp.release_date,end= " ")
            print("")

list1 = NetflixMovieList()
while True:
    choice = int(input("1. Add Movie to the list \n 2. Traverse the Movie List \n 3. Deleting the Old Movie from the list \n 4. Exit \n Enter your Choice :- "))
    if choice ==  1:
        movieName = input(" Enter the Movie Name :- ")
        release_date = input(" Enter the release date :- ")
        list1.addMovie(movieName,release_date)
        print("")
    elif choice == 2:
        print(" Your current list :- ",end=" ")
        list1.traverse()
        print("")
    elif choice == 3:
        list1.deleteMovie()
        print("")
    elif choice == 4:
        break
    else:
        print("Please enter the valid choice ")
 