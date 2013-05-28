#!/usr/bin/python

import scipy
import parameters_KrisB
import scipy.fftpack
import pylab

from scipy.constants import pi,hbar

class ssft():
    def __init__(self, lx,steps = 1001):
        self.p = parameters_KrisB.tp_parameters()
        self.p.N = 1e5
        # computational cell
        self.lx = lx
        self.steps = steps
        self.x,self.dx = scipy.linspace(-self.lx/2.,self.lx/2.,self.steps,endpoint=False,retstep=True)
        self.dk =  2*pi/self.lx
        self.k = 2*pi*scipy.fftpack.fftfreq(len(self.x), self.dx) ## k-grid

    def flat_psi(self):
        return self.Normalize(scipy.ones(self.x.shape))
    def rand_psi(self):
        return self.Normalize(scipy.rand(self.x.shape[0]))

    def Normalize(self,psi):
        ## Normalize the wavefunction to 1 in real space
        return (self.p.N/((scipy.absolute(psi)**2).sum()*self.dx))**.5*psi
    def Normalize_k(self,psi_k):
        ## Normalize the wavefunction to 1 in momentum space
        return (1./((scipy.absolute(psi_k)**2).sum()*self.dk))**.5*psi_k


    def interaction(self,psi):
        return 4*pi*hbar**2*self.p.a1d*2**.5/(self.p.m)*scipy.absolute(psi)**2

    def ssft(self, potential, dt=-.1j*50e-6,max_its = 10000, start_psi = None, precision= 1e-8):
        self.dt = dt
        ## kinetic energy part
        self.T = hbar**2*self.k**2/(2*self.p.m)
        self.exp_T =  scipy.exp(-1j*self.dt/(2.*hbar)*self.T)
        self.exp_2T =  scipy.exp(-1j*self.dt/(hbar)*self.T)

        if start_psi == None:
        ## Initialize psi to TF-solution
            psi = self.rand_psi()
        else:
            psi = self.Normalize(start_psi)
        
        psi_old = scipy.array(psi)
        exp_prefactor = -1j*self.dt/hbar
        

        psik = scipy.fftpack.fft(psi)
        psik *= self.exp_T
        psi = scipy.fftpack.ifft(psik)
        for i in scipy.arange(max_its):
#            print i
            if scipy.iscomplex(self.dt):
                psi = self.Normalize(psi)
            psi *= scipy.exp(exp_prefactor*(potential+self.interaction(psi)))
            psik = scipy.fftpack.fft(psi)
            psik *= self.exp_2T
            psi = scipy.fftpack.ifft(psik)
            if precision != None:
                if ((scipy.absolute(psi-psi_old)/scipy.absolute(psi)).sum() < precision)*(i>50):
                    break
                else:
                    psi_old = psi
        if scipy.iscomplex(self.dt):
            psi = self.Normalize(psi)
        psi *= scipy.exp(-1j*self.dt/hbar*(potential+self.interaction(psi)))
        psik = scipy.fftpack.fft(psi)
        psik *= self.exp_T
        psi = scipy.fftpack.ifft(psik)
        if (i == max_its-1)*(precision != None):
            print 'warning: algorithm did not converge!'
        return self.Normalize(psi)


        
if __name__ == '__main__':
    p = parameters.tp_parameters()
    N = 201
    omega = 2*pi*100

    isft = ssft(lx=25e-6,steps=N)

    potential = .5*isft.p.m*omega**2*isft.x**2
    pylab.plot(potential)
    
    psi = isft.ssft(potential = potential,dt=-.1j*50e-6,start_psi=isft.flat_psi())


    pylab.plot(isft.x*1e6,scipy.absolute(psi)**2,'r',lw=4)
    pylab.xlabel('position x ($\\mu$m)')
    pylab.ylabel('density')
    pylab.show()
