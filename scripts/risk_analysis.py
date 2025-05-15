import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json

# Ensure directories exist
os.makedirs('results/interventions/risks', exist_ok=True)

# Read the comprehensive risk register that was previously created
risk_df = pd.read_csv('results/interventions/risks/comprehensive_risk_register.csv')

print("Columns available in risk_df:", risk_df.columns.tolist())

# The error is happening because 'mitigation_strategies' is already a list, not a string
# Fix: Check if the value is a string before trying to split it
def count_strategies(strategies):
    if isinstance(strategies, str):
        return len(strategies.split('; '))
    elif isinstance(strategies, list):
        return len(strategies)
    else:
        return 0

# Apply the fixed function to count strategies
risk_df['num_strategies'] = risk_df['mitigation_strategies'].apply(count_strategies)

# Same approach for root causes
def count_causes(causes):
    if isinstance(causes, str):
        return len(causes.split('; '))
    elif isinstance(causes, list):
        return len(causes)
    else:
        return 0

risk_df['num_causes'] = risk_df['root_causes'].apply(count_causes)

# Create risk vs mitigation analysis visualization
plt.figure(figsize=(12, 8))
plt.scatter(
    risk_df['num_causes'],
    risk_df['num_strategies'],
    s=100,
    c=risk_df['risk_score'],
    cmap='YlOrRd',
    alpha=0.7
)

# Add risk IDs as labels
for idx, risk in risk_df.iterrows():
    plt.annotate(
        risk['risk_id'],
        (risk['num_causes'], risk['num_strategies']),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )

plt.xlabel('Number of Root Causes Identified', fontsize=12)
plt.ylabel('Number of Mitigation Strategies Developed', fontsize=12)
plt.title('Risk Analysis: Causes vs. Mitigation Strategies', fontsize=14)
plt.grid(True, alpha=0.3)
plt.colorbar(label='Risk Score')
plt.tight_layout()
plt.savefig('results/interventions/risks/risk_mitigation_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("Risk mitigation analysis visualization saved")

# Check for required columns before grouping
required_columns = ['category', 'risk_score', 'likelihood_score', 'impact_score', 'num_strategies']
missing_columns = [col for col in required_columns if col not in risk_df.columns]

if missing_columns:
    print(f"Warning: Missing columns: {missing_columns}. Adding dummy columns for analysis.")
    for col in missing_columns:
        if col == 'likelihood_score':
            # Map likelihood values to scores if the column exists
            if 'likelihood' in risk_df.columns:
                likelihood_map = {"Low": 1, "Medium": 2, "High": 3}
                risk_df['likelihood_score'] = risk_df['likelihood'].map(likelihood_map)
            else:
                risk_df['likelihood_score'] = 2  # Default medium value
        elif col == 'impact_score':
            # Map impact values to scores if the column exists
            if 'impact' in risk_df.columns:
                impact_map = {"Low": 1, "Medium": 2, "High": 3}
                risk_df['impact_score'] = risk_df['impact'].map(impact_map)
            else:
                risk_df['impact_score'] = 2  # Default medium value
        else:
            risk_df[col] = 0  # Add dummy column

# Now we can safely group by category
category_analysis = risk_df.groupby('category').agg({
    'risk_score': ['mean', 'max', 'count'],
    'likelihood_score': 'mean',
    'impact_score': 'mean',
    'num_strategies': 'mean'
}).reset_index()

# Create a consolidated chart showing risk categories
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for number of risks by category
bars = ax1.bar(
    category_analysis['category'],
    category_analysis[('risk_score', 'count')],
    alpha=0.7,
    color='lightblue',
    label='Number of Risks'
)

# Add labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2.,
        height + 0.1,
        f'{int(height)}',
        ha='center',
        fontsize=9
    )

ax1.set_xlabel('Risk Category', fontsize=12)
ax1.set_ylabel('Number of Risks', fontsize=12)
ax1.tick_params(axis='x', rotation=45)

# Create a second y-axis for average risk score
ax2 = ax1.twinx()
ax2.plot(
    category_analysis['category'],
    category_analysis[('risk_score', 'mean')],
    'ro-',
    linewidth=2,
    markersize=8,
    label='Avg Risk Score'
)

# Add average risk score labels
for i, score in enumerate(category_analysis[('risk_score', 'mean')]):
    ax2.text(
        i,
        score + 0.2,
        f'{score:.1f}',
        ha='center',
        fontsize=9,
        color='red'
    )

ax2.set_ylabel('Average Risk Score', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add a title and legend
plt.title('Risk Analysis by Category', fontsize=14)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('results/interventions/risks/risk_category_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("Risk category analysis visualization saved")

print("\nRisk analysis corrections completed successfully!")