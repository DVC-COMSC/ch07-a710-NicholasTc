import matplotlib.pyplot as plt

data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']


# ******************************
# Make your code
# ******************************
fig, ax = plt.subplots()
ax.bar(labels, data1)
ax.bar(labels, data2, bottom=data1)
ax.legend(names)
ax.set_title('Stacked graph for scores')

plt.show()

fig.savefig('A10.png')
