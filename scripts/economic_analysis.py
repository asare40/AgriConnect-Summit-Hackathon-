import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('results/interventions/economic', exist_ok=True)

# Define economic parameters for ROI analysis
interventions_economic = {
    'Hermetic Storage Bags': {
        'implementation_cost': 250000,  # Naira per ton capacity
        'annual_operating_cost': 25000,  # Naira per ton capacity per year
        'lifespan_years': 3,
        'expected_loss_reduction': 0.70,  # 70% reduction in storage losses
        'capacity_tons': 1,
        'beneficiaries_per_unit': 5,  # Number of farmers per ton capacity
    },
    'Metal Silos': {
        'implementation_cost': 850000,  # Naira per ton capacity
        'annual_operating_cost': 42500,  # Naira per ton capacity per year
        'lifespan_years': 10,
        'expected_loss_reduction': 0.85,  # 85% reduction in storage losses
        'capacity_tons': 5,
        'beneficiaries_per_unit': 20,  # Number of farmers per ton capacity
    },
    'Improved Threshers': {
        'implementation_cost': 1200000,  # Naira per unit
        'annual_operating_cost': 150000,  # Naira per unit per year
        'lifespan_years': 8,
        'expected_loss_reduction': 0.60,  # 60% reduction in threshing losses
        'capacity_tons': 3,  # Tons per day
        'beneficiaries_per_unit': 100,  # Number of farmers per unit
    },
    'Solar Dryers': {
        'implementation_cost': 650000,  # Naira per unit
        'annual_operating_cost': 65000,  # Naira per unit per year
        'lifespan_years': 5,
        'expected_loss_reduction': 0.75,  # 75% reduction in drying-related losses
        'capacity_tons': 0.5,  # Tons per day
        'beneficiaries_per_unit': 25,  # Number of farmers per unit
    },
    'Mini Rice Mills': {
        'implementation_cost': 3500000,  # Naira per unit
        'annual_operating_cost': 500000,  # Naira per unit per year
        'lifespan_years': 10,
        'expected_loss_reduction': 0.80,  # 80% reduction in milling losses
        'capacity_tons': 2,  # Tons per day
        'beneficiaries_per_unit': 200,  # Number of farmers per unit
    },
    'Training Programs': {
        'implementation_cost': 150000,  # Naira per program
        'annual_operating_cost': 75000,  # Naira per program per year
        'lifespan_years': 2,
        'expected_loss_reduction': 0.30,  # 30% reduction in losses through behavior change
        'capacity_tons': None,  # Not applicable
        'beneficiaries_per_unit': 50,  # Farmers per training program
    }
}

# Define crop values for economic calculations (Naira per ton)
crop_values = {
    'Maize': 230000,
    'Rice': 650000,
    'Sorghum': 200000,
    'Millet': 180000
}

# Estimate baseline losses (tons per hectare)
baseline_losses = {
    'Maize': 0.9,  # 30% of 3.0 tons/ha average yield
    'Rice': 1.4,  # 35% of 4.0 tons/ha average yield
    'Sorghum': 0.4,  # 25% of 1.6 tons/ha average yield
    'Millet': 0.3   # 22% of 1.4 tons/ha average yield
}

# Calculate ROI for each intervention and crop combination
roi_data = []

for intervention, int_details in interventions_economic.items():
    for crop, value in crop_values.items():
        # Skip if not applicable (e.g., rice mills only for rice)
        if intervention == 'Mini Rice Mills' and crop != 'Rice':
            continue
            
        # Get baseline loss for this crop
        baseline_loss = baseline_losses[crop]
        
        # Calculate potential loss reduction in tons
        if int_details['capacity_tons'] is not None:
            potential_reduction = baseline_loss * int_details['expected_loss_reduction'] * int_details['capacity_tons'] * 250  # Assume 250 working days per year
        else:
            # For training programs, assume 2 hectares per farmer
            potential_reduction = baseline_loss * int_details['expected_loss_reduction'] * int_details['beneficiaries_per_unit'] * 2
        
        # Calculate value of loss reduction
        annual_value = potential_reduction * value
        
        # Calculate total costs over lifespan
        total_cost = int_details['implementation_cost'] + (int_details['annual_operating_cost'] * int_details['lifespan_years'])
        
        # Calculate benefits over lifespan
        total_benefit = annual_value * int_details['lifespan_years']
        
        # Calculate ROI
        roi = (total_benefit - total_cost) / total_cost * 100
        
        # Calculate payback period in years
        if annual_value > int_details['annual_operating_cost']:
            payback = int_details['implementation_cost'] / (annual_value - int_details['annual_operating_cost'])
        else:
            payback = float('inf')  # Infinite payback period if annual value doesn't exceed operating costs
        
        # Calculate cost per beneficiary
        cost_per_beneficiary = int_details['implementation_cost'] / int_details['beneficiaries_per_unit']
        
        # Calculate cost per ton saved
        if potential_reduction > 0:
            cost_per_ton = int_details['implementation_cost'] / potential_reduction
        else:
            cost_per_ton = float('inf')
        
        # Add to result list
        roi_data.append({
            'Intervention': intervention,
            'Crop': crop,
            'Implementation Cost (₦)': int_details['implementation_cost'],
            'Annual Operating Cost (₦)': int_details['annual_operating_cost'],
            'Lifespan (years)': int_details['lifespan_years'],
            'Expected Loss Reduction (%)': int_details['expected_loss_reduction'] * 100,
            'Potential Annual Reduction (tons)': potential_reduction,
            'Annual Value of Reduction (₦)': annual_value,
            'Total Cost over Lifespan (₦)': total_cost,
            'Total Benefit over Lifespan (₦)': total_benefit,
            'ROI (%)': roi,
            'Payback Period (years)': payback,
            'Cost per Beneficiary (₦)': cost_per_beneficiary,
            'Cost per Ton Saved (₦)': cost_per_ton
        })

# Convert to DataFrame
roi_df = pd.DataFrame(roi_data)

# Save the ROI analysis to CSV
roi_df.to_csv('results/interventions/economic/roi_analysis.csv', index=False)
print("ROI analysis saved to 'results/interventions/economic/roi_analysis.csv'")

# Create a bar chart of ROI by intervention and crop
plt.figure(figsize=(14, 8))

# Group by intervention and crop
roi_summary = roi_df.pivot(index='Intervention', columns='Crop', values='ROI (%)')

# Plot as grouped bar chart
roi_summary.plot(kind='bar', figsize=(14, 8))
plt.title('ROI by Intervention and Crop Type', fontsize=16)
plt.xlabel('Intervention', fontsize=14)
plt.ylabel('ROI (%)', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.legend(title='Crop Type')

plt.tight_layout()
plt.savefig('results/interventions/economic/roi_by_intervention.png', dpi=300, bbox_inches='tight')
plt.close()
print("ROI chart saved to 'results/interventions/economic/roi_by_intervention.png'")

# Create a scatter plot of payback period vs. cost per beneficiary
plt.figure(figsize=(12, 8))

# Create a color map for different interventions
intervention_types = roi_df['Intervention'].unique()
colors = plt.cm.tab10(np.linspace(0, 1, len(intervention_types)))
intervention_colors = {intervention: colors[i] for i, intervention in enumerate(intervention_types)}

# Create scatter plot
for intervention in intervention_types:
    subset = roi_df[roi_df['Intervention'] == intervention]
    plt.scatter(
        subset['Cost per Beneficiary (₦)'] / 1000,  # Convert to thousands
        subset['Payback Period (years)'],
        s=subset['ROI (%)'] / 10,  # Size based on ROI
        label=intervention,
        alpha=0.7,
        c=[intervention_colors[intervention]] * len(subset)
    )

plt.title('Investment Efficiency Analysis', fontsize=16)
plt.xlabel('Cost per Beneficiary (₦ thousands)', fontsize=14)
plt.ylabel('Payback Period (years)', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(title='Intervention Type')

# Add annotations for best options (low cost, quick payback)
best_options = roi_df.sort_values(by=['Payback Period (years)', 'Cost per Beneficiary (₦)'])[:3]
for _, row in best_options.iterrows():
    plt.annotate(
        f"{row['Intervention']} ({row['Crop']})",
        (row['Cost per Beneficiary (₦)']/1000, row['Payback Period (years)']),
        xytext=(10, -10),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
    )

plt.tight_layout()
plt.savefig('results/interventions/economic/investment_efficiency.png', dpi=300, bbox_inches='tight')
plt.close()
print("Investment efficiency chart saved to 'results/interventions/economic/investment_efficiency.png'")

# Create a scale-up scenario analysis
# Define three scenarios for scale-up
scenarios = {
    'Conservative': {
        'coverage': 0.10,  # 10% of potential beneficiaries
        'efficiency': 0.80,  # 80% of expected loss reduction achieved
        'cost_overrun': 1.20  # 20% cost overrun
    },
    'Realistic': {
        'coverage': 0.25,  # 25% of potential beneficiaries
        'efficiency': 0.90,  # 90% of expected loss reduction achieved
        'cost_overrun': 1.10  # 10% cost overrun
    },
    'Optimistic': {
        'coverage': 0.40,  # 40% of potential beneficiaries
        'efficiency': 1.00,  # 100% of expected loss reduction achieved
        'cost_overrun': 1.00  # No cost overrun
    }
}

# Define the total potential beneficiaries by crop
potential_beneficiaries = {
    'Maize': 5000000,
    'Rice': 3500000,
    'Sorghum': 2500000,
    'Millet': 2000000
}

# Create scenario analysis data
scenario_data = []

for intervention, int_details in interventions_economic.items():
    # Choose the best crop for this intervention based on ROI
    intervention_roi = roi_df[roi_df['Intervention'] == intervention]
    if len(intervention_roi) == 0:
        continue
        
    best_crop_row = intervention_roi.loc[intervention_roi['ROI (%)'].idxmax()]
    crop = best_crop_row['Crop']
    
    for scenario_name, scenario_params in scenarios.items():
        # Calculate number of units needed
        beneficiaries = potential_beneficiaries[crop] * scenario_params['coverage']
        units_needed = beneficiaries / int_details['beneficiaries_per_unit']
        
        # Calculate implementation cost
        total_implementation_cost = units_needed * int_details['implementation_cost'] * scenario_params['cost_overrun']
        
        # Calculate annual operating cost
        annual_operating_cost = units_needed * int_details['annual_operating_cost'] * scenario_params['cost_overrun']
        
        # Get baseline loss and calculate potential reduction
        baseline_loss = baseline_losses[crop]
        if int_details['capacity_tons'] is not None:
            annual_reduction = baseline_loss * int_details['expected_loss_reduction'] * scenario_params['efficiency'] * int_details['capacity_tons'] * 250 * units_needed
        else:
            # For training programs
            annual_reduction = baseline_loss * int_details['expected_loss_reduction'] * scenario_params['efficiency'] * beneficiaries * 2
        
        # Calculate value of loss reduction
        annual_value = annual_reduction * crop_values[crop]
        
        # Calculate ROI over 5 years
        five_year_cost = total_implementation_cost + (annual_operating_cost * 5)
        five_year_benefit = annual_value * 5
        five_year_roi = (five_year_benefit - five_year_cost) / five_year_cost * 100
        
        scenario_data.append({
            'Intervention': intervention,
            'Crop': crop,
            'Scenario': scenario_name,
            'Beneficiaries': beneficiaries,
            'Units Required': units_needed,
            'Total Implementation Cost (₦)': total_implementation_cost,
            'Annual Operating Cost (₦)': annual_operating_cost,
            'Annual Loss Reduction (tons)': annual_reduction,
            'Annual Value (₦)': annual_value,
            '5-Year Cost (₦)': five_year_cost,
            '5-Year Benefit (₦)': five_year_benefit,
            '5-Year ROI (%)': five_year_roi
        })

# Convert to DataFrame
scenario_df = pd.DataFrame(scenario_data)

# Save the scenario analysis to CSV
scenario_df.to_csv('results/interventions/economic/scale_up_scenarios.csv', index=False)
print("Scale-up scenario analysis saved to 'results/interventions/economic/scale_up_scenarios.csv'")

# Create a visualization of 5-year ROI by scenario
pivot_scenario = scenario_df.pivot_table(
    values='5-Year ROI (%)', 
    index='Intervention',
    columns='Scenario'
)

plt.figure(figsize=(12, 8))
pivot_scenario.plot(kind='bar', figsize=(12, 8))
plt.title('5-Year ROI by Intervention and Scale-up Scenario', fontsize=16)
plt.xlabel('Intervention', fontsize=14)
plt.ylabel('5-Year ROI (%)', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.legend(title='Scenario')

# Add horizontal line at ROI = 0
plt.axhline(y=0, color='red', linestyle='-', alpha=0.3)
plt.tight_layout()

plt.savefig('results/interventions/economic/scenario_roi_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("Scenario ROI analysis chart saved to 'results/interventions/economic/scenario_roi_analysis.png'")

print("\nAll economic analyses completed successfully!")