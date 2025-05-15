import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('results/interventions/regional', exist_ok=True)

# Define Nigeria's geopolitical zones and their states
geopolitical_zones = {
    'North Central': ['Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau', 'Abuja Federal Capital Territory'],
    'North East': ['Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe'],
    'North West': ['Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara'],
    'South East': ['Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo'],
    'South South': ['Akwa Ibom', 'Bayelsa', 'Cross River', 'Delta', 'Edo', 'Rivers'],
    'South West': ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo']
}

# Define region-specific challenges and recommended interventions
regional_interventions = {
    'North Central': {
        'Main Crops': ['Maize', 'Rice', 'Sorghum', 'Millet'],
        'Key Challenges': [
            'Limited access to improved storage facilities',
            'Poor market access for smallholder farmers',
            'Inadequate processing infrastructure',
            'High transportation costs due to poor roads'
        ],
        'Recommended Interventions': [
            'Community-level metal silos for grain storage',
            'Mobile processing units for rice and maize',
            'Farmer aggregation centers in strategic locations',
            'Digital market information systems'
        ],
        'Priority States': ['Niger', 'Benue', 'Plateau'],
        'Potential Impact': 'High'
    },
    'North East': {
        'Main Crops': ['Maize', 'Rice', 'Sorghum', 'Millet'],
        'Key Challenges': [
            'Security concerns affecting market access',
            'Limited extension services',
            'Poor post-harvest handling knowledge',
            'Fluctuating climate conditions affecting drying'
        ],
        'Recommended Interventions': [
            'Household-level hermetic storage solutions',
            'Solar dryers for proper grain drying',
            'Mobile-based extension services',
            'Early warning systems for climate variability'
        ],
        'Priority States': ['Adamawa', 'Taraba', 'Bauchi'],
        'Potential Impact': 'Medium-High'
    },
    'North West': {
        'Main Crops': ['Maize', 'Rice', 'Sorghum', 'Millet'],
        'Key Challenges': [
            'Large volumes with inadequate storage infrastructure',
            'High levels of aflatoxin contamination',
            'Limited mechanization for post-harvest operations',
            'Poor quality control systems'
        ],
        'Recommended Interventions': [
            'Commercial-scale warehouse receipt systems',
            'Aflatoxin mitigation programs',
            'Subsidized threshers and shellers',
            'Quality assessment training and tools'
        ],
        'Priority States': ['Kano', 'Kaduna', 'Katsina'],
        'Potential Impact': 'Very High'
    },
    'South East': {
        'Main Crops': ['Maize', 'Rice'],
        'Key Challenges': [
            'Land fragmentation limiting economies of scale',
            'High humidity affecting grain quality',
            'Limited access to finance for technology adoption',
            'Poor electricity for processing operations'
        ],
        'Recommended Interventions': [
            'Cooperative-based storage and processing centers',
            'Improved rice parboiling equipment',
            'Solar-powered processing equipment',
            'Group-based financial products'
        ],
        'Priority States': ['Ebonyi', 'Enugu', 'Anambra'],
        'Potential Impact': 'Medium'
    },
    'South South': {
        'Main Crops': ['Maize', 'Rice'],
        'Key Challenges': [
            'High humidity and rainfall affecting drying',
            'Limited processing infrastructure',
            'Poor transportation networks in riverine areas',
            'Land availability constraints'
        ],
        'Recommended Interventions': [
            'All-weather drying equipment',
            'Improved storage with moisture control',
            'Water-resistant packaging materials',
            'Strategic collection centers in accessible locations'
        ],
        'Priority States': ['Cross River', 'Edo', 'Delta'],
        'Potential Impact': 'Medium'
    },
    'South West': {
        'Main Crops': ['Maize', 'Rice'],
        'Key Challenges': [
            'Land pressure from urbanization',
            'High cost of labor for post-harvest operations',
            'Market competition from imports',
            'Limited specialized storage for grains'
        ],
        'Recommended Interventions': [
            'Mechanized post-harvest handling equipment',
            'Value addition and processing technologies',
            'Urban market linkage platforms',
            'Quality certification systems'
        ],
        'Priority States': ['Oyo', 'Ekiti', 'Ondo'],
        'Potential Impact': 'Medium-High'
    }
}

# Create DataFrame for regional interventions
regional_rows = []
for region, details in regional_interventions.items():
    row = {
        'Region': region,
        'Main Crops': ', '.join(details['Main Crops']),
        'Key Challenges': '; '.join(details['Key Challenges']),
        'Recommended Interventions': '; '.join(details['Recommended Interventions']),
        'Priority States': ', '.join(details['Priority States']),
        'Potential Impact': details['Potential Impact']
    }
    regional_rows.append(row)

regional_df = pd.DataFrame(regional_rows)

# Save the regional intervention strategies to CSV
regional_df.to_csv('results/interventions/regional/regional_strategies.csv', index=False)
print("Regional intervention strategies saved to 'results/interventions/regional/regional_strategies.csv'")

# Create a visualization showing impact potential by region
impact_scale = {
    'Low': 1,
    'Medium': 2,
    'Medium-High': 3,
    'High': 4,
    'Very High': 5
}

# Convert impact ratings to numerical values
regions = list(regional_interventions.keys())
impact_values = [impact_scale[regional_interventions[r]['Potential Impact']] for r in regions]

# Create bar chart of regional impact potential
plt.figure(figsize=(12, 7))
bars = plt.bar(regions, impact_values, color=plt.cm.viridis(np.array(impact_values) / 5))

plt.title('Potential Impact of Post-Harvest Loss Interventions by Region', fontsize=16)
plt.xlabel('Geopolitical Zone', fontsize=14)
plt.ylabel('Impact Potential', fontsize=14)
plt.ylim(0, 5.5)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, v in enumerate(impact_values):
    impact_label = list(impact_scale.keys())[list(impact_scale.values()).index(v)]
    plt.text(i, v + 0.1, impact_label, ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('results/interventions/regional/regional_impact_potential.png', dpi=300, bbox_inches='tight')
plt.close()
print("Regional impact potential visualization saved to 'results/interventions/regional/regional_impact_potential.png'")

# Create a regional intervention priority map
# For each region, determine the most critical intervention type
intervention_types = ['Storage', 'Processing', 'Transportation', 'Education', 'Market Linkages', 'Policy']

# Assign priority scores (1-10) for each intervention type by region
regional_priorities = {
    'North Central': {'Storage': 9, 'Processing': 8, 'Transportation': 7, 'Education': 5, 'Market Linkages': 8, 'Policy': 6},
    'North East': {'Storage': 8, 'Processing': 6, 'Transportation': 7, 'Education': 9, 'Market Linkages': 5, 'Policy': 7},
    'North West': {'Storage': 10, 'Processing': 7, 'Transportation': 6, 'Education': 6, 'Market Linkages': 8, 'Policy': 7},
    'South East': {'Storage': 7, 'Processing': 9, 'Transportation': 5, 'Education': 6, 'Market Linkages': 7, 'Policy': 5},
    'South South': {'Storage': 8, 'Processing': 7, 'Transportation': 9, 'Education': 6, 'Market Linkages': 5, 'Policy': 6},
    'South West': {'Storage': 6, 'Processing': 8, 'Transportation': 5, 'Education': 7, 'Market Linkages': 9, 'Policy': 8}
}

# Create DataFrame for the heatmap
priority_data = pd.DataFrame(regional_priorities).T

# Create a heatmap
plt.figure(figsize=(12, 8))
ax = plt.gca()
im = ax.imshow(priority_data.values, cmap='YlOrRd')

# Set ticks and labels
ax.set_xticks(np.arange(len(intervention_types)))
ax.set_yticks(np.arange(len(regions)))
ax.set_xticklabels(intervention_types)
ax.set_yticklabels(regions)

# Rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.set_label('Intervention Priority (1-10 scale)', rotation=270, labelpad=20)

# Add value annotations on the heatmap
for i in range(len(regions)):
    for j in range(len(intervention_types)):
        text = ax.text(j, i, priority_data.values[i, j],
                       ha="center", va="center", color="black" if priority_data.values[i, j] < 7 else "white")

plt.title('Regional Intervention Type Priorities', fontsize=16)
plt.tight_layout()
plt.savefig('results/interventions/regional/intervention_priority_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("Regional intervention priority heatmap saved to 'results/interventions/regional/intervention_priority_heatmap.png'")

print("\nAll regional targeting analyses completed successfully!")