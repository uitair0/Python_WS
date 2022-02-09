import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C++', 'C#', 'ETC']
plt.pie(values, labels=labels, autopct='%.1f%%',
        startangle=90, counterclock=False)
plt.show()
