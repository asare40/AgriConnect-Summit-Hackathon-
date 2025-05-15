import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('results/interventions', exist_ok=True)

# Define the key intervention categories
intervention_categories = {
    'Storage Solutions': {
        'description': 'Improved storage facilities and technologies',
        'potential_impact': 'High',
        'implementation_cost': 'Medium to High',
        'timeframe': 'Medium-term (1-2 years)',
        'specific_methods': [
            'Hermetic storage bags for smallholders',
            'Community-level metal silos',
            'Warehouse receipt systems in major production zones',
            'Cold chain solutions for perishables',
            'Low-cost moisture meters for proper drying verification'
        ]
    },
    'Processing Technologies': {
        'description': 'Improved processing equipment and methods',
        'potential_impact': 'High',
        'implementation_cost': 'High',
        'timeframe': 'Medium to Long-term (2-3 years)',
        'specific_methods': [
            'Mini rice mills with proper destoning and polishing',
            'Solar dryers for grain and other crops',
            'Mobile processing units for remote areas',
            'Threshers and shellers to reduce losses during processing',
            'Parboiling equipment for rice with improved energy efficiency'
        ]
    },
    'Transportation & Handling': {
        'description': 'Improved logistics and handling systems',
        'potential_impact': 'Medium',
        'implementation_cost': 'Medium',
        'timeframe': 'Short to Medium-term (6-18 months)',
        'specific_methods': [
            'Standardized crates for transport and handling',
            'Improved rural roads in high-production zones',
            'Collection centers with quality assessment tools',
            'Training on proper handling techniques',
            'Cushioning materials for delicate crops'
        ]
    },
    'Education & Training': {
        'description': 'Capacity building for farmers and other value chain actors',
        'potential_impact': 'Medium to High',
        'implementation_cost': 'Low to Medium',
        'timeframe': 'Short-term (3-12 months)',
        'specific_methods': [
            'Farmer field schools on harvest and post-harvest management',
            'Digital extension services via mobile phones',
            'Demonstration plots showing proper techniques',
            'Train-the-trainer programs for extension agents',
            'Video-based learning modules in local languages'
        ]
    },
    'Market Linkages': {
        'description': 'Improved connections between producers and markets',
        'potential_impact': 'Medium',
        'implementation_cost': 'Low to Medium',
        'timeframe': 'Short to Medium-term (6-18 months)',
        'specific_methods': [
            'Digital platforms connecting farmers to buyers',
            'Cooperative marketing strategies',
            'Contract farming arrangements',
            'Market information systems',
            'Aggregation centers in strategic locations'
        ]
    },
    'Policy & Financing': {
        'description': 'Enabling policy environment and financial services',
        'potential_impact': 'High (long-term)',
        'implementation_cost': 'Variable',
        'timeframe': 'Long-term (2-5 years)',
        'specific_methods': [
            'Subsidies for post-harvest technologies',
            'Low-interest loans for storage and processing equipment',
            'Quality standards and enforcement',
            'Insurance products for stored produce',
            'Public-private partnerships for infrastructure development'
        ]
    }
}

# Create a DataFrame for the intervention strategies
intervention_df = pd.DataFrame.from_dict(intervention_categories, orient='index')
intervention_df.reset_index(inplace=True)
intervention_df.rename(columns={'index': 'Intervention Category'}, inplace=True)

# Save the intervention strategies to CSV
intervention_df.to_csv('results/interventions/intervention_strategies.csv', index=False)
print("Intervention strategies saved to 'results/interventions/intervention_strategies.csv'")

# Create crop-specific intervention recommendations based on loss profiles
crop_interventions = {
    'Maize': {
        'Primary Issues': 'High moisture content at storage, weevil infestation, improper drying',
        'Priority Interventions': ['Storage Solutions', 'Education & Training', 'Processing Technologies'],
        'Region Specific': {
            'North': 'Focus on large-scale metal silos and warehouse systems',
            'South': 'Focus on hermetic bags and household-level storage improvements'
        },
        'Success Metrics': 'Reduction in storage losses by 15-20% within 2 years',
        'Potential Partners': 'IITA, State Agricultural Development Programs, USAID'
    },
    'Rice': {
        'Primary Issues': 'Poor threshing, inadequate parboiling, improper drying, milling losses',
        'Priority Interventions': ['Processing Technologies', 'Storage Solutions', 'Market Linkages'],
        'Region Specific': {
            'North': 'Improved parboiling equipment, solar dryers',
            'South': 'Mini rice mills, improved quality assessment systems'
        },
        'Success Metrics': 'Improved milling yield by 10-15%, reduced breakage rate by 20%',
        'Potential Partners': 'Africa Rice Center, Rice Farmers Association, State Ministries of Agriculture'
    },
    'Sorghum': {
        'Primary Issues': 'Bird damage, mold growth, threshing losses',
        'Priority Interventions': ['Education & Training', 'Storage Solutions', 'Processing Technologies'],
        'Region Specific': {
            'North': 'Focus on large community storage with fumigation capabilities',
            'Middle Belt': 'Improved threshing equipment and drying platforms'
        },
        'Success Metrics': 'Reduced field and storage losses by 18% within 2 years',
        'Potential Partners': 'ICRISAT, Sorghum Farmers Association, Agricultural Research Institutes'
    },
    'Millet': {
        'Primary Issues': 'Grain mold, rodent damage, improper storage',
        'Priority Interventions': ['Storage Solutions', 'Education & Training', 'Transportation & Handling'],
        'Region Specific': {
            'North': 'Improved traditional storage structures, metal silos',
            'North East': 'Community-based seed storage systems'
        },
        'Success Metrics': 'Reduced storage losses by 15% within 18 months',
        'Potential Partners': 'ICRISAT, State Agricultural Extension Services, Local NGOs'
    }
}

# Create a DataFrame for the crop-specific interventions
crop_int_rows = []
for crop, details in crop_interventions.items():
    row = {
        'Crop': crop,
        'Primary Issues': details['Primary Issues'],
        'Priority Interventions': ', '.join(details['Priority Interventions']),
    }
    for region, strategy in details['Region Specific'].items():
        row[f'Region: {region}'] = strategy
    row['Success Metrics'] = details['Success Metrics']
    row['Potential Partners'] = details['Potential Partners']
    crop_int_rows.append(row)

crop_int_df = pd.DataFrame(crop_int_rows)

# Save the crop-specific interventions to CSV
crop_int_df.to_csv('results/interventions/crop_specific_interventions.csv', index=False)
print("Crop-specific interventions saved to 'results/interventions/crop_specific_interventions.csv'")

# Create a heatmap showing the relationship between interventions and crops
# Create a matrix of intervention effectiveness by crop
crops = list(crop_interventions.keys())
interventions = list(intervention_categories.keys())

# Create a matrix to represent the effectiveness of each intervention for each crop
# Based on whether the intervention is in the priority list and its position
effectiveness_matrix = np.zeros((len(crops), len(interventions)))

for i, crop in enumerate(crops):
    priorities = crop_interventions[crop]['Priority Interventions']
    for j, intervention in enumerate(interventions):
        if intervention in priorities:
            # Assign value based on priority position (higher value for higher priority)
            effectiveness_matrix[i, j] = len(priorities) - priorities.index(intervention)
        else:
            effectiveness_matrix[i, j] = 0.5  # Some baseline effectiveness

# Create the heatmap
plt.figure(figsize=(12, 8))
plt.imshow(effectiveness_matrix, cmap='YlGnBu', aspect='auto')
plt.colorbar(label='Intervention Priority (higher = more recommended)')
plt.xticks(np.arange(len(interventions)), interventions, rotation=45, ha='right')
plt.yticks(np.arange(len(crops)), crops)
plt.title('Intervention Prioritization by Crop Type', fontsize=16)
plt.tight_layout()
plt.savefig('results/interventions/intervention_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("Intervention heatmap saved to 'results/interventions/intervention_heatmap.png'")

# Create a cost-impact matrix for different interventions
# Define relative impact and cost values (1-10 scale)
intervention_cost_impact = {
    'Storage Solutions': {'cost': 7, 'impact': 9, 'timeframe': 6},
    'Processing Technologies': {'cost': 9, 'impact': 8, 'timeframe': 8},
    'Transportation & Handling': {'cost': 6, 'impact': 6, 'timeframe': 5},
    'Education & Training': {'cost': 4, 'impact': 7, 'timeframe': 3},
    'Market Linkages': {'cost': 5, 'impact': 6, 'timeframe': 5},
    'Policy & Financing': {'cost': 8, 'impact': 9, 'timeframe': 9}
}

# Extract the data
int_names = list(intervention_cost_impact.keys())
costs = [intervention_cost_impact[i]['cost'] for i in int_names]
impacts = [intervention_cost_impact[i]['impact'] for i in int_names]
timeframes = [intervention_cost_impact[i]['timeframe'] for i in int_names]

# Create cost-impact matrix visualization
plt.figure(figsize=(10, 8))
plt.scatter(costs, impacts, s=np.array(timeframes) * 50, alpha=0.7, c=range(len(int_names)), cmap='viridis')

# Add labels for each point
for i, name in enumerate(int_names):
    plt.annotate(name, (costs[i], impacts[i]), 
                 xytext=(5, 5), textcoords='offset points', fontsize=10)

plt.grid(alpha=0.3)
plt.xlabel('Implementation Cost (1-10 scale)', fontsize=12)
plt.ylabel('Potential Impact (1-10 scale)', fontsize=12)
plt.title('Cost-Impact Analysis of Intervention Strategies', fontsize=16)

# Add a line dividing the quadrants (high impact/low cost is ideal)
plt.axhline(y=5.5, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=5.5, color='gray', linestyle='--', alpha=0.5)

# Add quadrant labels
plt.text(3, 8, 'HIGH IMPACT\nLOW COST\n(Most Desirable)', ha='center', va='center', bbox=dict(facecolor='lightgreen', alpha=0.5))
plt.text(8, 8, 'HIGH IMPACT\nHIGH COST', ha='center', va='center', bbox=dict(facecolor='lightyellow', alpha=0.5))
plt.text(3, 3, 'LOW IMPACT\nLOW COST', ha='center', va='center', bbox=dict(facecolor='lightyellow', alpha=0.5))
plt.text(8, 3, 'LOW IMPACT\nHIGH COST\n(Least Desirable)', ha='center', va='center', bbox=dict(facecolor='lightcoral', alpha=0.5))

plt.tight_layout()
plt.savefig('results/interventions/cost_impact_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("Cost-impact analysis saved to 'results/interventions/cost_impact_analysis.png'")

# Generate a roadmap for implementation
implementation_phases = {
    'Phase 1 (0-6 months)': [
        'Conduct detailed needs assessment in priority states',
        'Begin farmer education and training programs',
        'Pilot hermetic storage bags distribution in high-loss regions',
        'Establish baseline measurements for monitoring progress',
        'Identify and engage key implementation partners'
    ],
    'Phase 2 (7-18 months)': [
        'Scale up successful storage solutions from pilot phase',
        'Deploy mobile processing units in strategic locations',
        'Implement standardized crates for transportation',
        'Launch digital market linkage platforms',
        'Engage policy stakeholders for longer-term interventions'
    ],
    'Phase 3 (19-36 months)': [
        'Establish community-level storage and processing centers',
        'Develop financial products specific to post-harvest management',
        'Integrate quality standards into market systems',
        'Build capacity of local manufacturers for technology production',
        'Develop policy framework to sustain interventions'
    ]
}

# Create a DataFrame for the implementation roadmap
roadmap_rows = []
for phase, activities in implementation_phases.items():
    for i, activity in enumerate(activities):
        roadmap_rows.append({
            'Phase': phase,
            'Activity Number': i+1,
            'Activity': activity
        })

roadmap_df = pd.DataFrame(roadmap_rows)

# Save the implementation roadmap to CSV
roadmap_df.to_csv('results/interventions/implementation_roadmap.csv', index=False)
print("Implementation roadmap saved to 'results/interventions/implementation_roadmap.csv'")

print("\nAll intervention planning documents and visualizations have been created successfully!")