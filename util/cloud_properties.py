# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:34:24 2013

@author: Will
"""

from acmconstants import M, HBAR, A, K_B
from math import pi, log
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

hbreak = 50*'-'

#User Input
f_x = 1 #Hz
f_y = 1000 #Hz
f_z = f_y
N = 1e4 #atoms
max_l = 5 #Max l in excitation spectrum
T = 100e-9 #K

omega_x = 2*pi*f_x #Hz
omega_y = 2*pi*f_y #Hz
omega_z = 2*pi*f_z
omega_bar = (omega_x * omega_y * omega_z)**(1.0 / 3)
f_bar = omega_bar / (2*pi)


print 'Particle Number: %d'%N
print 'f_x: %2.2f Hz'%f_x
print 'f_y: %2.2f Hz'%f_y
print 'f_z: %2.2f Hz'%f_z
print 'Temperature: %2.0f nK'%(T * 1e9)

print '\nNon-interacting Bose Gas'
print hbreak
Tc_nonint = 4.5 * (f_bar / 100) * N**(1.0 / 3) *1e-9 #K
print 'T_c: %2.0f nK'%(Tc_nonint * 1e9)
con_frac_ni = 1 - (T / Tc_nonint)**3
if T > Tc_nonint:
    con_frac_ni = 0
print 'Condensate Fraction: %2.2f'%con_frac_ni

#Single Particle Ground State
#print '\nSingle Particle Ground State Oscillator Lengths'
a_osc_x = (HBAR / (M*omega_x))**0.5
a_osc_y = (HBAR / (M*omega_y))**0.5
a_osc_z = (HBAR / (M*omega_z))**0.5
print "a_osc_x: %2.2f um"%(a_osc_x * 1e6)
print "a_osc_y: %2.2f um"%(a_osc_y * 1e6)
print "a_osc_z: %2.2f um"%(a_osc_z * 1e6)


R_x = a_osc_x * (N * A / a_osc_x)**0.2
R_y = a_osc_y * (N * A / a_osc_y)**0.2
R_z = a_osc_z * (N * A / a_osc_z)**0.2
print "R_x: %2.2f um"%(R_x*1e6)
print "R_y: %2.2f um"%(R_y*1e6)
print "R_z: %2.2f um"%(R_z*1e6)

V = (4.0 * pi * R_x * R_y * R_z / 3)
n = N / V
print 'Volume: %2.2e cm^3'%(V * 1e6)
print 'Density: %2.2e atom/cm^3'%(n / 1e6)

omega_bar = (omega_x * omega_y * omega_z)**(1.0/3)
a_bar = (HBAR / (M*omega_bar))**0.5

print '\nInteractions'
print hbreak
print 'Scattering Length: %2.2f nm'%(A * 1e9)
U_0 = (4*pi*HBAR**2*A / M)
print 'Effective Interaction: %2.2e Hz / (atom/cm^3)'%(1e6*U_0 / (2*pi*HBAR))
print 'Interaction Energy: %2.2f Hz'%(n*U_0 / (2*pi*HBAR))
print 'Interaction Energy Temperature: %2.2f nK'%(n*U_0 *1e9/ K_B)
s = (n*U_0 / M)**0.5
print 'Speed of Sound: %2.2f mm/s'%(s*1e3)


#Thomas-Fermi
print '\nThomas-Fermi Approximation'
print hbreak
tf_goodness = N*A / a_bar
if tf_goodness > 10:
    print 'Thomas-Fermi is valid'
else:
    print 'Thomas-Fermi is non valid!!!'
print 'TF Parameter: %2.2f'%tf_goodness
mu = 0.5*(15)**0.4 * (N * A / a_bar)**0.4 * HBAR * omega_bar
print "mu: %2.2f Hz"%(mu / (HBAR*2*pi))

R_tf_x = (2*mu / (M * omega_x**2))**0.5
R_tf_y = (2*mu / (M * omega_y**2))**0.5
R_tf_z = (2*mu / (M * omega_z**2))**0.5
print "R_tf_x: %2.2f um"%(R_tf_x * 1e6)
print "R_tf_y: %2.2f um"%(R_tf_y * 1e6)
print "R_tf_z: %2.2f um"%(R_tf_z * 1e6)


R_bar = 1.719 * (N * A / a_bar)**0.2 * a_bar

#Surface Structure
print '\nSurface Thickness'
print hbreak
delta_x = (0.5 * a_osc_x**4 / R_tf_x)**(1.0/3)
delta_y = (0.5 * a_osc_y**4 / R_tf_y)**(1.0/3)
delta_z = (0.5 * a_osc_z**4 / R_tf_z)**(1.0/3)
print "delta_x: %2.2f um"%(delta_x*1e6)
print "delta_y: %2.2f um"%(delta_y*1e6)
print "delta_z: %2.2f um"%(delta_z*1e6)


healing_length = ((4.0 / 3) * (R_tf_x * R_tf_y * R_tf_x)) / (8 * pi * N * A)
print "\nHealing Length: %2.6f nm"%(healing_length*1e9)

print '\nAnisotropic Cloud Excitation Spectrum'
print hbreak
anisotropy = omega_x / omega_y 
print 'Anisotropy: %f'%anisotropy #Anisotropy parameter
l = np.array(range(1,max_l + 1))
spectrum_1 = np.sqrt(l) * omega_y / (2*pi)
spectrum_2 = np.sqrt(l - 1 + anisotropy**2) * omega_y / (2*pi)
#plt.plot(l, spectrum_1, 'g.', l, spectrum_2, 'b.', markersize = 10)
#plt.xlabel('l')
#plt.ylabel('Excitation Frequency (Hz)')
#plt.suptitle('Anisotropic Trap Excitations')
#plt.plot(l, spectrum_2)
#plt.show()
for freq in np.sort(np.concatenate([spectrum_1,spectrum_2])):
    print '%2.0f Hz'%freq

#Finite Temperature Effects, chp 11 of Pethick and Smith
print '\nFinite Temperature Effects'
print hbreak
int_importance = N**(1.0 / 6) * A / a_bar
print 'Interaction Parameter: %2.2f'%int_importance
T_0 = ((15.0)**0.4 / 7.0) * tf_goodness**0.4 * HBAR * omega_bar / K_B
print 'Interaction Equivalent Temperature: %2.2f nK'%(T_0 * 1e9)
omega_m = (omega_x + omega_y + omega_z) / 3
Tc_shift_pct = -0.73 * omega_m / omega_bar * N**(-1.0 / 3) - 1.33 * A / a_bar * N**(1.0 / 6)
print 'Percent change in Tc: %2.2f %%'%(100*Tc_shift_pct)
Tc_int = (1 + Tc_shift_pct)*Tc_nonint
print 'True T_c: %2.0f nK'%(Tc_int * 1e9)
t = T / Tc_nonint
if t > 1:
    con_frac_int = 0
else:
    con_frac_int = 1 - (t**3 + 2.15*(int_importance)**0.4 * t**2 * (1 - t**3)**0.4)
print 'True Condensate Fraction: %2.2f'%con_frac_int

#One dimensionality, chp 15 of P&S
print '\nLow-dimensional Clouds'
print hbreak
print 'X Freezing Temperature: %2.2f nK'%(HBAR * omega_x *1e9/ K_B)
print 'Y Freezing Temperature: %2.2f nK'%(HBAR * omega_y *1e9/ K_B)
print 'Z Freezing Temperature: %2.2f nK'%(HBAR * omega_z *1e9/ K_B)
dimension = 3
print 'Thermal Equivalent Frequency: %2.2f Hz'%(K_B*T/(HBAR*2*pi))
#Should thresholdbe higher, ie 10*K_B_T ??
if (HBAR*omega_x > K_B*T):
    print 'X motion is frozen'
    dimension -= 1
if (HBAR*omega_y > K_B*T):
    print 'Y motion is frozen'
    dimension -= 1
if (HBAR*omega_z > K_B*T):
    print 'Z motion is frozen'
    dimension -= 1
print 'Cloud Dimension: %d'%dimension
if dimension == 1:
    L = max([R_tf_x, R_tf_y, R_tf_z])
    x_tr = min([a_osc_x, a_osc_y, a_osc_z])
    x_lo = max([a_osc_x, a_osc_y, a_osc_z])
    omega_long = min([omega_x, omega_y, omega_z])
    n_1D = N / (2*L)
    print '1D Density: %2.2e atom/cm^3'%(n_1D*1e6)
#    T_Q_1D = (HBAR**2 * n_1D**2 / (M*K_B))
#    print 'Quantum Effects Temperature: %2.2f nK'%(T_Q_1D*1e9)
#    if T < T_Q_1D:
#        print 'Quantum Effects are Important'
#    phase_stdev = (M * K_B * T * L/ (2*pi*n_1D*HBAR**2))*0.5
#    print 'Phase Fluctuations: %2.2f rad'%phase_stdev
#    density_stdev = 
#    phase_corr_l = n_1D * HBAR**2 / (M*K_B*T)
#    print 'Phase Correlation Length: %2.2f um'%(phase_corr_l*1e6)
    g_1D = 2*HBAR**2*A / (M*x_tr**2)
    print '1D coupling strength: %e'%g_1D
    gamma_param = M*g_1D / (HBAR**2*n_1D)
    print 'Gamma, Coupling Parameter: %e'%gamma_param
    if gamma_param < 0.1:
        print 'Gas is weakly interacting'
    if gamma_param > 10:
        print 'Gas is strongly interacting'
    mu_1D = n_1D*g_1D
    print '1D Chemical Potential: %2.2f Hz'%(mu_1D / (2*pi*HBAR))
    spectrum_3 = min([f_x, f_y, f_z])*np.sqrt(0.5*l*(l+1))
    corr_length_1D = HBAR / (M*n_1D*g_1D)**0.5 #from petrov, prl 85 3745
    print '1D Correlation Length: %2.2f nm'%(corr_length_1D * 1e9)
    T_degen_1D = N*HBAR*omega_long / K_B
    print '1D Degeneracy Temperature: %2.2f uK'%(T_degen_1D*1e6)
#    alpha_1D = A * x_lo / x_tr**2
    alpha_1D = M*g_1D*x_lo / HBAR**2
    print 'Alpha, Size Parameter: %2.2e'%alpha_1D
    T_phase = T_degen_1D * HBAR * omega_long / mu_1D
    print 'Phase Freeze Temperature: %2.2f nK'%(T_phase*1e9)
    
    print '\n1D Thomas-Fermi T=0 Results' #from petrov
    print hbreak
    mu_1D_TF = HBAR * omega_long*(3.0*N*alpha_1D / (4*2**0.5))**(2.0/3)
    print '1D TF Chemical Potential: %2.2f Hz'%(mu_1D_TF / (2*pi*HBAR))
    R_1D_TF = (2*mu_1D_TF / (M*omega_long**2))**0.5
    print '1D TF Cloud Length: %2.2f um'%(R_1D_TF*1e6)
    max_n_1D_TF = mu_1D_TF / g_1D
    print '1D TF Max Density: %2.2e atom/cm^3'%(max_n_1D_TF*1e6)
    
    print '\n1D Weakly-Interacting Thomas-Fermi Finite T Results'
    print hbreak
    n_vac_fluc = max_n_1D_TF*(gamma_param**0.25)
    n_vac_fluc = 0 #don't trust paper, ignore
    print 'Density Vacuum Fluctuations: %e atom/cm^3'%(n_vac_fluc*1e6)
    n_th_fluc = (max_n_1D_TF**2 * T * min([K_B*T / mu_1D_TF, 1.0]) / T_degen_1D)**0.5
    print 'Density Thermal Fluctuations: %e atom/cm^3'%(n_th_fluc*1e6)
    n_fluc_tot = (n_vac_fluc**2 + n_th_fluc**2)**0.5
#    print 'Density SNR: %2.0f'%(max_n_1D_TF / n_fluc_tot) #what is signal really?
    ph_vac_fluc = ((gamma_param**0.5 / pi)*log(R_1D_TF / corr_length_1D))**0.5
    print 'Phase Vacuum Fluctuations: %2.2f rad'%ph_vac_fluc
    ph_th_fluc = (8*T*mu_1D_TF * abs(log((1 + 0.5*R_1D_TF) / (1 - 0.5*R_1D_TF)))/ (3*T_degen_1D * HBAR * omega_long))**0.5
    print 'Phase Thermal Fluctuations: %2.2e rad'%ph_th_fluc
    ph_fluc_tot = (ph_th_fluc**2 + ph_vac_fluc**2)**0.5
    print 'Phase Fluctuations: %2.2f rad'%ph_fluc_tot
    T_phase_petrov = T_degen_1D * HBAR * omega_long / mu_1D_TF
    print 'Phase Freeze Temperature: %2.2f nK'%(T_phase_petrov * 1e9)
    
    # 1D phase diagram, petrov
#    T_scaled_axis = np.array([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000])
    T_scaled_axis = np.logspace(0, 3)
#    N_axis = np.array([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000])
    T_degen_line = T_scaled_axis
    
    T_ph_prefactor = (32.0 / (9 * alpha_1D**2))**(1.0 / 3)
    T_ph_line = (T_scaled_axis / T_ph_prefactor)**3
    T_true_axis = HBAR*omega_long*T_scaled_axis / K_B #K
    
    plt.plot(T_true_axis*1e9, T_degen_line, 'k', T_true_axis*1e9, T_ph_line, 'k')
    plt.plot(T*1e9, N, 'bo')
    plt.ylim((1,100000))
    plt.xlim((1, 1000))
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('T / nK')
    plt.ylabel('N')
    plt.title('Petrov Phase Diagram')
    plt.show()
    
    #Which regime of degeneracy??
    print '\nPetrov Gas Classification'
    print hbreak
    if T < T_degen_1D:
        print 'Degenerate'
        if alpha_1D < 1:
            print 'Weakly Interacting'
            if T < T_phase_petrov:
                print 'True Condensate'
            else:
                print 'Quasicondensate'
        else:
            print 'Tonks Gas'
    else:
        print 'Thermal'
    
    print '\n1D Low Energy Excitations:'
    print hbreak
    for freq in spectrum_3:
        print '%2.2f Hz'%freq
if dimension == 2:
    area = R_tf_x * R_tf_y * R_tf_z / min([R_tf_x, R_tf_y, R_tf_z])
    T_Q_2D = (2*pi*HBAR**2*N / (M*K_B*area))
    if T < T_Q_2D:
        print 'Quantum Effects are Important'
        
#3-body losses
#L = 4e-30 #cm^6 / sec, constant for Rb87 from P&S Chp 5
#n_0 = n*1e-6 #atom/cm
#t = np.arange(0,10, 0.05)
#f = lambda n, t:-1*n**3
#soln = odeint(f, 1, t)
#soln_true = N * soln
#t_true = t / (L * n_0**2)
#plt.plot(t_true*1e3, soln_true)
#plt.xlabel('Time (ms)')
#plt.ylabel('Atom Number')
#plt.title('3 Body Losses')
#plt.show()