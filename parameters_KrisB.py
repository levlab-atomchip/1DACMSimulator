#!/usr/bin/python

## class providing all the parameters of the experiment
## computes some usefull quantities out of them
## Kris B. inspired by Ferdl B., 25.7.2009


#### !!!!!!!!!!!!!!!!!!!
# to change:
# g0m and U0m
#### !!!!!!!!!!!!!!!!!!!




try:
    from enthought.traits.api import HasTraits, Float, Property
except:
    from traits.api import HasTraits, Float, Property
import scipy

# some constants
from scipy.constants import hbar,pi,c
from scipy.constants import epsilon_0 as epsilon0
#pi = scipy.pi
#hbar = 1.05457266912510e-34
#c = 299792458
#epsilon0 = 8.85e-12

class parameters(HasTraits):

    # general variables
    m = Float(1.44316060e-25) #atomic mass
    a0 = Float(5.4505231e-9) #scatterering length

    # experimental parameters
    g0p1 = Float(8.92814442456*2*pi*1e6) # single atom coupling strength sigma-plus
    g0p2 = Float(14.1166358303*2*pi*1e6) # single atom coupling strength sigma-plus


    g0m = Float(2*pi*11e6) # single atom coupling strength sigma-minus
    kappa = Float(1.3*2*pi*1e6) # cavity decay
#    waist = Float(26e-6)# ??


    freq_d2 = Float(2*pi*384.2304844685e12) # freq of D2 line
    freq_d1 = Float(2*pi*377.107463380e12) # freq of D1 line

    d1p = Float(1.46325985261e-29) # dipole matrix element for d1 line
    d2p = Float(2.31361697147e-29) # dipole matrix element for d2 line


    wx = Float(2 * pi * 252) #dipole trap frequencies: cavity axis
    wy = Float(2 * pi * 48) #dipole trap frequencies: dipole trap axis
    wz = Float(2 * pi * 238) #dipole trap frequencies: vertical axis

    w_trans_y = Float(53e-6) #y-waist of transportbeam
    w_trans_x = Float(29e-6) #x-waist of transportbeam

    w_c = Float(25e-6) # cavity mode waist
    



    # experiment (or run) specific variables
    N = Float(100000,desc='atom number')
    lambda780 = Float(c/382.13476e12) # guess what that would be
    lambda830 = Float(c/360.8640e12)# guess what that would be




    DeltaA2 = Property( depends_on = ['lambda780','freq_d2'], cached=True ,desc='atom probe detuning to D2')
    def _get_DeltaA2(self):
        return c/self.lambda780*2*pi-self.freq_d2

    DeltaA = Property( depends_on = ['DeltaA'], cached=True ,desc='atom probe detuning to D2')
    def _get_DeltaA(self):
        return self.DeltaA2

    DeltaA1 = Property( depends_on = ['lambda780','freq_d1'], cached=True ,desc='atom probe detuning to D1')
    def _get_DeltaA1(self):
        return c/self.lambda780*2*pi-self.freq_d1


    U0p = Property( depends_on = ['g0p1','g0p2','DeltaA1','DeltaA2'], cached=True ,desc='780nm lattice depth per photon (frequency)')
    def _get_U0p(self):
        return self.g0p1**2/self.DeltaA1 + self.g0p2**2/self.DeltaA2
#        return self.g0p**2/self.DeltaA
    
    
    U0m = Property( depends_on = ['g0m','DeltaA'], cached=True ,desc='780nm lattice depth per photon (frequency)' )
    def _get_U0m(self):
        # add the d1 line!!!!!!!!!
        return self.g0m**2/self.DeltaA
    

    gp = Property( depends_on = ['U0p','N'], cached=True, desc='optomechanical coupling strength')
    def _get_gp(self):
        return self.U0p*scipy.sqrt(self.N/8)

    gm = Property( depends_on = ['U0m','N'], cached=True, desc='optomechanical coupling strength')
    def _get_gm(self):
        return self.U0m*scipy.sqrt(self.N/8)


    #cavity lattice 780

    k780 = Property( depends_on = ['lambda780'], cached=True, desc='')
    def _get_k780(self):
        return 2*pi/self.lambda780


    Erec780 = Property( depends_on = ['k780','m'], cached=True, desc='')
    def _get_Erec780(self):
        return (hbar*self.k780)**2/(2*self.m)


    wrec780 = Property( depends_on = ['Erec780'], cached=True, desc='')
    def _get_wrec780(self):
        return self.Erec780/hbar


    G780 = Property( depends_on = ['k780'], cached=True, desc='')
    def _get_G780(self):
        return 2*self.k780 



    #cavity lattice 830

    k830 = Property( depends_on = ['lambda830'], cached=True, desc='')
    def _get_k830(self):
        return 2*pi/self.lambda830


    Erec830 = Property( depends_on = ['k830','m'], cached=True, desc='')
    def _get_Erec830(self):
        return (hbar*self.k830)**2/(2*self.m)


    wrec830 = Property( depends_on = ['Erec830'], cached=True, desc='')
    def _get_wrec830(self):
        return self.Erec830/hbar


    G830 = Property( depends_on = ['k830'], cached=True, desc='')
    def _get_G830(self):
        return 2*self.k830 



    # some stuff for GPE and Thomas Fermi

    dx = Float(500e-9) # spatial stepsize for thomas fermi solution (x-direction)
    dy = Float(1000e-9) # spatial stepsize for thomas fermi solution (y-direction)
    dz = Float(500e-9) # spatial stepsize for thomas fermi solution (z-direction)

    lx = Float(13e-6) # size of grid for thomas fermi solution (x-direction)
    ly = Float(40e-6) # size of grid for thomas fermi solution (x-direction)
    lz = Float(13e-6) # size of grid for thomas fermi solution (x-direction)


    x_1d = Property( depends_on = ['lx','dx'], cached=True ,desc='x grid')
    def _get_x_1d(self):
        return scipy.mgrid[-self.lx/2:self.lx/2:self.dx]

    grid_3d = Property( depends_on = ['dx','dy','dz','lx','ly','lz'], cached=True ,desc='grid')
    def _get_grid_3d(self):
        return scipy.mgrid[-self.lx/2:self.lx/2:self.dx,-self.ly/2:self.ly/2:self.dy,-self.lz/2:self.lz/2:self.dz]


    x_3d = Property( depends_on = ['grid_3d'], cached=True ,desc='x grid')
    def _get_x_3d(self):
        return self.grid_3d[0,:,:,:]

    y_3d = Property( depends_on = ['grid_3d'], cached=True ,desc='y grid')
    def _get_y_3d(self):
        return self.grid_3d[1,:,:,:]
    z_3d = Property( depends_on = ['grid_3d'], cached=True ,desc='z grid')
    def _get_z_3d(self):
        return self.grid_3d[2,:,:,:]

    mean_tf_density = Property( depends_on = ['N'], cached=True, desc='mean Thomas-Fermi density. Only valid for our trap parameters!!!!!!!!')
    def _get_mean_tf_density(self):
        return 1.36586508e+18*self.N**(2./5.)



    wbar = Property( depends_on = ['wx','wy','wz'], cached=True, desc='')
    def _get_wbar(self):
        return (self.wx*self.wy*self.wz)**(1/3.)


    abar = Property( depends_on = ['m','wbar'], cached=True, desc='')
    def _get_abar(self):
        return (hbar/(self.m*self.wbar))**.5


    mu = Property( depends_on = ['N','a0','abar','wbar'], cached=True, desc='')
    def _get_mu(self):
        return 15**(2./5.)/2.*(self.N*self.a0/self.abar)**(2./5.)*hbar*self.wbar


    Rx = Property( depends_on = ['mu','m','wx'], cached=True, desc='Thomas Fermi radius')
    def _get_Rx(self):
        return (2*self.mu/(self.m*self.wx**2))**.5

    Ry = Property( depends_on = ['mu','m','wy'], cached=True, desc='Thomas Fermi radius')
    def _get_Ry(self):
        return (2*self.mu/(self.m*self.wy**2))**.5

    Rz = Property( depends_on = ['mu','m','wz'], cached=True, desc='Thomas Fermi radius')
    def _get_Rz(self):
        return (2*self.mu/(self.m*self.wz**2))**.5

    def harm_pot_3d(self,x=None,y=None,z=None):
        if x == None:
            x = self.x_3d
        if y == None:
            y = self.y_3d
        if z == None:
            z = self.z_3d
        return self.m/2.*(self.wx**2*x**2+self.wy**2*y**2+self.wz**2*z**2)

    def psiTF_3d(self,x=None,y=None,z=None):
        if x == None:
            x = self.x_3d
        if y == None:
            y = self.y_3d
        if z == None:
            z = self.z_3d
        interaction = 4*pi*hbar**2*self.a0/self.m
        return (scipy.maximum(0,(self.mu-self.harm_pot_3d(x,y,z))/interaction))**.5

    a1d = Property( depends_on = ['N','a0','abar','wbar','m','wx'], cached=True, desc='')
    def _get_a1d(self):
        return ((15*self.N*self.a0/self.abar)**(2/5.)*hbar*self.wbar/2)**(3/2.)*(2*self.m)**.5/(3*self.wx*hbar**2*pi*self.N)


    a2d = Property( depends_on = ['N','m','wx','wz','a0','wbar','m'], cached=True, desc='')
    def _get_a2d(self):
        return 5**(4./5.)*(self.a0*self.N/self.abar)**(4./5.)*self.wbar**2/(2*3**(1./5.)*self.N*pi*self.wx*self.wz)
    mu2d = Property( depends_on = ['m','N','wx','wz','a0'], cached=True, desc='')
    def _get_mu2d(self):
        return self.m*(self.N*3*pi*self.wx*self.wz/(2*pi))**.5/(4*hbar*self.a0**.5)



    # is per definition the same as self.mu
#    mu1d = Property( depends_on = ['m','wx','a1d'], cached=True, desc='')
#    def _get_mu1d(self):
#        return (3/(2*self.m)**.5*self.wx*hbar**2*pi*self.N*self.a1d)**(2/3.)
    def harm_pot_1d(self,x=None, w = None):
        if x == None:
            x = self.x_1d
        if w == None:
            w = self.wx
        return self.m/2.*self.wx**2*x**2

    def psiTF_1d(self,x=None, w = None):
        if x == None:
            x = self.x_1d
        if w == None:
            w = self.wx
        interaction = 4*pi*hbar**2*self.a1d/self.m
        return (scipy.maximum(0,(self.mu-self.harm_pot_1d(x,w))/interaction))**.5


class tp_parameters(parameters):
    DeltaC = Float(0)

    def mode_func_cavity_3d(self,x,y,z):
        return scipy.exp(-2.*(y**2+z**2)/self.w_c**2)

    def mode_func_pump_3d(self,x,y,z):
        return scipy.exp(-2.*x**2/self.w_trans_x**2)*scipy.exp(-2.*y**2/self.w_trans_y**2)

    
    def Oc(self,x=None,y=None,z=None):
        if x == None:
            x = self.x_3d
            dx = self.dx
        else:
            dx = x[1]-x[0]
        if y == None:
            y = self.y_3d
            dy = self.dy
        else:
            dy = y[1]-y[0]
        if z == None:
            z = self.z_3d
            dz = self.dz
        else:
            dz = z[1]-z[0]

        return (scipy.absolute(self.psiTF_3d(x,y,z))**2/self.N*self.mode_func_cavity_3d(x,y,z)).sum()*dx*dy*dz

    def Ocp(self,x=None,y=None,z=None):
        if x == None:
            x = self.x_3d
            dx = self.dx
        else:
            dx = x[1]-x[0]
        if y == None:
            y = self.y_3d
            dy = self.dy
        else:
            dy = y[1]-y[0]
        if z == None:
            z = self.z_3d
            dz = self.dz
        else:
            dz = z[1]-z[0]

        return (scipy.absolute(self.psiTF_3d(x,y,z))**2/self.N*self.mode_func_cavity_3d(x,y,z)*self.mode_func_pump_3d(x,y,z)).sum()*dx*dy*dz


    def test(self):
        pot = lambda x,y,z: self.m/2.*(self.wx**2*x**2+self.wy**2*y**2+self.wz**2*z**2)
        u0 = 4*pi*hbar**2*self.a0/self.m
        TF = lambda x,y,z: scipy.maximum(self.mu-pot(x,y,z)/u0,0)
        import mpmath
        print 'hi'
        print mpmath.quad(TF,[-self.Rx,self.Rx],[-self.Ry,self.Ry],[-self.Rz,self.Rz])
        



if __name__ == '__main__':
    import scipy
    import pylab
    
    a = tp_parameters()
    res = [[],[],[]]
    for i in scipy.arange(500e-9,20000e-9,500e-9):
        print i
        a.dy = i

        res[0] += [i]
        res[1] += [a.Oc()]
        res[2] += [a.Ocp()]


    res = scipy.array(res)


    pylab.plot(res[0]*1e9,res[1],'x',label='Oc')
    pylab.plot(res[0]*1e9,res[2],'x',label='Ocp')

    pylab.legend()
    pylab.show()
