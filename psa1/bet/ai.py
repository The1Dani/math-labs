
import numpy as np

# Simulation parameters
num_simulations = 1_000_000 * 10# Large number of plays for better average estimation

# Function to simulate one game
def simulate_game():
    tosses = 1
    while np.random.rand() > 0.5:  # Keep flipping until the first heads
        tosses += 1
    return 2**tosses

# Run the simulation
payouts = [simulate_game() for _ in range(num_simulations)]

# Calculate the average payout
average_payout = np.mean(payouts)
print(f"Average payout: {average_payout:.2f}")