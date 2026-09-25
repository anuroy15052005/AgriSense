import os

folders = [
    "backend",
    "frontend",
    "models",
    "data",
    "notebooks"
]
files = [
    "backend/main.py",
    "backend/prediction.py",
    "backend/schemas.py",
    "frontend/index.html",
    "frontend/style.css",
    "frontend/script.js",
    "models/.gitkeep",
    "data/.gitkeep",
    "notebooks/.gitkeep",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
for file in files:
    with open(file, "w", encoding="utf-8") as f:
        pass

print("Project files created successfully.")