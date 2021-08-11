import pandas as pd
from matplotlib import pyplot as plt

# x = [1,2,3,4]
# y = [2,5,6,7]
# z = [10, 5, 2, 1]

# plt.plot(x,y)
# plt.plot(x,z)


sample_data = pd.read_csv("data.csv")

plt.plot(sample_data.Column_1,sample_data.Column_2, 'o')
plt.plot(sample_data.Column_1,sample_data.Column_3)
plt.plot(sample_data.Column_1,sample_data.Column_4)
plt.title('Basic Data Visualization')
plt.xlabel('Column_1 label')
plt.ylabel('[C_4 Label, C_3 Label, C_2 Label]')
plt.legend(['This is Column_2', 'This is Column_3', 'This is Column_4'])
plt.show()



# print(sample_data.Column_1)