# import os
# import numpy as np
import matplotlib.pyplot as plt

fvList = open( 'vList.txt' , 'r')
v = [];
for line in fvList:
    v.append(float(line))

# make plots from simulation data
for vRun in v:
    vStr = '%.0f' % (vRun*100)
    filename = 'fpt_v0_' + vStr + '.dat'
    fv = open(filename, 'r')

    n = [];
    mean = [];
    std = [];
    for line in fv:
        row  = line.split()
        n.append(float(row[0]))
        mean.append(float(row[1]))
        std.append(float(row[2]))

    vStr = '%.3f' %vRun
    plt.errorbar( n, mean, yerr=std, label=vStr)

plt.xscale('log')
plt.yscale('log')

plt.legend(loc=2)
plt.xlabel('N')
plt.ylabel('FPT')
plt.title('Mean FPT for different Drift Velocity')
# plt.savefig('mfpt_n90_2.png')
plt.show()
