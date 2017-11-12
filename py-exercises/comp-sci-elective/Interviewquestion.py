"""
Interview Question:
If we list all the natural nmbers below 10 that ar emultiples of 3 or 5, we get 3,5,6,9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 50,000,000.
"""
import time

class sum_finder():
    def main(self, max):
        total = 0
        for i in range(1, max):
            if i % 3 == 0 or i % 5 == 0:
                total = total + i
        return total


if __name__ == "__main__":
    main = sum_finder()
    now = time.time()
    result = main.main(1000)
    then = time.time()
    print(result)
    print("This took {}s".format(then - now))
