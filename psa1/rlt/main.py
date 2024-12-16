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
        
def dalembert(rounds, bet=1, selection="R"):

    # Initialize variables
    balance = 0
    win = 0
    loss = 0

    # Iterate through the rounds
    for _ in range(rounds):

        # If the selection is correct
        if roulette(selection):

            # Increase the balance by the bet
            balance += bet

            # Increase the win count
            win += 1

        # If the selection is incorrect
        else:

            # Decrease the balance by the bet
            balance -= bet

            # Increase the loss count
            loss += 1

    # Return the balance, win count, and loss count
    return balance, win, loss

def main():
    
    bot = 10
    upp = 10_000

    win_ratio = 0
    n = 0

    for _ in range(bot,upp + bot, bot):

        _, w, _ = dalembert(1000)

        win_ratio += w / 1000

        n += 1

    win_ratio = win_ratio / n * 100

    print(f"Win ratio: {win_ratio:.2f}%")



if __name__ == "__main__":
    main()