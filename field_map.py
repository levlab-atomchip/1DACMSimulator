import pylab
import scipy
import parameters
import scipy.fftpack
import numpy as np
import CloudImage
import glob
import scipy.misc
from scipy.constants import hbar,pi,c

class field_map():
    def __init__(self, b_field = None, height = 10e-6, file_dir = ''):
        self.b_field = b_field
        self.height = height
        self.file_dir = file_dir
        self.image_files = []
        self.CloudImages = []
        self.getFiles()
        self.fillImages()
        
    def getFiles(self):
        self.image_files = glob.glob(self.file_dir + '/*.mat')
        return

    def fillImages(self):
        self.cloud_images = [CloudImage.CloudImage(i) 
                                for i in self.image_files]
        return

    def getVariableList(self):
        return [i.getVariableValues(i.getVariablesFile(),'Variables.m') 
                    for i in self.cloud_images]

    def checkSet(self):
        #return true if all images in field_map have same variables.m file
        var_list = self.getVariableList()
        return all(i == var_list[0] for i in var_list) 

    def fillField(self):
        #Right now we just return a dictionary, when we know the 
        #control parameters we can organize this in a 2D array
        field_dict = {}
        for i in self.cloud_images:
            field_dict[i.getContParam()] = i.getBField()
        return field_dict

    def filterFunction(self,k_x,k_y,
                       c_x = 0.32e6,
                       c_y=0.22e6,
                       s_x=0.05e6,
                       s_y = 0.05e-6):
        return (1+scipy.exp((k_x-c_x)/s_x))*(1+scipy.exp((k_y-c_y)/s_y))

    def getJ(self):
        bfield = self.fillField()

        bimg = scipy.misc.imread('/Users/Pants/Desktop/Play Time/bfield.png',
                                 flatten=True)
        bfield = bimg/bimg.max() *300e-9
        
        #k_x1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[1], self.cloud_images[0].c1) ## k-grid
        #k_y1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[0], self.cloud_images[0].c1)
        #k_x,k_y = np.meshgrid(k_x1[0][:],k_y1[0][:])

        k_x1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[1], 1e-6) ## k-grid
        k_y1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[0], 1e-6)
        k_x,k_y = np.meshgrid(k_x1,k_y1)
        
        B_k = scipy.fftpack.fft2(bfield)
        B_k = 1.0/self.filterFunction(k_x,k_y) * B_k

        x = scipy.linspace(0,bfield.shape[1]*1e-6,bfield.shape[1])
        y = scipy.linspace(0,bfield.shape[0]*1e-6,bfield.shape[0])
        x,y = scipy.meshgrid(x,y)
        r_x = self.height/(x**2+self.height**2+y**2)**(1.5)
        r_k = scipy.fftpack.fft2(r_x)

        #r_k = 1.0/r_k
        ###########
        #r_k/=scipy.absolute(r_k).max()
        #B_k/=scipy.absolute(B_k).max()
        eky = scipy.exp((k_x**2+k_y**2)**(0.5)*self.height)
        eky/=scipy.absolute(eky).max()
        ###########
        #j = scipy.fftpack.ifft2(B_k * scipy.exp((k_x**2+k_y**2)**(0.5)*self.height))
        j =4*pi/(4*pi*10**-7)* scipy.fftpack.ifft2(B_k *1./r_k)
        
        pylab.figure(1)
        pylab.imshow(bfield)

        pylab.figure(2)
        pylab.subplot(2,1,1)
        pylab.imshow(scipy.real(j))
        pylab.subplot(2,1,2)
        pylab.imshow(scipy.imag(j))

        pylab.figure(3)
        pylab.subplot(3,1,1)
        pylab.pcolormesh(scipy.real(j))
        pylab.subplot(3,1,2)
        pylab.pcolormesh(scipy.fftpack.fftshift(scipy.absolute(1./r_k)))
        pylab.subplot(3,1,3)
        pylab.pcolormesh(scipy.fftpack.fftshift(scipy.absolute(eky)))
        return j,r_x,r_k,eky,B_k
        #return [r_k, k_x,k_y]
        #return self.filterFunction(k_x,k_y)
        #return [k_x,k_y]
        #return scipy.fftpack.ifft(B_k)
