""" 0-prime game module """


def isWinner(x, nums):
    """ Chooses a winner based on x rounds with nums \
          integers to check for prime numbers """
def is_prime(n):
    """ Checks if a number given n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True
def calculate_primes(n, primes):
    """ Calculate all primes """
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)

    # number of players
    if (len(nums) < 1) or (x < 1):
        return None
def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    ben = maria = 0
    players_wins = {"Maria": 0, "Ben": 0}

    # 1 == Maria | 2 == Ben
    count = 0
    for rounds in range(x):
        y = nums[rounds]
        non_uniq = set()
    primes = [0, 0, 2]

        # prime numbers are picked out via sieve of erathosthenes algorithm
    calculate_primes(max(nums), primes)

        for number in range(2, nums[rounds] + 1):
    for round in range(x):
        sum_options = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])

            if number in non_uniq:
                continue
            else:
                count = (2 if count == 1 else 1)
                multiplier = 1
                product = 0
                # add prime number & multiples to set
                while (product <= nums[rounds]):
                    product = number * multiplier
                    multiplier += 1
                    if (product <= nums[rounds]):
                        non_uniq.add(product)
        if (nums[rounds] == 1):
            count = (2 if count == 1 else 1)
        if (count == 2):
            ben += 1
        if (sum_options % 2):
            winner = "Maria"
        else:
            maria += 1
            winner = "Ben"
        if winner:
            players_wins[winner] += 1

    # return None if equal
    if (maria != ben):
        return ("Maria" if maria > ben else "Ben")
    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return (None)
    return None
