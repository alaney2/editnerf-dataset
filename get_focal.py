import math
import json


# camera_angle_x_radians = 0.6911112070083618
# camera_angle_y_radians = 0.4710899591445923
# image_width_pixels = 1920
# image_height_pixels = 1080

# f_x_pixels = image_width_pixels / (2 * math.tan(camera_angle_x_radians / 2))
# f_y_pixels = image_height_pixels / (2 * math.tan(camera_angle_y_radians / 2))

# focal_length = (f_x_pixels / image_width_pixels + f_y_pixels / image_height_pixels) / 2

# print(f"Computed focal length: {focal_length}")

path = './plane_dataset/plane1'

with open(f'{path}/transforms_train.json', 'r') as file:
    parsed_data = json.load(file)

camera_angle_x_radians = parsed_data["camera_angle_x"]
camera_angle_y_radians = parsed_data["camera_angle_y"]
image_width_pixels = parsed_data["w"]
image_height_pixels = parsed_data["h"]

f_x_pixels = image_width_pixels / (2 * math.tan(camera_angle_x_radians / 2))
f_y_pixels = image_height_pixels / (2 * math.tan(camera_angle_y_radians / 2))

focal_length = (f_x_pixels / image_width_pixels + f_y_pixels / image_height_pixels) / 2

print(f"Computed focal length: {focal_length}")
