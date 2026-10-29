class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name #establishes name
        self.number = number #establishes number
    def __str__(self):
        return f"{self.name} : {self.number}" #returns in a string format
    
class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key #name of the contact
        self.value = value #contact
        self.next = None


class HashTable: #fast lookups, rather than checking every value, it finds exactly where a value should be stored, associates keys with values
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self, size): 
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index] #gets the list

        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return
        while current: #runs until a value of None is reached
            if current.key == key: 
                current.value = value
                return 
            if current.next is None:
                break #stops
            current = current.next

        current.next = Node(key, value) #adds to the end of the list
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current: 
            if current.key == key: 
                return current.value
            current = current.next
        return None
    
    def print_table(self):
        for i in range(self.size): 
            print (f"{i}: ", end="") #new method to try

            current = self.data[i]

            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

# Test your hash table implementation here.  
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890 

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 

table = HashTable(10)
#table.insert("Moby Dick", "Checked Out")
#table.insert("Brave New World", "Available")
#table.insert("1984", "Available")

#table = HashTable(10)
#table.print_table()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
print(type(table.print_table))
table.print_table()

contact = table.search("John") 
print("\nSearch result:", contact)

#EDGE CASES
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")
#table.print_table()



john = Contact("John", "909-876-1234")
rebecca = Contact("Rebecca", "111-555-0002")

table.insert(john.name, john) #new way of testing to include the name
table.insert(rebecca.name, rebecca)
table.print_table()


#DESIGN MEMO
# The hash table is the right structure for fast lookups as it correlates keys to values, and does not search
# through a list one by one. This allows for a better user experience, and for more efficient code that eliminates the chance of lagging
# or breaking down due to too many values needing to be sifted through. Collisions were handled using seperate chaining to eliminate the chance of
# overwriting a value, and following a traversal structure to add the new node, not replace an existing one. 
# An engineer might choose a hash table over a list or a tree if the values are significantly large, and if the values need to be quickly searched.
# The hash table also allows for multiple values to be stored with a similar index without overwriting them, and the tables are efficient with larger amounts of data. 



