# GenAI Project 
## Models 
``` plaintext
Last Update Models :
12/16/2024 
Model : Model-LoRA-4-20241216T110523Z-001
----------------------------------------------------
```

## Problem
If you encounter an error while loading the `safetensors` file (e.g., **`Failed to load the file`**), the issue may arise due to:

1. **Incomplete download:** The file may not have been fully downloaded.
2. **Corruption during transfer:** The file may have been corrupted while downloading or uploading.
3. **Incorrect file structure:** Ensure all necessary files for the model are present in the folder.

# Solution

### 1. Verify file size
Check the file size after downloading and compare it with the original size on Google Drive. If it’s smaller, re-download the file.

```bash
ls -lh ./model_files/model.safetensors
```
### 2. Re-download the file

 Re-download the file
 ``` python
import gdown

folder_url = "#"
gdown.download_folder(folder_url, output="./model_files", quiet=False)
```
### 3. Check required files
``` plaintext
Ensure the following files are in the ./model_files directory:

model.safetensors (or pytorch_model.bin)
config.json
Tokenizer files:
tokenizer.json
special_tokens_map.json
```


