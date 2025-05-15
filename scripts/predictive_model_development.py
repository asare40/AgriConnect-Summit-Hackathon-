import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

# Ensure directories exist
os.makedirs('results/dashboard/predictive_model', exist_ok=True)

# Create synthetic data for the model development
# In a production environment, this would be actual data from various sources

# Generate base data with states, crops, and seasons
np.random.seed(42)

# Define parameters
num_samples = 1000
states = ["Kano", "Kaduna", "Benue", "Lagos", "Ogun", "Oyo", "Borno", "Adamawa", "Rivers", "Anambra", "Niger", "Plateau"]
crops = ["Maize", "Rice", "Sorghum", "Millet", "Vegetables"]
value_chain_stages = ["Harvesting", "Processing", "Storage", "Transportation", "Market"]

# Create factors that affect post-harvest losses
humidity_by_state = {
    "Kano": 35, "Kaduna": 40, "Benue": 65, "Lagos": 80, "Ogun": 75, "Oyo": 70, 
    "Borno": 30, "Adamawa": 45, "Rivers": 85, "Anambra": 75, "Niger": 50, "Plateau": 55
}

temperature_by_state = {
    "Kano": 33, "Kaduna": 30, "Benue": 28, "Lagos": 27, "Ogun": 27, "Oyo": 28, 
    "Borno": 35, "Adamawa": 32, "Rivers": 26, "Anambra": 27, "Niger": 31, "Plateau": 25
}

infrastructure_score_by_state = {
    "Kano": 65, "Kaduna": 70, "Benue": 45, "Lagos": 85, "Ogun": 75, "Oyo": 70, 
    "Borno": 30, "Adamawa": 40, "Rivers": 60, "Anambra": 55, "Niger": 50, "Plateau": 45
}

base_loss_rate_by_crop = {
    "Maize": 28, "Rice": 30, "Sorghum": 25, "Millet": 22, "Vegetables": 40
}

loss_distribution_by_stage = {
    "Maize": {"Harvesting": 0.15, "Processing": 0.30, "Storage": 0.35, "Transportation": 0.15, "Market": 0.05},
    "Rice": {"Harvesting": 0.10, "Processing": 0.35, "Storage": 0.30, "Transportation": 0.20, "Market": 0.05},
    "Sorghum": {"Harvesting": 0.15, "Processing": 0.25, "Storage": 0.40, "Transportation": 0.15, "Market": 0.05},
    "Millet": {"Harvesting": 0.