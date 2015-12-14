import os
import numpy as np
import matplotlib.pyplot as plt

vi = 0.10;
vf = 0.45;
dv = 0.05;
nv =  int(round( (vf-vi)/dv )) + 1
v = [ (vi + float(x)*dv) for x in range(nv) ];

fv = open( 'vList.txt' , 'w')

for vRun in v:
    # read in input parameters
    f = open( 'input.txt', 'r+')
    content = [x.strip('\n') for x in f.readlines()]
    f.close()

    # replace v with desired value
    f = open( 'input.txt', 'w+')
    content[4] = '%.3f' % vRun
    fv.write(content[4]+'\n')
    # re-write inpute.txt with new 'v' value
    for x in content:
        f.write(str(x)+'\n')
    f.close()

    os.system('./a.out')
    os.system('python analysis.py')

fv.close()
