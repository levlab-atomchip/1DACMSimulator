import scipy
import parameters
import time
import scipy.weave
import multiprocessing
import math
from scipy.constants import pi

class wire():
    def __init__(self, j = None, length = None, width = None, dx = None):
        self.j = j #let j be a 3D array with [:,:,0] = j_x , [:,:,1] = j_y,
        self.length = length
        self.width = width
        self.dx = dx
        self.p = parameters.bfield_parameters()

    def oneWire(self,I,current_width,current_direction):
        self.j = scipy.zeros([scipy.floor(self.length/self.dx),scipy.floor(self.width/self.dx),2])
        if current_direction == 'x':
            midpoint = scipy.floor(self.width/self.dx/2)
            self.j[:,midpoint - scipy.floor(current_width/self.dx/2):midpoint + scipy.floor(current_width/self.dx/2),0] = I/(current_width*self.length)
        elif current_direction == 'y':
            self.j[scipy.floor(self.length/self.dx/2) - scipy.floor(current_width/self.dx/2):scipy.floor(self.length/self.dx/2) + scipy.floor(current_width/self.dx/2),:,1] = I/(current_width*self.width)
        else:
            print('Specify a real direction for your onewire!')
        return

    def gaussian(self,maxVal,midPoint,stdDev,x):
        output = [maxVal*scipy.exp(-(i-midPoint)**2/(2*stdDev**2)) for i in x]
        return output

    def gaussianWire(self,I,current_width,current_direction):
        self.j = scipy.zeros([scipy.floor(self.length/self.dx),scipy.floor(self.width/self.dx),2])
        if current_direction == 'x':
            midpoint = self.width/2
            g_line = self.gaussian(I,midpoint,current_width,scipy.arange(scipy.floor(self.width/self.dx))*self.dx)
            for i in scipy.arange(scipy.floor(self.length/self.dx)):
                self.j[i,:,0] = g_line
        elif current_direction == 'y':
            midpoint = scipy.floor(self.length/self.dx/2)
            g_line = self.gaussian(I,midpoint,current_width,scipy.arange(scipy.floor(self.length/self.dx)))
            for i in scipy.arange(scipy.floor(self.width/self.dx)):
                self.j[:,i,1] = g_line
        else:
            print('Specify a real direction for your onewire!')
        return
        

    def fillGrating(self, I, current_width, grating_spacing, current_direction):
        #x is the length direction
        self.j = scipy.zeros([scipy.floor(self.length/self.dx),scipy.floor(self.width/self.dx),2])
        if current_direction =='x':
            n_grating = scipy.floor(self.width/(grating_spacing+current_width))
            for i in scipy.arange(n_grating):
                self.j[:,i*scipy.floor((current_width + grating_spacing)/self.dx):i*scipy.floor((current_width + grating_spacing)/self.dx)+scipy.floor(current_width/self.dx),0] = I/(current_width*self.length*n_grating)
        elif current_direction =='y':
            n_grating = scipy.floor(self.length/(grating_spacing+current_width))
            for i in scipy.arange(n_grating):
                self.j[i:i+scipy.floor(grating_spacing/self.dx),:,1] = I/(current_width*self.width*n_grating)
        else:
            print('Specify a real direction for fillGrating!')
        return

    def biotSavart(self, position):
        B = [0,0,pi]
        B_x = 0
        B_y = 0
        B_z = 0
        prefactor = self.p.mu_0/(4*pi)*self.dx*self.dx
        x_prime = scipy.linspace(-self.length/2.,self.length/2.,self.length/self.dx,endpoint = False)
        y_prime = scipy.linspace(-self.width/2.,self.width/2.,self.width/self.dx,endpoint = False)

        #remove points with j = 0
        y_grid,x_grid = scipy.meshgrid(y_prime,x_prime)
        j_x = self.j[:,:,0]
        j_y = self.j[:,:,1]
        jx_index = scipy.nonzero(j_x)
        jy_index = scipy.nonzero(j_y)

        if scipy.size(jy_index) == 0 and scipy.size(jx_index) != 0:
            denomx = (((x_grid[jx_index]-position[0])**2 + (y_grid[jx_index] - position[1])**2 + position[2]**2)**(3.0/2))
            B_y = sum(-1.0*j_x[jx_index]*position[2]/denomx)
            B_z = sum((j_x[jx_index]*(position[1]-y_grid[jx_index]))/denomx)
        elif scipy.size(jx_index) == 0 and scipy.size(jy_index) != 0:
            denomy = (((x_grid[jy_index]-position[0])**2 + (y_grid[jy_index] - position[1])**2 + position[2]**2)**(3.0/2))
            B_x = sum(j_y[jy_index]*position[2]/denomy)
            B_z = -1.0*sum(j_y[jy_index] * (position[0]-x_grid[jy_index])/denomy)
        else:
            denomx = (((x_grid[jx_index]-position[0])**2 + (y_grid[jx_index] - position[1])**2 + position[2]**2)**(3.0/2))
            denomy = (((x_grid[jy_index]-position[0])**2 + (y_grid[jy_index] - position[1])**2 + position[2]**2)**(3.0/2))
            B_x = sum(j_y[jy_index]*position[2]/denomy)
            B_y = sum(-1.0*j_x[jx_index]*position[2]/denomx)
            B_z = sum((j_x[jx_index]*(position[1]-y_grid[jx_index]))/denomx) - sum(j_y[jy_index] * (position[0]-x_grid[jy_index])/denomy)
        
        B = [prefactor*B_x,prefactor* B_y,prefactor*B_z]
        return B

    def fieldMap(self,height,length = 0, width = 0):
        x = scipy.linspace(-length/2.,length/2.,length/self.dx,endpoint = False)
        y = scipy.linspace(-width/2.,width/2.,width/self.dx,endpoint = False)
        bx_field = scipy.zeros([length/self.dx,width/self.dx])
        by_field = scipy.zeros([length/self.dx,width/self.dx])
        bz_field = scipy.zeros([length/self.dx,width/self.dx])
        for i in scipy.arange(scipy.size(x)):
            p = [[x[i],j,height] for j in y]
            B = scipy.array(map(self.biotSavart,p))
            bx_field[i,:] = B[:,0]
            by_field[i,:] = B[:,1]
            bz_field[i,:] = B[:,2]

        return [bx_field,by_field,bz_field]

    def mp_fieldMap(self,height,length = 0, width = 0,nprocs = 4):
        x = scipy.linspace(-length/2.,length/2.,length/self.dx,endpoint = False)
        y = scipy.linspace(-width/2.,width/2.,width/self.dx,endpoint = False)
        plist = []
        for i in x:
            for j in y:
                plist.append(tuple([i,j,height]))
        nums = tuple(plist)
        
        def worker(nums, out_q):
            outdict = {}
            for n in nums:
                outdict[n] = self.biotSavart(n)
            out_q.put(outdict)

        out_q = multiprocessing.Queue()
        chunksize = int(math.ceil(len(nums)/float(nprocs)))
        procs = []

        for i in range(nprocs):
            p = multiprocessing.Process(target = worker, args=(nums[chunksize * i:chunksize * (i+1)],out_q))
            procs.append(p)
            p.start()

        result_dict = {}

        for i in range(nprocs):
            result_dict.update(out_q.get())

        for p in procs:
            p.join()


        b_x = scipy.zeros([scipy.size(x),scipy.size(y)])
        b_y = scipy.zeros([scipy.size(x),scipy.size(y)])
        b_z = scipy.zeros([scipy.size(x),scipy.size(y)])
        for i in scipy.arange(scipy.size(x)):
            for j in scipy.arange(scipy.size(y)):
                b_x[i,j] = result_dict[(x[i],y[j],height)][0]
                b_y[i,j] = result_dict[(x[i],y[j],height)][1]
                b_z[i,j] = result_dict[(x[i],y[j],height)][2]
        
        return [b_x, b_y, b_z]

    
    def benchmark(self,length,width,dx, n_loop = 1):
        
        self.gaussianWire(1.0,10e-6,'x')
        print('to the loops')
        print('mp_fieldMap:')
        for i in range(3):
            t1 = time.time()
            self.mp_fieldMap(1e-6,self.length,self.width)
            t2 = time.time()
            print(t2-t1)

        print('fieldMap:')
        for i in range(3):
            t1 = time.time()
            self.fieldMap(1e-6, self.length,self.width)
            t2 = time.time()
            print(t2-t1)

        return
