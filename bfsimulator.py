# -*- coding: utf-8 -*-
"""
Created on 2013-07-10

Magnetic Trap Simulator, Python edition
This is a Python port of the most up-to-date simulator I had written in 
MatLab as of 7/4/10. It simulates
the combined fields from the macrowires and microwires.

This is a class-based implementation, unlike BFieldSim

@author: Will
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#from AtomChip import *
import numpy as np
#import acwires
import matplotlib.pyplot as plt
from math import pi, sqrt
from acmconstants import K_B, M

clear = "\n"*100

class BFieldSimulator():
    def __init__(self):      
        self.resolution=0.0001 # resolution of the plots, meters
        self.plotleft=-0.005 # boundary of plots, meters
        self.plotright=0.005
        self.nhorz = (self.plotright - self.plotleft) / self.resolution
        self.plottop = 0.0025
        self.plotbottom = -0.0025
        self.nvert = (self.plottop - self.plotbottom) / self.resolution
        self.x, self.y =np.meshgrid(np.arange(self.plotleft, self.plotright, self.resolution), 
                                    np.arange(self.plotbottom, self.plottop, self.resolution))
        self.n = 5000
#        self.z = 445e-6
    #    z_range = np.zeros(2,n)
        self.z_range = np.linspace(1e-6,3.5e-3,self.n) #meters
        self.z_spacing = self.z_range[1]-self.z_range[0] #meters
    def zoom(self, zoom_factor, center_pt = [0, 0]):
        center_pt = [self.x_trap, self.y_trap]
        self.resolution = self.resolution / zoom_factor
        x_cen = center_pt[0]
        y_cen = center_pt[1]
        self.plotleft = x_cen - 0.5*self.nhorz*self.resolution
        self.plotright = x_cen + 0.5*self.nhorz*self.resolution
        self.plottop = y_cen + 0.5*self.nvert*self.resolution
        self.plotbottom = y_cen - 0.5*self.nvert*self.resolution

        self.x, self.y =np.meshgrid(
                np.linspace(self.plotleft, self.plotright, self.nhorz), 
                np.linspace(self.plotbottom, self.plottop, self.nvert))

    def set_chip(self, chip):
        self.wirespecs = chip['wirespecs']
        #for ii = 1:n
        self.B_tot_trap = np.array([])
        self.B_ybias = chip['B_ybias']
        self.B_bias = np.array((chip['B_xbias'], chip['B_ybias'], chip['B_zbias']))
        #print B_bias
        self.x_trap = 0
        self.y_trap = 0
        self.resolution=0.0001 # resolution of the plots, meters
        self.plotleft=-0.005 # boundary of plots, meters
        self.plotright=0.005
        self.nhorz = (self.plotright - self.plotleft) / self.resolution
        self.plottop = 0.0025
        self.plotbottom = -0.0025
        self.nvert = (self.plottop - self.plotbottom) / self.resolution
        self.x, self.y =np.meshgrid(np.arange(self.plotleft, self.plotright, self.resolution), 
                                    np.arange(self.plotbottom, self.plottop, self.resolution))
        self.n = 5000
#        self.z = 445e-6
    #    z_range = np.zeros(2,n)
        self.z_range = np.linspace(1e-6,3.5e-3,self.n) #meters
        self.z_spacing = self.z_range[1]-self.z_range[0] #meters

    def calc_trap_height(self):
        for ii in xrange(self.n):
            self.tot_field = np.array((0.0,0.0,0.0))
            for wire in self.wirespecs:
                if wire.current != 0:
                    this_field = wire.bfieldcalc(self.x_trap, self.y_trap, self.z_range[ii])
                    self.tot_field = self.tot_field + this_field

            self.tot_field_norm = np.linalg.norm(self.tot_field + self.B_bias)

            self.B_tot_trap = np.append(self.B_tot_trap,self.tot_field_norm)

#            min_B_tot = np.min(self.B_tot_trap)
            self.min_index = np.argmin(self.B_tot_trap)
            
            self.trap_height = self.z_range[self.min_index]
            self.z_trap = self.trap_height
#            print 'Trap Height is %2.0f'%1e6*self.trap_height

    def plot_z(self):
        plt.plot(self.z_range*1e3, self.B_tot_trap*1e4)
        plt.xlabel('Z axis (mm)') #Standard axis labelling
        plt.ylabel('Effective |B|, (G)')
        plt.show()

    def calc_xz(self):        
        self.x, self.z = np.meshgrid(np.arange(self.plotleft, self.plotright, self.resolution), self.z_range)
        self.B_tot = np.zeros(self.x.shape)
        for coords in np.ndenumerate(self.x):
            tot_field = np.array((0.0,0.0,0.0))
            for wire in self.wirespecs.allwires:
                this_field = wire.bfieldcalc(self.x[coords[0]], 
                                             self.y_trap, 
                                             self.z[coords[0]])
                tot_field += this_field
            tot_field_norm = np.linalg.norm(tot_field + self.B_bias)
            self.B_tot[coords[0]] = tot_field_norm
            
    def plot_xz(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot_surface(self.x*1e3,self.z*1e3,self.B_tot*1e4, rstride=8, cstride=8, alpha=0.3)
        plt.xlabel('X axis (mm)')
        plt.ylabel('Z axis (mm)') #standard axis labelling
        ax.set_zlabel('B field (G)')
        plt.show()
        
    def calc_xy(self):
        self.B_tot = np.zeros(self.x.shape)
        for coords in np.ndenumerate(self.x):    
            tot_field = np.array((0.0,0.0,0.0))
            i = 1
            for wire in self.wirespecs:
                i += 1
                this_field = wire.bfieldcalc(self.x[coords[0]], 
                                              self.y[coords[0]], 
                                                self.z_trap)
                tot_field += this_field
            tot_field_norm = np.linalg.norm(tot_field + self.B_bias)
            self.B_tot[coords[0]] = tot_field_norm

    def analyze_trap(self):
        trap_params = {}
        min_ind = np.unravel_index(self.B_tot.argmin(), self.B_tot.shape)
        x_ind = min_ind[0]
#        print 'x_ind: %d'%x_ind
        y_ind = min_ind[1]
#        print 'y_ind: %d'%y_ind
        self.x_trap = self.x[0, y_ind]
        self.y_trap = self.y[x_ind, 0]
        
        GradBx,GradBy = np.gradient(self.B_tot,self.resolution, self.resolution)
        GGradBx, GGradByx = np.gradient(GradBx,self.resolution, self.resolution)
        GGradBxy,GGradBy = np.gradient(GradBy,self.resolution, self.resolution)
        ## Extract and print frequency
        # The first part attempts to extract the transverse and longitudinal
        # frequencies by fitting to a paraboloid and extracting the principal values
        self.traploc = [x_ind, y_ind]
#        print traploc
#        print GGradBy
        a = abs(GGradBy[(self.traploc[0],self.traploc[1])])
        b = abs(.5*(GGradByx[(self.traploc[0],self.traploc[1])] 
                + GGradBxy[(self.traploc[0],self.traploc[1])]))
        c = abs(GGradBx[(self.traploc[0],self.traploc[1])])
#        print a
#        print b
#        print c
        Principal_Matrix = np.array([[a, b], [b, c]])
        self.values, self.vectors = np.linalg.eig(Principal_Matrix)
        freqs = []
        for val in self.values:
            freqs.append((1.2754)*sqrt(abs(val))) #Hz
        self.f_transverse = max(freqs)
        self.f_longitudinal = min(freqs)
        self.omega_transverse = 2*pi*self.f_transverse
        self.omega_longitudinal = 2*pi*self.f_longitudinal
        
        # Try to extract f_transverse by fitting a parabola to z_range
        grad_z = np.gradient(self.B_tot_trap, self.z_spacing)
        ggrad_z = np.gradient(grad_z, self.z_spacing)
        ddBdzz = ggrad_z[self.min_index]
        self.f_z = 1.2754*sqrt(abs(ddBdzz))
        self.omega_z = 2*pi*self.f_z
        
        self.B_ybias = self.B_ybias*1e4 #Gauss
        self.B_tot_center = self.B_tot[(self.traploc[0],self.traploc[1])]*1e4 #Gauss
        self.trap_height = self.trap_height #microns
        
        ## Other Trap Parameters
        self.ODT_temp = 1e-6 #Kelvin, a guess
        self.f_rad_ODT = 40 #Hz, extracted from Lin
        self.f_ax_ODT = .3 #Hz, extracted from Lin
        
        self.AC_trap_temp = (((self.f_z**2 * self.f_longitudinal)
                        /(self.f_rad_ODT**2 * self.f_ax_ODT))**(1/3)
                        * self.ODT_temp)
#        cloud_length = (2*1e6*(k_B * AC_trap_temp 
#                        / (m_Rb87 * omega_longitudinal**2))**.5) #microns
        self.cloud_width = (2*1e6*(K_B * self.AC_trap_temp 
                        / (M * self.omega_z**2))**.5) #microns
        trap_params['h'] = self.trap_height
        trap_params['f_long'] = self.f_longitudinal
        trap_params['f_trans'] = self.f_transverse
        trap_params['f_z'] = self.f_z
        return trap_params
                
        
    def plot_xy(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot_surface(self.x*1e3,self.y*1e3,self.B_tot*1e4, 
                        rstride=8, 
                        cstride=8, 
                        alpha=0.3)
        plt.xlabel('X axis (mm)')
        plt.ylabel('Y axis (mm)') #standard axis labelling
#            plt.zlabel('B field (G)')
        ax.set_zlabel('B field (G)')
        plt.show()
        
if __name__ == '__main__':
    import bsimtest
    bsimtest.unittest.main()