#from enum import Enum
import math


class HashMap:

    # Note to self for enum:
    # Enum works similar to Java (not like I've used it there but whatever)
    # Where it lets you input letters, and it treats it like some integer
    # To get the actual letters do ClassName.(enumName). To get the value, add .value at the end

    def __init__(self, size: int = 100) -> None:
        self.__size = size
        self.__map = [[] for _ in range(self.__size)]
        self.__load = 0
        self.__weight = 0

    def __str__(self) -> str:
        res = "{"
        for item in self.__map:
            if item != [] and item != [None, None]:
                res += str(item[0]) + ": " + str(item[1]) + ", "
        res = res[0:len(res) - 2]
        res += "}" if res != "" else ""
        return res

    def insertOrReplace(self, key, value) -> bool:
        if key is None and value is None:
            print("No NoneType attributes can be added to this HashMap as a key and value pair.")
            return False
        # check if key in map at hashed index is possible for insertion
        index = hash(key) % self.__size
        # if empty bucket at index
        if self.__map[index] == [] or self.__map[index] == [None, None]:
            self.__map[index] = [key, value]
            self.__weight += 1
            self.__setLoad()
            self.__resize()
            return True

        # else if there is a full bucket but the keys match, replace
        elif len(self.__map[index]) == 2:
            if self.__map[index][0] == key:
                self.__map[index] = [key, value]
                self.__weight += 1
                self.__setLoad()
                self.__resize()
                return True
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
                    return True
            if counter == index:
                b = True
            else:
                counter = (counter + 1) % self.__size

        if b:
            return False  # this accounts for a bug if the thing is full. if my code is right it won't
        # ever happen but you know. stuff happens.
        else:
            self.__map[counter] = [key, value]
            self.__weight += 1
            self.__setLoad()
            self.__resize()
            return True

    def find(self, key):
        index = hash(key) % self.__size
        if self.__map[index][0] == key:
            return True
        else:
            if self._linearProbe(key) == -1:
                return False
            return True

    def get(self, key):
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
        index = hash(key) % self.__size
        counter = (index + 1) % self.__size
        while self.__map[counter] != [] and counter != index:
            if self.__map[counter][0] == key:
                return counter
            else:
                counter = (counter + 1) % self.__size
        return -1

    def __resize(self) -> None:
        if self.__load > 0.75:
            def isPrime(n):

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

            def nextPrime(N):

                # Base case
                if (N <= 1):
                    return 2

                prime = N
                found = False

                # Loop continuously until isPrime returns
                # True for a number greater than n
                while (not found):
                    prime = prime + 1

                    if (isPrime(prime) == True):
                        found = True

                return prime

            # above inner functions taken from https://www.geeksforgeeks.org/program-to-find-the-next-prime-number/#
            # because I'm focusing on hash map stuff not finding new primes

            num = nextPrime(self.__size)
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
        self.__load = self.__weight / self.__size

    def getKeys(self) -> []:
        res = []
        for item in self.__map:
            if item != [] and item != [None, None]:
                res.append(item[0])
        return res

    def getValues(self):
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
print(hm.getLoad())