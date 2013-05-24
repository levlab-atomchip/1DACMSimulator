"""
Classes for atoms and transitions
"""
from acmconstants import C, HBAR
from math import pi

class Atom():
	def __init__(self, name, Z, mass, N_nucleons, transitions):
		self.name = name
		self.Z = Z
		self.mass = mass
		self.N_nucleons = N_nucleons
		self.transitions = transitions
		
class Transition():
	def __init__(self, species, name, wavelength, gamma):
		self.species = species
		self.name = name
		self.wavelength = wavelength
		self.gamma = gamma
		
		self.k = 2 * pi / wavelength
		self.freq = C / wavelength
		self.omega = 2 * pi * freq