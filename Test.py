# DS
#Collision technique


def display_hash(hashTable): 
      
    for i in range(len(hashTable)): 
        print(i, end = " ") 
          
        for j in hashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
              
        print() 
  
HashTable = [ [] for _ in range(10)] 
   
def Hashing(keyvalue): 
    return keyvalue % len(HashTable) 
  
def insert(Hashtable, keyvalue, value): 
      
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].append(value) 
  
insert(HashTable, 15, 'Prabhat') 
insert(HashTable, 25, 'Vishal') 
insert(HashTable, 20, 'Aakash') 
insert(HashTable, 9, 'Harvey') 
insert(HashTable, 25, 'Louis') 
insert(HashTable, 29, 'Mike') 
  
display_hash (HashTable) 
