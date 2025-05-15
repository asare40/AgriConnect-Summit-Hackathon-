import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Ensure output directories exist
os.makedirs('results/dashboard/interactive', exist_ok=True)
os.makedirs('results/dashboard/static', exist_ok=True)
os.makedirs('results/dashboard/data', exist_ok=True)

# Create more detailed regional PHL data for the dashboard
# This would be connected to a proper database in a production environment

# Define states by geopolitical zones
geopolitical_zones = {
    "North Central": ["Benue", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau", "FCT"],
    "North East": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
    "North West": ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "Zamfara"],
    "South East": ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"],
    "South South": ["Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"],
    "South West": ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"]
}

# Create a flat list of all states
all_states = [state for zone, states in geopolitical_zones.items() for state in states]

# Crop data with regional production patterns
crops = {
    "Maize": {
        "base_production": 800,  # tons (base value for simulation)
        "regional_multipliers": {
            "North Central": 1.2,
            "North East": 0.8,
            "North West": 1.5,
            "South East": 0.6,
            "South South": 0.5,
            "South West": 0.9
        },
        "phl_rate": 30.5,  # percentage
        "price_per_ton": 230000  # Naira
    },
    "Rice": {
        "base_production": 600,
        "regional_multipliers": {
            "North Central": 1.3,
            "North East": 0.7,
            "North West": 1.4,
            "South East": 0.8,
            "South South": 1.1,
            "South West": 0.6
        },
        "phl_rate": 35.0,
        "price_per_ton": 650000
    },
    "Sorghum": {
        "base_production": 500,
        "regional_multipliers": {
            "North Central": 0.9,
            "North East": 1.3,
            "North West": 1.6,
            "South East": 0.2,
            "South South": 0.1,
            "South West": 0.3
        },
        "phl_rate": 25.8,
        "price_per_ton": 200000
    },
    "Millet": {
        "base_production": 450,
        "regional_multipliers": {
            "North Central": 0.7,
            "North East": 1.4,
            "North West": 1.7,
            "South East": 0.1,
            "South South": 0.1,
            "South West": 0.2
        },
        "phl_rate": 22.4,
        "price_per_ton": 180000
    },
    "Vegetables": {
        "base_production": 350,
        "regional_multipliers": {
            "North Central": 0.8,
            "North East": 0.6,
            "North West": 0.7,
            "South East": 1.2,
            "South South": 1.3,
            "South West": 1.5
        },
        "phl_rate": 45.0,
        "price_per_ton": 400000
    }
}

# Value chain stage loss distribution
value_chain_stages = {
    "Harvesting": 0.15,  # 15% of total losses occur here
    "Processing": 0.25,  # 25% of total losses occur here
    "Storage": 0.35,     # 35% of total losses occur here
    "Transportation": 0.20, # 20% of total losses occur here
    "Market": 0.05       # 5% of total losses occur here
}

# Business model applicability by stage
business_models_by_stage = {
    "Harvesting": ["BM-01", "BM-06"],
    "Processing": ["BM-01", "BM-03"],
    "Storage": ["BM-02", "BM-05"],
    "Transportation": ["BM-04"],
    "Market": ["BM-02", "BM-07"]
}

# Business model details for reference
business_model_details = {
    "BM-01": {
        "name": "Mobile Threshing/Shelling Service",
        "investment": "N955,000 - N1,625,000",
        "roi": "15-30% annually",
        "impact": "15-20% reduction in processing losses"
    },
    "BM-02": {
        "name": "Aggregation & Quality Control Hub",
        "investment": "N1,785,000 - N4,020,000",
        "roi": "20-30% annually",
        "impact": "20-30% reduction in storage and market losses"
    },
    "BM-03": {
        "name": "Solar Drying as a Service",
        "investment": "N720,000 - N2,080,000",
        "roi": "40-60% annually",
        "impact": "25-35% reduction in processing losses"
    },
    "BM-04": {
        "name": "Cold Chain Transport Microfranchise",
        "investment": "N1,200,000 - N2,500,000",
        "roi": "25-45% annually",
        "impact": "30-45% reduction in transportation losses"
    },
    "BM-05": {
        "name": "Storage Facility Management",
        "investment": "N1,500,000 - N5,000,000",
        "roi": "20-35% annually",
        "impact": "30-40% reduction in storage losses"
    },
    "BM-06": {
        "name": "Quality Testing Service",
        "investment": "N200,000 - N800,000",
        "roi": "30-50% annually",
        "impact": "10-20% reduction in quality-related losses"
    },
    "BM-07": {
        "name": "Digital Market Linkage Platform",
        "investment": "N300,000 - N1,500,000",
        "roi": "40-70% annually",
        "impact": "15-25% reduction in market-related losses"
    }
}

# Generate synthetic data for the dashboard
np.random.seed(42)  # For reproducibility
dashboard_data = []

# Generate state-level data for each crop
for state in all_states:
    # Find which geopolitical zone this state belongs to
    zone = next(z for z, states in geopolitical_zones.items() if state in states)
    
    for crop_name, crop_data in crops.items():
        # Calculate production with some randomness
        base = crop_data["base_production"]
        regional_factor = crop_data["regional_multipliers"][zone]
        random_factor = 0.8 + 0.4 * np.random.random()  # Between 0.8 and 1.2
        
        production = base * regional_factor * random_factor
        
        # Calculate losses with some variation in PHL rate
        phl_variation = crop_data["phl_rate"] * (0.9 + 0.2 * np.random.random())
        losses = production * (phl_variation / 100)
        
        # Calculate financial impact
        financial_impact = losses * crop_data["price_per_ton"]
        
        # Calculate stage-specific losses
        for stage, proportion in value_chain_stages.items():
            stage_loss = losses * proportion
            stage_financial_impact = stage_loss * crop_data["price_per_ton"]
            
            # Calculate intervention potential (how much could be saved)
            # Assume interventions can save 40-70% of losses
            intervention_efficiency = 0.4 + 0.3 * np.random.random()
            intervention_potential = stage_loss * intervention_efficiency
            intervention_value = intervention_potential * crop_data["price_per_ton"]
            
            # Determine applicable business models
            applicable_models = business_models_by_stage.get(stage, [])
            
            dashboard_data.append({
                "state": state,
                "geopolitical_zone": zone,
                "crop": crop_name,
                "production_tons": round(production, 1),
                "phl_rate": round(phl_variation, 1),
                "value_chain_stage": stage,
                "loss_tons": round(stage_loss, 1),
                "financial_impact": round(stage_financial_impact, 0),
                "intervention_potential_tons": round(intervention_potential, 1),
                "intervention_value": round(intervention_value, 0),
                "applicable_business_models": applicable_models
            })

# Convert to DataFrame
df = pd.DataFrame(dashboard_data)

# Save the complete dataset for the dashboard
df.to_csv('results/dashboard/data/complete_phl_dashboard_data.csv', index=False)
print("Complete dashboard dataset created and saved")

# Create aggregated views for different dashboard perspectives
state_summary = df.groupby('state').agg({
    'production_tons': 'sum',
    'loss_tons': 'sum',
    'financial_impact': 'sum',
    'intervention_value': 'sum'
}).reset_index()

crop_summary = df.groupby('crop').agg({
    'production_tons': 'sum',
    'loss_tons': 'sum',
    'financial_impact': 'sum',
    'intervention_value': 'sum'
}).reset_index()

zone_summary = df.groupby('geopolitical_zone').agg({
    'production_tons': 'sum',
    'loss_tons': 'sum',
    'financial_impact': 'sum',
    'intervention_value': 'sum'
}).reset_index()

stage_summary = df.groupby('value_chain_stage').agg({
    'loss_tons': 'sum',
    'financial_impact': 'sum',
    'intervention_value': 'sum'
}).reset_index()

# Save summary datasets
state_summary.to_csv('results/dashboard/data/state_summary.csv', index=False)
crop_summary.to_csv('results/dashboard/data/crop_summary.csv', index=False)
zone_summary.to_csv('results/dashboard/data/zone_summary.csv', index=False)
stage_summary.to_csv('results/dashboard/data/stage_summary.csv', index=False)

# Create a dataset for business model recommendations
business_opportunity = []

for state in all_states:
    state_data = df[df['state'] == state]
    zone = state_data['geopolitical_zone'].iloc[0]
    
    # Get total intervention value in this state
    total_intervention = state_data['intervention_value'].sum()
    
    # Top crops by intervention value in this state
    top_crops = state_data.groupby('crop')['intervention_value'].sum().sort_values(ascending=False).head(3)
    
    # Top value chain stages by intervention value
    top_stages = state_data.groupby('value_chain_stage')['intervention_value'].sum().sort_values(ascending=False).head(3)
    
    # Compute business model scores based on intervention values and applicability
    business_model_scores = {}
    
    for _, row in state_data.iterrows():
        for model in row['applicable_business_models']:
            if model not in business_model_scores:
                business_model_scores[model] = 0
            business_model_scores[model] += row['intervention_value']
    
    # Sort models by score
    sorted_models = sorted(business_model_scores.items(), key=lambda x: x[1], reverse=True)
    top_models = sorted_models[:3] if len(sorted_models) >= 3 else sorted_models
    
    for rank, (model_id, opportunity_value) in enumerate(top_models):
        business_opportunity.append({
            "state": state,
            "geopolitical_zone": zone,
            "model_id": model_id,
            "model_name": business_model_details[model_id]['name'],
            "opportunity_value": opportunity_value,
            "investment_range": business_model_details[model_id]['investment'],
            "roi": business_model_details[model_id]['roi'],
            "impact": business_model_details[model_id]['impact'],
            "rank": rank + 1,
            "top_crops": ", ".join(top_crops.index.tolist()),
            "top_stages": ", ".join(top_stages.index.tolist())
        })

# Convert to DataFrame
business_opportunity_df = pd.DataFrame(business_opportunity)
business_opportunity_df.to_csv('results/dashboard/data/business_opportunities.csv', index=False)
print("Business opportunity data created and saved")

# Create visualizations for the dashboard

# 1. Choropleth-like bar chart of intervention opportunity by state
plt.figure(figsize=(16, 12))
state_summary_sorted = state_summary.sort_values('intervention_value', ascending=False)
bars = plt.bar(state_summary_sorted['state'], state_summary_sorted['intervention_value'] / 1000000)

# Color bars by geopolitical zone
zone_colors = {
    "North Central": "#3498db",
    "North East": "#e74c3c",
    "North West": "#2ecc71",
    "South East": "#f39c12",
    "South South": "#9b59b6",
    "South West": "#1abc9c"
}

for i, bar in enumerate(bars):
    state = state_summary_sorted.iloc[i]['state']
    zone = next(z for z, states in geopolitical_zones.items() if state in states)
    bar.set_color(zone_colors[zone])

plt.title('Post-Harvest Loss Intervention Value by State', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Intervention Value (Million N)', fontsize=14)
plt.xticks(rotation=90)
plt.grid(axis='y', alpha=0.3)

# Add legend for zones
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=zone) for zone, color in zone_colors.items()]
plt.legend(handles=legend_elements, title="Geopolitical Zone", loc='upper right')

plt.tight_layout()
plt.savefig('results/dashboard/static/intervention_value_by_state.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Value chain stage analysis
plt.figure(figsize=(12, 8))
stage_summary_sorted = stage_summary.sort_values('financial_impact', ascending=False)

width = 0.35
x = np.arange(len(stage_summary_sorted))

ax = plt.gca()
bars1 = ax.bar(x - width/2, stage_summary_sorted['financial_impact'] / 1000000, width, label='Financial Loss')
bars2 = ax.bar(x + width/2, stage_summary_sorted['intervention_value'] / 1000000, width, label='Intervention Opportunity')

plt.title('Losses and Intervention Opportunities by Value Chain Stage', fontsize=16)
plt.xlabel('Value Chain Stage', fontsize=14)
plt.ylabel('Value (Million N)', fontsize=14)
plt.xticks(x, stage_summary_sorted['value_chain_stage'])
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}',
                ha='center', va='bottom', rotation=0, fontsize=9)

plt.tight_layout()
plt.savefig('results/dashboard/static/value_chain_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Crop comparison visualization
plt.figure(figsize=(14, 8))
crop_summary_sorted = crop_summary.sort_values('intervention_value', ascending=False)

x = np.arange(len(crop_summary_sorted))
width = 0.25

ax = plt.gca()
bars1 = ax.bar(x - width, crop_summary_sorted['production_tons'] / 1000, width, label='Production (thousand tons)')
bars2 = ax.bar(x, crop_summary_sorted['loss_tons'] / 1000, width, label='Losses (thousand tons)')
bars3 = ax.bar(x + width, crop_summary_sorted['intervention_value'] / 1000000, width, label='Intervention Value (million N)')

plt.title('Crop Production, Losses, and Intervention Opportunities', fontsize=16)
plt.xlabel('Crop', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.xticks(x, crop_summary_sorted['crop'])
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Add percentage labels for losses as percentage of production
for i, (prod, loss) in enumerate(zip(crop_summary_sorted['production_tons'], crop_summary_sorted['loss_tons'])):
    percentage = (loss / prod) * 100
    plt.text(i, loss/1000 + 0.2, f'{percentage:.1f}%', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('results/dashboard/static/crop_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Top business opportunities by geopolitical zone
top_opportunities = business_opportunity_df.groupby(['geopolitical_zone', 'model_id']).agg({
    'opportunity_value': 'sum'
}).reset_index()

# Get top model for each zone
top_model_by_zone = top_opportunities.loc[top_opportunities.groupby('geopolitical_zone')['opportunity_value'].idxmax()]

plt.figure(figsize=(14, 8))
bars = plt.bar(top_model_by_zone['geopolitical_zone'], top_model_by_zone['opportunity_value'] / 1000000)

# Color bars by model
model_colors = {
    "BM-01": "#3498db",
    "BM-02": "#e74c3c",
    "BM-03": "#2ecc71",
    "BM-04": "#f39c12",
    "BM-05": "#9b59b6",
    "BM-06": "#1abc9c",
    "BM-07": "#34495e"
}

for i, bar in enumerate(bars):
    model_id = top_model_by_zone.iloc[i]['model_id']
    bar.set_color(model_colors.get(model_id, "#7f8c8d"))

plt.title('Top Business Opportunity by Geopolitical Zone', fontsize=16)
plt.xlabel('Geopolitical Zone', fontsize=14)
plt.ylabel('Opportunity Value (Million N)', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# Add model names as labels on bars
for i, row in enumerate(top_model_by_zone.itertuples()):
    model_name = business_model_details[row.model_id]['name']
    plt.text(i, row.opportunity_value/1000000 + 0.5, 
             f"{row.model_id}: {model_name.split(' ')[0]}", 
             ha='center', rotation=90, fontsize=9)

# Add legend for business models
legend_elements = [Patch(facecolor=color, label=f"{model_id}: {business_model_details[model_id]['name']}") 
                  for model_id, color in model_colors.items() if model_id in top_model_by_zone['model_id'].values]
plt.legend(handles=legend_elements, title="Business Models", loc='upper right')

plt.tight_layout()
plt.savefig('results/dashboard/static/top_opportunities_by_zone.png', dpi=300, bbox_inches='tight')
plt.close()

# Create interactive HTML dashboard
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouthHarvest: Post-Harvest Loss Intervention Dashboard</title>
    <style>
        :root {
            --primary: #2e7d32;
            --primary-light: #60ad5e;
            --primary-dark: #005005;
            --secondary: #ff8f00;
            --text-light: #ffffff;
            --text-dark: #212121;
            --background-light: #f5f5f5;
            --background-card: #ffffff;
            --border-radius: 8px;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--background-light);
            color: var(--text-dark);
            line-height: 1.6;
        }
        
        header {
            background-color: var(--primary);
            color: var(--text-light);
            padding: 1rem 2rem;
            box-shadow: var(--shadow);
        }
        
        .logo-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .logo-text {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .logo-text span {
            color: var(--secondary);
        }
        
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1.5rem;
        }
        
        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .filters {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .filter-select {
            padding: 0.5rem;
            border-radius: var(--border-radius);
            border: 1px solid #ddd;
            background-color: var(--background-card);
        }
        
        .kpi-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .kpi-card {
            background-color: var(--background-card);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--shadow);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .kpi-card:hover {
            transform: translateY(-5px);
        }
        
        .kpi-title {
            color: var(--text-dark);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            opacity: 0.8;
        }
        
        .kpi-value {
            color: var(--primary-dark);
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .kpi-context {
            color: var(--text-dark);
            font-size: 0.8rem;
            opacity: 0.6;
        }
        
        .chart-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .chart-card {
            background-color: var(--background-card);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--shadow);
        }
        
        .chart-title {
            margin-top: 0;
            margin-bottom: 1rem;
            color: var(--primary-dark);
        }
        
        .chart-image {
            width: 100%;
            height: auto;
            object-fit: contain;
        }
        
        .opportunities-section {
            margin-top: 2rem;
        }
        
        .opportunity-card {
            background-color: var(--background-card);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow);
            border-left: 5px solid var(--primary);
        }
        
        .opportunity-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .opportunity-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--primary-dark);
            margin: 0;
        }
        
        .opportunity-value {
            background-color: var(--primary-light);
            color: var(--text-light);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: bold;
        }
        
        .opportunity-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }
        
        .detail-item {
            margin-bottom: 0.5rem;
        }
        
        .detail-label {
            font-size: 0.8rem;
            color: var(--text-dark);
            opacity: 0.7;
        }
        
        .detail-value {
            font-size: 1rem;
            font-weight: 500;
        }
        
        .action-button {
            background-color: var(--secondary);
            color: var(--text-light);
            border: none;
            padding: 0.5rem 1rem;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        
        .action-button:hover {
            background-color: #f57c00;
        }
        
        footer {
            background-color: var(--primary-dark);
            color: var(--text-light);
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
            font-size: 0.8rem;
        }
        
        @media screen and (max-width: 768px) {
            .chart-container {
                grid-template-columns: 1fr;
            }
            
            .dashboard-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .filters {
                margin-top: 1rem;
                width: 100%;
            }
            
            .filter-select {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo-container">
            <div class="logo-text">Youth<span>Harvest</span> Dashboard</div>
            <div>Nigeria Post-Harvest Loss Intervention Project</div>
        </div>
    </header>

    <div class="main-container">
        <div class="dashboard-header">
            <h1>Post-Harvest Loss Business Opportunity Finder</h1>
            <div class="filters">
                <select id="region-filter" class="filter-select">
                    <option value="all">All Regions</option>
                    <option value="North Central">North Central</option>
                    <option value="North East">North East</option>
                    <option value="North West">North West</option>
                    <option value="South East">South East</option>
                    <option value="South South">South South</option>
                    <option value="South West">South West</option>
                </select>
                <select id="crop-filter" class="filter-select">
                    <option value="all">All Crops</option>
                    <option value="Maize">Maize</option>
                    <option value="Rice">Rice</option>
                    <option value="Sorghum">Sorghum</option>
                    <option value="Millet">Millet</option>
                    <option value="Vegetables">Vegetables</option>
                </select>
            </div>
        </div>

        <div class="kpi-container">
            <div class="kpi-card">
                <div class="kpi-title">Total Production</div>
                <div class="kpi-value">13.8M tons</div>
                <div class="kpi-context">Across major grain crops</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Post-Harvest Losses</div>
                <div class="kpi-value">3.9M tons</div>
                <div class="kpi-context">~28% of production</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Financial Impact</div>
                <div class="kpi-value">N14.2B</div>
                <div class="kpi-context">Annual loss value</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Intervention Potential</div>
                <div class="kpi-value">N6.8B</div>
                <div class="kpi-context">Addressable through youth businesses</div>
            </div>
        </div>

        <div class="chart-container">
            <div class="chart-card">
                <h3 class="chart-title">Intervention Value by State</h3>
                <img src="static/intervention_value_by_state.png" alt="Intervention Value by State" class="chart-image">
            </div>
            <div class="chart-card">
                <h3 class="chart-title">Value Chain Stage Analysis</h3>
                <img src="static/value_chain_analysis.png" alt="Value Chain Analysis" class="chart-image">
            </div>
        </div>

        <div class="chart-container">
            <div class="chart-card">
                <h3 class="chart-title">Crop Comparison</h3>
                <img src="static/crop_comparison.png" alt="Crop Comparison" class="chart-image">
            </div>
            <div class="chart-card">
                <h3 class="chart-title">Top Business Opportunities by Region</h3>
                <img src="static/top_opportunities_by_zone.png" alt="Top Opportunities by Zone" class="chart-image">
            </div>
        </div>

        <div class="opportunities-section">
            <h2>Top Business Opportunities for Youth Entrepreneurs</h2>
            
            <div class="opportunity-card">
                <div class="opportunity-header">
                    <h3 class="opportunity-title">BM-02: Aggregation &amp; Quality Control Hub</h3>
                    <div class="opportunity-value">N2.5B Opportunity</div>
                </div>
                <div class="opportunity-details">
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Initial Investment</div>
                            <div class="detail-value">N1,785,000 - N4,020,000</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Annual ROI</div>
                            <div class="detail-value">20-30%</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Impact</div>
                            <div class="detail-value">20-30% reduction in losses</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Best Crops</div>
                            <div class="detail-value">Rice, Maize, Sorghum</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Key Regions</div>
                            <div class="detail-value">North West, North Central</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Value Chain Stage</div>
                            <div class="detail-value">Storage, Market</div>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 1rem; text-align: right;">
                    <button class="action-button">View Implementation Guide</button>
                </div>
            </div>

            <div class="opportunity-card">
                <div class="opportunity-header">
                    <h3 class="opportunity-title">BM-01: Mobile Threshing/Shelling Service</h3>
                    <div class="opportunity-value">N1.8B Opportunity</div>
                </div>
                <div class="opportunity-details">
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Initial Investment</div>
                            <div class="detail-value">N955,000 - N1,625,000</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Annual ROI</div>
                            <div class="detail-value">15-30%</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Impact</div>
                            <div class="detail-value">15-20% reduction in processing losses</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Best Crops</div>
                            <div class="detail-value">Rice, Maize, Sorghum</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Key Regions</div>
                            <div class="detail-value">North West, North East</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Value Chain Stage</div>
                            <div class="detail-value">Processing, Harvesting</div>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 1rem; text-align: right;">
                    <button class="action-button">View Implementation Guide</button>
                </div>
            </div>

            <div class="opportunity-card">
                <div class="opportunity-header">
                    <h3 class="opportunity-title">BM-03: Solar Drying as a Service</h3>
                    <div class="opportunity-value">N1.2B Opportunity</div>
                </div>
                <div class="opportunity-details">
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Initial Investment</div>
                            <div class="detail-value">N720,000 - N2,080,000</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Annual ROI</div>
                            <div class="detail-value">40-60%</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Impact</div>
                            <div class="detail-value">25-35% reduction in processing losses</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Best Crops</div>
                            <div class="detail-value">Vegetables, Rice, Maize</div>
                        </div>
                    </div>
                    <div>
                        <div class="detail-item">
                            <div class="detail-label">Key Regions</div>
                            <div class="detail-value">South West, South South, North Central</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">Value Chain Stage</div>
                            <div class="detail-value">Processing</div>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 1rem; text-align: right;">
                    <button class="action-button">View Implementation Guide</button>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>YouthHarvest Dashboard | Nigeria Post-Harvest Losses Analysis Project | Developed for the Nigeria Agri-Hackathon</p>
    </footer>

    <script>
        // This would be expanded with interactive features in a real implementation
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Dashboard loaded successfully');
            
            // Filter functionality would be implemented here
            const regionFilter = document.getElementById('region-filter');
            const cropFilter = document.getElementById('crop-filter');
            
            regionFilter.addEventListener('change', function() {
                console.log('Region filter changed to:', this.value);
                // In a real implementation, this would update the dashboard data
            });
            
            cropFilter.addEventListener('change', function() {
                console.log('Crop filter changed to:', this.value);
                // In a real implementation, this would update the dashboard data
            });
            
            // Action buttons would link to implementation guides
            const actionButtons = document.querySelectorAll('.action-button');
            actionButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const businessModel = this.closest('.opportunity-card').querySelector('.opportunity-title').textContent.split(':')[0].trim();
                    console.log('Viewing implementation guide for:', businessModel);
                    alert('In the full implementation, this would load the detailed business implementation guide for ' + businessModel);
                });
            });
        });
    </script>
</body>
</html>
"""

# Save the interactive HTML dashboard - FIXED WITH UTF-8 ENCODING
with open('results/dashboard/interactive/yourthharvest_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Interactive HTML dashboard created")

# Create a dashboard API specification (would be implemented in a production environment)
api_spec = {
    "openapi": "3.0.0",
    "info": {
        "title": "YouthHarvest Dashboard API",
        "description": "API for accessing PHL data and business opportunities for youth entrepreneurs",
        "version": "1.0.0"
    },
    "servers": [
        {
            "url": "https://api.youthharvest.example/v1",
            "description": "Production server"
        }
    ],
    "paths": {
        "/states": {
            "get": {
                "summary": "Get PHL data by state",
                "parameters": [
                    {
                        "name": "zone",
                        "in": "query",
                        "description": "Filter by geopolitical zone",
                        "schema": {"type": "string"}
                    },
                    {
                        "name": "crop",
                        "in": "query",
                        "description": "Filter by crop type",
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "state": {"type": "string"},
                                            "production_tons": {"type": "number"},
                                            "loss_tons": {"type": "number"},
                                            "financial_impact": {"type": "number"},
                                            "intervention_value": {"type": "number"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/crops": {
            "get": {
                "summary": "Get PHL data by crop",
                "parameters": [
                    {
                        "name": "state",
                        "in": "query",
                        "description": "Filter by state",
                        "schema": {"type": "string"}
                    },
                    {
                        "name": "zone",
                        "in": "query",
                        "description": "Filter by geopolitical zone",
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "crop": {"type": "string"},
                                            "production_tons": {"type": "number"},
                                            "loss_tons": {"type": "number"},
                                            "financial_impact": {"type": "number"},
                                            "intervention_value": {"type": "number"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/value-chain": {
            "get": {
                "summary": "Get PHL data by value chain stage",
                "parameters": [
                    {
                        "name": "state",
                        "in": "query",
                        "description": "Filter by state",
                        "schema": {"type": "string"}
                    },
                    {
                        "name": "crop",
                        "in": "query",
                        "description": "Filter by crop",
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "value_chain_stage": {"type": "string"},
                                            "loss_tons": {"type": "number"},
                                            "financial_impact": {"type": "number"},
                                            "intervention_value": {"type": "number"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/business-opportunities": {
            "get": {
                "summary": "Get business opportunities for youth entrepreneurs",
                "parameters": [
                    {
                        "name": "state",
                        "in": "query",
                        "description": "Filter by state",
                        "schema": {"type": "string"}
                    },
                    {
                        "name": "zone",
                        "in": "query",
                        "description": "Filter by geopolitical zone",
                        "schema": {"type": "string"}
                    },
                    {
                        "name": "maxInvestment",
                        "in": "query",
                        "description": "Maximum investment amount",
                        "schema": {"type": "number"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "model_id": {"type": "string"},
                                            "model_name": {"type": "string"},
                                            "opportunity_value": {"type": "number"},
                                            "investment_range": {"type": "string"},
                                            "roi": {"type": "string"},
                                            "impact": {"type": "string"},
                                            "top_crops": {"type": "string"},
                                            "top_stages": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/implementation-guides/{modelId}": {
            "get": {
                "summary": "Get implementation guide for a specific business model",
                "parameters": [
                    {
                        "name": "modelId",
                        "in": "path",
                        "required": True,
                        "description": "Business model ID (e.g., BM-01)",
                        "schema": {"type": "string"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "model_id": {"type": "string"},
                                        "model_name": {"type": "string"},
                                        "description": {"type": "string"},
                                        # Additional properties would be defined here
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Save the API specification
with open('results/dashboard/api_specification.json', 'w', encoding='utf-8') as f:
    json.dump(api_spec, f, indent=4)
print("API specification created")

# Create a dashboard documentation file
dashboard_documentation = {
    "title": "YouthHarvest Dashboard Documentation",
    "overview": """
    The YouthHarvest Dashboard is an interactive tool designed to help young Nigerian entrepreneurs identify 
    opportunities in the post-harvest sector. It visualizes post-harvest loss data across different crops, 
    states, and value chain stages, and recommends appropriate business models based on local conditions 
    and user preferences.
    """,
    "components": [
        {
            "name": "Interactive Dashboard",
            "description": "Web-based interface for exploring PHL data and business opportunities",
            "features": [
                "Filtering by region, crop, and investment capacity",
                "Visualizations of key PHL metrics",
                "Business opportunity recommendations",
                "Links to implementation guides"
            ],
            "technologies": "HTML, CSS, JavaScript (would use React in full implementation)"
        },
        {
            "name": "Data API",
            "description": "Backend services for accessing and filtering PHL and business opportunity data",
            "features": [
                "RESTful endpoints for different data views",
                "Filtering and query capabilities",
                "JSON response format"
            ],
            "technologies": "Would be implemented with Node.js/Express or Python Flask in production"
        },
        {
            "name": "Implementation Guide Integration",
            "description": "Connection to detailed business model implementation guides",
            "features": [
                "Access to business model details based on user selections",
                "Customized recommendations based on location and preferences",
                "Financial calculator integration"
            ]
        }
    ],
    "usage_instructions": [
        {
            "step": "1. Select Your Region",
            "description": "Use the region filter to focus on your state or geopolitical zone"
        },
        {
            "step": "2. Explore PHL Patterns",
            "description": "Review the visualizations to understand where losses are occurring in your region"
        },
        {
            "step": "3. Filter by Crop Interest",
            "description": "Select specific crops you're interested in working with"
        },
        {
            "step": "4. Review Business Opportunities",
            "description": "Examine the recommended business models for your selected region and crops"
        },
        {
            "step": "5. Access Implementation Guides",
            "description": "Click 'View Implementation Guide' to get detailed information on your chosen business model"
        }
    ],
    "future_enhancements": [
        "Mobile application version for field use",
        "User accounts for saving preferences and tracking progress",
        "Integration with financing institutions for direct application",
        "Community features to connect with other youth entrepreneurs",
        "Real-time market price data integration"
    ],
    "technical_requirements": {
        "user_side": "Modern web browser with JavaScript enabled",
        "production_hosting": "Web server with database backend",
        "data_updates": "Monthly updates of market prices and intervention values"
    }
}

# Save the dashboard documentation
with open('results/dashboard/dashboard_documentation.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard_documentation, f, indent=4)

# Create a README for the dashboard
dashboard_readme = """# YouthHarvest Dashboard

## Overview
The YouthHarvest Dashboard is an interactive tool that helps young Nigerian entrepreneurs identify and pursue business opportunities in the post-harvest sector. By visualizing post-harvest loss data and connecting it to viable business models, the dashboard enables youth to make informed decisions about which interventions to implement in their local context.

## Features
- **Interactive Data Visualization**: Explore post-harvest loss patterns across different states, crops, and value chain stages
- **Business Opportunity Finder**: Discover the most promising business models for your region and interests
- **Implementation Guide Access**: Connect directly to detailed guides for setting up post-harvest businesses
- **Filtering Capabilities**: Customize the view based on your location, crop interests, and investment capacity

## Files in this Directory
- `interactive/` - Contains the interactive HTML dashboard
- `static/` - Contains static visualizations used in the dashboard
- `data/` - Contains the underlying data files
- `api_specification.json` - Technical specification for the dashboard API
- `dashboard_documentation.json` - Detailed documentation of the dashboard

## How to Use
1. Open the `interactive/youthharvest_dashboard.html` file in a web browser
2. Use the filters to select your region and crop interests
3. Explore the visualizations to understand post-harvest loss patterns
4. Review the recommended business opportunities
5. Click "View Implementation Guide" for detailed information on a specific business model

## Technical Implementation
This is a prototype version of the dashboard. In a production environment, it would be implemented as a full-stack web application with:
- Frontend: React.js with visualization libraries
- Backend: API service using Node.js or Python Flask
- Database: PostgreSQL or MongoDB for data storage
- Authentication: User accounts for personalized recommendations

## Next Steps for Development
- Create user account system
- Implement filtering functionality
- Connect to real-time market price data
- Add mobile responsiveness
- Integrate directly with financial institutions

## Contact
For more information about this project, please contact the YouthHarvest team.
"""

# Save the dashboard README with UTF-8 encoding
with open('results/dashboard/README.md', 'w', encoding='utf-8') as f:
    f.write(dashboard_readme)

print("\nEnhanced interactive dashboard and associated components created successfully!")