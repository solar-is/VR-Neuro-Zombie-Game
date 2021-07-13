from urllib.request import urlopen
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import time

N = 600
values = np.zeros(N)
for i in range(N):
    value = int(urlopen('http://127.0.0.1:8000/hr/get').read().decode())
    values[i] = value
    time.sleep(1)

print(values)

CI = (60*1000)/values
dRR = max(CI)-min(CI)
M = stats.mode(CI).mode

n, bins, p = plt.hist(CI, bins=range(int(min(CI)), int(max(CI)), 50), edgecolor='black', label='Распределение кардиоинтервалов')
plt.vlines(M, ymin=0, ymax=max(n), color='r', label='Мода')
plt.legend()
AM = 0
for i in range(len(bins)):
    if bins[i] > M:
        AM = n[i-1]
        break
IN = (AM/N)*100/(2*M/1000*(dRR/1000))

plt.title('Индекс напряженности = {}'.format(IN))
plt.savefig('Graph.png')
