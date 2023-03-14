import os

directory_name = "my_directory"
directory_path = os.path.join("D:", directory_name)

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory '{directory_name}' created successfully!")
else:
    print(f"Directory '{directory_name}' already exists.")