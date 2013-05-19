# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:13:07 2013

@author: Will
"""

text = '''nwire(i).name = 'Left Upper Bias Lead Rod'
nwire(i).zd = -40e-2
nwire(i).length =40e-2
nwire(i).x0 = -40e-3
nwire(i).width = 0
nwire(i).y0 = 0
nwire(i).breadth = 0
nwire(i).current = -I_out
nwire(i).subwires = 1
n_nwires = n_nwires + 1
n_nsubwires = n_nsubwires + nwire(i).subwires^2
i = i + 1

nwire(i).name = 'Right Upper Bias Lead Rod'
nwire(i).zd = -40e-2
nwire(i).length =40e-2
nwire(i).x0 = 40e-3
nwire(i).width = 0
nwire(i).y0 = 0
nwire(i).breadth = 0
nwire(i).current = I_out
nwire(i).subwires = 1
n_nwires = n_nwires + 1
n_nsubwires = n_nsubwires + nwire(i).subwires^2
i = i + 1

nwire(i).name = 'Left Lower Bias Lead Rod'
nwire(i).zd = -40e-2
nwire(i).length =390e-3
nwire(i).x0 = -30e-3
nwire(i).width = 0
nwire(i).y0 = 0
nwire(i).breadth = 0
nwire(i).current = -I_out
nwire(i).subwires = 1
n_nwires = n_nwires + 1
n_nsubwires = n_nsubwires + nwire(i).subwires^2
i = i + 1

nwire(i).name = 'Right Lower Bias Lead Rod'
nwire(i).zd = -40e-2
nwire(i).length =390e-3
nwire(i).x0 = 30e-3
nwire(i).width = 0
nwire(i).y0 = 0
nwire(i).breadth = 0
nwire(i).current = I_out
nwire(i).subwires = 1
n_nwires = n_nwires + 1
n_nsubwires = n_nsubwires + nwire(i).subwires^2
i = i + 1'''
#print lines.split('\n\n')
#print lines.split('\n')
#for line in lines.split('\n'):
#    print line.split('=')

for lines in text.split('\n\n'):
    args = [line.split('=')[1] for line in lines.split('\n')]
#    print args
    print "nwires.append(NWire(%s, %s, %s, %s, %s, %s, %s, %s, %s))\n"%(args[0],args[2],args[4],args[6],args[7],args[8],args[3],args[5],args[1])