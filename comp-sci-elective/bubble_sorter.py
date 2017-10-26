"""
@package example
@author
Bubble Sorting
"""
from pprint import pprint as pp

class bubble_sort():
    def main(self, my_array):
        is_sorted = False
        array_len = len(my_array)
        while not is_sorted:
            is_sorted = True
            array_len = array_len - 1
            for i in range(0, array_len):
                if my_array[i]> my_array[i + 1]:
                    temp = my_array[i]
                    my_array[i] = my_array[i + 1]
                    my_array[i + 1] = temp
                    is_sorted = False
        return my_array
    def play(self, my_array):
        result = my_array.sort()


if __name__ == "__main__":
    my_array = [3,1,8,9,7,5]
    main = bubble_sort()
    result2 = main.play(my_array)
    result = main.main(my_array)
    print(result)
