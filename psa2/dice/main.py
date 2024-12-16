import random
import matplotlib.pyplot as plt


exp_count = 1_000_000

results = [sum([random.randint(1,6) for _ in range(3)]) for _ in range(exp_count)]

# print(results)
print(results.count(18))


# plt.style.use('_mpl-gallery')

plt.hist(results, bins=range(3, 20, 1), edgecolor='black', align='left', rwidth=0.8)
plt.xticks(range(3, 20))
plt.xlabel('Sum of 3 dice')
plt.ylabel('Frequency')

plt.show()