from ImageManager import ImageManager
class FilterManager(ImageManager):

    def __init__(self):
        super().__init__()

    def get_median(filter_size, i, j, data):
        filter_size = format_size(filter_size)
        mid_position = filter_size // 2
        neighbors = []
        for z in range(filter_size):
            if i + z - mid_position < 0 or i + z - mid_position > len(data) - 1:
                for c in range(filter_size):
                    neighbors.append(0)
            elif j + z - mid_position < 0 or j + mid_position > len(data[0]) - 1:
                neighbors.append(0)
            else:
                for k in range(filter_size):
                    neighbors.append(data[i + z - mid_position][j + k - mid_position])

        neighbors.sort()
        return neighbors[len(neighbors) // 2]

    def apply_median(img, filter_size, img_name):
        obtained, original = get_empty_image_with_same_dimensions(img)
        for i in range(len(original)):
            for j in range(len(original[0])):
                obtained[i][j] = get_median(filter_size,i,j,original)

        save_image(img_name, obtained.astype('uint8'))
        draw_histogram("hist_"+img_name,obtained)

    def apply_piecewise_linear(img_name, img, coordinates_x, coordinates_y):
        x = np.array(range(0, _max_pixel+1), dtype=np.uint8)
        interp = np.interp(x, coordinates_x, coordinates_y)
        obtained = img.copy()
        for i in range(obtained.shape[0]):
            for j in range(obtained.shape[1]):
                index = int(np.round(obtained[i][j]))
                obtained[i][j] = interp[index]
        draw_histogram(img_name, obtained)
        save_image(img_name, obtained)


f = FilterManager()
img = f.read_image("images/einstein.jpg")
img = f.rgb_to_gray(img)
#save_image("save_test.jpg", img.copy())
f.apply_negative("iamges/results/negative_test.jpg", img.copy())
#apply_logarithmic("log_test.jpg", img.copy())
#apply_gamma_correction("gamma_test.jpg", img.copy(), 1.5)
#draw_histogram("histogram_test.jpg", img.copy())
#apply_equalized_histogram("eq_test.jpg", img.copy())
#apply_median(img.copy(), -5, "median2.jpg")

# coordinates_x = np.array([0,10,11,13,14,255])
# coordinates_y = np.array([0,10,11,100,101,255])
# apply_piecewise_linear("piecewise_linear.jpg",img.copy(),coordinates_x,coordinates_y)