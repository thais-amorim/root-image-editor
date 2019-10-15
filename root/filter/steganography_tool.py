from PIL import Image 

class SteganographyTool():

    # Convert encoding data into 8-bit binary 
    # form using ASCII value of characters 
    @staticmethod
    def genData(data): 
            
            # list of binary codes 
            # of given data 
            newd = []  
            
            for i in data: 
                newd.append(format(ord(i), '08b')) 
            return newd 
            
    # Pixels are modified according to the 
    # 8-bit binary data and finally returned 
    @staticmethod
    def modPix(pix, data): 
        
        datalist = SteganographyTool.genData(data) 
        lendata = len(datalist) 
        imdata = iter(pix) 
    
        for i in range(lendata): 
            
            # Extracting 3 pixels at a time 
            pix = [value for value in imdata.__next__()[:3] +
                                    imdata.__next__()[:3] +
                                    imdata.__next__()[:3]] 
                                        
            # Pixel value should be made  
            # odd for 1 and even for 0 
            for j in range(0, 8): 
                if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
                    
                    if (pix[j]% 2 != 0): 
                        pix[j] -= 1
                        
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
                    pix[j] -= 1
                    
            # Eigh^th pixel of every set tells  
            # whether to stop ot read further. 
            # 0 means keep reading; 1 means the 
            # message is over. 
            if (i == lendata - 1): 
                if (pix[-1] % 2 == 0): 
                    pix[-1] -= 1
            else: 
                if (pix[-1] % 2 != 0): 
                    pix[-1] -= 1
    
            pix = tuple(pix) 
            yield pix[0:3] 
            yield pix[3:6] 
            yield pix[6:9] 
    @staticmethod
    def encode_enc(newimg, data): 
        w = newimg.size[0]
        print(newimg.getdata())
        (x, y) = (0, 0) 
        
        for pixel in SteganographyTool.modPix(newimg.getdata(), data): 
            
            # Putting modified pixels in the new image 
            newimg.putpixel((x, y), pixel) 
            if (x == w - 1): 
                x = 0
                y += 1
            else: 
                x += 1
                
    # Encode data into image 
    @staticmethod
    def encode(name, data): 
        # img = input("Enter image name(with extension): ") 
        image = Image.open(name, 'r') 
        
        # data = input("Enter data to be encoded: ") 
        if (len(data) == 0): 
            raise ValueError('Texto está vazio.') 
            
        newimg = image.copy() 
        SteganographyTool.encode_enc(newimg, data) 
        
        # new_img_name = input("Enter the name of new image(with extension): ")
        # newimg.save(new_img_name, 'bmp') 
        return newimg
    
    # Decode the data in the image 
    @staticmethod
    def decode(name): 
        # img = input("Enter image name(with extension): ") 
        image = Image.open(name, 'r') 
        
        data = '' 
        imgdata = iter(image.getdata()) 
        
        while (True): 
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]] 
            # string of binary data 
            binstr = '' 
            
            for i in pixels[:8]: 
                if (i % 2 == 0): 
                    binstr += '0'
                else: 
                    binstr += '1'
                    
            data += chr(int(binstr, 2)) 
            if (pixels[-1] % 2 != 0): 
                return data 
                
    # # Main Function         
    # def main(): 
    #     a = int(input(":: Welcome to Steganography ::\n"
    #                         "1. Encode\n2. Decode\n")) 
    #     if (a == 1): 
    #         encode() 
            
    #     elif (a == 2): 
    #         print("Decoded word - " + decode()) 
    #     else: 
    #         raise Exception("Enter correct input") 
            
    # # Driver Code 
    # if name == '__main__' : 
        
    #     # Calling main function 
    #     main()