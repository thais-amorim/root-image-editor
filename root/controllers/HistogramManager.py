from ImageManager import ImageManager
class HistogramManager(ImageManager): 

    def __init__(self):
        super().__init__()

    def draw_histogram(img_name, img):
        data = img.flatten()
        plt.hist(data, _max_pixel+1, [0,256])
        plt.savefig(_images_path + img_name)
        plt.close()

    def apply_equalized_histogram(img_name, img):
        # Getting the pixel values of the image
        original = np.array(img)
        # Creating a new matrix for the image
        equalized_img = np.copy(original)
        # Getting unique pixels and frequency of the values from the image
        unique_pixels, pixels_frequency = np.unique(original, return_counts=True)
        # Image pixels divided by the size of the image
        pk = pixels_frequency/img.size
        pk_length = len(pk)
        # Getting the cummulative frequency of the unique pixel values
        sk = np.cumsum(pk)
        # Multiplying the cummulative frequency by the maximum value of the pixels
        mul = sk*np.max(original)
        roundVal = np.round(mul)
        # Mapping the pixels for the equalization
        for i in range(len(original)):
            for j in range(len(original[0])):
                equalized_img[i][j] = roundVal[np.where(unique_pixels == original[i][j])]

        save_image(img_name, equalized_img.astype('uint8'))
        draw_histogram("hist_"+img_name,equalized_img)


draw_histogram(img_name, obtained)
save_image(img_name, obtained)
 