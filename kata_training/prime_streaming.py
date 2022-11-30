# It's a generator that yields prime numbers
# Path: codewars_python/kata_training/prime_streaming.py
# pylint: disable=too-few-public-methods
# codewars error: Execution Timed Out (12000 ms)

class Primes:
    @staticmethod
    def stream():
        """
        It returns a generator that yields all prime numbers
        """
        is_prime = lambda n: all(n % i for i in range(2, n))
        n = 2
        while True:
            if is_prime(n):
                yield n
            n += 1


def main() -> None:
    """
    It prints the first 1000 prime numbers
    """
    stream = Primes.stream()
    for _ in range(1000):
        print(next(stream))
    
    
if __name__ == '__main__':
    main()
