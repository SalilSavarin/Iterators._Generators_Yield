nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None], []
]

class FlatIterator():
    cursor = 0
    cursor_index = -1
    def __init__(self,collection) -> None:
       self.collection = collection
    
    def __iter__(self):
        return self

    def __next__(self):
        self.cursor_index += 1
        while self.cursor_index > len(self.collection[self.cursor]) - 1:
            self.cursor += 1
            self.cursor_index = 0
            if self.cursor > len(self.collection) - 1:
                raise StopIteration            
        return self.collection[self.cursor][self.cursor_index]
                
      
# for i in FlatIterator(nested_list):
#     print(i)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)

def my_next(some_list):
    cursor = 0
    cursor_index = -1
    while True:
        cursor_index += 1
        while cursor_index > len(some_list[cursor]) - 1:
            cursor +=1
            cursor_index = 0
            if cursor > len(some_list) - 1:
                return
        yield some_list[cursor][cursor_index]

for item in my_next(nested_list):
    print(item)