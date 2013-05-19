# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:54:24 2013

@author: Will
"""

#hwire(i).name = 'Central Trapping Macrowire'
#hwire(i).xl = -l_trap/2
#hwire(i).length = l_trap
#hwire(i).y0 = -w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -h_rad
#hwire(i).height = h_rad
#hwire(i).current = I_in
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#
#vwire(i).name = 'Left Axial Bias Macrowire'
#vwire(i).yd = -l_ax/2
#vwire(i).length = l_ax
#vwire(i).x0 = -a_ax/2-w_ax/2
#vwire(i).width = w_ax
#vwire(i).z0 = -sub - h_ax/2
#vwire(i).height = h_ax
#vwire(i).current = I_ax
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2

# nwire(i).name = 'Left Axial Lead Macrowire'
# nwire(i).zd = -15e-3
# nwire(i).length =13.7e-3
# nwire(i).x0 = -8.75e-3
# nwire(i).width = 3e-3
# nwire(i).y0 = 4e-3
# nwire(i).breadth = 1e-3
# nwire(i).current = -I_ax
# nwire(i).subwires = n
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1

#fin_horz_params = zeros(5,n_hsubwires)
#XL = []
#XR = []
#Y0 = []
#Z0 = []
#I = []
#
##for ii = 1:n_hwires
#for ii in range(n_hwires):
#    nn = hwire(ii).subwires
#    XL = [XL, hwire(ii).xl*ones(1,nn^2)]
#    XR = [XR, (hwire(ii).xl + hwire(ii).length)*ones(1,nn^2)]
#    Y0 = [Y0, repmat(linspace(hwire(ii).y0, (hwire(ii).y0 + hwire(ii).width), nn),1,nn)]
#    z_values = linspace(hwire(ii).z0, (hwire(ii).z0 + hwire(ii).height),nn)
#    Z_vector = []
##    for jj = 1:hwire(ii).subwires
#    for jj in range(hwire(ii).subwires):
#        Z_vector = [Z_vector, z_values(jj)*ones(1,nn)]
#    Z0 = [Z0, Z_vector]
#    I = [I, hwire(ii).current/nn^2 * ones(1,nn^2)]
#
#fin_horz_params(1,:) = XL
#fin_horz_params(2,:) = XR
#fin_horz_params(3,:) = Y0
#fin_horz_params(4,:) = Z0
#fin_horz_params(5,:) = I

from math import pi, sqrt
import numpy as np

mu = (4*pi)*10**-7 

class Wire():
    def __init__(self, name, length, width, height, current, subwires):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.current = current
        self.subwires = subwires
        
class HWire(Wire):
    def __init__(self, name, length, width, height, current, subwires, xl, y0, z0):
        Wire.__init__(self, name, length, width, height, current, subwires)
        self.xl = xl
        self.y0 = y0
        self.z0 = z0
        
    def bfieldcalc(self,x,y,z):
        #loops over subwires, calculating magnetic field at point (x,y,z)
        XL = self.xl
        XR = self.xl + self.length
        suby = np.linspace(self.y0, self.y0 + self.width, self.subwires)
        subz = np.linspace(self.z0, self.z0 + self.height, self.subwires)
        nn = self.subwires**2
        const_G=mu*self.current/(4*pi*nn)
        for i in range(self.subwires): #loop over y
            for j in range(self.subwires): #loop over z
                beta = (z-subz[j])**2 + (y-suby[i])**2
                B_G=const_G*((x-XL)/(beta*sqrt(beta+
                    (x-XL)**2))-(x-XR)/(beta*sqrt(beta+(x-XR)**2)))
                B_Gy=B_G*(subz[j]-z)
                B_Gz=B_G*(y-suby[i])
        return np.array((0, B_Gy, B_Gz))
        
                
class VWire(Wire):
    def __init__(self, name, length, width, height, current, subwires, x0, yd, z0):
        Wire.__init__(self, name, length, width, height, current, subwires)
        self.x0 = x0
        self.yd = yd
        self.z0 = z0
        
    def bfieldcalc(self,x,y,z):
        #loops over subwires, calculating magnetic field at point (x,y,z)
        YD = self.yd
        YU = self.yd + self.length
        subx = np.linspace(self.x0, self.x0 + self.width, self.subwires)
        subz = np.linspace(self.z0, self.z0 + self.height, self.subwires)
        nn = self.subwires**2
        const_G=mu*self.current/(4*pi*nn)
        for i in range(self.subwires): #loop over x
            for j in range(self.subwires): #loop over z
                beta = (z-subz[j])**2 + (x-subx[i])**2
                B_G=const_G*((y - YD)/(beta*sqrt(beta+
                    (y - YD)**2))-(y - YU)/(beta*sqrt(beta+(y - YU)**2)))
                B_Gx=B_G*(z - subz[j])
                B_Gz=B_G*(subx[i] - x)
        return np.array((B_Gx, 0, B_Gz))
        
        
class NWire(Wire):
    def __init__(self, name, length, width, height, current, subwires, x0, y0, zd):
        Wire.__init__(self, name, length, width, height, current, subwires)
        self.x0 = x0
        self.y0 = y0
        self.zd = zd
        
    def bfieldcalc(self,x,y,z):
        #loops over subwires, calculating magnetic field at point (x,y,z)
        ZD = self.zd
        ZU = self.zd + self.length
        subx = np.linspace(self.x0, self.x0 + self.width, self.subwires)
        suby = np.linspace(self.y0, self.y0 + self.height, self.subwires)
        nn = self.subwires**2
        const_G=mu*self.current/(4*pi*nn)
        for i in range(self.subwires): #loop over x
            for j in range(self.subwires): #loop over y
                beta = (x-subx[i])**2 + (y-suby[j])**2
                B_G=const_G*((z - ZD)/(beta*sqrt(beta+
                    (z - ZD)**2))-(z - ZU)/(beta*sqrt(beta+(z - ZU)**2)))
                B_Gx=B_G*(suby[j] - y)
                B_Gy=B_G*(x - subx[i])
        return np.array((B_Gx, B_Gy, 0))