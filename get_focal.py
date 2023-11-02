import math

camera_angle_x_radians = 0.6911112070083618
camera_angle_y_radians = 0.4710899591445923
image_width_pixels = 1920
image_height_pixels = 1080

f_x_pixels = image_width_pixels / (2 * math.tan(camera_angle_x_radians / 2))
f_y_pixels = image_height_pixels / (2 * math.tan(camera_angle_y_radians / 2))

focal_length = (f_x_pixels / image_width_pixels + f_y_pixels / image_height_pixels) / 2

print(f"Computed focal length: {focal_length}")
