from pathlib import Path

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
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("Project files created successfully.")