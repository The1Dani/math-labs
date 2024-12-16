import random
import matplotlib.pyplot as plt

REPUBLICAN = 1
DEMOCRAT = 0
TIE = -1


def getting_vote(republican_percentage):
    if random.randint(0, 1) <= republican_percentage:
        vote = REPUBLICAN
    else:
        vote = DEMOCRAT

    return vote

def experiment(sample_size, republican_percentage):

    
    samples = [getting_vote(republican_percentage) for _ in range(sample_size)]

    if samples.count(REPUBLICAN) > samples.count(DEMOCRAT):
        return REPUBLICAN
    elif samples.count(REPUBLICAN) < samples.count(DEMOCRAT):
        return DEMOCRAT
    else:
        return TIE



results = [experiment(1000, 0.48) for _ in range(100)]

plt.hist(results, bins=range(-1, 3), edgecolor='black', align='mid', rwidth=0.8)
plt.xticks(range(-1, 3))
plt.xticks([DEMOCRAT, REPUBLICAN, TIE], ['Democrats', 'Republicans', 'Tie'])
plt.xlabel('Winner')
plt.ylabel('Frequency')
plt.show()


results = [experiment(3000, 0.49) for _ in range(100)]

plt.hist(results, bins=range(-1, 3), edgecolor='black', align='mid', rwidth=0.8)
plt.xticks(range(-1, 3))
plt.xticks([DEMOCRAT, REPUBLICAN, TIE], ['Democrats', 'Republicans', 'Tie'])
plt.xlabel('Winner')
plt.ylabel('Frequency')
plt.show()
