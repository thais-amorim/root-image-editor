    
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

    # def fft(self,x):
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
        t = []
        N = len(x)
        for k in range(N):
            a = 0
            for n in range(N):
                a += x[n]*cmath.exp(-2j*cmath.pi*k*n*(1/N))
            t.append(a)
        return t

    def omega(self,n, m):
        return cmath.exp((2j * cmath.pi * m) / n)

    def fft2(self,img):
        h,w = img.shape
        print(h)
        print(w)
        f = np.zeros((h,w),dtype=np.complex)
        print(f[:,0].shape)
        for i in range (h):
            f[i,:] = np.fft.fft(img[i,:])
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


f  = FourierManager()

img = f.read_image("./images/photography.jpg")
img = np.around( f.rgb_to_gray(img))







x = img
obt = f.fft2(x)
expected = np.fft.fft2(x)

# print(expected)
# print("------")
# print(obt)
print("Teste fft")
print(np.allclose(obt,expected))

# obt = f.fft2(img)
# expected = np.fft.fft2(img)
print("Teste fft2")
print(np.allclose(obt,expected))


shift = np.fft.fftshift(obt)
shift2 = f.fftshift(obt)
# print(obt)
# print("------")
# print(shift)
# print("------")
# print(shift2)
print("Teste shift")
print(np.allclose(shift,shift2))



ishift = f.ifftshift(shift2)
print('Test ishift')
print(np.allclose(obt,ishift))



y = np.random.rand(10)
y = f.fft(y)
obt2 = f.ifft(y)
expected2 = np.fft.ifft(y)

# print(obt2)
# print("------")
# print(expected2)

print("Teste ifft")
print(np.allclose(obt2,expected2))


obt = f.ifftshift(shift)

obt2 = f.ifft2(obt)
expected = np.fft.ifft2(obt)
print("Teste ifft2")
print(np.allclose(obt2,expected))

import matplotlib.pyplot as plt
plt.imshow(obt2,cmap='gray')
plt.show()

