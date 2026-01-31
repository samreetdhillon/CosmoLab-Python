import os

# Define the structure
folders = [
    "notebooks",
    "src",
    "data",
    "assets/diagrams",
    "tests"
]

files = {
    "notebooks/01_Expansion_and_Metrics.ipynb": "",
    "notebooks/02_Friedmann_Solver.ipynb": "",
    "notebooks/03_Distance_Ladder.ipynb": "",
    "notebooks/04_Linear_Perturbations.ipynb": "",
    "src/__init__.py": "",
    "src/physics_engine.py": "# Core physics functions\n",
    "src/solvers.py": "# ODE integration logic\n",
    "data/supernova_data.csv": "z,mb,dmb\n",  # Header for mock data
    "tests/test_physics.py": "import unittest\n",
    "requirements.txt": "",
    "README.md": "# Cosmology Pedagogy Series\nInteractive notebooks for modern cosmology.",
    ".gitignore": "*.pyc\n.ipynb_checkpoints/\n__pycache__/\nvirtual_env/"
}

def create_repo():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Created file: {filepath}")

if __name__ == "__main__":
    create_repo()
    print("\n✅ Repository structure generated successfully!")