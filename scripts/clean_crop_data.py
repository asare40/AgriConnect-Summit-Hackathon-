import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Create results directory if it doesn't exist
os.makedirs('results/plots', exist_ok=True)

# Clean the raw data
def clean_crop_data(raw_data):
    # Split the raw data into lines
    lines = raw_data.strip().split('\n')
    
    # Parse header
    header = ["State"] + [col.strip('"') for col in lines[0].split(';')[1:]]
    
    # Parse rows
    rows = []
    for line in lines[1:]:
        parts = line.split(';')
        row = [parts[0].strip('"')]  # State name
        for val in parts[1:]:
            # Clean and convert values
            val = val.strip('"')
            if val == "":
                row.append(0)  # Replace empty strings with 0
            else:
                try:
                    row.append(int(val))
                except ValueError:
                    row.append(0)  # In case of conversion errors
        rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(rows, columns=header)
    return df

# Raw data you provided
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

# Clean the data
df = clean_crop_data(raw_data)

# Save cleaned data to CSV
df.to_csv('results/clean_crop_data.csv', index=False)
print(f"Cleaned data saved to 'results/clean_crop_data.csv'")

# Calculate total production by crop
crop_totals = df.sum(numeric_only=True)
print("\nTotal Production by Crop Type:")
for crop, total in crop_totals.items():
    print(f"{crop}: {total:,}")

# Create bar plot of total production by crop
plt.figure(figsize=(12, 8))
crop_totals.plot(kind='bar', color='steelblue')
plt.title('Total Grain Production in Nigeria by Crop Type', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('Production Volume', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, v in enumerate(crop_totals):
    plt.text(i, v + 0.5, f'{v:,}', ha='center', fontsize=10, rotation=0)

plt.tight_layout()
plt.savefig('results/plots/total_production_by_crop.png', dpi=300, bbox_inches='tight')
plt.close()
print("Created plot: 'results/plots/total_production_by_crop.png'")

# Create a visualization of post-harvest losses by crop type
# Assuming an average post-harvest loss rate for each crop
loss_rates = {
    'Maize': 35.0,
    'Rice': 30.0,
    'Sorghum': 26.0,
    'Millet': 20.0,
    'Wheat': 15.0,
    'Barley': 14.0,
    'Fonio': 28.0,
    'Oats': 12.0,
    'Teff': 18.0
}

# Create post-harvest losses bar chart
plt.figure(figsize=(12, 8))
x = range(len(loss_rates))
plt.bar(x, list(loss_rates.values()), color='firebrick')
plt.title('Average Post-Harvest Losses by Crop Type in Nigeria', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('Loss Percentage (%)', fontsize=14)
plt.xticks(x, list(loss_rates.keys()), rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, (crop, rate) in enumerate(loss_rates.items()):
    plt.text(i, rate + 0.5, f'{rate:.1f}%', ha='center', fontsize=12)

plt.tight_layout()
plt.savefig('results/plots/post_harvest_losses_by_crop.png', dpi=300, bbox_inches='tight')
plt.close()
print("Created plot: 'results/plots/post_harvest_losses_by_crop.png'")

# Create a heatmap of production by state and crop
plt.figure(figsize=(15, 12))
# Select top 15 states by total production
state_totals = df.set_index('State').sum(axis=1).sort_values(ascending=False)
top_states = state_totals.head(15).index
top_crops = ['Maize', 'Rice', 'Sorghum', 'Millet']  # Main crops with data

heatmap_data = df[df['State'].isin(top_states)].set_index('State')[top_crops]

# Use log scale for better visualization since values vary widely
heatmap_data_log = np.log10(heatmap_data.replace(0, 1))

sns.heatmap(heatmap_data_log, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5)
plt.title('Log10 of Crop Production by State (Top 15 States)', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('State', fontsize=14)
plt.tight_layout()
plt.savefig('results/plots/production_heatmap_by_state.png', dpi=300, bbox_inches='tight')
plt.close()
print("Created plot: 'results/plots/production_heatmap_by_state.png'")

# Calculate estimated post-harvest losses for each crop and state
losses_df = pd.DataFrame()
losses_df['State'] = df['State']

for crop in df.columns[1:]:
    if crop in loss_rates:
        losses_df[crop] = df[crop] * (loss_rates[crop] / 100)

# Save calculated losses to CSV
losses_df.to_csv('results/post_harvest_losses_calculated.csv', index=False)
print(f"Calculated post-harvest losses saved to 'results/post_harvest_losses_calculated.csv'")

# Create a visualization of total post-harvest losses by crop
total_losses_by_crop = losses_df.sum(numeric_only=True)
plt.figure(figsize=(12, 8))
total_losses_by_crop.plot(kind='bar', color='darkred')
plt.title('Estimated Total Post-Harvest Losses by Crop Type in Nigeria', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('Volume Lost', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, v in enumerate(total_losses_by_crop):
    plt.text(i, v + 0.5, f'{int(v):,}', ha='center', fontsize=10, rotation=0)

plt.tight_layout()
plt.savefig('results/plots/total_losses_by_crop.png', dpi=300, bbox_inches='tight')
plt.close()
print("Created plot: 'results/plots/total_losses_by_crop.png'")

# Financial impact of post-harvest losses
# Assuming average prices per unit for each crop
crop_prices = {
    'Maize': 120,  # Naira per unit
    'Rice': 350,
    'Sorghum': 110,
    'Millet': 100,
    'Wheat': 300,
    'Barley': 250,
    'Fonio': 400,
    'Oats': 280,
    'Teff': 450
}

# Calculate financial losses
financial_df = pd.DataFrame()
financial_df['Crop'] = list(crop_prices.keys())
financial_df['Loss Volume'] = [total_losses_by_crop[crop] if crop in total_losses_by_crop else 0 for crop in crop_prices]
financial_df['Price Per Unit'] = [crop_prices[crop] for crop in crop_prices]
financial_df['Financial Loss'] = financial_df['Loss Volume'] * financial_df['Price Per Unit']

# Save financial losses to CSV
financial_df.to_csv('results/financial_impact.csv', index=False)
print(f"Financial impact data saved to 'results/financial_impact.csv'")

# Create a bar chart of financial losses
plt.figure(figsize=(12, 8))
sorted_financial = financial_df.sort_values('Financial Loss', ascending=False)
plt.bar(sorted_financial['Crop'], sorted_financial['Financial Loss'] / 1_000_000, color='darkgreen')
plt.title('Financial Impact of Post-Harvest Losses by Crop Type', fontsize=16)
plt.xlabel('Crop Type', fontsize=14)
plt.ylabel('Financial Loss (Million Naira)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of bars
for i, v in enumerate(sorted_financial['Financial Loss'] / 1_000_000):
    if v > 0:
        plt.text(i, v + 0.5, f'{v:.1f}M', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('results/plots/financial_impact_by_crop.png', dpi=300, bbox_inches='tight')
plt.close()
print("Created plot: 'results/plots/financial_impact_by_crop.png'")

print("\nAll plots created successfully.")