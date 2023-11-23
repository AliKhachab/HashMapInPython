import math

class HashMap:
    def __init__(self, size: int = 100) -> None:
        '''
        @param: size (int). Default value of 100.
        Constructor

        Makes the hash map.
        '''

        self.__size = size
        self.__map = [[] for _ in range(self.__size)]
        self.__load = 0 # load as in weight/size. see resize method.
        self.__weight = 0 # weight as in how many key value pairs are in the hash map.

    def __str__(self) -> str:
        '''toString'''

        res = "{"
        for item in self.__map:
            if item != [] and item != [None, None]:
                res += str(item[0]) + ": " + str(item[1]) + ", "
        res = res[0:len(res) - 2]
        res += "}" if res != "" else ""
        return res

    def insertOrReplace(self, key, value):
        '''
        @param: key (any type)
        @param: value (any type)
        Note: key and value cannot both be None

        Inserts the key and value into the hash map.
        If the key already exists, it replaces the value for that key with the new value.
        '''

        if key is None and value is None:
            print("No NoneType attributes can be added to this HashMap as a key and value pair.")
            return
        
        # check if key in map at hashed index is possible for insertion
        index = hash(key) % self.__size

        # if empty bucket at index
        if self.__map[index] == [] or self.__map[index] == [None, None]:
            self.__map[index] = [key, value]
            self.__weight += 1

            # increases weight, sets new load, and resizes if need be.

            self.__setLoad()
            self.__resize()
            return

        # else if there is a full bucket but the keys match, replace.
        # no need to change weight because we are just replacing a key value pair. 

        elif len(self.__map[index]) == 2:
            if self.__map[index][0] == key:
                self.__map[index] = [key, value]
                return
        
        # else linear probe and find a bucket
        counter = (index + 1) % self.__size
        b = False
        while self.__map[counter] != [] and self.__map[counter] != [None, None]:
            if len(self.__map[counter]) == 2:
                if self.__map[counter][0] == key:
                    self.__map[counter] = [key, value]
                    self.__weight += 1
                    self.__setLoad()
                    self.__resize()
                    return
            if counter == index:
                b = True
                break
            else:
                counter = (counter + 1) % self.__size

        if not b:
            # linear probing worked, we found an empty bucket or a bucket with a matching key -- update that index
            # to store [key, value]
            self.__map[counter] = [key, value]
            self.__weight += 1
            self.__setLoad()
            self.__resize()
            return
        
        else:
        # this accounts for a bug where the hash map load resizing protocol is 
            # bugged and for some reason the hash map is full. this *shouldn't be happening* though.
            self.__load = 1.0 #force override the load value to trigger self.resize()'s if statement
            self.__resize() # do self.resize()
            self.insertOrReplace(key, value) #recursive call now that there is space in the hash map
            return

            

    def find(self, key) -> bool:
        '''
        @param: key (any type)

        Checks if key is in map.
        '''
        index = hash(key) % self.__size
        if self.__map[index][0] == key:
            return True
        else:
            if self._linearProbe(key) == -1:
                return False
            return True

    def get(self, key):
        '''
        @param: key (any type)

        Gets the value for the following key.
        '''
        index = hash(key) % self.__size
        if self.__map[index][0] == key:
            return self.__map[index][1]
        else:
            num = self._linearProbe(key)
            if num != -1:
                return self.__map[num][1]
            else:
                print(f"~~~No key value pair with the key {key} was found.~~~")

    def delete(self, key) -> None:
        '''
        @param: key (any type)

        Deletes a key value pair from the map.
        '''
        index = hash(key) % self.__size
        if self.__map[index][0] == key:
            self.__map[index] = [None, None]
            self.__weight -= 1
            self.__setLoad()
        else:
            val = self._linearProbe(key)
            if val != -1:
                self.__map[val] = [None, None]
                self.__weight -= 1
                self.__setLoad()
            else:
                print(f"~~~No key value pair with the key {key} was found.~~~")

    def _linearProbe(self, key) -> int:
        '''
        @param: key
        
        Method used for linear probing.
        '''
        index = hash(key) % self.__size
        counter = (index + 1) % self.__size
        while self.__map[counter] != [] and counter != index:
            if self.__map[counter][0] == key:
                return counter
            else:
                counter = (counter + 1) % self.__size
        return -1
    
    # used in finding next array size for the hash map. not writing docstrings for these because this code isn't mine.
    @staticmethod
    def __isPrime(n):

                # Corner cases
                if (n <= 1):
                    return False
                if (n <= 3):
                    return True

                # This is checked so that we can skip
                # middle five numbers in below loop
                if (n % 2 == 0 or n % 3 == 0):
                    return False

                for i in range(5, int(math.sqrt(n) + 1), 6):
                    if (n % i == 0 or n % (i + 2) == 0):
                        return False

                return True
    @staticmethod
    def __nextPrime(N):

        # Base case
        if (N <= 1):
            return 2

        prime = N
        found = False

        # Loop continuously until isPrime returns
        # True for a number greater than n
        while (not found):
            prime = prime + 1

            if (HashMap.__isPrime(prime) == True):
                found = True

        return prime
    
    
            # above methods for primes taken from https://www.geeksforgeeks.org/program-to-find-the-next-prime-number/#

    
    def __resize(self) -> None:
        '''
        Resizes hash map when load is too big.
        '''
        if self.__load > 0.75:
            num = HashMap.__nextPrime(self.__size)
            keys = self.getKeys()
            values = self.getValues()
            self.__map = [[] for _ in range(num)]
            self.__size = num
            self.__weight = 0
            self.__load = 0
            for i in range(len(keys)):
                self.insertOrReplace(keys[i], values[i])

            print(f"Resize has occurred. New size is {self.__size}")

    def __setLoad(self) -> None:
        '''
        Sets load. Meant to be used when item is inserted or deleted.
        '''
        self.__load = self.__weight / self.__size

    def getKeys(self) -> []:
        '''
        Returns all keys.
        '''
        res = []
        for item in self.__map:
            if item != [] and item != [None, None]:
                res.append(item[0])
        return res

    def getValues(self):
        '''Returns all values.'''
        res = []
        for item in self.__map:
            if item != [] and item != [None, None]:
                res.append(item[1])
        return res

    def getLoad(self):
        
        return self.__load

hm = HashMap(5)
for i in range(0, 10, 2):
    hm.insertOrReplace(i, i+1)

print(hm)
print(hm.getLoad()) # getLoad was just for me to check if my resizing worked. basically debugging tool.