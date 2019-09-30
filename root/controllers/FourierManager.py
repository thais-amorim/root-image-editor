    
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




f  = FourierManager()

img = f.read_image("./images/photography.jpg")
img = np.around( f.rgb_to_gray(img))





# x = [0,1,2,3,4,5,6,7,8,9,10]
x = np.random.rand(5,10)
# print(x)
# print(x[0::2][0::2][0::2][0::2])
# print(x[1::2])
# print(x[0:2])

# n = x.shape[0]
# e = math.ceil(abs(cmath.log(n,2)))
# print(e)
# print(2**e)
# v = np.zeros(2**e)
# v[:x.shape[0]] = x
# print(v)


# obt = f.fft(x)
# expected = np.fft.fft(x)
# print(expected)
# print("------")
# print(obt)

# print(np.allclose(obt,expected))

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




















# h,w = img.shape
# for i in range (h):
#     print(np.allclose(f.fft(img[i,:]), np.fft.fft(img[i,:])))
    

# x = np.random.random(1024)
# f  = FourierManager()
# print(np.allclose(f.fft(x), np.fft.fft(x)))

# img = f.read_image("./images/photography.jpg")
# img = f.rgb_to_gray(img)
# print(np.fft.fft2(img))
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print(f.fft2(img))

