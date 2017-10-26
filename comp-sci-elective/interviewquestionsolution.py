import time

class sigma_finder():
    def sum_divisible_by(self, number, max):
        p = max/number
        sum = number * ( p * (p + 1)) / 2
        print("{} * ( {} * ({})) / 2 = {}".format(number, p, p+1, sum))
        return sum

    def main(self, limit):
        result = self.sum_divisible_by(3, limit) + self.sum_divisible_by(5, limit) - self.sum_divisible_by(15, limit)
        return result
if __name__ == "__main__":
    limit = 50000000
    main = sigma_finder()
    now = time.time()
    result = main.main(limit)
    then = time.time()
    print("The sum of the multiples of 3 to 5 below {} is {}".format(limit, result))
    print("This took {}s".format(then - now))
