import numpy as np
import matplotlib.pyplot as plt

f = open( 'input.txt', 'r')

content = [x.strip('\n') for x in f.readlines()]
content.pop(0)
content = [ float(x) for x in content]

runTotal = int(content[0])
N = int(content[1])
L = content[2]
v = content[3]

print content

print runTotal
print N
print L
print v

tMean = [];
tSdev = [];

for i in range(N):
    filename = 'tRun0' + str(i+1) + '.dat'

    if (i+1) >= 10:
        filename = 'tRun' + str(i+1) + '.dat'

    f = open(filename,'r')
    tRun = [ float(x.strip('\n')) for x in f.readlines()]

    tMean.append(np.mean(tRun))
    tSdev.append(np.std(tRun))

n = [ i+1 for i in range(N)]
plt.errorbar( n, tMean, yerr=tSdev)
plt.xlim([min(n)-1, max(n)+1])
plt.xticks(n)
plt.xlabel('N')
plt.ylabel('FPT')
plt.show()
