# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:36:44 2013

Magnetic Trap Simulator, Python edition
This is a Python port of the most up-to-date simulator I had written in 
MatLab as of 7/4/10. It simulates
the combined fields from the macrowires and microwires.
This script requires the support script 'Field_Realistic.m'.
Documentation is the accompanying text file.

@author: Will
"""



## Trap parameters
# The script needs:
#       -the bias field (B_ybias) in Gauss
#       -the central wire length (l) in microns
#       -the trap height (h) in microns
#       -the wire current (I) in amps
#
# Formulae are provided for deriving the necessary bias field to realize a
# particular trap height. Trap length must be provided, plus any two of
# (B_ybias, I, and h).


# Axes are defined so that z is up (out of the chip plane), x is along the
# central axis of the z trap ( = ODT axis) and y follows the right-hand
# rule.

#The z ground plane is the top of the MACOR surface.


from AtomChip import *
import numpy as np
import acwires

#Simulation Mode
fieldplot = 0
plotxz = 1

## Plot parameters
plot_on=1
#plot freq (1) or G/cm^2 (0)?
#plot gradient of x (1) or y (0)?
freq=1 
xplot=0
# all distance in units of meters
# resolution=a/4000 # resolution of the plots, meters
# plotleft=-a_ax/50 # boundary of plots, meters
# plotright=a_ax/50
# plottop = a/50
# plotbottom = -a/50

resolution=a/50 # resolution of the plots, meters
plotleft=-a_ax # boundary of plots, meters
plotright=a_ax
plottop = a
plotbottom = -a
# 
# resolution=a/400 # resolution of the plots, meters
# plotleft=-a_ax/8 # boundary of plots, meters
# plotright=a_ax/8
# plottop = a/8
# plotbottom = -a/8
# 
# resolution=a/2000 # resolution of the plots, meters
# plotleft= -l_med/4 # boundary of plots, meters
# plotright= l_med/4
# plottop = a/40
# plotbottom = -a/40

# resolution=a/100000 # resolution of the plots, meters
# plotleft=-l_med/500 # boundary of plots, meters
# plotright=l_med/500
# plottop = a/500
# plotbottom = -a/500

# For traps along y-axis
# plotleft=-10*a # boundary of plots, microns
# plotright=10*a
# plottop = 3*a
# plotbottom = -a

(fin_horz_params, fin_vert_params, fin_norm_params) = Wire_Geometry_Specification_Realistic_101910()
## Find trap

if plotxz == 1:
    n = 100 #how many points to check
    z_range = np.zeros(2,n)
    z_range(1,:) = np.linspace(z*.8,z*1.5,n) #meters
else:
    n = 1000
    z_range = np.zeros(2,n)
    z_range(1,:) = np.linspace(z*.9,z*1.1,n) #meters
end

z_spacing = z_range(1,2)-z_range(1,1) #meters


#for ii = 1:n
for ii in range(n):
    B_tot_center=Field_Realistic(x_trap,y_trap,z_range(1,ii),B_xbias,B_ybias,B_zbias, fin_horz_params, fin_vert_params,fin_norm_params)
    z_range(2,ii) = B_tot_center #in Tesla


#correct for gravity
gravity_equivalent_field = (m_Rb87 * g)/(mu_B) * z_range(1,:)
z_range(2,:) = z_range(2,:) - gravity_equivalent_field
[min_B_tot, min_index] = min(z_range(2,:))

trap_height = z_range(1,min_index)
if fieldplot == 0:
    disp(['Trap Height is ', num2str(10^6*trap_height)])
#trap_height = h*1e-6
#trap_height = 3e-3

figure(13)
plot(z_range(1,:)*1e3, z_range(2,:)*1e4)
xlabel('Z axis (mm)') #Standard axis labelling
ylabel('Effective |B|, (G)')

## Field calculations

if fieldplot == 1:
    
    # permute coordinates to create slices in other planes.
    
    if plotxz == 1:
        
        [x,z] =meshgrid(plotleft:resolution:plotright, z_range(1,:))
        B_tot=Field_Realistic(x,y_trap,z,B_xbias,B_ybias,B_zbias, fin_horz_params, fin_vert_params,fin_norm_params)
        B_tot_grav_corr = B_tot - (m_Rb87 * g)/(mu_B) * z
        
        figure(1)
        meshc(x*10^3,z*10^3,B_tot_grav_corr*10^4)
        xlabel('X axis (mm)')
        ylabel('Z axis (mm)') #standard axis labelling
        zlabel('B field (G)')
        view(0,90)
        
    else:
        
        [x,y]=meshgrid(plotleft:resolution:plotright, plotbottom:resolution:plottop)
        B_tot=Field_Realistic(x,y,trap_height,B_xbias,B_ybias,B_zbias, fin_horz_params, fin_vert_params,fin_norm_params)
        
        
        
        #find the trap
        [min_field, y_ind] = min(B_tot)
        [min_field, x_ind] = min(min_field)
        y_ind = y_ind(1,x_ind)
        x_trap = x(1,x_ind)
        y_trap = y(y_ind,1)
        
        [GradBx,GradBy]=gradient(B_tot,resolution)
        [GGradBx,GGradByx]=gradient(GradBx,resolution)
        [GGradBxy,GGradBy]=gradient(GradBy,resolution)
        ## Extract and print frequency
        # The first part attempts to extract the transverse and longitudinal
        # frequencies by fitting to a paraboloid and extracting the principal values
        traploc = [y_ind, x_ind]
        a = abs(GGradBy(traploc(1),traploc(2)))
        b = abs(.5*(GGradByx(traploc(1),traploc(2)) + GGradBxy(traploc(1),traploc(2))))
        c = abs(GGradBx(traploc(1),traploc(2)))
        Principal_Matrix = [a, b; b, c]
        [vectors, values] = eig(Principal_Matrix)
        freqs = (1.2754)*sqrt(abs(eig(Principal_Matrix))) #Hz
        f_transverse = max(freqs)
        f_longitudinal = min(freqs)
        omega_transverse = 2*pi*f_transverse
        omega_longitudinal = 2*pi*f_longitudinal
        
        # Try to extract f_transverse by fitting a parabola to z_range
        grad_z = gradient(z_range(2,:), z_spacing)
        ggrad_z = gradient(grad_z, z_spacing)
        ddBdzz = ggrad_z(min_index)
        f_z = 1.2754*sqrt(abs(ddBdzz))
        omega_z = 2*pi*f_z
        
        B_ybias = B_ybias*10^4 #Gauss
        B_tot_center = B_tot(traploc(1),traploc(2))*1e4 #Gauss
        trap_height = trap_height*1e6 #microns
        
        ## Other Trap Parameters
        ODT_temp = 1e-6 #Kelvin, a guess
        f_rad_ODT = 40 #Hz, extracted from Lin
        f_ax_ODT = .3 #Hz, extracted from Lin
        
        AC_trap_temp = ((f_z^2 * f_longitudinal)/(f_rad_ODT^2 * f_ax_ODT))^(1/3) * ODT_temp
        cloud_length = 2*1e6*(k_B * AC_trap_temp / (m_Rb87 * omega_longitudinal^2))^.5 #microns
        cloud_width = 2*1e6*(k_B * AC_trap_temp / (m_Rb87 * omega_z^2))^.5 #microns
        
        ## Plotting
        if plot_on==1:
            figure(1)
            meshc(x*10^3,y*10^3,B_tot*10^4)
            xlabel('X axis (mm)')
            ylabel('Y axis (mm)') #standard axis labelling
            zlabel('B field (G)')
            view(0,0)
            
            #     figure(14)
            #     plot(z_range(1,:)*1e3, ggrad_z)
            #     xlabel('Z axis (\mum)') #Standard axis labelling
            #     ylabel('2nd Derivative of Field Strength')
