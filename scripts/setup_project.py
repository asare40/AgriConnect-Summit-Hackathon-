import os
import json
import shutil
import pandas as pd
import numpy as np
from datetime import datetime

print("="*80)
print("NIGERIA POST-HARVEST LOSSES ANALYSIS PROJECT SETUP")
print("="*80)
print("\nSetting up project structure...\n")

# Create directory structure
directories = [
    'data/raw',        # Original data files
    'data/processed',  # Cleaned, validated data
    'data/final',      # Analysis-ready datasets
    'scripts',         # Analysis scripts
    'visualizations',  # Output visualizations
    'docs'             # Documentation
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")

# Create project configuration
config = {
    'project_name': 'Nigeria Post-Harvest Losses Analysis',
    'start_date': datetime.now().strftime('%Y-%m-%d'),
    'primary_focus': 'Post-Harvest Losses',
    'secondary_focus': 'Agricultural Finance',
    'datasets': {
        'post_harvest_losses': 'data/final/post_harvest_losses.csv',
        'value_chain': 'data/final/value_chain.csv',
        'financial_impact': 'data/final/financial_impact.csv',
        'nutrient_losses': 'data/final/nutrient_losses.csv',
        'climate_data': 'data/final/climate_data.csv'
    },
    'version': '1.0.0'
}

# Save project configuration
with open('project_config.json', 'w') as f:
    json.dump(config, f, indent=4)
print("Created project configuration: project_config.json")

# Create README file with project information
readme = """# Nigeria Post-Harvest Losses Analysis Project

## Project Overview
This project analyzes post-harvest losses in Nigerian agriculture with a focus on agricultural finance.

## Directory Structure
- `data/raw`: Original data files
- `data/processed`: Cleaned and validated data files
- `data/final`: Analysis-ready datasets
- `scripts`: Analysis and visualization scripts
- `visualizations`: Output visualizations
- `docs`: Project documentation

## Datasets
1. **Post-Harvest Losses**: Loss percentages by crop and region
2. **Value Chain**: Losses at different stages of the agricultural value chain
3. **Financial Impact**: Economic impact of post-harvest losses
4. **Nutrient Losses**: Nutritional impact of post-harvest losses
5. **Climate Data**: Climate data for contextual analysis

## Analysis Workflow
1. Data preparation using `prepare_datasets.py`
2. Basic data visualization using `create_visualizations.py`
3. Specialized analyses using specific scripts in the `scripts` directory

## Getting Started
1. Run `prepare_datasets.py` to set up the datasets
2. Run `create_visualizations.py` to generate basic visualizations
"""

with open('README.md', 'w') as f:
    f.write(readme)
print("Created project README file: README.md")

print("\nProject structure setup complete!")
print("Next step: Run prepare_datasets.py to create clean, analysis-ready datasets.")