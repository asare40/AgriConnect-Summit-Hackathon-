"""
YouthHarvest Project: Stakeholder Report Generator
Date: 2025-05-12
Author: asare40

This script generates a comprehensive stakeholder report for the YouthHarvest Project,
including executive summary, data insights, business models, and implementation roadmap.
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import matplotlib.ticker as mtick

# Ensure output directories exist
os.makedirs('reports', exist_ok=True)
os.makedirs('reports/figures', exist_ok=True)

# Set global styling options
plt.style.use('fivethirtyeight')
sns.set_palette('colorblind')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Constants
REPORT_DATE = "May 12, 2025"
REPORT_TITLE = "YouthHarvest Project: Transforming Post-Harvest Losses into Youth Opportunities"

# ============================================================
# DATA PREPARATION AND LOADING
# ============================================================

def load_phl_data():
    """
    Load post-harvest loss data from project files.
    In a real implementation, this would read from actual project data files.
    """
    # Simulating data based on previous information
    # Regional post-harvest loss data
    regions = ['North West', 'North East', 'North Central', 'South West', 'South East', 'South South']
    
    # Loss percentages by region
    regional_loss_pct = pd.DataFrame({
        'Region': regions,
        'Loss_Percentage': [32, 40, 28, 25, 30, 38],
        'Annual_Tonnage_Lost': [1350000, 950000, 780000, 650000, 450000, 550000],
        'Value_Lost_Millions': [850, 650, 520, 480, 320, 420]
    })
    
    # Loss by value chain stage
    stages = ['Harvesting', 'Storage', 'Processing', 'Transportation', 'Marketing']
    stage_loss = pd.DataFrame({
        'Stage': stages,
        'Loss_Percentage': [15, 32, 28, 18, 7]
    })
    
    # Crop-specific losses
    crops = ['Maize', 'Rice', 'Tomatoes', 'Yams', 'Cassava', 'Fruits', 'Vegetables']
    crop_loss = pd.DataFrame({
        'Crop': crops,
        'Loss_Percentage': [25, 30, 45, 35, 28, 40, 42],
        'Annual_Tonnage_Lost': [850000, 750000, 650000, 580000, 480000, 520000, 490000]
    })
    
    # Youth unemployment data by region
    youth_unemployment = pd.DataFrame({
        'Region': regions,
        'Unemployment_Rate': [45, 52, 38, 35, 42, 47],
        'Youth_Population': [4200000, 3800000, 3500000, 4500000, 3200000, 2800000]
    })
    
    # Seasonal variation in losses
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    seasonal_data = pd.DataFrame({
        'Month': months,
        'Loss_Index': [85, 90, 105, 115, 125, 130, 120, 105, 90, 80, 75, 80]
    })
    
    # Business model data
    business_models = [
        {
            "model_id": "BM-01",
            "model_name": "Mobile Threshing/Shelling Service",
            "investment_range": "N955,000 - N1,625,000",
            "annual_roi": "15-30%",
            "payback_period": "2-3 years",
            "job_creation": "2-5 per business",
            "loss_reduction": "15-20%",
            "technical_difficulty": "Medium"
        },
        {
            "model_id": "BM-02",
            "model_name": "Aggregation & Quality Control Hub",
            "investment_range": "N1,785,000 - N4,020,000",
            "annual_roi": "20-30%",
            "payback_period": "1.5-3 years",
            "job_creation": "5-12 per business",
            "loss_reduction": "20-30%",
            "technical_difficulty": "Medium-Low"
        },
        {
            "model_id": "BM-03",
            "model_name": "Solar Drying as a Service",
            "investment_range": "N720,000 - N2,080,000",
            "annual_roi": "40-60%",
            "payback_period": "1-2.5 years",
            "job_creation": "2-6 per business",
            "loss_reduction": "25-35%",
            "technical_difficulty": "Low"
        },
        {
            "model_id": "BM-04",
            "model_name": "Cold Chain Transport Microfranchise",
            "investment_range": "N2,500,000 - N5,000,000",
            "annual_roi": "25-40%",
            "payback_period": "2-4 years",
            "job_creation": "3-8 per business",
            "loss_reduction": "30-45%",
            "technical_difficulty": "Medium"
        },
        {
            "model_id": "BM-05",
            "model_name": "Storage Facility Management",
            "investment_range": "N3,500,000 - N8,000,000",
            "annual_roi": "15-25%",
            "payback_period": "3-5 years",
            "job_creation": "4-10 per business",
            "loss_reduction": "25-40%",
            "technical_difficulty": "Medium"
        },
        {
            "model_id": "BM-06",
            "model_name": "Quality Testing Service",
            "investment_range": "N200,000 - N800,000",
            "annual_roi": "20-35%",
            "payback_period": "1-2 years",
            "job_creation": "1-3 per business",
            "loss_reduction": "10-15%",
            "technical_difficulty": "High"
        },
        {
            "model_id": "BM-07",
            "model_name": "Digital Market Linkage Platform",
            "investment_range": "N1,000,000 - N2,500,000",
            "annual_roi": "35-70%",
            "payback_period": "1-3 years",
            "job_creation": "3-8 per business",
            "loss_reduction": "15-25%",
            "technical_difficulty": "Very High"
        }
    ]
    
    business_models_df = pd.DataFrame(business_models)
    
    # Implementation timeline data
    implementation_phases = [
        {
            "phase": "Phase 1",
            "timeline": "0-12 months",
            "regions": ["North West", "North East"],
            "focus_crops": ["Maize", "Rice", "Tomatoes"],
            "business_models": ["BM-01", "BM-03", "BM-06"],
            "youth_target": 100,
            "estimated_impact": "N450-650 million value preserved"
        },
        {
            "phase": "Phase 2",
            "timeline": "12-24 months",
            "regions": ["North Central", "South West"],
            "focus_crops": ["Yams", "Cassava", "Vegetables", "Maize"],
            "business_models": ["BM-01", "BM-02", "BM-03", "BM-07"],
            "youth_target": 600,
            "estimated_impact": "N1.2-1.8 billion value preserved"
        },
        {
            "phase": "Phase 3",
            "timeline": "24-36 months",
            "regions": ["South East", "South South", "All regions"],
            "focus_crops": ["All major crops"],
            "business_models": ["All models"],
            "youth_target": 6000,
            "estimated_impact": "N4-6 billion value preserved"
        }
    ]
    
    implementation_df = pd.DataFrame(implementation_phases)
    
    return {
        'regional_loss': regional_loss_pct,
        'stage_loss': stage_loss,
        'crop_loss': crop_loss,
        'youth_unemployment': youth_unemployment,
        'seasonal_variation': seasonal_data,
        'business_models': business_models_df,
        'implementation_phases': implementation_df
    }

# ============================================================
# DATA VISUALIZATION FUNCTIONS
# ============================================================

def plot_regional_losses(data, save_path='reports/figures/regional_losses.png'):
    """Generate regional loss map and charts"""
    regional_data = data['regional_loss']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # Plot percentage losses by region
    ax1.bar(regional_data['Region'], regional_data['Loss_Percentage'], color=sns.color_palette('Blues_d', len(regional_data)))
    ax1.set_title('Post-Harvest Loss Percentage by Region')
    ax1.set_ylabel('Loss Percentage (%)')
    ax1.set_ylim(0, 50)
    ax1.set_xticklabels(regional_data['Region'], rotation=45, ha='right')
    for i, v in enumerate(regional_data['Loss_Percentage']):
        ax1.text(i, v + 1, f"{v}%", ha='center')
    
    # Plot absolute losses by region
    ax2.bar(regional_data['Region'], regional_data['Annual_Tonnage_Lost']/1000000, color=sns.color_palette('Reds_d', len(regional_data)))
    ax2.set_title('Annual Post-Harvest Losses by Region')
    ax2.set_ylabel('Million Tons Lost')
    ax2.set_xticklabels(regional_data['Region'], rotation=45, ha='right')
    for i, v in enumerate(regional_data['Annual_Tonnage_Lost']/1000000):
        ax2.text(i, v + 0.05, f"{v:.2f}M", ha='center')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

def plot_value_chain_losses(data, save_path='reports/figures/value_chain_losses.png'):
    """Generate value chain stage loss analysis"""
    stage_data = data['stage_loss']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create pie chart of losses by stage
    wedges, texts, autotexts = ax.pie(
        stage_data['Loss_Percentage'], 
        labels=stage_data['Stage'],
        autopct='%1.1f%%',
        startangle=90,
        shadow=False,
        colors=sns.color_palette('viridis', len(stage_data)),
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}
    )
    
    # Styling
    ax.set_title('Post-Harvest Losses by Value Chain Stage')
    plt.setp(autotexts, size=10, weight="bold")
    
    # Add annotation
    plt.annotate(
        'Storage and Processing\nrepresent over 60% of losses',
        xy=(0.05, 0.05), xycoords='figure fraction',
        bbox=dict(boxstyle="round,pad=0.5", fc="lightyellow", alpha=0.8)
    )
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

def plot_crop_losses(data, save_path='reports/figures/crop_losses.png'):
    """Generate crop-specific loss analysis"""
    crop_data = data['crop_loss']
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot percentage losses by crop
    colors = sns.color_palette('YlOrBr', len(crop_data))
    bars = ax1.barh(crop_data['Crop'], crop_data['Loss_Percentage'], color=colors)
    ax1.set_title('Post-Harvest Loss Percentage by Crop Type')
    ax1.set_xlabel('Loss Percentage (%)')
    ax1.set_xlim(0, 50)
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        ax1.text(width + 1, bar.get_y() + bar.get_height()/2, f"{width}%", 
                ha='left', va='center')
    
    # Plot absolute losses by crop
    bars = ax2.barh(crop_data['Crop'], crop_data['Annual_Tonnage_Lost']/1000, color=colors)
    ax2.set_title('Annual Post-Harvest Losses by Crop Type (Thousand Tons)')
    ax2.set_xlabel('Thousand Tons Lost')
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        ax2.text(width + 10, bar.get_y() + bar.get_height()/2, f"{width/1000:.1f}K", 
                ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

def plot_seasonal_variation(data, save_path='reports/figures/seasonal_variation.png'):
    """Generate seasonal variation in post-harvest losses"""
    seasonal_data = data['seasonal_variation']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create line chart of seasonal variation
    ax.plot(seasonal_data['Month'], seasonal_data['Loss_Index'], marker='o', linewidth=3, color='#FF5722')
    ax.set_title('Seasonal Variation in Post-Harvest Losses')
    ax.set_ylabel('Loss Index (100 = Average)')
    ax.set_ylim(70, 140)
    
    # Add horizontal line at index 100
    ax.axhline(y=100, color='gray', linestyle='--', alpha=0.7)
    
    # Highlight peak loss periods
    ax.fill_between(seasonal_data['Month'], seasonal_data['Loss_Index'], 100, 
                    where=(seasonal_data['Loss_Index'] >= 100),
                    color='#FFAB91', alpha=0.4, label='Above Average Losses')
    
    # Add annotations for key periods
    ax.annotate('Peak Harvest Season', 
                xy=(5, seasonal_data['Loss_Index'][5]), 
                xytext=(5, 135),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
                ha='center')
    
    ax.annotate('Lowest Loss Period', 
                xy=(10, seasonal_data['Loss_Index'][10]), 
                xytext=(10, 60),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
                ha='center')
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

def plot_business_models_comparison(data, save_path='reports/figures/business_models_comparison.png'):
    """Generate business models comparison chart"""
    business_data = data['business_models']
    
    # Extract investment minimums and maximums
    business_data[['investment_min', 'investment_max']] = business_data['investment_range'].str.split(' - ', expand=True)
    business_data['investment_min'] = business_data['investment_min'].str.replace('N', '').str.replace(',', '').astype(float)
    business_data['investment_max'] = business_data['investment_max'].str.replace('N', '').str.replace(',', '').astype(float)
    
    # Extract ROI values
    business_data[['roi_min', 'roi_max']] = business_data['annual_roi'].str.split('-', expand=True)
    business_data['roi_min'] = business_data['roi_min'].str.rstrip('%').astype(float)
    business_data['roi_max'] = business_data['roi_max'].str.rstrip('%').astype(float)
    
    # Extract loss reduction values
    business_data[['loss_red_min', 'loss_red_max']] = business_data['loss_reduction'].str.split('-', expand=True)
    business_data['loss_red_min'] = business_data['loss_red_min'].str.rstrip('%').astype(float)
    business_data['loss_red_max'] = business_data['loss_red_max'].str.rstrip('%').astype(float)
    
    # Calculate averages for plotting
    business_data['avg_investment'] = (business_data['investment_min'] + business_data['investment_max']) / 2 / 1000000  # in millions
    business_data['avg_roi'] = (business_data['roi_min'] + business_data['roi_max']) / 2
    business_data['avg_loss_reduction'] = (business_data['loss_red_min'] + business_data['loss_red_max']) / 2
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
    
    # Investment vs. ROI chart
    scatter = ax1.scatter(
        business_data['avg_investment'], 
        business_data['avg_roi'],
        s=business_data['avg_loss_reduction'] * 20,  # Size based on loss reduction
        c=business_data.index,  # Color based on index
        cmap='viridis',
        alpha=0.7
    )
    
    # Add business model labels
    for i, model in enumerate(business_data['model_name']):
        ax1.annotate(
            model,
            (business_data['avg_investment'].iloc[i], business_data['avg_roi'].iloc[i]),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)
        )
    
    ax1.set_title('Business Model Comparison: Investment vs. ROI')
    ax1.set_xlabel('Average Investment Required (Million Naira)')
    ax1.set_ylabel('Average Annual ROI (%)')
    ax1.grid(True, alpha=0.3)
    
    # Create legend for bubble size
    handles, labels = ax1.get_legend_handles_labels()
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label=f'{size}%',
                  markerfacecolor='gray', markersize=np.sqrt(size*10))
        for size in [15, 25, 35, 45]
    ]
    ax1.legend(handles=legend_elements, title="Loss Reduction %", 
             loc="upper right", title_fontsize=10)
    
    # Job creation vs investment chart
    job_min = business_data['job_creation'].str.split('-', expand=True)[0].astype(int)
    job_max = business_data['job_creation'].str.split('-', expand=True)[1].str.split(' ', expand=True)[0].astype(int)
    business_data['avg_jobs'] = (job_min + job_max) / 2
    
    ax2.bar(
        business_data['model_name'], 
        business_data['avg_jobs'],
        color=sns.color_palette('viridis', len(business_data))
    )
    ax2.set_title('Average Jobs Created per Business Model')
    ax2.set_ylabel('Jobs per Business')
    ax2.set_xticklabels(business_data['model_name'], rotation=45, ha='right')
    
    # Add data labels
    for i, v in enumerate(business_data['avg_jobs']):
        ax2.text(i, v + 0.1, f"{v:.1f}", ha='center')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

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
        
        # Add implementation details
        details = (f"Regions: {', '.join(eval(impl_data['regions'].iloc[i]))}\n"
                  f"Models: {', '.join(eval(impl_data['business_models'].iloc[i]))}\n"
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
    
    return save_path

def plot_impact_projection(data, save_path='reports/figures/impact_projection.png'):
    """Generate impact projection visualization"""
    # Create projection data
    years = ['Current', 'Year 1', 'Year 2', 'Year 3']
    youth_businesses = [0, 100, 700, 7000]
    phl_reduction = [0, 5, 12, 20]  # percentage reduction
    value_preserved = [0, 0.5, 2, 5]  # billion Naira
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # Plot youth businesses created
    ax1.bar(years, youth_businesses, color=sns.color_palette('Blues', len(years)))
    ax1.set_title('Youth Businesses Created')
    ax1.set_ylabel('Number of Businesses')
    
    # Add data labels
    for i, v in enumerate(youth_businesses):
        ax1.text(i, v + 200, f"{v}", ha='center')
    
    # Plot PHL reduction and value preserved
    ax2.set_title('Post-Harvest Loss Reduction & Value Preserved')
    
    color = 'tab:red'
    ax2.set_xlabel('Project Timeline')
    ax2.set_ylabel('PHL Reduction (%)', color=color)
    line1 = ax2.plot(years, phl_reduction, 'o-', color=color, linewidth=3, label='PHL Reduction (%)')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 25)
    
    # Add second y-axis for value preserved
    ax3 = ax2.twinx()
    color = 'tab:blue'
    ax3.set_ylabel('Value Preserved (Billion ₦)', color=color)
    line2 = ax3.plot(years, value_preserved, 'o-', color=color, linewidth=3, label='Value Preserved (Billion ₦)')
    ax3.tick_params(axis='y', labelcolor=color)
    ax3.set_ylim(0, 6)
    
    # Combine legends from both axes
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, loc="upper left")
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return save_path

# ============================================================
# REPORT GENERATION FUNCTIONS
# ============================================================

def create_stakeholder_report():
    """Create main stakeholder report in PDF format"""
    # Load data
    print("Loading data...")
    data = load_phl_data()
    
    # Generate visualizations
    print("Generating visualizations...")
    regional_losses_fig = plot_regional_losses(data)
    value_chain_fig = plot_value_chain_losses(data)
    crop_losses_fig = plot_crop_losses(data)
    seasonal_fig = plot_seasonal_variation(data)
    business_models_fig = plot_business_models_comparison(data)
    roadmap_fig = plot_implementation_roadmap(data)
    impact_fig = plot_impact_projection(data)
    
    # Create PDF document
    print("Creating report document...")
    report_path = "reports/YouthHarvest_Stakeholder_Report.pdf"
    doc = SimpleDocTemplate(
        report_path,
        pagesize=letter,
        rightMargin=inch/2,
        leftMargin=inch/2,
        topMargin=inch/2,
        bottomMargin=inch/2
    )
    
    # Get style sheets
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Title', 
        parent=styles['Heading1'], 
        fontName='Helvetica-Bold',
        fontSize=16,
        alignment=1,
        spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        name='Subtitle', 
        parent=styles['Heading2'], 
        fontName='Helvetica-Bold',
        fontSize=14,
        spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='Body', 
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8
    ))
    
    # Build content
    content = []
    
    # Cover page
    content.append(Paragraph(REPORT_TITLE, styles['Title']))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Stakeholder Report", styles['Subtitle']))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Date: {REPORT_DATE}", styles['Normal']))
    content.append(Spacer(1, 36))
    
    # Add company logo or project image here if available
    # content.append(Image("logo.png", width=3*inch, height=1.5*inch))
    
    content.append(Spacer(1, 36))
    
    # Executive Summary
    content.append(Paragraph("Executive Summary", styles['Subtitle']))
    content.append(Paragraph(
        "The YouthHarvest Project addresses two critical challenges facing Nigeria: significant post-harvest losses in "
        "the agricultural sector (30-50% of production) and high youth unemployment (42.5% for ages 15-34). Through "
        "data-driven analysis and business model development, the project has identified targeted opportunities to "
        "transform post-harvest loss points into youth entrepreneurship opportunities.",
        styles['Body']
    ))
    content.append(Paragraph(
        "Our analysis reveals that post-harvest losses represent approximately ₦4 billion in annual value lost, "
        "with the highest absolute losses occurring in the North West region (1.25-1.45 million tons annually). "
        "Storage (32%) and processing (28%) represent the highest loss stages across the value chain. We have "
        "developed seven youth-appropriate business models that directly address these loss points, with investment "
        "requirements ranging from ₦200,000 to ₦8 million and ROI potential of 15-70% annually.",
        styles['Body']
    ))
    content.append(Paragraph(
        "Full implementation over a three-year period has the potential to create 5,000-7,000 youth-led businesses, "
        "generate 15,000-25,000 direct jobs, and preserve ₦4-6 billion in annual agricultural value through a "
        "15-20% reduction in targeted post-harvest losses.",
        styles['Body']
    ))
    
    content.append(Spacer(1, 12))
    
    # Problem Analysis
    content.append(Paragraph("1. Post-Harvest Loss Analysis", styles['Subtitle']))
    content.append(Paragraph(
        "Our comprehensive data analysis revealed significant regional and crop-specific patterns in post-harvest losses "
        "across Nigeria. The following visualizations highlight key findings that informed our intervention strategy.",
        styles['Body']
    ))
    
    # Regional Loss Analysis
    content.append(Paragraph("1.1 Regional Loss Distribution", styles['Subtitle']))
    content.append(Paragraph(
        "Post-harvest losses show significant regional variation across Nigeria, with the North East and South South "
        "regions experiencing the highest percentage losses (38-40%), while the North West region shows the highest "
        "absolute tonnage lost due to its larger production volumes (1.35 million tons annually).",
        styles['Body']
    ))
    
    content.append(Image(regional_losses_fig, width=7*inch, height=3.5*inch))
    content.append(Spacer(1, 12))
    
    # Value Chain Analysis
    content.append(Paragraph("1.2 Value Chain Loss Analysis", styles['Subtitle']))
    content.append(Paragraph(
        "Analysis by value chain stage reveals that storage (32%) and processing (28%) represent the critical "
        "intervention points, accounting for 60% of all post-harvest losses. This pattern is consistent across "
        "regions, indicating that targeted solutions in these areas would have the highest impact potential.",
        styles['Body']
    ))
    
    content.append(Image(value_chain_fig, width=5*inch, height=3*inch))
    content.append(Spacer(1, 12))
    
    # Crop-Specific Analysis
    content.append(Paragraph("1.3 Crop-Specific Loss Patterns", styles['Subtitle']))
    content.append(Paragraph(
        "Different crops show varying vulnerability to post-harvest losses, with perishables such as tomatoes (45%), "
        "vegetables (42%), and fruits (40%) showing the highest percentage losses. However, staple crops like maize "
        "and rice represent the highest absolute tonnage lost, indicating the importance of addressing both "
        "categories.",
        styles['Body']
    ))
    
    content.append(Image(crop_losses_fig, width=7*inch, height=5*inch))
    content.append(Spacer(1, 12))
    
    # Seasonal Variation
    content.append(Paragraph("1.4 Seasonal Variation in Losses", styles['Subtitle']))
    content.append(Paragraph(
        "Post-harvest losses show significant seasonal patterns, with peak loss periods occurring during the main "
        "harvest months (May-July) when processing and storage capacities are overwhelmed. Understanding these "
        "seasonal patterns is critical for timing interventions and managing business operations.",
        styles['Body']
    ))
    
    content.append(Image(seasonal_fig, width=7*inch, height=3*inch))
    content.append(Spacer(1, 12))
    
    # Youth Opportunity Mapping
    content.append(Paragraph("2. Youth Opportunity Mapping", styles['Subtitle']))
    content.append(Paragraph(
        "Based on our data analysis, we've developed seven youth-appropriate business models that directly address "
        "identified loss points. Each model has been designed for implementation by young entrepreneurs, with "
        "careful consideration of investment requirements, technical complexity, market demand, and profit "
        "potential.",
        styles['Body']
    ))
    
    content.append(Image(business_models_fig, width=7*inch, height=7*inch))
    content.append(Spacer(1, 12))
    
    # Business Models Detail
    content.append(Paragraph("2.1 Business Model Summaries", styles['Subtitle']))
    
    # Create table for business models
    table_data = [
        ['Model ID', 'Business Model', 'Investment Range', 'Annual ROI', 'PHL Reduction', 'Payback Period']
    ]
    
    for _, model in data['business_models'].iterrows():
        table_data.append([
            model['model_id'],
            model['model_name'],
            model['investment_range'],
            model['annual_roi'],
            model['loss_reduction'],
            model['payback_period']
        ])
    
    model_table = Table(table_data, colWidths=[0.6*inch, 2.2*inch, 1.5*inch, 1*inch, 1.1*inch, 1.1*inch])
    model_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    content.append(model_table)
    content.append(Spacer(1, 12))
    
    content.append(Paragraph(
        "Each business model includes detailed implementation guides covering equipment specifications, "
        "operational procedures, marketing strategies, and financial projections. These guides are available "
        "in both detailed technical format and simplified quick-start versions for youth entrepreneurs.",
        styles['Body']
    ))
    
    # Implementation Roadmap
    content.append(Paragraph("3. Implementation Roadmap", styles['Subtitle']))
    content.append(Paragraph(
        "We have developed a phased implementation approach over three years, starting with pilot projects in "
        "high-impact regions and gradually scaling to national coverage. This approach allows for testing, "
        "refinement, and progressive scaling of the most successful models.",
        styles['Body']
    ))
    
    content.append(Image(roadmap_fig, width=7*inch, height=3*inch))
    content.append(Spacer(1, 12))
    
    # Impact Projections
    content.append(Paragraph("4. Impact Projections", styles['Subtitle']))
    content.append(Paragraph(
        "Based on our analysis and implementation roadmap, we project the following impacts over the three-year "
        "implementation period:",
        styles['Body']
    ))
    
    content.append(Image(impact_fig, width=7*inch, height=3*inch))
    content.append(Spacer(1, 12))
    
    content.append(Paragraph(
        "The projected 15-20% reduction in targeted post-harvest losses represents approximately ₦4-6 billion "
        "in preserved value annually, while creating 15,000-25,000 direct jobs through 5,000-7,000 youth-led "
        "businesses. Secondary benefits include improved food security, reduced import dependence, and "
        "strengthened rural economies.",
        styles['Body']
    ))
    
    # Partnership Opportunities
    content.append(Paragraph("5. Partnership Opportunities", styles['Subtitle']))
    content.append(Paragraph(
        "Successful implementation of the YouthHarvest Project requires strategic partnerships across multiple "
        "sectors. We have identified the following partnership opportunities:",
        styles['Body']
    ))
    
    partnership_data = [
        ['Partner Type', 'Role', 'Specific Opportunities'],
        ['Financial Institutions', 'Provide affordable financing for youth entrepreneurs', 'Youth-in-agriculture loans (5-9% interest), equipment leasing, inventory financing'],
        ['Training Organizations', 'Build youth technical and business capacity', 'Technical skills training, business management courses, mentorship programs'],
        ['Technology Providers', 'Supply appropriate technology solutions', 'Equipment supply, digital platforms, IoT sensors, mobile applications'],
        ['Government Agencies', 'Create enabling policy environment', 'Integration with existing youth programs, regulatory support, extension services'],
        ['Development Organizations', 'Provide implementation support', 'Technical assistance, grant funding, M&E support, knowledge sharing']
    ]
    
    partner_table = Table(partnership_data, colWidths=[1.5*inch, 2*inch, 4*inch])
    partner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    content.append(partner_table)
    content.append(Spacer(1, 12))
    
    # Next Steps
    content.append(Paragraph("6. Next Steps and Recommendations", styles['Subtitle']))
    content.append(Paragraph(
        "Based on our analysis and findings, we recommend the following next steps for stakeholder consideration:",
        styles['Body']
    ))
    
    next_steps = [
        "1. Initiate pilot implementation in North West and North East regions, focusing on Mobile Threshing/Shelling Service and Solar Drying as a Service models.",
        "2. Engage financing partners to develop youth-friendly financial products aligned with identified business models.",
        "3. Establish a multi-stakeholder coordination platform to align implementation efforts.",
        "4. Develop detailed training curricula for each business model.",
        "5. Deploy the interactive YouthHarvest dashboard to support youth entrepreneur decision-making.",
        "6. Create monitoring and evaluation framework to track implementation progress and impact."
    ]
    
    for step in next_steps:
        content.append(Paragraph(step, styles['Body']))
    
    content.append(Spacer(1, 12))
    
    # Contact Information
    content.append(Paragraph("Contact Information", styles['Subtitle']))
    content.append(Paragraph(
        "For more information about the YouthHarvest Project, please contact:",
        styles['Body']
    ))
    content.append(Paragraph(
        "Project Lead: [Name]\nEmail: [Email]\nPhone: [Phone Number]\nWebsite: [Website]",
        styles['Body']
    ))
    
    # Build PDF document
    doc.build(content)
    print(f"Report successfully generated: {report_path}")
    return report_path

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    report_path = create_stakeholder_report()
    print(f"YouthHarvest Stakeholder Report generated at: {report_path}")
    
    # Additional message about dashboard deployment
    print("\nNote: For the interactive UI deployment:")
    print("1. The visualizations in this report can be integrated into a web-based dashboard")
    print("2. Use Flask/FastAPI backend with React frontend for full interactivity")
    print("3. Ensure mobile responsiveness for field access by youth entrepreneurs")
    print("4. Consider offline functionality for areas with limited connectivity")