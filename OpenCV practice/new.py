# import cv2

# # Load an image (replace with your own path if needed)
# img = cv2.imread('img.jpg')

# # Check if the image loaded correctly
# if img is not None:
#     cv2.imshow("Test Image", img)
#     cv2.waitKey(0)  # Waits until you press a key
#     cv2.destroyAllWindows()
# else:
#     print("Image not found or path is incorrect.")

import numpy as np

grid = np.zeros((10, 10))
grid[5, 5] = 1  # start infection at center

for _ in range(10):  # 10 time steps
    infected = np.where(grid == 1)
    for i, j in zip(*infected):
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 10 and 0 <= nj < 10 and grid[ni, nj] == 0:
                if np.random.rand() < 0.3:  # 30% infection chance
                    grid[ni, nj] = 1
print(grid)
