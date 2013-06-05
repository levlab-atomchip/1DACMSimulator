import pylab
import scipy
import parameters
import scipy.fftpack
import numpy as np
import CloudImage
import glob
import scipy.misc
from scipy.constants import hbar,pi,c

class FieldMap():
    def __init__(self, b_field = None, height = 10, file_dir = ''):
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
                       c_x = 0.0,
                       c_y=0.0,
                       s_x=0.05,
                       s_y = 0.05):
        return (1+scipy.exp((k_x-c_x)/s_x))*(1+scipy.exp((k_y-c_y)/s_y))
#        return 1

    def getJ(self):
#        bfield = self.fillField()

        bimg = scipy.misc.imread('wildermuth_B.png',
                                 flatten=True)
        jimg = scipy.misc.imread('wildermuth_J.png',
                                 flatten=True)
        bmax = bimg.max()
        bmin = bimg.min()
        bfield = (bimg - bmin)/(bmax - bmin) *350
        jmin = jimg.min()
        jmax = jimg.max()
        jfield = ((jimg - jmin) / (jmax - jmin) - 0.25) * 200
        #k_x1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[1], self.cloud_images[0].c1) ## k-grid
        #k_y1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[0], self.cloud_images[0].c1)
        #k_x,k_y = np.meshgrid(k_x1[0][:],k_y1[0][:])

        k_x1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[1], 1) ## k-grid
        k_y1 = 2*pi*scipy.fftpack.fftfreq(bfield.shape[0], 1)
        k_x,k_y = np.meshgrid(k_x1,k_y1)
        k = np.sqrt(k_x**2 + k_y**2)
        
        B_k = scipy.fftpack.fft2(bfield)
#        B_k = scipy.fftpack.fftshift(B_k)
        B_k = 1.0 / self.filterFunction(k_x,k_y) * B_k
#        B_k = scipy.fftpack.ifftshift(B_k)

#        x = scipy.linspace(0,bfield.shape[1]*1,bfield.shape[1])
#        y = scipy.linspace(0,bfield.shape[0]*1,bfield.shape[0])
#        x,y = scipy.meshgrid(x,y)
#        r_x = self.height/(x**2+self.height**2+y**2)**(1.5)
#        r_k = scipy.fftpack.fft2(r_x)

        #r_k = 1.0/r_k
        ###########
        #r_k/=scipy.absolute(r_k).max()
        #B_k/=scipy.absolute(B_k).max()
#        eky = scipy.exp((k_x**2+k_y**2)**(0.5)*self.height)
#        eky/=scipy.absolute(eky).max()
        ###########
        #j = scipy.fftpack.ifft2(B_k * scipy.exp((k_x**2+k_y**2)**(0.5)*self.height))
#        j =4*pi/(4*pi*10**-7)* scipy.fftpack.ifft2(B_k *1./r_k)
#        J = scipy.fftpack.ifft2(B_k * np.exp(k * self.height))
#        print 'size B_k: '
#        print B_k.shape
#        print 'size k:'
#        print k.shape
#        print B_k
#        print np.exp(k)
#        print k
        J = 1e-8*scipy.fftpack.ifft2(B_k * np.exp(k * self.height))
#        J = scipy.fftpack.fftshift(J)

        
#        pylab.figure(1)
#        pylab.imshow(bfield)
#        pylab.show()
#
        pylab.figure(2)
        pylab.subplot(3,1,1)
        pylab.imshow(bfield)
        pylab.colorbar()
        pylab.subplot(3,1,2)
        pylab.imshow(jfield)
        pylab.colorbar()
        pylab.subplot(3,1,3)
        imgplt = pylab.imshow(scipy.absolute(J))
        pylab.colorbar()
        imgplt.set_clim(0.0, 0.25*np.max(scipy.absolute(J)))
        pylab.show()
#
#        pylab.figure(3)
#        pylab.subplot(3,1,1)
#        pylab.pcolormesh(scipy.real(J))
#        pylab.subplot(3,1,2)
#        pylab.pcolormesh(scipy.fftpack.fftshift(scipy.absolute(1./r_k)))
#        pylab.subplot(3,1,3)
#        pylab.pcolormesh(scipy.fftpack.fftshift(scipy.absolute(eky)))
#        return J,r_x,r_k,eky,B_k
        return J
        #return [r_k, k_x,k_y]
        #return self.filterFunction(k_x,k_y)
        #return [k_x,k_y]
        #return scipy.fftpack.ifft(B_k)

if __name__ == '__main__':
    test_field_map = FieldMap()
    test_field_map.getJ()