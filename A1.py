import numpy as np

# Step 1: Camera calibration matrix
camera_matrix = np.array([
    [961.461004058896, 0, 618.9908302325701],
    [0, 964.8013393433856, 342.0805337054228],
    [0, 0, 1]
])

# Calibration image resolution
calib_width, calib_height = 1280, 720   

# Test image resolution (Rubik's cube image)
test_width, test_height = 2220, 1480    

# Step 2: Rescale intrinsic matrix
scale_x = test_width / calib_width
scale_y = test_height / calib_height

# Adjust focal lengths and principal point coordinates
camera_matrix[0, 0] *= scale_x   # fx
camera_matrix[0, 2] *= scale_x   # cx
camera_matrix[1, 1] *= scale_y   # fy
camera_matrix[1, 2] *= scale_y   # cy

print("Updated camera matrix:\n", camera_matrix)

# Step 3: Clicked points (from lab/class)
P1 = (974, 958)   # First point (x1, y1)
P2 = (1241, 959)  # Second point (x2, y2)

# Distance from camera to object (cm)
Z = 34.0

# Step 4: Pixel differences
dx_pixels = abs(P2[0] - P1[0])
dy_pixels = abs(P2[1] - P1[1])

# Extract intrinsics for scaling
fx, fy = camera_matrix[0, 0], camera_matrix[1, 1]

# Step 5: Convert to world coordinates
dx_world = (dx_pixels * Z) / fx
dy_world = (dy_pixels * Z) / fy
diagonal_distance = np.sqrt(dx_world**2 + dy_world**2)

# Step 6: Print results in clear format
print("Camera Dimension Measurement:")
print(f"Clicked Points: P1={P1}, P2={P2}")
print(f"Z = {Z:.2f} cm")
print(f"Δx_pixels = {dx_pixels}, Δy_pixels = {dy_pixels}\n")

print(f"ΔX_world = {dx_world:.4f} cm")
print(f"ΔY_world = {dy_world:.4f} cm")
print(f"Diagonal distance = {diagonal_distance:.4f} cm\n")
