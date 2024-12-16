import random


def roulette(selection):

    # Randomly select a number between 0 and 36
    number = random.randint(0, 36)

    match selection:
        
        case "G":
            return number == 0

        case "R":
            return number % 2 == 1

        case "B":
            return number % 2 == 0

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def fibo_strat(money, k):
    m = money
    n = 1
    bet = 1
    while m > 0 and m >= bet and n < k + 1:
        m -= bet
        # print(bet, n)
        if roulette("R"):
            m += bet*2
        
        n += 1
        bet = fibo(n)
    return m , m > money

def exp(money, k, reps):
    wins = 0
    total = 0
    for _ in range(reps):
        m, w = fibo_strat(money, k)
        if w:
            wins += 1
        total += m - money
    
    return round(wins/reps*100, 1), round(total/reps, 1)


def main():
    
    rounds = int(input("Enter the number of rounds: "))
    e = int(input("Enter the number of experiments: "))
    print(exp(100, rounds, e))

if __name__ == "__main__":
    main()