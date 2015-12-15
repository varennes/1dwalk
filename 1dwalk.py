# 1d walk, FPT process
import random
import numpy as np
import matplotlib.pyplot as plt

# get simulation parameter values
f = open( 'input.txt', 'r+')
content = [x.strip('\n') for x in f.readlines()]
f.close()

runTotal = int(content[1])
N = float(content[2])
L = float(content[3])

vi = 0.40;
vf = 0.45;
dv = 0.05;
nv =  int(round( (vf-vi)/dv )) + 1
v = [ (vi + float(x)*dv) for x in range(nv) ];


for vRun in v:
    nList = []
    FPTmean = []
    FPTstdv = []
    pRight = 0.5 + vRun;
    pLeft  = 0.5 - vRun;

    for i in range(1,int(N)+1,2):

        nList.append(i)
        x = []
        tList = []

        for iRun in range(runTotal):
            # print ' n = ' + str(i) + ' run # '+ str(iRun)
            # FPT process
            x = [ float(j) for j in range(i)]
            xCOMi = np.mean(x)
            dCOM = 0.0
            t = 0
            while dCOM < L:

                iList = [ii for ii in range(i)]
                # random.shuffle(iList)
                for j in iList:
                    r = random.random()

                    if r < pRight:
                        if ((j != (i-1)) and (i != 0)):
                            if (x[j]+1.0) != x[j+1]:
                                x[j] += 1.0
                        else:
                            x[j] += 1.0
                    else:
                        if ((j != 0) and (i != 0)):
                            if (x[j]-1.0) != x[j-1]:
                                x[j] += -1.0
                        else:
                            x[j] += -1.0

                xCOM = np.mean(x)
                dCOM = xCOM - xCOMi
                t += 1

            tList.append(t)

        FPTmean.append(np.mean(tList))
        FPTstdv.append(np.std(tList))

    # re-scale data
    # print nList
    nList = [ n/L for n in nList]
    vStr = '%.3f' %(vRun*2.0)
    tScale = 2.0*vRun/L

    FPTmean = [ mean*tScale for mean in FPTmean]
    FPTstdv = [ stdv*tScale for stdv in FPTstdv]

    plt.errorbar( nList, FPTmean, yerr=FPTstdv, label=vStr)

plt.legend(loc=2)
# plt.ylim([1.0, 2.2])
# plt.xlim([min(nList)-0.01, max(nList)+0.01])
# plt.xscale('log')
# plt.yscale('log')
plt.xlabel(r'$N/L$')
plt.ylabel(r'$<\tau>v/L$')
plt.title('Mean FPT for different Drift Velocity (python version)')
# plt.savefig('fig/mfptPY_n300_1.png')
plt.show()
