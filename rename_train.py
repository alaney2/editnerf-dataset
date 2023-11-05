import os

main_directory = "./plane_dataset"

for i in range(1, 41):  # This will cover plane1 to plane40
    train_dir_path = os.path.join(main_directory, f'plane{i}', 'train')
    
    if os.path.exists(train_dir_path) and os.path.isdir(train_dir_path):
        os.rename(train_dir_path, os.path.join(main_directory, f'plane{i}', 'images'))