import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Fix for the colorbar error in the first visualization
def create_post_harvest_losses_plot():
    # Calculate zone variation for error bars
    zone_variations = {}
    for crop in ['Maize', 'Rice', 'Sorghum', 'Millet']:
        if f'{crop}_LossRate' in losses_df.columns:
            zone_variations[crop] = losses_df[f'{crop}_LossRate'].std()
    
    # Plot base loss rates with error bars
    crops = list(base_loss_rates.keys())
    rates = [base_loss_rates[crop] for crop in crops]
    errors = [zone_variations.get(crop, 0) for crop in crops]
    
    # Sort by loss rate
    sorted_idx = np.argsort(rates)[::-1]  # Descending order
    sorted_crops = [crops[i] for i in sorted_idx]
    sorted_rates = [rates[i] for i in sorted_idx]
    sorted_errors = [errors[i] for i in sorted_idx]
    
    # Create a figure and axis explicitly
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create a color gradient
    colors = plt.cm.YlOrRd(np.linspace(0.3, 0.8, len(sorted_rates)))
    
    # Plot with gradient colors
    bars = ax.bar(range(len(sorted_crops)), sorted_rates, yerr=sorted_errors, capsize=10, color=colors)
    
    # Add labels and styling
    ax.set_title('Average Post-Harvest Losses by Crop Type in Nigeria', fontsize=16)
    ax.set_xlabel('Crop Type', fontsize=14)
    ax.set_ylabel('Loss Percentage (%)', fontsize=14)
    ax.set_xticks(range(len(sorted_crops)))
    ax.set_xticklabels(sorted_crops, rotation=45)
    ax.grid(axis='y', alpha=0.3)
    
    # Add a color bar to indicate severity - FIXED by providing the ax argument
    sm = plt.cm.ScalarMappable(cmap=plt.cm.YlOrRd, norm=plt.Normalize(vmin=min(sorted_rates)-5, vmax=max(sorted_rates)+5))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)  # Pass the ax argument here
    cbar.set_label('Severity of Loss (%)', fontsize=12)
    
    # Add value labels on top of bars
    for i, v in enumerate(sorted_rates):
        ax.text(i, v + sorted_errors[i] + 0.5, f'{v:.1f}%', ha='center', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('results/plots/enhanced/improved_post_harvest_losses_by_crop.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created enhanced plot: 'improved_post_harvest_losses_by_crop.png'")

# Create directories
os.makedirs('results/plots/enhanced', exist_ok=True)

# Same data and setup as before
raw_data = ''';"Maize";"Rice";"Sorghum";"Millet";"Wheat";"Barley";"Fonio";"Oats";"Teff"
Abia;"96620";"58290";"0";"0";"";"";"";"";""
Abuja Federal Capital Territory;"454420";"415000";"132900";"57160";"";"";"";"";""
Adamawa;"442390";"275790";"292000";"166800";"";"";"";"";""
Akwa Ibom;"92040";"24020";"0";"0";"";"";"";"";""
Anambra;"109500";"99310";"0";"0";"";"";"";"";""
Bauchi;"581010";"250080";"447200";"76610";"";"";"";"";""
Bayelsa;"87210";"94720";"0";"0";"";"";"";"";""
Benue;"386330";"517650";"204800";"86940";"";"";"";"";""
Borno;"626650";"189510";"347500";"78130";"";"";"";"";""
Cross River;"112770";"163530";"0";"0";"";"";"";"";""
Delta;"163290";"50520";"0";"0";"";"";"";"";""
Ebonyi;"167280";"145730";"0";"0";"";"";"";"";""
Edo;"159700";"137890";"0";"0";"";"";"";"";""
Ekiti;"299460";"140470";"0";"0";"";"";"";"";""
Enugu;"182790";"94250";"14200";"0";"";"";"";"";""
Gombe;"648790";"215080";"331300";"118730";"";"";"";"";""
Imo;"134970";"85490";"0";"0";"";"";"";"";""
Jigawa;"332440";"215310";"351600";"71080";"";"";"";"";""
Kaduna;"977030";"360370";"446200";"51600";"";"";"";"";""
Kano;"357060";"438720";"618600";"88420";"";"";"";"";""
Katsina;"362360";"220260";"357600";"153070";"";"";"";"";""
Kebbi;"335680";"348690";"406500";"75570";"";"";"";"";""
Kogi;"430870";"534650";"129900";"38760";"";"";"";"";""
Kwara;"335490";"431940";"151700";"30920";"";"";"";"";""
Lagos;"261510";"85850";"0";"0";"";"";"";"";""
Nasarawa;"311950";"417390";"165100";"31730";"";"";"";"";""
Niger;"700610";"629800";"549700";"113610";"";"";"";"";""
Ogun;"286240";"93580";"0";"0";"";"";"";"";""
Ondo;"396340";"120180";"0";"0";"";"";"";"";""
Osun;"381930";"115830";"0";"0";"";"";"";"";""
Oyo;"315820";"108600";"64900";"0";"";"";"";"";""
Plateau;"656480";"250450";"311700";"74810";"";"";"";"";""
Rivers;"135860";"80680";"0";"0";"";"";"";"";""
Sokoto;"260990";"163090";"376800";"188530";"";"";"";"";""
Taraba;"605800";"388160";"340700";"93780";"";"";"";"";""
Yobe;"302700";"160470";"271000";"245260";"";"";"";"";""
Zamfara;"252070";"220620";"413600";"85440";"";"";"";"";""'''

# Clean the raw data
def clean_crop_data(raw_data):
    lines = raw_data.strip().split('\n')
    header = ["State"] + [col.strip('"') for col in lines[0].split(';')[1:]]
    rows = []
    for line in lines[1:]:
        parts = line.split(';')
        row = [parts[0].strip('"')]  # State name
        for val in parts[1:]:
            val = val.strip('"')
            if val == "":
                row.append(0)  # Replace empty strings with 0
            else:
                try:
                    row.append(int(val))
                except ValueError:
                    row.append(0)  # In case of conversion errors
        rows.append(row)
    df = pd.DataFrame(rows, columns=header)
    return df

df = clean_crop_data(raw_data)

# Assign geopolitical zones to states
geopolitical_zones = {
    'North Central': ['Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau', 'Abuja Federal Capital Territory'],
    'North East': ['Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe'],
    'North West': ['Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara'],
    'South East': ['Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo'],
    'South South': ['Akwa Ibom', 'Bayelsa', 'Cross River', 'Delta', 'Edo', 'Rivers'],
    'South West': ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo']
}

# Create zone mapping dictionary
state_to_zone = {}
for zone, states in geopolitical_zones.items():
    for state in states:
        state_to_zone[state] = zone

# Add zone column to dataframe
df['Zone'] = df['State'].map(state_to_zone)

# More realistic post-harvest loss rates by crop and region
# These represent average post-harvest loss percentages based on literature
base_loss_rates = {
    'Maize': 30.0,
    'Rice': 35.0,
    'Sorghum': 25.0,
    'Millet': 22.0,
    'Wheat': 18.0,
    'Barley': 16.0,
    'Fonio': 28.0,
    'Oats': 15.0,
    'Teff': 20.0
}

# Regional factors (some regions have higher/lower losses due to infrastructure, climate, etc.)
zone_factors = {
    'North Central': 1.05,
    'North East': 1.25,
    'North West': 1.15,
    'South East': 0.90,
    'South South': 1.10,
    'South West': 0.85
}

# Value chain stage loss distribution (percentage of total loss at each stage)
value_chain_stages = {
    'Harvesting': 0.15,
    'Processing': 0.25,
    'Storage': 0.35,
    'Transportation': 0.20,
    'Market': 0.05
}

# Create post-harvest losses DataFrame
losses_df = pd.DataFrame()
losses_df['State'] = df['State']
losses_df['Zone'] = df['Zone']

for crop in ['Maize', 'Rice', 'Sorghum', 'Millet']:
    # Skip crops with no production data
    if crop not in df.columns:
        continue
    
    # Calculate losses based on production, base loss rate, and zone factor
    losses_df[f'{crop}_Production'] = df[crop]
    losses_df[f'{crop}_LossRate'] = losses_df['Zone'].map(
        lambda zone: base_loss_rates[crop] * zone_factors.get(zone, 1.0)
    )
    losses_df[f'{crop}_Loss'] = losses_df[f'{crop}_Production'] * losses_df[f'{crop}_LossRate'] / 100

# Run just the function with the colorbar error
create_post_harvest_losses_plot()

print("Fixed the colorbar issue and created the plot successfully!")