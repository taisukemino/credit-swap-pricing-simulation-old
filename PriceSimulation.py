from matplotlib import pyplot as plt
import random

coveragePoolSize = []
premiumPoolSize = []

covTokenPrice = []
premTokenPrice = []

for i in range(10):
    coveragePoolSize.append(random.randint(1, 1001))
    premiumPoolSize.append(random.randint(1, 1001))

    covTokenPrice.append(coveragePoolSize[i] / premiumPoolSize[i])
    premTokenPrice.append(premiumPoolSize[i] / coveragePoolSize[i])

print('covTokenPrice', covTokenPrice)
print('premTokenPrice', premTokenPrice)

plt.plot(covTokenPrice, premTokenPrice)
plt.show()

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
