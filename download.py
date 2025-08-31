import kagglehub

# Download latest version
path = kagglehub.dataset_download("koluit/human-resource-data-set-the-company")

print("Path to dataset files:", path)