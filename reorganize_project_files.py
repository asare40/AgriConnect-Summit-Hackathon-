import os
import shutil
import re
from pathlib import Path
import sys

# Define the correct project structure based on our outline
PROJECT_STRUCTURE = {
    'data': {
        'raw': {},
        'processed': {},
        'analysis': {}
    },
    'scripts': {},
    'results': {
        'plots': {},
        'interventions': {
            'regional': {},
            'economic': {},
            'risks': {},
            'stakeholders': {}
        },
        'youth_opportunities': {},
        'dashboard': {}
    },
    'documentation': {
        'executive_summaries': {},
        'technical_reports': {},
        'implementation_guides': {}
    },
    'final_deliverables': {}
}

def create_directory_structure(base_path, structure):
    """Create the directory structure defined in the structure dict."""
    for dir_name, sub_dirs in structure.items():
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
        
        # Create subdirectories recursively
        if sub_dirs:
            create_directory_structure(dir_path, sub_dirs)

def categorize_file(filename):
    """Determine which folder a file belongs to based on its name and content."""
    
    # Common naming patterns for different file types
    patterns = {
        # Data files
        r'.*raw.*\.(csv|xlsx|json|txt)$': 'data/raw',
        r'.*processed.*\.(csv|xlsx|json|txt)$': 'data/processed',
        r'.*analysis.*\.(csv|xlsx|json|txt)$': 'data/analysis',
        
        # Python scripts
        r'.*\.(py)$': 'scripts',
        
        # Plot files and visualizations
        r'.*\.(png|jpg|jpeg|svg)$': 'results/plots',
        r'.*chart.*\.(png|jpg|jpeg|svg)$': 'results/plots',
        r'.*plot.*\.(png|jpg|jpeg|svg)$': 'results/plots',
        r'.*visualization.*\.(png|jpg|jpeg|svg)$': 'results/plots',
        
        # Intervention files
        r'.*intervention.*\.(csv|xlsx|json|txt|md)$': 'results/interventions',
        r'.*regional.*\.(csv|xlsx|json|txt|md)$': 'results/interventions/regional',
        r'.*economic.*\.(csv|xlsx|json|txt|md)$': 'results/interventions/economic',
        r'.*risk.*\.(csv|xlsx|json|txt|md)$': 'results/interventions/risks',
        r'.*stakeholder.*\.(csv|xlsx|json|txt|md)$': 'results/interventions/stakeholders',
        
        # Youth opportunity files
        r'.*youth.*\.(csv|xlsx|json|txt|md)$': 'results/youth_opportunities',
        r'.*business.*model.*\.(csv|xlsx|json|txt|md)$': 'results/youth_opportunities',
        r'.*skill.*\.(csv|xlsx|json|txt|md)$': 'results/youth_opportunities',
        
        # Dashboard files
        r'.*dashboard.*\.(html|css|js|csv|json)$': 'results/dashboard',
        r'.*map.*\.(html|csv|json|geojson)$': 'results/dashboard',
        
        # Documentation files
        r'.*executive.*summary.*\.(md|docx|pdf|txt)$': 'documentation/executive_summaries',
        r'.*technical.*\.(md|docx|pdf|txt)$': 'documentation/technical_reports',
        r'.*implementation.*guide.*\.(md|docx|pdf|txt)$': 'documentation/implementation_guides',
        r'.*manual.*\.(md|docx|pdf|txt)$': 'documentation/implementation_guides',
        
        # Final deliverables
        r'.*final.*\.(md|docx|pdf|txt|json)$': 'final_deliverables',
        r'.*submission.*\.(md|docx|pdf|txt|json)$': 'final_deliverables',
        r'.*proposal.*\.(md|docx|pdf|txt|json)$': 'final_deliverables'
    }
    
    # Check if the filename matches any patterns
    for pattern, folder in patterns.items():
        if re.match(pattern, filename.lower()):
            return folder
    
    # For files that don't match any pattern
    return None

def move_file(src, dest_folder, project_root):
    """Move a file to the appropriate destination folder."""
    dest_path = os.path.join(project_root, dest_folder, os.path.basename(src))
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    try:
        # Handle duplicate files by adding a suffix
        if os.path.exists(dest_path):
            base, extension = os.path.splitext(dest_path)
            counter = 1
            while os.path.exists(f"{base}_{counter}{extension}"):
                counter += 1
            dest_path = f"{base}_{counter}{extension}"
        
        # Move the file
        shutil.move(src, dest_path)
        print(f"Moved: {src} → {dest_path}")
        return True
    except Exception as e:
        print(f"Error moving {src}: {str(e)}")
        return False

def cleanup_empty_directories(directory):
    """Recursively remove empty directories."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if os.path.exists(dir_path) and not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
            except Exception as e:
                print(f"Error removing directory {dir_path}: {str(e)}")

def reorganize_project(project_root):
    """Main function to reorganize the project structure."""
    print(f"Starting project reorganization at: {project_root}")
    
    # Create the correct directory structure
    create_directory_structure(project_root, PROJECT_STRUCTURE)
    
    # Find all files in the project
    all_files = []
    for root, dirs, files in os.walk(project_root):
        # Skip the .git directory if it exists
        if '.git' in dirs:
            dirs.remove('.git')
        
        # Skip venv or virtual environment directories
        dirs_to_remove = [d for d in dirs if d == 'venv' or d == 'env' or d.startswith('.')]
        for d in dirs_to_remove:
            dirs.remove(d)
            
        for file in files:
            # Skip this script itself and any system files
            if file == os.path.basename(__file__) or file.startswith('.'):
                continue
            all_files.append(os.path.join(root, file))
    
    # Move files to their correct locations
    for file_path in all_files:
        rel_path = os.path.relpath(file_path, project_root)
        
        # Skip files already in the correct location
        correct_location = False
        for base_dir in PROJECT_STRUCTURE.keys():
            if rel_path.startswith(base_dir + os.sep):
                correct_location = True
                break
        
        if not correct_location:
            target_folder = categorize_file(os.path.basename(file_path))
            if target_folder:
                move_file(file_path, target_folder, project_root)
            else:
                print(f"Uncategorized file: {file_path}")
    
    # Cleanup empty directories
    cleanup_empty_directories(project_root)
    
    print("\nProject reorganization completed!")
    print(f"All files have been organized according to the structure defined in the project outline.")

if __name__ == "__main__":
    # Use current directory if no argument is provided
    project_root = os.getcwd()
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    
    if not os.path.isdir(project_root):
        print(f"Error: {project_root} is not a valid directory.")
        sys.exit(1)
    
    print(f"This script will reorganize files in: {project_root}")
    confirmation = input("Continue? (y/n): ")
    if confirmation.lower() != 'y':
        print("Operation cancelled.")
        sys.exit(0)
    
    reorganize_project(project_root)
    
    print("\nFile Structure Summary:")
    for root, dirs, files in os.walk(project_root):
        level = root.replace(project_root, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")