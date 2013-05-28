# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:13:50 2013

@author: Will
"""

from acmconstants import MU_B, HBAR
from math import sqrt
import matplotlib.pylab as plt

class Slower():
    pass

class ZeemanSlower(Slower):
    pass

class ChirpedSlower(Slower):
    pass
	
class BasicZS(ZeemanSlower):
	def __init__(self, B_0, z_0, omega, I, atom):
		self.B_0 = B_0
		self.z_0 = z_0
		self.omega = omega
		self.I = I
		self.atom = atom
		self.mu_prime = (self.atom.g_e * self.atom.M_e - self.atom.g_g * self.atom.M_g) * MU_B
	def get_v_0(self):
		# mu_prime = (self.atom.g_e * self.atom.M_e - self.atom.g_g * self.atom.M_g) * MU_B
		k = self.atom.k
		self.v_0 = self.mu_prime * self.B_0 / (HBAR * k)
		return self.v_0
	def tune_B_0(self, v_0):
		# mu_prime = (self.atom.g_e * self.atom.M_e - self.atom.g_g * self.atom.M_g) * MU_B
		k = self.atom.k
		self.B_0 = HBAR * k * v_0 / self.mu_prime
	def get_eta(self):
		v_0 = self.get_v_0()
		k = self.atom.k
		gamma = self.atom.gamma
		M = self.atom.M
		self.eta = M * v_0**2 / (self.z_0 * HBAR * k * gamma)
		return self.eta
	def get_vss(self, z):
		delta = self.omega - self.atom.omega
		gamma = self.atom.gamma
		s_0 = self.I / self.atom.I_sat
		eta = self.get_eta()
		k = self.atom.k
		v_0 = self.get_v_0()
		
		v_ss_prime = (delta - 0.5 * gamma * sqrt(s_0 * (1 - eta) / eta - 1)) / k
		v_r = v_0 * sqrt( 1 - z / self.z_0)
		return v_ss_prime + v_r
	def plot_vss(self, window):
		vss = [self.get_vss(z) for z in window.window]
		plt.plot(window.window, vss)
		plt.xlabel('Position')
		plt.ylabel('Steady-State Velocity')
		plt.title('Steady-State Velocity Profile')
		plt.show()
	def get_damping(self):
		omega_r = self.atom.omega_r
		eta = self.get_eta()
		s_0 = self.I / self.atom.I_sat
		return (4 * omega_r * eta**2) * sqrt((1 - eta) * s_0 / eta - 1) / s_0
	def get_accel(self, z):
		eta = self.get_eta()
		delta = self.omega - self.atom.omega
		zbar = 1 - z / self.z_0
		a_max = HBAR * self.atom.k * self.atom.gamma / (2 * self.atom.M)
		return -1 * eta * a_max * (1 + (1 - (HBAR * delta / (self.mu_prime * self.B_0)) / sqrt(zbar)))
	def plot_accel(self, window):
		accel = [self.get_accel(z) for z in window.window]
		plt.plot(window.window, accel)
		plt.xlabel('Position')
		plt.ylabel('Acceleration')
		plt.title('Acceleration Profile')
		plt.show()
		
		
		