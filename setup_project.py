import os

# Define project folder structure
project_root = os.getcwd()  # Use current working directory
folders = ["scripts", "config", "logs", "tests"]

# Create project folders
for folder in folders:
    path = os.path.join(project_root, folder)
    os.makedirs(path, exist_ok=True)

# Create placeholder files
placeholder_files = {
    "README.md": "## Automation Project\n\nAutomations for managing NAS and systems.",
    "config/streamdeck_config.json": "{}",
    "config/settings.json": "{}",
    "logs/.gitkeep": ""  # Keep the logs directory in version control
}

for filename, content in placeholder_files.items():
    filepath = os.path.join(project_root, filename)
    with open(filepath, "w") as f:
        f.write(content)

print(f"Automation project setup complete at {project_root}.")
