import kagglehub

# Download latest version
path = kagglehub.dataset_download("asisheriberto/music-classification-wav")

print("Path to dataset files:", path)
