import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Print working directory to help with debugging path issues
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Create output directory with absolute path
output_dir = os.path.join(current_dir, "results", "plots")
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory created: {output_dir}")

# Post-harvest loss rates by crop type
post_harvest_loss_rates = {
    'Maize': 30.5,
    'Rice': 35.0,
    'Sorghum': 25.8,
    'Millet': 22.4
}

# Create the plot
plt.figure(figsize=(10, 6))

# Create bar chart
crops = list(post_harvest_loss_rates.keys())
rates = list(post_harvest_loss_rates.values())

bars = plt.bar(
    crops,
    rates,
    color=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']  # Distinct colors for each crop
)

# Add title and labels
plt.title('Average Post-Harvest Losses by Crop Type in Nigeria', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('Loss Percentage (%)', fontsize=14)
plt.ylim(0, max(rates) * 1.2)  # Add space above bars

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,
        height + 0.5,
        f'{height:.1f}%',
        ha='center',
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# Save the file with absolute path
output_file = os.path.join(output_dir, "post_harvest_losses.png")
plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.close()

# Verify the file was saved
if os.path.exists(output_file):
    print(f"SUCCESS: Plot saved to {output_file}")
    print(f"File size: {os.path.getsize(output_file) / 1024:.2f} KB")
else:
    print(f"ERROR: Failed to save plot to {output_file}")
    sys.exit(1)

# Create a simple HTML file to view the image
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Post-Harvest Losses Chart</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        h1 {{ color: #333; }}
        .chart {{ margin-top: 20px; border: 1px solid #ddd; }}
        img {{ width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Post-Harvest Losses by Crop Type in Nigeria</h1>
        <div class="chart">
            <img src="post_harvest_losses.png" alt="Post-Harvest Losses Chart">
        </div>
    </div>
</body>
</html>
"""

# Save the HTML file
html_file = os.path.join(output_dir, "view_chart.html")
with open(html_file, "w") as f:
    f.write(html_content)

print(f"HTML viewer created: {html_file}")
print("\nDirections to find your chart:")
print(f"1. Open file explorer")
print(f"2. Navigate to: {output_dir}")
print(f"3. You should see 'post_harvest_losses.png' and 'view_chart.html'")
print(f"4. Double-click on 'view_chart.html' to view the chart in your browser")