import random

def coin_flip():
    return random.choice(['H','T'])

def game():
    j = 0
    got_heads = 0

    while not got_heads:
        j += 1
        if coin_flip() == 'H':
            got_heads = 1

    return 2**j

def repeat(rep):
    biggest = 0
    total = 0
    for i in range(1, rep + 1):
        won = game()
        total += won
        if won > biggest:
            k = i
            biggest = won

    return total/rep, biggest, k

def main():

    rep = int(input("Enter number of repetitions: "))#*1_000_000
    res, biggest, k = repeat(rep)
    
    print(f"${res:.2f}, ${biggest:_}, {k:_}")

if __name__ == "__main__":
    main()