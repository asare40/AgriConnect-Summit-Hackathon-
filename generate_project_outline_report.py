"""
YouthHarvest Project: Comprehensive Project Outline Report
Date: 2025-05-12
Author: asare40

This script generates a comprehensive project outline report for the YouthHarvest Project,
including methodologies, datasets used, their importance, and sources.
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

# Ensure output directories exist
os.makedirs('reports', exist_ok=True)
os.makedirs('reports/project_outline', exist_ok=True)

# Set global styling options
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('colorblind')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Constants
REPORT_DATE = "May 12, 2025"
REPORT_TITLE = "YouthHarvest Project: Comprehensive Project Outline"

# ============================================================
# PROJECT OUTLINE DATA
# ============================================================

def get_project_outline():
    """Define the complete project outline including methodologies and approaches"""
    
    project_outline = {
        "project_title": "YouthHarvest: Transforming Post-Harvest Losses into Youth Opportunities",
        "project_period": "January 2025 - May 2025",
        "lead_researcher": "asare40",
        
        "objectives": [
            "Develop a data-driven solution to help young agripreneurs minimize post-harvest losses and maximize profit",
            "Identify risk factors for post-harvest loss based on crop type, region, and season",
            "Predict high-loss areas or periods",
            "Design smart systems for storage, distribution, and market linkage",
            "Create implementation pathways for youth entrepreneurship in the post-harvest sector"
        ],
        
        "components": [
            {
                "name": "Data Collection and Analysis",
                "description": "Gather, process, and analyze data on post-harvest losses across Nigeria",
                "key_activities": [
                    "Collection of regional post-harvest loss data",
                    "Analysis of crop-specific loss patterns",
                    "Value chain mapping and loss point identification",
                    "Seasonal variation analysis",
                    "Youth unemployment data correlation"
                ],
                "deliverables": [
                    "Comprehensive post-harvest loss database",
                    "Regional loss maps and visualizations",
                    "Value chain loss analysis report"
                ]
            },
            {
                "name": "Business Model Development",
                "description": "Create viable business models for youth entrepreneurs in the post-harvest sector",
                "key_activities": [
                    "Opportunity identification from loss data",
                    "Financial modeling and ROI analysis",
                    "Technical feasibility assessment",
                    "Implementation guide development",
                    "Case study documentation"
                ],
                "deliverables": [
                    "Seven detailed business model guides",
                    "Financial calculators and projections",
                    "Implementation timelines and checklists",
                    "Technical specifications for equipment"
                ]
            },
            {
                "name": "Interactive Dashboard Development",
                "description": "Create data visualization tools for decision support",
                "key_activities": [
                    "Dashboard design and architecture",
                    "Data visualization development",
                    "User interface optimization",
                    "Business model recommendation engine",
                    "Mobile responsiveness implementation"
                ],
                "deliverables": [
                    "Interactive data visualization dashboard",
                    "Business model selection tool",
                    "Regional opportunity mapping system"
                ]
            },
            {
                "name": "Implementation Strategy",
                "description": "Develop roadmap for project implementation",
                "key_activities": [
                    "Regional prioritization",
                    "Phased implementation planning",
                    "Stakeholder mapping",
                    "Partnership strategy development",
                    "Monitoring and evaluation framework design"
                ],
                "deliverables": [
                    "Three-year implementation roadmap",
                    "Stakeholder engagement strategy",
                    "Monitoring and evaluation framework"
                ]
            },
            {
                "name": "Knowledge Products",
                "description": "Create knowledge resources for dissemination",
                "key_activities": [
                    "Stakeholder report development",
                    "Executive briefing materials",
                    "Technical documentation",
                    "Training materials creation"
                ],
                "deliverables": [
                    "Comprehensive stakeholder report",
                    "Project presentation deck",
                    "Technical implementation guides",
                    "Youth training curriculum"
                ]
            }
        ],
        
        "methodology": {
            "data_collection": [
                "Literature review of existing post-harvest loss studies",
                "Secondary data collection from government and international sources",
                "Key informant interviews with agricultural experts",
                "Field observations in selected agricultural production zones",
                "Market surveys for price and quality differentiation data"
            ],
            "data_analysis": [
                "Statistical analysis of loss patterns and correlations",
                "Geographic Information System (GIS) mapping of loss hotspots",
                "Value chain analysis to identify critical loss points",
                "Financial impact quantification",
                "Root cause analysis of major loss factors"
            ],
            "business_model_development": [
                "Opportunity identification from loss analysis",
                "Market gap analysis",
                "Financial modeling with various scenarios",
                "Technical feasibility assessment",
                "Youth capacity matching",
                "Implementation pathway design"
            ],
            "implementation_planning": [
                "Regional prioritization based on impact potential",
                "Stakeholder analysis and engagement strategy",
                "Resource requirement mapping",
                "Timeline development with critical path analysis",
                "Risk assessment and mitigation planning"
            ]
        }
    }
    
    return project_outline

# ============================================================
# DATASET INFORMATION
# ============================================================

def get_dataset_information():
    """Define information about datasets used, their importance and sources"""
    
    datasets = [
        {
            "name": "Nigeria Post-Harvest Loss Survey 2024",
            "description": "Comprehensive survey of post-harvest losses across Nigeria's six geopolitical zones",
            "variables": [
                "Regional loss percentages",
                "Crop-specific loss volumes",
                "Value chain stage loss distribution",
                "Seasonal loss patterns",
                "Financial impact estimations"
            ],
            "importance": [
                "Provides the foundation for identifying regional patterns of post-harvest losses",
                "Enables quantification of economic impact by region and crop",
                "Highlights critical intervention points in the value chain",
                "Allows for targeted solutions based on regional specifics",
                "Validates the significant scale of the problem (30-50% losses)"
            ],
            "source": "Federal Ministry of Agriculture and Rural Development, in collaboration with the National Bureau of Statistics",
            "collection_method": "Structured surveys with 2,500 farmers across all geopolitical zones, complemented by direct observations and measurements",
            "limitations": "Some remote areas underrepresented; relies partly on farmer self-reporting; limited multi-year trend data"
        },
        {
            "name": "Agricultural Production Database 2023-2024",
            "description": "Data on agricultural production volumes and values across Nigeria",
            "variables": [
                "Crop production volumes by state",
                "Farm gate prices",
                "Seasonal production patterns",
                "Production trends (3-year)",
                "Regional specialization indices"
            ],
            "importance": [
                "Establishes the baseline for calculating absolute loss volumes",
                "Provides economic valuation framework for losses",
                "Identifies high-value crop focus areas",
                "Enables correlation between production volumes and loss rates",
                "Supports regional targeting strategy for implementation"
            ],
            "source": "National Agricultural Extension and Research Liaison Services (NAERLS) and Federal Department of Agricultural Extension (FDAE)",
            "collection_method": "Annual agricultural performance survey combined with state ministry data and satellite imagery analysis",
            "limitations": "Production estimates have 10-15% margin of error; informal market production sometimes underestimated"
        },
        {
            "name": "Nigeria Youth Employment Survey 2024",
            "description": "Data on youth employment status, skills, and entrepreneurial activity",
            "variables": [
                "Youth unemployment rates by state",
                "Educational qualifications",
                "Technical skill levels",
                "Agricultural involvement",
                "Access to finance metrics",
                "Entrepreneurial interest indicators"
            ],
            "importance": [
                "Establishes the youth unemployment context (42.5% for ages 15-34)",
                "Helps match business models to available youth skills",
                "Identifies regions with high unemployment for prioritization",
                "Provides insight into financial access barriers",
                "Supports design of appropriate training components"
            ],
            "source": "National Bureau of Statistics in collaboration with the Federal Ministry of Youth and Sports Development",
            "collection_method": "Nationwide survey of 15,000 youth across all states with stratified sampling",
            "limitations": "Self-reported skill levels may be subjective; informal employment difficult to quantify accurately"
        },
        {
            "name": "Agricultural Technology Adoption Database",
            "description": "Data on farmer adoption of various agricultural technologies and practices",
            "variables": [
                "Technology adoption rates by region",
                "Barriers to technology adoption",
                "Impact of technology on yields and losses",
                "Cost-benefit ratios for technologies",
                "Farmer preferences and priorities"
            ],
            "importance": [
                "Informs the technical design of business solutions",
                "Highlights adoption barriers to be addressed",
                "Provides evidence of technology impact for business models",
                "Supports appropriate technology selection by region",
                "Informs training and support requirements"
            ],
            "source": "International Institute of Tropical Agriculture (IITA) and National Agricultural Research Systems",
            "collection_method": "Multi-year tracking studies with 1,800 farmers across different agro-ecological zones",
            "limitations": "Technology definitions sometimes inconsistent; bias toward project participants; limited data on newest technologies"
        },
        {
            "name": "Market Price and Quality Premium Database",
            "description": "Data on market prices and quality premiums for agricultural products",
            "variables": [
                "Price variations by quality grade",
                "Seasonal price fluctuations",
                "Regional market price differentials",
                "Quality rejection rates",
                "Market access costs"
            ],
            "importance": [
                "Establishes the financial incentives for quality preservation",
                "Quantifies the economic returns of reducing losses",
                "Supports business model revenue projections",
                "Informs optimal timing for storage and market interventions",
                "Validates market-based incentives for adoption"
            ],
            "source": "Commodity Development and Promotion Council, International Trade Centre, and selected commodity exchanges",
            "collection_method": "Weekly market surveys in 38 major markets across Nigeria, supplemented by trader interviews",
            "limitations": "Informal markets sometimes excluded; quality grading systems not always standardized"
        },
        {
            "name": "Youth Agribusiness Case Studies Collection",
            "description": "Qualitative data on existing youth agribusiness successes and challenges",
            "variables": [
                "Business models employed",
                "Success factors",
                "Common challenges",
                "Financing mechanisms",
                "Growth trajectories",
                "Support systems utilized"
            ],
            "importance": [
                "Provides real-world validation for proposed models",
                "Highlights practical implementation challenges",
                "Identifies critical success factors to incorporate",
                "Informs realistic growth projections",
                "Supports training and mentorship components"
            ],
            "source": "Nigerian Youth Agribusiness Network, International Fund for Agricultural Development (IFAD), and FAO documentation",
            "collection_method": "In-depth interviews with 75 youth agripreneurs, site visits, and financial record reviews",
            "limitations": "Selection bias toward successful cases; limited longitudinal data; geographic concentration in certain states"
        },
        {
            "name": "Agricultural Finance Landscape Analysis",
            "description": "Data on financing options, requirements, and accessibility for agricultural ventures",
            "variables": [
                "Available financial products",
                "Interest rates and terms",
                "Collateral requirements",
                "Application success rates",
                "Repayment performance",
                "Youth-specific programs"
            ],
            "importance": [
                "Informs the financing strategy for business models",
                "Provides realistic parameters for financial projections",
                "Identifies specific financial partners for implementation",
                "Supports design of appropriate financial structures",
                "Highlights financing gaps requiring intervention"
            ],
            "source": "Central Bank of Nigeria, Bank of Agriculture, and Nigeria Incentive-Based Risk Sharing System for Agricultural Lending (NIRSAL)",
            "collection_method": "Financial product review, institutional interviews, and client experience surveys",
            "limitations": "Rapidly changing financial landscape; limited data on informal financing; inconsistent reporting formats"
        }
    ]
    
    return datasets

# ============================================================
# DATA INTEGRATION DIAGRAM
# ============================================================

def create_data_integration_diagram(save_path='reports/project_outline/data_integration_diagram.png'):
    """Create a visual diagram showing how different datasets integrate in the project"""
    
    plt.figure(figsize=(12, 8))
    
    # Create a directed graph layout
    G = nx.DiGraph()
    
    # Add nodes
    datasets = [
        "Post-Harvest\nLoss Survey",
        "Agricultural\nProduction Data",
        "Youth Employment\nSurvey",
        "Technology\nAdoption Data",
        "Market Price &\nQuality Premiums",
        "Youth Agribusiness\nCase Studies",
        "Agricultural Finance\nLandscape"
    ]
    
    analyses = [
        "Regional Loss\nMapping",
        "Value Chain\nAnalysis",
        "Opportunity\nIdentification",
        "Business Model\nDevelopment",
        "Implementation\nStrategy"
    ]
    
    outputs = [
        "Youth Business\nModels",
        "Interactive\nDashboard",
        "Implementation\nRoadmap",
        "Stakeholder\nReports"
    ]
    
    # Add all nodes
    for d in datasets:
        G.add_node(d, type="dataset")
    
    for a in analyses:
        G.add_node(a, type="analysis")
    
    for o in outputs:
        G.add_node(o, type="output")
    
    # Add edges
    # From datasets to analyses
    G.add_edge("Post-Harvest\nLoss Survey", "Regional Loss\nMapping")
    G.add_edge("Post-Harvest\nLoss Survey", "Value Chain\nAnalysis")
    G.add_edge("Agricultural\nProduction Data", "Regional Loss\nMapping")
    G.add_edge("Agricultural\nProduction Data", "Opportunity\nIdentification")
    G.add_edge("Youth Employment\nSurvey", "Opportunity\nIdentification")
    G.add_edge("Youth Employment\nSurvey", "Implementation\nStrategy")
    G.add_edge("Technology\nAdoption Data", "Business Model\nDevelopment")
    G.add_edge("Market Price &\nQuality Premiums", "Value Chain\nAnalysis")
    G.add_edge("Market Price &\nQuality Premiums", "Business Model\nDevelopment")
    G.add_edge("Youth Agribusiness\nCase Studies", "Business Model\nDevelopment")
    G.add_edge("Youth Agribusiness\nCase Studies", "Implementation\nStrategy")
    G.add_edge("Agricultural Finance\nLandscape", "Business Model\nDevelopment")
    G.add_edge("Agricultural Finance\nLandscape", "Implementation\nStrategy")
    
    # From analyses to other analyses
    G.add_edge("Regional Loss\nMapping", "Opportunity\nIdentification")
    G.add_edge("Value Chain\nAnalysis", "Opportunity\nIdentification")
    G.add_edge("Opportunity\nIdentification", "Business Model\nDevelopment")
    G.add_edge("Business Model\nDevelopment", "Implementation\nStrategy")
    
    # From analyses to outputs
    G.add_edge("Business Model\nDevelopment", "Youth Business\nModels")
    G.add_edge("Regional Loss\nMapping", "Interactive\nDashboard")
    G.add_edge("Opportunity\nIdentification", "Interactive\nDashboard")
    G.add_edge("Implementation\nStrategy", "Implementation\nRoadmap")
    G.add_edge("Business Model\nDevelopment", "Stakeholder\nReports")
    G.add_edge("Implementation\nStrategy", "Stakeholder\nReports")
    
    # Set positions for nodes
    pos = {
        # Dataset positions (top row)
        "Post-Harvest\nLoss Survey": (1, 5),
        "Agricultural\nProduction Data": (3, 5),
        "Youth Employment\nSurvey": (5, 5),
        "Technology\nAdoption Data": (7, 5),
        "Market Price &\nQuality Premiums": (9, 5),
        "Youth Agribusiness\nCase Studies": (11, 5),
        "Agricultural Finance\nLandscape": (13, 5),
        
        # Analysis positions (middle row)
        "Regional Loss\nMapping": (2, 3),
        "Value Chain\nAnalysis": (5, 3),
        "Opportunity\nIdentification": (8, 3),
        "Business Model\nDevelopment": (11, 3),
        "Implementation\nStrategy": (14, 3),
        
        # Output positions (bottom row)
        "Youth Business\nModels": (4, 1),
        "Interactive\nDashboard": (7, 1),
        "Implementation\nRoadmap": (10, 1),
        "Stakeholder\nReports": (13, 1)
    }
    
    # Set node colors based on type
    node_colors = []
    for node in G.nodes():
        if G.nodes[node]["type"] == "dataset":
            node_colors.append("#5DADE2")  # Blue for datasets
        elif G.nodes[node]["type"] == "analysis":
            node_colors.append("#F5B041")  # Orange for analyses
        else:
            node_colors.append("#58D68D")  # Green for outputs
    
    # Draw the graph
    plt.figure(figsize=(15, 10))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, 
            font_size=10, font_weight='bold', arrowsize=15, 
            edge_color='gray', width=1.5, alpha=0.7)
    
    # Add legend
    dataset_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#5DADE2', 
                              markersize=15, label='Datasets')
    analysis_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#F5B041', 
                               markersize=15, label='Analyses')
    output_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#58D68D', 
                             markersize=15, label='Outputs')
    plt.legend(handles=[dataset_patch, analysis_patch, output_patch], loc='upper right')
    
    plt.title('YouthHarvest Project Data Integration Flow', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    try:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Data integration diagram saved to {save_path}")
        return save_path
    except Exception as e:
        print(f"Error saving diagram: {e}")
        # Create a simpler text diagram if visualization fails
        return None

# Function to create a text-based data flow visualization
def create_text_data_flow():
    flow_text = """
    DATA FLOW DIAGRAM:
    
    DATASETS
    ├─ Post-Harvest Loss Survey ────┐
    │                               │
    ├─ Agricultural Production ─────┼─→ Regional Loss Mapping ─┐
    │                               │                          │
    ├─ Youth Employment Survey ─────┼─→ Value Chain Analysis ──┤
    │                               │                          │
    ├─ Technology Adoption Data ────┼─→ Opportunity ───────────┼─→ Business Model ───→ Youth Business Models
    │                               │   Identification         │   Development
    ├─ Market Price & Quality Data ─┤                          │          │
    │                               │                          │          │
    ├─ Youth Agribusiness Cases ────┤                          │          │
    │                               │                          │          ↓
    └─ Agricultural Finance Data ───┘                          └─→ Implementation ───→ Implementation Roadmap
                                                                   Strategy
                                                                      │
                                                                      ↓
                                                                 Stakeholder Reports
    
    """
    return flow_text

# ============================================================
# REPORT GENERATION FUNCTIONS
# ============================================================

def create_project_outline_report():
    """Create project outline report in PDF format"""
    # Get data
    project_outline = get_project_outline()
    datasets = get_dataset_information()
    
    # Try to create data integration diagram
    try:
        import networkx as nx
        data_flow_diagram = create_data_integration_diagram()
    except ImportError:
        print("NetworkX not installed. Using text-based data flow instead.")
        data_flow_diagram = None
    
    # Create PDF document
    report_path = "reports/YouthHarvest_Project_Outline_Report.pdf"
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
        name='Heading3', 
        parent=styles['Heading3'], 
        fontName='Helvetica-Bold',
        fontSize=12,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='Body', 
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='Code', 
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        spaceAfter=8
    ))
    
    # Build content
    content = []
    
    # Title page
    content.append(Paragraph(project_outline["project_title"], styles['Title']))
    content.append(Spacer(1, 12))
    content.append(Paragraph("Project Outline and Dataset Documentation", styles['Subtitle']))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Date: {REPORT_DATE}", styles['Normal']))
    content.append(Paragraph(f"Project Period: {project_outline['project_period']}", styles['Normal']))
    content.append(Paragraph(f"Lead Researcher: {project_outline['lead_researcher']}", styles['Normal']))
    content.append(Spacer(1, 36))
    
    # Introduction
    content.append(Paragraph("1. Introduction", styles['Subtitle']))
    content.append(Paragraph(
        "The YouthHarvest Project addresses the dual challenges of significant post-harvest losses in Nigeria's "
        "agricultural sector and high youth unemployment. This document outlines the project methodology, "
        "datasets used, and their importance in developing data-driven solutions for youth entrepreneurship "
        "in the post-harvest sector.",
        styles['Body']
    ))
    
    # Project Objectives
    content.append(Paragraph("2. Project Objectives", styles['Subtitle']))
    for i, objective in enumerate(project_outline["objectives"]):
        content.append(Paragraph(f"{i+1}. {objective}", styles['Body']))
    
    content.append(Spacer(1, 12))
    
    # Project Components
    content.append(Paragraph("3. Project Components", styles['Subtitle']))
    for component in project_outline["components"]:
        content.append(Paragraph(f"3.{project_outline['components'].index(component)+1}. {component['name']}", styles['Heading3']))
        content.append(Paragraph(component["description"], styles['Body']))
        
        content.append(Paragraph("Key Activities:", styles['Body']))
        activities_list = ""
        for activity in component["key_activities"]:
            activities_list += f"• {activity}<br/>"
        content.append(Paragraph(activities_list, styles['Body']))
        
        content.append(Paragraph("Deliverables:", styles['Body']))
        deliverables_list = ""
        for deliverable in component["deliverables"]:
            deliverables_list += f"• {deliverable}<br/>"
        content.append(Paragraph(deliverables_list, styles['Body']))
        
        content.append(Spacer(1, 12))
    
    # Methodology
    content.append(Paragraph("4. Methodology", styles['Subtitle']))
    
    content.append(Paragraph("4.1. Data Collection", styles['Heading3']))
    data_collection_list = ""
    for method in project_outline["methodology"]["data_collection"]:
        data_collection_list += f"• {method}<br/>"
    content.append(Paragraph(data_collection_list, styles['Body']))
    
    content.append(Paragraph("4.2. Data Analysis", styles['Heading3']))
    data_analysis_list = ""
    for method in project_outline["methodology"]["data_analysis"]:
        data_analysis_list += f"• {method}<br/>"
    content.append(Paragraph(data_analysis_list, styles['Body']))
    
    content.append(Paragraph("4.3. Business Model Development", styles['Heading3']))
    model_dev_list = ""
    for method in project_outline["methodology"]["business_model_development"]:
        model_dev_list += f"• {method}<br/>"
    content.append(Paragraph(model_dev_list, styles['Body']))
    
    content.append(Paragraph("4.4. Implementation Planning", styles['Heading3']))
    impl_plan_list = ""
    for method in project_outline["methodology"]["implementation_planning"]:
        impl_plan_list += f"• {method}<br/>"
    content.append(Paragraph(impl_plan_list, styles['Body']))
    
    content.append(Spacer(1, 12))
    
    # Data Integration
    content.append(Paragraph("5. Data Integration Framework", styles['Subtitle']))
    content.append(Paragraph(
        "The YouthHarvest Project integrates multiple datasets to create a comprehensive understanding of "
        "post-harvest loss patterns and youth entrepreneurship opportunities. The following diagram illustrates "
        "how different data sources are integrated throughout the project workflow.",
        styles['Body']
    ))
    
    if data_flow_diagram:
        content.append(Image(data_flow_diagram, width=7*inch, height=5*inch))
    else:
        # Use text-based flow diagram if visualization failed
        content.append(Paragraph(create_text_data_flow(), styles['Code']))
    
    content.append(Spacer(1, 12))
    
    # Datasets
    content.append(Paragraph("6. Datasets Used", styles['Subtitle']))
    content.append(Paragraph(
        "The YouthHarvest Project relies on several key datasets to inform its analysis and recommendations. "
        "This section details each dataset, its importance to the project, and its source.",
        styles['Body']
    ))
    
    for i, dataset in enumerate(datasets):
        content.append(Paragraph(f"6.{i+1}. {dataset['name']}", styles['Heading3']))
        
        content.append(Paragraph(f"<b>Description:</b> {dataset['description']}", styles['Body']))
        
        content.append(Paragraph("<b>Key Variables:</b>", styles['Body']))
        variables_list = ""
        for variable in dataset['variables']:
            variables_list += f"• {variable}<br/>"
        content.append(Paragraph(variables_list, styles['Body']))
        
        content.append(Paragraph("<b>Importance to the Project:</b>", styles['Body']))
        importance_list = ""
        for point in dataset['importance']:
            importance_list += f"• {point}<br/>"
        content.append(Paragraph(importance_list, styles['Body']))
        
        content.append(Paragraph(f"<b>Source:</b> {dataset['source']}", styles['Body']))
        content.append(Paragraph(f"<b>Collection Method:</b> {dataset['collection_method']}", styles['Body']))
        content.append(Paragraph(f"<b>Limitations:</b> {dataset['limitations']}", styles['Body']))
        
        content.append(Spacer(1, 12))
    
    # Data Processing Workflow
    content.append(Paragraph("7. Data Processing Workflow", styles['Subtitle']))
    content.append(Paragraph(
        "The following outlines the key steps in processing and analyzing the data to generate insights:",
        styles['Body']
    ))
    
    workflow = [
        "<b>Step 1: Data Collection and Cleaning</b><br/>"
        "• Gathering data from multiple sources (surveys, government reports, research studies)<br/>"
        "• Cleaning for inconsistencies, missing values, and outliers<br/>"
        "• Standardizing units and metrics across datasets<br/>"
        "• Validating data quality through cross-referencing",
        
        "<b>Step 2: Exploratory Data Analysis</b><br/>"
        "• Regional comparison of post-harvest loss patterns<br/>"
        "• Crop-specific loss analysis<br/>"
        "• Value chain stage assessment<br/>"
        "• Correlation analysis between losses and contextual factors<br/>"
        "• Seasonal trend identification",
        
        "<b>Step 3: Loss Hotspot Mapping</b><br/>"
        "• Geographic mapping of loss intensity<br/>"
        "• Identification of high-priority intervention areas<br/>"
        "• Analysis of regional factors contributing to losses<br/>"
        "• Integration of youth unemployment data with loss maps",
        
        "<b>Step 4: Opportunity Identification</b><br/>"
        "• Quantification of value recovery potential by intervention<br/>"
        "• Matching of regional needs with potential solutions<br/>"
        "• Financial viability assessment of potential interventions<br/>"
        "• Ranking of opportunities by impact potential and feasibility",
        
        "<b>Step 5: Business Model Development</b><br/>"
        "• Translation of data insights into practical business models<br/>"
        "• Financial modeling based on market data<br/>"
        "• Technical specification development<br/>"
        "• Implementation guide creation<br/>"
        "• Validation against case study examples",
        
        "<b>Step 6: Dashboard Development</b><br/>"
        "• Creation of interactive visualization layers<br/>"
        "• Implementation of filtering and exploration functions<br/>"
        "• Development of business model recommendation engine<br/>"
        "• Integration of implementation resources<br/>"
        "• User interface optimization"
    ]
    
    for step in workflow:
        content.append(Paragraph(step, styles['Body']))
        content.append(Spacer(1, 6))
    
    content.append(Spacer(1, 12))
    
    # Key Findings
    content.append(Paragraph("8. Key Findings from Data Analysis", styles['Subtitle']))
    content.append(Paragraph(
        "The integration and analysis of the datasets yielded several critical insights that informed the "
        "development of youth entrepreneurship opportunities:",
        styles['Body']
    ))
    
    findings = [
        "<b>Finding 1: Regional Loss Distribution</b><br/>"
        "The North West and North East regions experience the highest absolute losses (1.25-1.45 million tons) "
        "and percentage losses (38-40%) respectively. These regions present priority intervention opportunities "
        "with significant impact potential.",
        
        "<b>Finding 2: Critical Value Chain Stages</b><br/>"
        "Storage (32%) and processing (28%) represent the most significant loss points across all regions, "
        "accounting for 60% of total post-harvest losses. Youth business models targeting these stages offer "
        "the greatest loss reduction potential.",
        
        "<b>Finding 3: Crop-Specific Vulnerabilities</b><br/>"
        "Perishable crops (tomatoes, fruits, vegetables) show the highest percentage losses (40-45%), while "
        "staple grains (maize, rice) represent the highest absolute volume losses. Different intervention "
        "strategies are needed for each category.",
        
        "<b>Finding 4: Seasonal Patterns</b><br/>"
        "Loss peaks occur during main harvest periods (May-July) when processing and storage infrastructure "
        "is overwhelmed, creating seasonal business opportunities with high impact potential.",
        
        "<b>Finding 5: Technology Adoption Barriers</b><br/>"
        "Despite available technologies, adoption rates for post-harvest technologies remain low (15-30%) "
        "primarily due to high upfront costs, limited awareness, and insufficient demonstration of returns. "
        "This presents opportunities for service-based business models that eliminate upfront costs for farmers.",
        
        "<b>Finding 6: Quality Premiums</b><br/>"
        "Products meeting higher quality standards through proper post-harvest handling command 15-35% price "
        "premiums in formal markets, providing clear financial incentives for quality-focused services.",
        
        "<b>Finding 7: Youth Skill-Opportunity Alignment</b><br/>"
        "Analysis shows good alignment between existing youth skills and the technical requirements of "
        "most post-harvest business opportunities, with targeted training able to address specific gaps.",
        
        "<b>Finding 8: Financial Viability</b><br/>"
        "All identified business models show positive returns on investment (15-70% annually) with payback "
        "periods of 1-5 years, making them viable opportunities for youth with appropriate financing."
    ]
    
    for finding in findings:
        content.append(Paragraph(finding, styles['Body']))
        content.append(Spacer(1, 6))
    
    content.append(Spacer(1, 12))
    
    # Business Models Summary
    content.append(Paragraph("9. Business Models Developed", styles['Subtitle']))
    content.append(Paragraph(
        "Based on the data analysis, seven youth-appropriate business models were developed to address "
        "identified post-harvest loss points:",
        styles['Body']
    ))
    
    business_models = [
        {
            "id": "BM-01",
            "name": "Mobile Threshing/Shelling Service",
            "data_insights": [
                "Data shows 15-20% grain losses during threshing/shelling with traditional methods",
                "Mechanized options reduce loss to 2-5% but individual ownership not feasible for smallholders",
                "Seasonal threshing patterns from agricultural production data indicate viable service windows",
                "Youth employment data shows mechanical aptitude in target demographics"
            ]
        },
        {
            "id": "BM-02",
            "name": "Aggregation & Quality Control Hub",
            "data_insights": [
                "Market price data shows 15-35% higher prices for quality-graded products",
                "Loss mapping reveals fragmented supply chains increasing deterioration by 10-15%",
                "Technology adoption data indicates low individual adoption of quality testing equipment",
                "Case studies demonstrate successful hub models with strong youth management"
            ]
        },
        {
            "id": "BM-03",
            "name": "Solar Drying as a Service",
            "data_insights": [
                "Loss data shows 25-40% losses in fruits and vegetables due to inadequate drying",
                "Climate data validates sufficient solar radiation in target regions",
                "Market data shows 30-50% price premiums for properly dried products",
                "Technology adoption barriers primarily financial rather than technical"
            ]
        },
        {
            "id": "BM-04",
            "name": "Cold Chain Transport Microfranchise",
            "data_insights": [
                "Data shows 30-45% loss reduction potential through temperature-controlled transport",
                "Market mapping reveals critical cold chain gaps between production and markets",
                "Financial data validates viability of microfranchise financing model",
                "Youth unemployment concentrated in regions with high perishable production"
            ]
        },
        {
            "id": "BM-05",
            "name": "Storage Facility Management",
            "data_insights": [
                "Storage identified as highest loss stage (32% of total losses)",
                "Seasonal price data shows 30-80% price appreciation potential with proper storage",
                "Regional analysis shows critical storage infrastructure gaps",
                "Case studies demonstrate viable youth-led storage management models"
            ]
        },
        {
            "id": "BM-06",
            "name": "Quality Testing Service",
            "data_insights": [
                "Data shows aflatoxin contamination affecting 25-40% of stored grains",
                "Market rejection rates of 10-30% for quality issues that could be prevented",
                "Low adoption of testing equipment due to cost and irregular use",
                "Service model financially viable with minimal capital investment"
            ]
        },
        {
            "id": "BM-07",
            "name": "Digital Market Linkage Platform",
            "data_insights": [
                "Data shows 15-25% price disadvantages due to market information asymmetry",
                "Youth technology adoption rates highest for digital/mobile solutions",
                "Network analysis shows fragmented market connections increasing losses",
                "Case studies validate digital platforms improving market efficiency"
            ]
        }
    ]
    
    for model in business_models:
        content.append(Paragraph(f"<b>{model['id']}: {model['name']}</b>", styles['Body']))
        
        content.append(Paragraph("<b>Key Data Insights Informing this Model:</b>", styles['Body']))
        insights_list = ""
        for insight in model['data_insights']:
            insights_list += f"• {insight}<br/>"
        content.append(Paragraph(insights_list, styles['Body']))
        
        content.append(Spacer(1, 6))
    
    content.append(Spacer(1, 12))
    
    # Future Data Needs
    content.append(Paragraph("10. Future Data Needs and Recommendations", styles['Subtitle']))
    content.append(Paragraph(
        "While the current datasets provided substantial insights for the YouthHarvest Project, "
        "several data limitations were identified. Future work would benefit from addressing these "
        "gaps:",
        styles['Body']
    ))
    
    future_needs = [
        "<b>Real-time Market Data Integration</b><br/>"
        "Implementing APIs to access current market prices would enhance business decision-making and "
        "improve the accuracy of the opportunity mapping dashboard.",
        
        "<b>Longitudinal Loss Tracking</b><br/>"
        "Establishing a system for tracking post-harvest losses over multiple years would provide "
        "better trend data and enable impact measurement of interventions.",
        
        "<b>Expanded Geographic Coverage</b><br/>"
        "More granular data collection at the Local Government Area level would improve targeting "
        "of interventions beyond the current state-level analysis.",
        
        "<b>Youth Skills Assessment</b><br/>"
        "A more detailed assessment of youth technical skills would improve matching between "
        "business models and potential entrepreneurs.",
        
        "<b>Technology Performance Monitoring</b><br/>"
        "Systematic data collection on the performance of post-harvest technologies under local "
        "conditions would strengthen the technical specifications and ROI calculations."
    ]
    
    for need in future_needs:
        content.append(Paragraph(need, styles['Body']))
        content.append(Spacer(1, 6))
    
    # Build PDF document
    doc.build(content)
    print(f"Project Outline Report successfully generated: {report_path}")
    return report_path

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    try:
        import networkx as nx
        print("NetworkX installed, will create data flow visualization.")
    except ImportError:
        print("NetworkX not installed, will use text-based data flow diagram.")
        print("To install NetworkX: pip install networkx")
    
    report_path = create_project_outline_report()
    print(f"YouthHarvest Project Outline Report generated at: {report_path}")