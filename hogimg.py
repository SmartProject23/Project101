import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import exposure
from skimage import io, color

# Load an example image
image_path = 'resources/YangeTest.jpg'
image = io.imread(image_path)

# Convert the image to grayscale if it's not already
if image.ndim == 3:
    image = color.rgb2gray(image)

# Compute HOG features
# `visualize=True` creates a visualization of the HOG features
# `block_norm` can be set to 'L2-Hys' for improved normalization
features, hog_image = hog(image, visualize=True, block_norm='L2-Hys')

# Enhance the contrast of the HOG image for visualization
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

# Display the original image and the HOG visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex=True, sharey=True)

ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input Image')

ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('HOG Visualization')
plt.show()

