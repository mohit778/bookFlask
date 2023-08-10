import numpy as np
import matplotlib.pyplot as plt
Women = [115, 215, 250, 200,315]
Men = [114, 230, 510, 370,270]

n=5
r = np.arange(n)
width = 0.25


plt.bar(r, Women, color = 'b',
        width = width, edgecolor = 'black',
        label='Women')
plt.bar(r + width, Men, color = 'g',
        width = width, edgecolor = 'black',
        label='Men')

plt.xlabel("Year")
plt.ylabel("Number of people voted")
plt.title("Number of people voted in each year")

# plt.grid(linestyle='--')
plt.xticks(r + width/2,['2018','2019','2020','2021','2022'])
plt.legend()

plt.show()