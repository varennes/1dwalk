import numpy as np
import matplotlib.pyplot as plt

def format(value):
    return "%.3f" % value

f = open( 'input.txt', 'r')
content = [x.strip('\n') for x in f.readlines()]
content.pop(0)
content = [ float(x) for x in content]
f.close()

runTotal = int(content[0])
N = int(content[1])
L = content[2]
v = content[3]

print ' '
print runTotal
print N
print L
print v

tMean = [];
tSdev = [];

for i in range(9,N,10):
    filename = 'tRun00' + str(i+1) + '.dat'

    if (i+1) >= 10:
        filename = 'tRun0' + str(i+1) + '.dat'

    if (i+1) >= 100:
        filename = 'tRun' + str(i+1) + '.dat'

    f = open(filename,'r')
    tRun = [ float(x.strip('\n')) for x in f.readlines()]

    tMean.append(np.mean(tRun))
    tSdev.append(np.std(tRun))

f.close()

vStr = '%.0f' % (v*100)
filename = 'fpt_v0_' + vStr + '.dat'
fo = open(filename, 'w')
j = 0
for i in range(9,N,10):
    s = str(i+1) + ' ' + str(tMean[j]) + ' ' + str(tSdev[j]) + '\n'
    fo.write(s)
    j += 1

# fo.write(str(formatted))
fo.close()

# n = [ i+1 for i in range(N)]
# plt.errorbar( n, tMean, yerr=tSdev)
# plt.xlim([min(n)-1, max(n)+1])
# # plt.xticks(n)
# plt.xlabel('N')
# plt.ylabel('FPT')
# plt.show()
#
# plt.errorbar( n, tMean, yerr=tSdev)
# plt.xscale('log')
# plt.yscale('log')
# plt.show()
