import gdown

# Download the folder from Google Drive
folder_url = "#"
gdown.download_folder(folder_url, output="./model_files", quiet=False)

# Verify the safetensors file
from safetensors.torch import load_file

file_path = "./model_files/model.safetensors"  # Path to the file

try:
    weights = load_file(file_path)
    print("The file is valid! Keys:", weights.keys())
except Exception as e:
    print("Failed to load the file:")
    print(e)
