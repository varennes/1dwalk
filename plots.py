# import os
import numpy as np
import matplotlib.pyplot as plt

# get simulation parameter values
f = open( 'input.txt', 'r+')
content = [x.strip('\n') for x in f.readlines()]
f.close()
L = float(content[2])

fvList = open( 'vList.txt' , 'r')
v = [];
for line in fvList:
    v.append(float(line))

tScale = [ 2.0*vRun/L for vRun in v]

tFit = []
tMean = []
vSlope = []

# make plots from simulation data
cList = ['b', 'g', 'r', 'c', 'm', 'k']
# plt.subplot(2,1,1)
i = 0;
for vRun in v:
    vStr = '%.0f' % (vRun*100)
    filename = 'fpt_v0_' + vStr + '.dat'
    fv = open(filename, 'r')

    n = [];
    mean = [];
    std = [];
    for line in fv:
        row  = line.split()
        n.append(float(row[0]) / L) # re-scaled n
        mean.append(float(row[1]) * tScale[i]) # re-scaled mean
        std.append(float(row[2]) * tScale[i]) # re-scaled std

    i += 1
    vStr = '%.3f' %(vRun*2.0)

    tMean.append(mean)

    # get log-log fit (base 10)
    # k = n.index(50)
    # fz = np.polyfit( np.log10(n[k:len(n)]), np.log10(mean[k:len(n)]), 1)
    # z  = np.polyval( fz, np.log10(n[k:len(n)]))
    # tFit.append(z)
    # vSlope.append('%.3f' %fz[0])

    plt.errorbar( n, mean, yerr=std, label=vStr, color=cList[i])

# plt.xscale('log')
# plt.yscale('log')

plt.legend(loc=2)
plt.xlabel(r'$N/L$')
plt.ylabel(r'$<\tau>v/L$')
plt.title('Mean FPT for different Drift Velocity')
# plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
plt.savefig('fig/mfpt_n300_4.png')
plt.show()

# plt.subplot(2,1,2)
# i = 0
# for vRun in v:
#     plt.plot(np.log10(n),np.log10(tMean[i]), 'o', color=cList[i]) #, label=['%.2f' %vRun])
#     plt.plot(np.log10(n[k:len(n)]),tFit[i], color=cList[i], label=vSlope[i])
#     i += 1
#
# plt.legend(loc=2)
# plt.title('FPT for different Drift Velocity, Log-log Fits')
# plt.xlabel('$\log_{10}(N)$')
# plt.ylabel('$\log_{10}(FPT)$')
# plt.savefig('fig/mfpt_n300_3.png')
# plt.show()
