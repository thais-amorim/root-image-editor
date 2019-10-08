    
from ImageManager import ImageManager
import numpy as np
import cmath
import math
_max_pixel = 255
_images_path = 'images/'
from cmath import exp, pi

class  FourierManager(ImageManager):

    def __init__(self):
        super().__init__()

    # def transform_radix2(self,x,bol):
    #     n = len(x)
    #     if n == 1:
    #         return x
    #     even = self.fft(x[0::2])
    #     odd = self.fft(x[1::2])
    #     combined = np.zeros(n,dtype=np.complex)
    #     for m in range(n//2):
    #         combined[m] = even[m] + self.omega(n, -m) * odd[m]
    #         combined[m + n//2] = even[m] - self.omega(n, -m) * odd[m]
    #     return combined

    ##Isso é dft na verdade
    def fft(self, x):
        return self.transform(x,False)
        # t = []
        # N = len(x)
        # for k in range(N):
        #     a = 0
        #     for n in range(N):
        #         a += x[n]*cmath.exp(-2j*cmath.pi*k*n*(1/N))
        #     t.append(a)
        # return t

    def omega(self,n, m):
        return cmath.exp((2j * cmath.pi * m) / n)

    def fft2(self,img):
        h,w = img.shape
        print(h)
        print(w)
        f = np.zeros((h,w),dtype=np.complex)
        print(f[:,0].shape)
        for i in range (h):
            f[i,:] = self.fft(img[i,:])
        f1 = np.rot90(f)
        f2 = np.zeros(f1.shape,dtype=np.complex)
        for i in range (w):
            f2[i,:] = self.fft(f1[i,:])
        f3 = np.rot90(f2,3)
        return f3

    def fftshift(self,F):
        ''' this shifts the centre of FFT of images/2-d signals'''
        
        M, N = F.shape
        # med_m = M//2 + M%2
        # med_n = N//2 + N%2

        
        # R1, R2 = F[0: M//2, 0: N//2], F[M//2: M, 0: N//2]
        # R3, R4 = F[0: M//2, N//2: N], F[M//2: M, N//2: N]

        # sF = np.zeros(F.shape,dtype = F.dtype)
        # sF[med_m: M, med_n: N], sF[0: med_m, 0: med_n] = R1, R4
        # sF[med_m: M, 0: med_n], sF[0: med_m, med_n: N]= R3, R2
        sF = np.roll(F,M//2,axis=0)
        sF = np.roll(sF,N//2,axis=1)
        return sF

    def ifftshift(self,F):
        ''' this shifts the centre of FFT of images/2-d signals'''
        
        M, N = F.shape
        # med_m = M//2 + M%2
        # med_n = N//2 + N%2

        
        # R1, R2 = F[0: M//2, 0: N//2], F[M//2: M, 0: N//2]
        # R3, R4 = F[0: M//2, N//2: N], F[M//2: M, N//2: N]

        # sF = np.zeros(F.shape,dtype = F.dtype)
        # sF[med_m: M, med_n: N], sF[0: med_m, 0: med_n] = R1, R4
        # sF[med_m: M, 0: med_n], sF[0: med_m, med_n: N]= R3, R2
        sF = np.roll(F,-(N//2),axis=1)
        sF = np.roll(sF,-(M//2),axis=0)

        return sF


    def ifft(self,fu):
        """ use recursive method to speed up"""
        fu = np.asarray(fu, dtype=complex)
        fu_conjugate = np.conjugate(fu)

        fx = self.fft(fu_conjugate)

        fx = np.conjugate(fx)
        fx = fx / fu.shape[0]

        return fx

    def ifft2(self,fu):
        h, w = fu.shape

        fx = np.zeros(fu.shape, dtype=complex)

        if len(fu.shape) == 2:
            for i in range(h):
                fx[i, :] = self.ifft(fu[i, :])

            for i in range(w):
                fx[:, i] = self.ifft(fx[:, i])

        elif len(fu.shape) == 3:
            for ch in range(3):
                fx[:, :, ch] = self.ifft(fu[:, :, ch])

        fx = np.real(fx)
        return fx


    def create_circular_mask(self,h, w, center=None, radius=None):

        if center is None: # use the middle of the image
            center = [int(w/2), int(h/2)]
        if radius is None: # use the smallest distance between the center and image walls
            radius = min(center[0], center[1], w-center[0], h-center[1])

        Y, X = np.ogrid[:h, :w]
        dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

        mask = dist_from_center <= radius
        return mask

    def lowPassFilter(self,img,radius):
        h,w = img.shape
        mask = self.create_circular_mask(h,w,None,radius)
        print(mask)
        masked_img = img.copy()
        masked_img[~mask] = 0
        return masked_img

    def highPassFilter(self,img,radius):
        h,w = img.shape
        mask = self.create_circular_mask(h,w,None,radius)
        print(mask)
        masked_img = img.copy()
        masked_img[mask] = 0
        return masked_img

    def bandPassFilter(self,img,radius_minor,radius_major):
        h,w = img.shape
        mask_minor = self.create_circular_mask(h,w,None,radius_minor)
        mask_major = self.create_circular_mask(h,w,None,radius_major)
        masked_img = img.copy()
        masked_img[~mask_major] = 0
        masked_img[mask_minor] = 0
        return masked_img

    import cmath, sys
    if sys.version_info.major == 2:
        range = xrange

    def convolve(self,x, y, realoutput=True):
        assert len(x) == len(y)
        n = len(x)
        x = self.transform(x, False)
        y = self.transform(y, False)
        for i in range(n):
            x[i] *= y[i]
        x = self.transform(x, True)
        
        # Scaling (because this FFT implementation omits it) and postprocessing
        if realoutput:
            return [(val.real / n) for val in x]
        else:
            return [(val / n) for val in x]

    def transform_radix2(self,vector, inverse):
        # Returns the integer whose value is the reverse of the lowest 'bits' bits of the integer 'x'.
        def reverse(x, bits):
            y = 0
            for i in range(bits):
                y = (y << 1) | (x & 1)
                x >>= 1
            return y
        
        # Initialization
        n = len(vector)
        levels = n.bit_length() - 1
        if 2**levels != n:
            raise ValueError("Length is not a power of 2")
        # Now, levels = log2(n)
        coef = (2 if inverse else -2) * cmath.pi / n
        exptable = [cmath.rect(1, i * coef) for i in range(n // 2)]
        vector = [vector[reverse(i, levels)] for i in range(n)]  # Copy with bit-reversed permutation
        
        # Radix-2 decimation-in-time FFT
        size = 2
        while size <= n:
            halfsize = size // 2
            tablestep = n // size
            for i in range(0, n, size):
                k = 0
                for j in range(i, i + halfsize):
                    temp = vector[j + halfsize] * exptable[k]
                    vector[j + halfsize] = vector[j] - temp
                    vector[j] += temp
                    k += tablestep
            size *= 2
        return vector

    def transform(self,vector, inverse):
        n = len(vector)
        if n == 0:
            return []
        elif n & (n - 1) == 0:  # Is power of 2
            return self.transform_radix2(vector, inverse)
        else:  # More complicated algorithm for arbitrary sizes
            return self.transform_bluestein(vector, inverse)

    def transform_bluestein(self,vector, inverse):
        # Find a power-of-2 convolution length m such that m >= n * 2 + 1
        n = len(vector)
        if n == 0:
            return []
        m = 2**((n * 2).bit_length())
        
        coef = (1 if inverse else -1) * cmath.pi / n
        exptable = [cmath.rect(1, (i * i % (n * 2)) * coef) for i in range(n)]  # Trigonometric table
        a = [(x * y) for (x, y) in zip(vector, exptable)] + [0] * (m - n)  # Temporary vectors and preprocessing
        b = exptable[ : n] + [0] * (m - (n * 2 - 1)) + exptable[ : 0 : -1]
        b = [x.conjugate() for x in b]
        c = self.convolve(a, b, False)[ : n]  # Convolution
        return [(x * y) for (x, y) in zip(c, exptable)]  # Postprocessing


f  = FourierManager()

img = f.read_image("./images/DFT_no_log.jpg")
img = f.rgb_to_gray(img)







# x = img
# # obt = f.fft2(x)
# # expected = np.fft.fft2(x)

# x = np.random.rand(256)
# # y = np.zeros(16)
# # y[6:] = x

# obt = np.fft.fft(x)
# expected = f.transform_bluestein(x,False)

# # print(np.fft.fft(x))
# # print("-------d")
# # print(f.transform_bluestein(x,False))
# print(np.allclose(obt,expected))

# print(expected)
# print("------")
# print(obt)


# print("Teste fft")
# print(np.allclose(obt,expected))

# # obt = f.fft2(img)
# # expected = np.fft.fft2(img)
# print("Teste fft2")
# print(np.allclose(obt,expected))


# shift = np.fft.fftshift(obt)
# shift2 = f.fftshift(obt)
# # print(obt)
# # print("------")
# # print(shift)
# # print("------")
# # print(shift2)
# print("Teste shift")
# print(np.allclose(shift,shift2))



# ishift = f.ifftshift(shift2)
# print('Test ishift')
# print(np.allclose(obt,ishift))



# y = np.random.rand(10)
# y = f.fft(y)
# obt2 = f.ifft(y)
# expected2 = np.fft.ifft(y)

# # print(obt2)
# # print("------")
# # print(expected2)

# print("Teste ifft")
# print(np.allclose(obt2,expected2))


# obt = f.ifftshift(shift)

# obt2 = f.ifft2(obt)
# expected = np.fft.ifft2(obt)
# print("Teste ifft2")
# print(np.allclose(obt2,expected))



# img = np.real(shift)


# img = np.interp(img, (img.min(), img.max()), (np.amin(img),np.amax(img)))

# print('img')
# print(img)
# ft = np.fft.fft2(img)
# print('fft2')
# print(ft)
# shift= np.fft.fftshift(ft)

# print('fftshift')
# print(shift)
# mag = abs(shift)
# print('real')
# print(mag)


# ret = abs(np.fft.ifft2(ft))
# print('ret')
# print(ret)













import matplotlib.pyplot as plt
import matplotlib as mpl
# n = mpl.colors.Normalize(vmin=-0,vmax=255)
import math 

img = np.random.rand(500,500)

ft = f.fft2(img)

# ft = np.fft.fft2(img)

print(np.allclose(ft,np.fft.fft2(img)))

# shift = f.fftshift(ft)

# mag = abs(shift)

# mag = np.log(mag)
# vmin = np.min(mag)
# vmax = np.max(mag)

# mag = f.bandPassFilter(mag,40,100)

# shift = f.bandPassFilter(shift,40,100)
# ishift = f.ifftshift(shift)
# p_img = abs(f.ifft2(ishift))

# plt.imshow(mag, cmap='gray',norm=plt.Normalize(vmin=vmin, vmax=vmax))
# plt.show()



# plt.subplot(121)
# plt.imshow(img, cmap='gray')
# plt.subplot(122)
# plt.imshow(p_img, cmap='gray')
# plt.show()
