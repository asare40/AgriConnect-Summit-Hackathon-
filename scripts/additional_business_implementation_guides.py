def plot_implementation_roadmap(data, save_path='reports/figures/implementation_roadmap.png'):
    """Generate implementation roadmap visualization"""
    impl_data = data['implementation_phases']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create timeline visualization
    phases = impl_data['phase']
    timelines = impl_data['timeline']
    targets = impl_data['youth_target']
    
    # Plot phases as timeline segments
    timeline_positions = [0, 12, 24, 36]
    for i in range(len(phases)):
        # Plot timeline
        ax.plot([timeline_positions[i], timeline_positions[i+1]], [1, 1], 'o-', linewidth=3, 
               color=sns.color_palette('viridis', 3)[i], markersize=10)
        
        # Add phase label
        ax.text((timeline_positions[i] + timeline_positions[i+1])/2, 1.1, phases[i], 
               ha='center', fontsize=12, weight='bold',
               bbox=dict(boxstyle="round,pad=0.3", fc=sns.color_palette('viridis', 3)[i], alpha=0.3))
        
        # Safely handle regions and business models without eval()
        regions = impl_data['regions'].iloc[i]
        if isinstance(regions, list):
            regions_str = ', '.join(regions)
        else:
            regions_str = str(regions)
            
        business_models = impl_data['business_models'].iloc[i]
        if isinstance(business_models, list):
            models_str = ', '.join(business_models)
        else:
            models_str = str(business_models)
        
        # Add implementation details
        details = (f"Regions: {regions_str}\n"
                  f"Models: {models_str}\n"
                  f"Target: {targets[i]} youth\n"
                  f"Impact: {impl_data['estimated_impact'].iloc[i]}")
        
        ax.annotate(details, xy=(timeline_positions[i] + 3, 0.85), xytext=(0, -50),
                   textcoords='offset points', va='top',
                   bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.8),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
    
    # Configure axes
    ax.set_ylim(0.5, 1.5)
    ax.set_xlim(-2, 38)
    ax.set_yticks([])
    ax.set_xticks([0, 12, 24, 36])
    ax.set_xticklabels(['Project Start', 'Year 1', 'Year 2', 'Year 3'])
    ax.set_title('YouthHarvest Implementation Roadmap')
    
    # Remove frame
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_pathimport os
import json

# Ensure directories exist
os.makedirs('results/youth_opportunities/implementation_guides', exist_ok=True)
os.makedirs('results/youth_opportunities/case_studies', exist_ok=True)

# Function to save a JSON object to a file with UTF-8 encoding
def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Saved file: {filename}")

# Create and save the business models one by one
# BM-02: Aggregation & Quality Control Hub
bm_02 = {
    "model_id": "BM-02",
    "model_name": "Aggregation & Quality Control Hub",
    "tagline": "Connecting farmers to markets through quality assurance",
    "description": "A youth-managed collection point that aggregates crops from smallholder farmers, ensures quality standards, adds value through sorting, grading, and packaging, and connects to larger markets. This business model reduces post-harvest losses by ensuring proper handling and rapid movement of products through the value chain.",
    "value_proposition": [
        "Reduces post-harvest losses by 20-30% through proper handling and storage",
        "Enables smallholders to access premium markets and better prices",
        "Provides transparent quality assessment and fair pricing",
        "Creates consistent supply for buyers and processors",
        "Speeds movement of products to market, reducing deterioration"
    ],
    "target_crops": ["Maize", "Rice", "Sorghum", "Cowpea", "Soybeans", "Vegetables (selected)"],
    "target_customers": {
        "upstream": [
            "Smallholder farmers (0.5-5 hectares)",
            "Farmer groups and cooperatives",
            "Local traders with ungraded produce"
        ],
        "downstream": [
            "Food processors and manufacturers",
            "Wholesalers and large traders",
            "Institutional buyers (schools, hospitals)",
            "Poultry and livestock feed producers",
            "Exporters (for crops meeting standards)"
        ]
    }
}

# Add equipment needs to BM-02
bm_02["equipment_needs"] = {
    "essential": [
        {"item": "Warehouse/storage space", "specifications": "100-300 square meters, secure, dry", "estimated_cost": "N300,000 - N900,000 annually (lease)", "lifespan": "Ongoing (lease renewal)"},
        {"item": "Weighing scales", "specifications": "Platform scale (300kg) and smaller scales", "estimated_cost": "N60,000 - N120,000", "lifespan": "5-7 years"},
        {"item": "Moisture meters", "specifications": "Digital grain moisture testers (2-3 units)", "estimated_cost": "N45,000 - N100,000", "lifespan": "3-5 years"},
        {"item": "Cleaning and sorting equipment", "specifications": "Manual or small motorized", "estimated_cost": "N150,000 - N500,000", "lifespan": "5-8 years"},
        {"item": "Pallets and tarpaulins", "specifications": "Wooden pallets (20-30), heavy-duty tarpaulins", "estimated_cost": "N80,000 - N150,000", "lifespan": "2-4 years"},
        {"item": "Office equipment", "specifications": "Basic furniture, computer/tablet", "estimated_cost": "N100,000 - N200,000", "lifespan": "3-5 years"},
        {"item": "Packaging materials", "specifications": "Bags, labels, sealing equipment", "estimated_cost": "N50,000 - N150,000 (initial stock)", "lifespan": "Consumable"}
    ],
    "optional": [
        {"item": "Small truck/pickup", "specifications": "1-3 ton capacity", "estimated_cost": "N1,500,000 - N4,000,000", "lifespan": "5-8 years"},
        {"item": "Generator", "specifications": "5-10 kVA", "estimated_cost": "N250,000 - N450,000", "lifespan": "5-7 years"},
        {"item": "Aflatoxin testing kit", "specifications": "Rapid test kit with reader", "estimated_cost": "N150,000 - N300,000", "lifespan": "3-5 years (device), test strips consumable"},
        {"item": "Small processing equipment", "specifications": "Depends on value addition activities", "estimated_cost": "N200,000 - N1,000,000", "lifespan": "5-8 years"}
    ]
}

# Add setup costs to BM-02
bm_02["setup_costs"] = {
    "premises": "N300,000 - N900,000 (annual lease)",
    "equipment": "N785,000 - N1,220,000",
    "licenses_and_permits": "N50,000 - N100,000",
    "staff_training": "N100,000 - N200,000",
    "initial_marketing": "N50,000 - N100,000",
    "working_capital": "N500,000 - N1,500,000",
    "total_initial_investment": "N1,785,000 - N4,020,000"
}

# Add revenue model to BM-02
bm_02["revenue_model"] = {
    "primary_revenue_streams": [
        {
            "stream": "Aggregation margin",
            "description": "Difference between buying price from farmers and selling price to buyers",
            "typical_margin": "5-15% depending on crop and quality",
            "example": "Buy maize at N230/kg, sell at N245/kg (6.5% margin)"
        },
        {
            "stream": "Quality assessment and grading services",
            "description": "Fee charged for testing, cleaning, sorting, and grading",
            "typical_margin": "N100-300 per bag depending on services required",
            "example": "N150 per bag for moisture testing, cleaning, and grading"
        }
    ],
    "secondary_revenue_streams": [
        {
            "stream": "Short-term storage services",
            "description": "Fee for temporary storage of graded products",
            "pricing": "N50-100 per bag per month"
        },
        {
            "stream": "Transportation services",
            "description": "Arranging or providing transport to markets",
            "pricing": "N100-300 per bag depending on distance"
        }
    ],
    "potential_monthly_revenue": "N500,000 - N2,000,000 (varies by season)",
    "annual_revenue_potential": "N3,000,000 - N15,000,000"
}

# Add operating costs to BM-02
bm_02["operating_costs"] = {
    "fixed_costs": {
        "rent": "N25,000 - N75,000 monthly",
        "staff_salaries": "N40,000 - N150,000 monthly (2-5 staff)",
        "utilities": "N15,000 - N40,000 monthly",
        "equipment_maintenance": "N10,000 - N30,000 monthly"
    },
    "variable_costs": {
        "procurement": "70-85% of sales revenue (crop purchase costs)",
        "packaging_materials": "N30-100 per bag processed",
        "fuel_and_transport": "N30,000 - N100,000 monthly (varies with volume)"
    },
    "total_monthly_operating_costs": "N400,000 - N1,800,000",
    "annual_operating_costs": "N2,500,000 - N12,000,000"
}

# Add profitability to BM-02
bm_02["profitability"] = {
    "gross_margin": "10-20% of revenue",
    "monthly_net_profit": "N50,000 - N400,000",
    "annual_net_profit": "N500,000 - N3,000,000",
    "payback_period": "1.5-3 years",
    "roi": "20-30% annually after payback"
}

# Save BM-02 to file
save_json(bm_02, 'results/youth_opportunities/implementation_guides/BM-02_aggregation_quality_control_hub.json')

# Create and save BM-03: Solar Drying as a Service
bm_03 = {
    "model_id": "BM-03",
    "model_name": "Solar Drying as a Service",
    "tagline": "Harnessing the sun for quality preservation",
    "description": "A youth-led business providing efficient solar drying services to farmers using improved solar drying technology. This service dramatically reduces post-harvest losses caused by improper drying, prevents aflatoxin contamination, and improves product quality and shelf life.",
    "value_proposition": [
        "Reduces post-harvest losses by 25-35% through proper moisture reduction",
        "Decreases drying time by 40-60% compared to traditional sun drying",
        "Protects products from contamination, insects, and animals during drying",
        "Improves product quality and extends shelf life significantly",
        "Reduces aflatoxin risk through controlled, faster drying",
        "Uses renewable energy for environmental sustainability"
    ]
}

# Add equipment needs to BM-03
bm_03["equipment_needs"] = {
    "essential": [
        {"item": "Solar dryers", "specifications": "Direct or indirect type, 50-100kg capacity each (2-5 units)", "estimated_cost": "N150,000 - N300,000 per unit", "lifespan": "5-7 years with proper maintenance"},
        {"item": "Moisture meter", "specifications": "Digital, suitable for multiple crop types", "estimated_cost": "N15,000 - N35,000", "lifespan": "3-5 years"},
        {"item": "Weighing scales", "specifications": "Table-top (10kg) and platform (100kg)", "estimated_cost": "N25,000 - N50,000", "lifespan": "4-6 years"},
        {"item": "Processing tables", "specifications": "Stainless steel or food-grade material", "estimated_cost": "N30,000 - N60,000", "lifespan": "5-8 years"}
    ],
    "optional": [
        {"item": "Mobile trailer", "specifications": "For transportable drying service", "estimated_cost": "N200,000 - N500,000", "lifespan": "5-8 years"},
        {"item": "Small generator", "specifications": "1-2 kVA for supplementary power", "estimated_cost": "N45,000 - N85,000", "lifespan": "3-5 years"}
    ]
}

# Add setup costs to BM-03
bm_03["setup_costs"] = {
    "equipment": "N500,000 - N1,500,000 (depending on number of dryers)",
    "site_preparation": "N50,000 - N200,000 (for fixed location)",
    "training": "N30,000 - N80,000",
    "licenses_and_permits": "N20,000 - N50,000",
    "marketing_materials": "N20,000 - N50,000",
    "working_capital": "N100,000 - N200,000",
    "total_investment": "N720,000 - N2,080,000"
}

# Save BM-03 to file
save_json(bm_03, 'results/youth_opportunities/implementation_guides/BM-03_solar_drying_service.json')

# Create a simpler business model comparison tool
comparison_tool = {
    "title": "Post-Harvest Business Model Comparison Tool",
    "description": "This tool helps you compare different youth-appropriate business models in the post-harvest sector to identify which options best match your circumstances, resources, and goals.",
    "models": [
        {
            "model_id": "BM-01",
            "model_name": "Mobile Threshing/Shelling Service",
            "investment_range": "N955,000 - N1,625,000",
            "technical_difficulty": "Medium",
            "roi": "15-30% annually",
            "seasonality": "High (seasonal operation)"
        },
        {
            "model_id": "BM-02", 
            "model_name": "Aggregation & Quality Control Hub",
            "investment_range": "N1,785,000 - N4,020,000",
            "technical_difficulty": "Medium-Low",
            "roi": "20-30% annually",
            "seasonality": "Medium (can operate year-round with crop diversity)"
        },
        {
            "model_id": "BM-03",
            "model_name": "Solar Drying as a Service",
            "investment_range": "N720,000 - N2,080,000",
            "technical_difficulty": "Low",
            "roi": "40-60% annually",
            "seasonality": "Medium-High (dependent on weather and harvest seasons)"
        }
    ]
}

# Save comparison tool to file
save_json(comparison_tool, 'results/youth_opportunities/business_model_comparison_tool.json')

# Create a usage guide for the business models
usage_guide = {
    "title": "How to Use the Youth Business Model Implementation Guides",
    "introduction": "These implementation guides are designed to help young Nigerian entrepreneurs establish viable businesses in the post-harvest sector. Each guide provides information on business setup, operations, financing, and growth strategies.",
    "steps": [
        {
            "step": "1. Assess Your Resources",
            "description": "Begin by evaluating your personal situation, skills, and available resources."
        },
        {
            "step": "2. Select Potential Business Models",
            "description": "Review the available business models and select those that match your skills, interests, and local conditions."
        },
        {
            "step": "3. Conduct Market Assessment",
            "description": "Validate the opportunity by understanding local market conditions and needs."
        },
        {
            "step": "4. Develop Business Plan",
            "description": "Create your specific business plan based on the implementation guide."
        },
        {
            "step": "5. Secure Financing",
            "description": "Explore available financing options to fund your startup."
        }
    ]
}

# Save usage guide to file
save_json(usage_guide, 'results/youth_opportunities/implementation_guides/usage_guide.json')

print("All business model files have been successfully created!")