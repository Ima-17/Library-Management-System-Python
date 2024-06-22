# define the available subjects for each resource type
BOOK_SUBJECTS = ["Science", "History", "Literature"]
MAGAZINE_SUBJECTS = ["Science", "Technology", "Sports"]
DVD_SUBJECTS = ["Astronomy", "Math", "Technology"]
CD_SUBJECTS = ["Music", "Math", "Foreign Languages"]
RESOURCE_TYPES = ["Book", "Magazine", "Dvd", "Cd"]

print("\n-------------Library system--------------\n")


# define the Resource class
class Resource:
    def __init__(self, number, title, subject, rental_price, num_copies):
        self.number = number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        self.is_available = True

    def display(self):
        print(f"{self.number} - {self.title} ({self.subject} - LKR.{self.rental_price} per day - {self.num_copies}")

    def lend(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def recieve(self):
        self.is_available = True


# define the book class
class Book(Resource):
    def __init__(self, number, title, format, subject, rental_price, num_copies):
        super().__init__(number, title, subject, rental_price, num_copies)
        self.format = format

    def display(self):
        print(f"{self.number}, {self.title}, {self.format}, {self.subject}, LKR.{self.rental_price} per day, "
              f" {self.num_copies} copies")


# define the magazine class
class Magazine(Resource):
    def __init__(self, number, title, color, subject, rental_price, num_copies):
        super().__init__(number, title, subject, rental_price, num_copies)
        self.color = color

    def display(self):
        print(f"{self.number}, {self.title}, {self.color}, {self.subject}, LKR.{self.rental_price} per day,  "
              f"{self.num_copies} copies")


# define the educational dvd class
class Dvd(Resource):
    def __init__(self, number, title, subject, rental_price, num_copies):
        super().__init__(number, title, subject, rental_price, num_copies)

    def display(self):
        print(f"{self.number}, {self.title}, {self.subject}, LKR.{self.rental_price} per day,  "
              f"{self.num_copies} copies")


# define the lecture cd class
class Cd(Resource):
    def __init__(self, number, title, subject, rental_price, num_copies):
        super().__init__(number, title, subject, rental_price, num_copies)

    def display(self):
        print(f"{self.number}, {self.title} ({self.subject}, LKR.{self.rental_price} per day, "
              f"{self.num_copies} copies")


# create an empty list to store all resource
resources = []


# function to add a new resource to the system
def add_resource():
    resource_type = input("Enter resource type (Book, Magazine, Dvd, Cd) : ")
    if resource_type == "Book":
        number = input("Enter book ISBN number: ")
        title = input("Enter book title: ")
        format = input("Enter book format type (Hardcover or Paperback): ")
        subject = input("Enter subject: ")
        rental_price = float(input("Enter rental price per day: "))
        num_copies = int(input("Enter number of copies: "))
        resource = Book(number, title, format, subject, rental_price, num_copies)
    elif resource_type == "Magazine":
        number = input("Enter magazine number: ")
        title = input("Enter magazine title: ")
        color = input("Enter color or black&white print: ")
        subject = input("Enter subject: ")
        rental_price = float(input("Enter rental price per day: "))
        num_copies = int(input("Enter number of copies: "))
        resource = Magazine(number, title, color, subject, rental_price, num_copies)
    elif resource_type == "Dvd":
        number = input("Enter dvd number: ")
        title = input("Enter dvd title: ")
        subject = input("Enter subject: ")
        rental_price = float(input("Enter rental price per day: "))
        num_copies = int(input("Enter number of copies: "))
        resource = Dvd(number, title, subject, rental_price, num_copies)
    elif resource_type == "cd":
        number = input("Enter cd number: ")
        title = input("Enter cd title: ")
        subject = input("Enter subject: ")
        rental_price = float(input("Enter rental price per day: "))
        num_copies = int(input("Enter number of copies: "))
        resource = Cd(number, title, subject, rental_price, num_copies)
    else:
        print("\nInvalid resource type")
        return
    resources.append(resource)
    print(f"\n{resource_type} '{resource.title}' has been added to the system.")


# function to remove a resource from the system
def remove_resource():
    resource_type = input("Enter resource type (Book, Magazine, Dvd, Cd) :")
    resource_number = input("Enter the number of the resource to be removed: ")
    for resource in resources:
        if type(resource).__name__ == resource_type and resource_number == resource.number:
            if resource.is_available:
                resources.remove(resource)
                print(f"\n{resource_type} {resource_number} has been removed from the file.")
            else:
                print(f"\n{resource_type} {resource_number} cannot be removed as it is currently on loan.")
                break
        else:
            print(f"\n{resource_type} {resource_number} could not be found in the system.")


# function to borrow a resource
def borrow_resource(resource_type):
    available_resource = [resource for resource in resources if isinstance(resource, resource_type) and
                          resource.is_available]
    resource_number = input("Enter resource number ")
    for resource in available_resource:
        if resource_number == resource.number:
            resource.is_available = False
            print(f"{resource_type} ,{resource_number} book is borrow success")
        else:
            resource.is_available = True
            break


def view_available_resources(resource_type):
    available_resource = [resource for resource in resources if isinstance(resource, resource_type) and
                          resource.is_available]
    if len(available_resource) > 0:
        for resource in available_resource:
            resource.display()
    else:
        print(f"No available {resource_type} resource found")


# function to view currently unavailable resources of a given type
def view_unavailable_resources(resource_type):
    unavailable_resources = [resource for resource in resources if isinstance(resource, resource_type)
                             and not resource.is_available]
    if len(unavailable_resources) > 0:
        print(f"Unavailable {resource_type.__name__} resources:")
        for resource in unavailable_resources:
            print(f"{resource.number}, {resource.title}, {resource.subject} {resource_type} is currently unavailable ")
    else:
        print(f"No unavailable {resource_type.__name__} resources found.")


# function to lend a resource
def lend_resource(resource):
    if resource.lend():
        print(f"Resource '{resource.title}' has been lent.")
    else:
        print(f"Resource '{resource.title}' is currently not available.")


# function to update a resource when received back
def receive_resource(resource):
    resource.receive()
    print(f"Resource '{resource.title}' has been received back.")


while True:
    print("\nSelect an option:")
    print("1. Add a new resource.")
    print("2. Remove a resource.")
    print("3. View available resources.")
    print("4. View unavailable resources.")
    print("5. Lend a resource.")
    print("6. Exit program.")

    option = input("Enter an option number: ")

    if option == "1":
        add_resource()
    elif option == "2":
        remove_resource()
    elif option == "3":
        x = input("Enter resource type (Book, Magazine, Dvd or Cd): ")
        if x == "Book":
            view_available_resources(Book)
        elif x == "Magazine":
            view_available_resources(Magazine)
        elif x == "Dvd":
            view_available_resources(Dvd)
        elif x == "Cd":
            view_available_resources(Cd)
        else:
            print("Enter valid resource type: ")
    elif option == "4":
        x = input("Enter resource type (Book, Magazine, Dvd or Cd): ")
        if x == "Book":
            view_unavailable_resources(Book)
        elif x == "Magazine":
            view_unavailable_resources(Magazine)
        elif x == "Dvd":
            view_unavailable_resources(Dvd)
        elif x == "Cd":
            view_unavailable_resources(Cd)
        else:
            print("Enter valid resource type: ")
    elif option == "5":
        x = input("Enter resource type (Book, Magazine, Dvd or Cd): ")
        if x == "Book":
            borrow_resource(Book)
        elif x == "Magazine":
            borrow_resource(Magazine)
        elif x == "Dvd":
            borrow_resource(Dvd)
        elif x == "Cd":
            borrow_resource(Cd)
        else:
            print("Enter valid resource type: ")
    elif option == "6":
        print("Goodbye!")
