from image_filter import *

img = read_image("images/mona_with_noisy.jpg")
img = rgb_to_gray(img)
#save_image("save_test.jpg", img.copy())
#apply_negative("negative_test.jpg", img.copy())
#apply_logarithmic("log_test.jpg", img.copy())
#apply_gamma_correction("gamma_test.jpg", img.copy(), 1.5)
#draw_histogram("histogram_test.jpg", img.copy())
#apply_equalized_histogram("eq_test.jpg", img.copy())
apply_median(img.copy(), 7, "median2.jpg")
