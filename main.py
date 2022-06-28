# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import hashClass


# def start_deliveries():

def test_hash():
    h = hashClass.HashMap()
    h.add('Bob', '567-8888')
    h.add('Ming', '293-6753')
    h.add('Ming', '333-8233')
    h.add('Ankit', '293-8625')
    h.add('Aditya', '852-6551')
    h.add('Alicia', '632-4123')
    h.add('Mike', '567-2188')
    h.add('Aditya', '777-8888')
    h.print()
    h.delete('Bob')
    h.print()
    print('Ming: ' + h.get('Ming'))
    print(h.keys())


def test_csv():
    with open('Book1.csv') as testList:
        people_data = csv.reader(testList, delimiter=',')
        next(people_data)
        for person in people_data:
            hkey = int(person[1])
            hvalue = Person(hkey, person[0], person[2])
            hashtest.add(hkey, hvalue)
            print(person)


class Hasher:
    def __init__(self,starting_buckets = 10):
        self._size = starting_buckets
        self._table = []
        for i in range(self._size):
            self._table.append([])

    def add(self, key, package):

        bucket = key % len(self._table) #get bucket number
        bucket_list = self._table[bucket] #get list of packages in bucket
        


class Person:
    def __init__(self, ID, name, color):
        self._ID = ID
        self._name = name
        self._color = color

    def __str__(self):
        #return f'{self._ID}, {self._name}, {self._color}'
        return '%s, %s, %s' % (self._ID, self._name, self._color)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hashtest = hashClass.HashMap()
    test_csv()
    print(hashtest.map)
    print('hashtest size is :',range(hashtest.size))
    print('hashtest len is :', len(hashtest.map))
    print('hashtest keys: ', hashtest.keys())
    #hashtest.print()
    hasher = Hasher()
    print(Hasher()._table)
    print(hashClass.HashMap().map)
    for i in range(0,len(hashtest.keys())):
        print('key: ',i+1,'person: ', hashtest.get(i+1))
        #print('Key {}: Person {}'.format(i,hashtest.get(i)))
    print (hashClass.HashMap().map)
