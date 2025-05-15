import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib
from datetime import datetime

# Ensure directories exist
os.makedirs('results/dashboard/predictive_model', exist_ok=True)
os.makedirs('results/dashboard/predictive_model/data', exist_ok=True)
os.makedirs('results/dashboard/predictive_model/visualizations', exist_ok=True)
os.makedirs('results/dashboard/predictive_model/model_files', exist_ok=True)

# Generate synthetic data for training the PHL predictive model
np.random.seed(42)  # For reproducibility

# Define parameters that influence post-harvest losses
# These parameters will be used to create our synthetic training data
params = {
    "geopolitical_zones": ["North Central", "North East", "North West", "South East", "South South", "South West"],
    "crops": ["Maize", "Rice", "Sorghum", "Millet", "Vegetables"],
    "seasons": ["Wet", "Dry"],
    "value_chain_stages": ["Harvesting", "Processing", "Storage", "Transportation", "Market"],
    "transportation_distance_km": {
        "min": 5,
        "max": 200
    },
    "storage_duration_days": {
        "min": 1,
        "max": 180
    },
    "harvesting_method": ["Manual", "Mechanical", "Semi-Mechanical"],
    "processing_method": ["Traditional", "Improved Traditional", "Modern", "None"],
    "storage_type": ["Open air", "Bags in house", "Traditional structure", "Improved structure", "Modern warehouse"],
    "transportation_type": ["Head load", "Animal drawn", "Motorcycle", "Small vehicle", "Large truck"],
    "market_type": ["Local/Village", "District", "Regional/State", "Export"]
}

# Base loss rates for each crop (percentage)
base_loss_rates = {
    "Maize": 28,
    "Rice": 32,
    "Sorghum": 25,
    "Millet": 22,
    "Vegetables": 45
}

# Influence factors for each parameter on post-harvest losses
# These will be used to adjust the base loss rates
influence_factors = {
    "geopolitical_zones": {
        "North Central": 0.0,  # baseline
        "North East": 0.05,    # 5% higher losses than baseline
        "North West": -0.02,   # 2% lower losses than baseline
        "South East": 0.03,
        "South South": 0.08,
        "South West": -0.04
    },
    "seasons": {
        "Wet": 0.15,    # 15% higher losses in wet season
        "Dry": -0.10    # 10% lower losses in dry season
    },
    "value_chain_stages": {
        "Harvesting": {
            "influence": 0.2,  # Harvesting contributes 20% of total losses
            "methods": {
                "Manual": 0.0,           # baseline
                "Semi-Mechanical": -0.3,  # 30% reduction compared to manual
                "Mechanical": -0.6       # 60% reduction compared to manual
            }
        },
        "Processing": {
            "influence": 0.25,  # Processing contributes 25% of total losses
            "methods": {
                "None": 0.0,             # No processing (baseline for some crops)
                "Traditional": 0.0,      # baseline for crops that need processing
                "Improved Traditional": -0.4,
                "Modern": -0.7
            }
        },
        "Storage": {
            "influence": 0.35,  # Storage contributes 35% of total losses
            "methods": {
                "Open air": 0.0,             # baseline
                "Bags in house": -0.2,
                "Traditional structure": -0.3,
                "Improved structure": -0.6,
                "Modern warehouse": -0.85
            },
            "duration_factor": 0.001   # Loss increases by 0.1% per day of storage (simplified)
        },
        "Transportation": {
            "influence": 0.15,  # Transportation contributes 15% of total losses
            "methods": {
                "Head load": 0.0,         # baseline
                "Animal drawn": -0.1,
                "Motorcycle": -0.3,
                "Small vehicle": -0.5,
                "Large truck": -0.6
            },
            "distance_factor": 0.0005   # Loss increases by 0.05% per km transported (simplified)
        },
        "Market": {
            "influence": 0.05,  # Market handling contributes 5% of total losses
            "methods": {
                "Local/Village": 0.0,      # baseline
                "District": -0.2,
                "Regional/State": -0.4,
                "Export": -0.7
            }
        }
    }
}

# Generate synthetic dataset for model training
def generate_synthetic_phl_data(num_samples=5000):
    data = []
    
    for _ in range(num_samples):
        # Select random values for each parameter
        crop = np.random.choice(params["crops"])
        zone = np.random.choice(params["geopolitical_zones"])
        season = np.random.choice(params["seasons"])
        stage = np.random.choice(params["value_chain_stages"])
        base_loss = base_loss_rates[crop]
        
        # Adjust loss based on geopolitical zone
        zone_factor = influence_factors["geopolitical_zones"][zone]
        
        # Adjust loss based on season
        season_factor = influence_factors["seasons"][season]
        
        # Get stage-specific parameters
        if stage == "Harvesting":
            method = np.random.choice(params["harvesting_method"])
            method_influence = influence_factors["value_chain_stages"][stage]["methods"][method]
            stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + method_influence)
            distance_km = 0
            duration_days = 0
            
        elif stage == "Processing":
            method = np.random.choice(params["processing_method"])
            method_influence = influence_factors["value_chain_stages"][stage]["methods"][method]
            stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + method_influence)
            distance_km = 0
            duration_days = 0
            
        elif stage == "Storage":
            method = np.random.choice(params["storage_type"])
            duration_days = np.random.randint(params["storage_duration_days"]["min"], params["storage_duration_days"]["max"])
            method_influence = influence_factors["value_chain_stages"][stage]["methods"][method]
            duration_influence = duration_days * influence_factors["value_chain_stages"][stage]["duration_factor"]
            stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + method_influence + duration_influence)
            distance_km = 0
            
        elif stage == "Transportation":
            method = np.random.choice(params["transportation_type"])
            distance_km = np.random.randint(params["transportation_distance_km"]["min"], params["transportation_distance_km"]["max"])
            method_influence = influence_factors["value_chain_stages"][stage]["methods"][method]
            distance_influence = distance_km * influence_factors["value_chain_stages"][stage]["distance_factor"]
            stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + method_influence + distance_influence)
            duration_days = 0
            
        else:  # Market
            method = np.random.choice(params["market_type"])
            method_influence = influence_factors["value_chain_stages"][stage]["methods"][method]
            stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + method_influence)
            distance_km = 0
            duration_days = 0
        
        # Calculate total adjusted loss for this specific scenario
        adjusted_stage_loss = stage_loss * (1 + zone_factor + season_factor)
        
        # Add some random noise to make the data more realistic
        noise = np.random.normal(0, adjusted_stage_loss * 0.05)  # 5% noise
        final_loss = max(0, min(100, adjusted_stage_loss + noise))  # Ensure loss is between 0-100%
        
        # Calculate hypothetical intervention impact
        # Assume modern methods can achieve at minimum 50% reduction in losses
        if stage == "Harvesting":
            best_method = "Mechanical"
        elif stage == "Processing":
            best_method = "Modern"
        elif stage == "Storage":
            best_method = "Modern warehouse"
        elif stage == "Transportation":
            best_method = "Large truck"
        else:  # Market
            best_method = "Export"
            
        # Calculate potential loss with best method
        if stage == "Harvesting" or stage == "Processing" or stage == "Market":
            best_method_influence = influence_factors["value_chain_stages"][stage]["methods"][best_method]
            best_stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + best_method_influence)
            best_adjusted_loss = best_stage_loss * (1 + zone_factor + season_factor)
        elif stage == "Storage":
            best_method_influence = influence_factors["value_chain_stages"][stage]["methods"][best_method]
            # Still account for duration, but with better storage
            duration_influence = duration_days * influence_factors["value_chain_stages"][stage]["duration_factor"] * 0.3  # Reduced effect of duration
            best_stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + best_method_influence + duration_influence)
            best_adjusted_loss = best_stage_loss * (1 + zone_factor + season_factor)
        else:  # Transportation
            best_method_influence = influence_factors["value_chain_stages"][stage]["methods"][best_method]
            # Still account for distance, but with better transportation
            distance_influence = distance_km * influence_factors["value_chain_stages"][stage]["distance_factor"] * 0.2  # Reduced effect of distance
            best_stage_loss = base_loss * influence_factors["value_chain_stages"][stage]["influence"] * (1 + best_method_influence + distance_influence)
            best_adjusted_loss = best_stage_loss * (1 + zone_factor + season_factor)
            
        intervention_impact = final_loss - best_adjusted_loss
        
        # Add record to dataset
        data.append({
            "crop": crop,
            "geopolitical_zone": zone,
            "season": season,
            "value_chain_stage": stage,
            "method": method,
            "transportation_distance_km": distance_km,
            "storage_duration_days": duration_days,
            "base_loss_rate": base_loss,
            "actual_loss_percentage": final_loss,
            "potential_reduction": intervention_impact,
            "best_practice_method": best_method
        })
    
    return pd.DataFrame(data)

# Generate the training dataset
print("Generating synthetic data for PHL prediction model...")
phl_data = generate_synthetic_phl_data(10000)

# Save the raw dataset
phl_data.to_csv('results/dashboard/predictive_model/data/phl_training_data.csv', index=False)
print(f"Training data generated with {len(phl_data)} samples")

# Data preprocessing for model training
def preprocess_data(df):
    # Create a copy of the dataframe to avoid modifying the original
    processed_df = df.copy()
    
    # Encode categorical variables
    categorical_cols = ['crop', 'geopolitical_zone', 'season', 'value_chain_stage', 'method']
    encoders = {}
    
    for col in categorical_cols:
        encoder = LabelEncoder()
        processed_df[col + '_encoded'] = encoder.fit_transform(processed_df[col])
        encoders[col] = encoder
    
    # Select features for model training
    features = [
        'crop_encoded', 'geopolitical_zone_encoded', 'season_encoded', 
        'value_chain_stage_encoded', 'method_encoded', 
        'transportation_distance_km', 'storage_duration_days', 'base_loss_rate'
    ]
    
    # Target variable
    target = 'actual_loss_percentage'
    
    return processed_df, features, target, encoders

# Preprocess data for model training
processed_data, features, target, encoders = preprocess_data(phl_data)

# Save the encoders for future use
joblib.dump(encoders, 'results/dashboard/predictive_model/model_files/categorical_encoders.joblib')

# Split data into training and testing sets
X = processed_data[features]
y = processed_data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
print("Training PHL prediction model...")
model = RandomForestRegressor(n_estimators=100, min_samples_leaf=2, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation:")
print(f"  Mean Absolute Error: {mae:.2f}%")
print(f"  Root Mean Squared Error: {rmse:.2f}%")
print(f"  R² Score: {r2:.3f}")

# Save model performance metrics
model_metrics = {
    "mean_absolute_error": mae,
    "root_mean_squared_error": rmse,
    "r_squared": r2,
    "training_samples": len(X_train),
    "testing_samples": len(X_test),
    "model_type": "RandomForestRegressor",
    "model_parameters": {
        "n_estimators": 100,
        "min_samples_leaf": 2
    },
    "date_trained": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open('results/dashboard/predictive_model/model_files/model_metrics.json', 'w') as f:
    json.dump(model_metrics, f, indent=4)

# Save the trained model
joblib.dump(model, 'results/dashboard/predictive_model/model_files/phl_prediction_model.joblib')
print("Model saved successfully")

# Generate feature importance visualization
feature_importance = model.feature_importances_
feature_names = features

plt.figure(figsize=(10, 6))
importance_df = pd.DataFrame({'feature': feature_names, 'importance': feature_importance})
importance_df = importance_df.sort_values('importance', ascending=False)

plt.barh(importance_df['feature'], importance_df['importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance for PHL Prediction')
plt.tight_layout()
plt.savefig('results/dashboard/predictive_model/visualizations/feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate actual vs. predicted visualization
plt.figure(figsize=(10, 8))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Loss Percentage')
plt.ylabel('Predicted Loss Percentage')
plt.title('Actual vs. Predicted Post