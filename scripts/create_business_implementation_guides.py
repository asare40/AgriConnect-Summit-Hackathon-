import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Ensure directories exist
os.makedirs('results/youth_opportunities/implementation_guides', exist_ok=True)
os.makedirs('results/youth_opportunities/case_studies', exist_ok=True)

# Define the business models we'll create detailed implementation guides for
# These are the top 5 models from our earlier youth business model analysis
priority_business_models = [
    {
        "model_id": "BM-01",
        "model_name": "Mobile Threshing/Shelling Service",
        "tagline": "Bringing processing power to the farm gate",
        "description": """
        A mobile service where youth entrepreneurs provide mechanical threshing and shelling services to farmers 
        using transportable equipment. This reduces post-harvest losses occurring during manual threshing, 
        saves farmers time and labor costs, and improves grain quality.
        """,
        "value_proposition": [
            "Reduces post-harvest losses by 15-20% through improved threshing/shelling efficiency",
            "Saves farmers 70-80% of the labor time required for manual processing",
            "Improves grain quality through faster processing and reduced damage",
            "Reduces drudgery and makes harvesting less labor-intensive",
            "Provides affordable access to mechanization without farmer investment"
        ],
        "target_crops": ["Maize", "Rice", "Sorghum", "Cowpea", "Groundnut"],
        "target_customers": [
            "Smallholder farmers (0.5-2 hectares)",
            "Medium-scale farmers (2-10 hectares)",
            "Farmer groups and cooperatives",
            "Community aggregation centers"
        ],
        "geographical_focus": [
            "Rural and peri-urban areas in grain-producing regions",
            "Priority states: Kano, Kaduna, Benue, Niger, Taraba"
        ],
        "equipment_needs": {
            "essential": [
                {"item": "Motorized thresher/sheller", "specifications": "1-2 ton/day capacity, petrol-powered", "estimated_cost": "N350,000 - N650,000", "lifespan": "5-8 years with proper maintenance"},
                {"item": "Motorcycle with trailer/tricycle", "specifications": "150-200cc with custom-built trailer", "estimated_cost": "N350,000 - N550,000", "lifespan": "4-6 years"},
                {"item": "Basic tools and spare parts kit", "specifications": "Wrenches, belts, filters, etc.", "estimated_cost": "N40,000 - N60,000", "lifespan": "2-3 years"},
                {"item": "Tarpaulins", "specifications": "Heavy-duty, 5m x 6m (2-3 pieces)", "estimated_cost": "N15,000 - N25,000", "lifespan": "2-3 seasons"}
            ],
            "optional": [
                {"item": "Digital weighing scale", "specifications": "Platform type, 100-150kg capacity", "estimated_cost": "N25,000 - N45,000", "lifespan": "3-5 years"},
                {"item": "Moisture meter", "specifications": "Digital grain moisture tester", "estimated_cost": "N15,000 - N35,000", "lifespan": "3-5 years"},
                {"item": "Small generator", "specifications": "1-2 kVA for charging phones, running small equipment", "estimated_cost": "N45,000 - N85,000", "lifespan": "3-4 years"},
                {"item": "Grain cleaning sieves", "specifications": "Manual cleaning screens, various sizes", "estimated_cost": "N10,000 - N20,000", "lifespan": "2-3 years"}
            ]
        },
        "setup_costs": {
            "equipment": "N755,000 - N1,285,000",
            "training": "N50,000 - N100,000",
            "licenses_and_permits": "N20,000 - N40,000",
            "initial_marketing": "N30,000 - N50,000",
            "working_capital": "N100,000 - N150,000",
            "total_investment": "N955,000 - N1,625,000"
        },
        "revenue_model": {
            "primary_revenue": "Service fee per bag or per kilogram processed",
            "pricing_strategy": "N150-250 per 100kg bag (depending on crop and region)",
            "average_daily_capacity": "1.0-1.5 tons (10-15 bags) per day",
            "potential_daily_revenue": "N1,500 - N3,750",
            "operating_days": "200-250 days per year (seasonal)",
            "annual_revenue_potential": "N300,000 - N937,500",
            "secondary_revenue_streams": [
                "Transportation of processed grain to market (N50-100 per bag)",
                "Equipment maintenance services during off-season",
                "Sale of by-products (e.g., rice husks for fuel)"
            ]
        },
        "operating_costs": {
            "fuel": "N1,000 - N1,500 per day (N200,000 - N375,000 annually)",
            "maintenance": "N40,000 - N80,000 annually",
            "labor": "N1,000 - N1,500 per day for assistant (optional)",
            "transportation": "N500 - N1,000 per day",
            "permits_and_fees": "N10,000 - N20,000 annually",
            "total_annual_operating_costs": "N250,000 - N470,000"
        },
        "profitability": {
            "gross_margin": "45-60%",
            "annual_net_profit": "N50,000 - N467,500",
            "payback_period": "2-3 years",
            "roi": "15-30% annually after payback"
        },
        "key_success_factors": [
            "Strategic location in areas with high production volume",
            "Quality service and equipment reliability",
            "Strong farmer relationships and trust",
            "Efficient scheduling and logistics",
            "Technical knowledge of machinery maintenance",
            "Weather monitoring to plan service delivery"
        ],
        "challenges_and_solutions": [
            {
                "challenge": "High upfront investment cost",
                "solutions": [
                    "Start with leased equipment through pay-as-you-earn model",
                    "Begin with one service (e.g., maize shelling) and expand later",
                    "Form partnership with 2-3 youth to share investment costs",
                    "Apply for youth in agriculture grants or subsidized loans"
                ]
            },
            {
                "challenge": "Seasonal nature of business",
                "solutions": [
                    "Map multiple crop seasons in your region to extend service period",
                    "Offer maintenance services for agricultural equipment in off-season",
                    "Add complementary services (e.g., grain cleaning, transportation)",
                    "Operate across different geographical areas with varied cropping calendars"
                ]
            },
            {
                "challenge": "Competition from traditional methods",
                "solutions": [
                    "Demonstrate clear cost and time savings to farmers",
                    "Offer free trials to influential farmers in new areas",
                    "Highlight quality improvements and reduced losses",
                    "Partner with agricultural extension officers for credibility"
                ]
            },
            {
                "challenge": "Machinery breakdowns",
                "solutions": [
                    "Invest in preventive maintenance and regular servicing",
                    "Keep critical spare parts inventory",
                    "Build relationship with reliable mechanic",
                    "Learn basic repair skills through technical training"
                ]
            }
        ],
        "implementation_steps": [
            {
                "step": "1. Market Research and Location Selection",
                "activities": [
                    "Identify high-potential areas with large production volumes",
                    "Map harvest seasons for target crops in your region",
                    "Assess current threshing/shelling practices and costs",
                    "Identify potential customer segments and their specific needs",
                    "Analyze competition (other service providers, manual alternatives)"
                ],
                "timeframe": "1-2 months",
                "resources_needed": "Transportation for site visits, questionnaire for farmer interviews",
                "success_indicators": "Comprehensive market assessment report with identified service area"
            },
            {
                "step": "2. Business Planning",
                "activities": [
                    "Develop detailed business plan with financial projections",
                    "Select appropriate technology based on local crops and conditions",
                    "Determine pricing strategy based on market research",
                    "Plan service routes and scheduling approach",
                    "Identify funding sources and prepare applications if needed"
                ],
                "timeframe": "1 month",
                "resources_needed": "Business plan template, calculator, crop production calendar",
                "success_indicators": "Completed business plan with clear financial projections"
            },
            {
                "step": "3. Equipment Acquisition and Testing",
                "activities": [
                    "Research equipment options and suppliers",
                    "Compare features, prices, and after-sales support",
                    "Purchase or lease selected equipment",
                    "Test equipment performance with different crop types",
                    "Make any necessary modifications for local conditions"
                ],
                "timeframe": "1-2 months",
                "resources_needed": "Equipment specifications, supplier contacts, test crops",
                "success_indicators": "Functional equipment with verified performance metrics"
            },
            {
                "step": "4. Skills Development",
                "activities": [
                    "Complete technical training on equipment operation",
                    "Learn basic maintenance and troubleshooting",
                    "Develop business management and record-keeping skills",
                    "Practice customer service and communication",
                    "Learn quality assessment of threshed/shelled grains"
                ],
                "timeframe": "2-4 weeks",
                "resources_needed": "Training manuals, tools, practice materials",
                "success_indicators": "Competency in equipment operation and basic maintenance"
            },
            {
                "step": "5. Marketing and Customer Acquisition",
                "activities": [
                    "Create simple branding (name, logo, colors)",
                    "Develop promotional materials (flyers, signage)",
                    "Conduct demonstrations in target communities",
                    "Partner with agricultural extension officers",
                    "Establish booking/reservation system"
                ],
                "timeframe": "Ongoing (intensive in first 2-3 months)",
                "resources_needed": "Demonstration materials, promotional items, phone for bookings",
                "success_indicators": "First 10-15 paying customers acquired"
            },
            {
                "step": "6. Operations Setup",
                "activities": [
                    "Develop standard operating procedures",
                    "Create service schedule and route planning",
                    "Establish quality control measures",
                    "Set up record-keeping system for services and finances",
                    "Prepare maintenance schedule for equipment"
                ],
                "timeframe": "2-3 weeks",
                "resources_needed": "SOP templates, logbook, maintenance checklist",
                "success_indicators": "Organized system for managing daily operations"
            },
            {
                "step": "7. Launch and Initial Operations",
                "activities": [
                    "Begin services in highest-potential area",
                    "Collect customer feedback systematically",
                    "Make operational adjustments based on experience",
                    "Track financial performance against projections",
                    "Build relationships with repeat customers"
                ],
                "timeframe": "First 3 months",
                "resources_needed": "Feedback forms, accounting records, customer database",
                "success_indicators": "Consistent customer base, positive feedback, service efficiency"
            },
            {
                "step": "8. Growth and Expansion",
                "activities": [
                    "Analyze performance data from initial operations",
                    "Identify opportunities for service improvement",
                    "Expand service area or crop types based on demand",
                    "Consider additional equipment or team members",
                    "Develop partnerships with aggregators or processors"
                ],
                "timeframe": "After 6-12 months of operation",
                "resources_needed": "Business performance data, market assessment for new areas",
                "success_indicators": "Increased customer base, improved efficiency, higher profits"
            }
        ],
        "digital_enhancements": {
            "essential": [
                {
                    "technology": "Mobile Booking System",
                    "description": "Simple phone-based system for scheduling services (can start with WhatsApp)",
                    "benefits": "Better route planning, reduced idle time, improved customer service",
                    "implementation": "Free to start with basic tools, N30,000-N50,000 for custom app development"
                },
                {
                    "technology": "Digital Financial Records",
                    "description": "Mobile app or spreadsheet for tracking expenses, revenue, and customer payments",
                    "benefits": "Improved financial management, easier tax reporting, credit history development",
                    "implementation": "Free to N15,000 depending on tools selected"
                }
            ],
            "advanced": [
                {
                    "technology": "GPS Tracking",
                    "description": "Location tracking for service routes and coverage optimization",
                    "benefits": "More efficient routing, data on service coverage areas, reduced fuel costs",
                    "implementation": "N15,000-N40,000 depending on system"
                },
                {
                    "technology": "Performance Monitoring Sensors",
                    "description": "Simple sensors to monitor machine performance and maintenance needs",
                    "benefits": "Predictive maintenance, reduced breakdowns, longer equipment life",
                    "implementation": "N50,000-N100,000 for basic monitoring setup"
                },
                {
                    "technology": "Digital Payments",
                    "description": "Mobile money integration for cashless transactions",
                    "benefits": "Reduced cash handling risks, easier bookkeeping, formal financial records",
                    "implementation": "Minimal costs using existing platforms (1-2.5% transaction fees)"
                }
            ]
        },
        "financing_options": [
            {
                "option": "Youth in Agriculture Loans",
                "providers": "Bank of Agriculture, NIRSAL Microfinance Bank",
                "features": "Reduced interest rates (5-9%), longer repayment periods (3-5 years)",
                "requirements": "Business plan, training completion certificate, 10-20% personal contribution",
                "application_process": "Visit nearest branch, complete application form, attach required documents"
            },
            {
                "option": "Equipment Leasing",
                "providers": "Agricultural equipment suppliers, TOHFAN, NECAS",
                "features": "Pay-as-you-earn model, maintenance support, upgrade options",
                "requirements": "25-30% down payment, regular monthly payments, training completion",
                "application_process": "Contact supplier directly, apply for leasing program"
            },
            {
                "option": "Cooperative Financing",
                "providers": "Youth cooperatives, village savings groups",
                "features": "Shared ownership, reduced individual investment, collective guarantees",
                "requirements": "Membership in cooperative, adherence to cooperative rules",
                "application_process": "Join existing cooperative or form new one with 5-10 members"
            },
            {
                "option": "Grants and Competitions",
                "providers": "USAID, GIZ, World Bank projects, AgroRise Challenge",
                "features": "Non-repayable funds, technical assistance, networking opportunities",
                "requirements": "Innovative approach, demonstrable impact, complete application",
                "application_process": "Monitor opportunities through agricultural extension services, apply online"
            }
        ],
        "case_study": {
            "title": "YouthShell Mobile Threshing Service: From Graduate to Agripreneur",
            "entrepreneur": "Ibrahim Mohammed, 27, Kaduna State",
            "background": """
            After graduating with a diploma in Agricultural Engineering, Ibrahim struggled to find formal 
            employment. Noticing farmers in his community spending days manually threshing maize and 
            losing significant portions to breakage and contamination, he saw a business opportunity.
            """,
            "starting_point": """
            Ibrahim started in 2023 with a single maize sheller purchased through a NIRSAL youth loan of 
            N500,000 with 20% personal contribution from his savings. He transported the machine using a 
            rented motorcycle initially.
            """,
            "implementation": """
            He began by offering free demonstrations to skeptical farmers, showing how his machine could 
            shell in minutes what took hours manually. Word spread quickly after harvest season began. 
            Ibrahim created a simple schedule, traveling between five villages on specific days of the week.
            """,
            "challenges_faced": """
            Early challenges included machine breakdowns due to maintenance inexperience, seasonal gaps in 
            revenue, and initial farmer hesitation. Ibrahim addressed these by obtaining technical training, 
            expanding to sorghum and rice threshing to cover different seasons, and documenting results to 
            show unconvinced farmers.
            """,
            "results": """
            By the end of the first year, Ibrahim had served over 200 farmers and processed approximately 
            300 tons of grain. His service reduced farmers' threshing costs by 40% while saving them 
            substantial time. Post-harvest losses decreased by an estimated 15% due to faster processing 
            and reduced grain damage.
            
            Ibrahim generated a gross revenue of N750,000 in the first year with net profits of N280,000 
            after expenses. By the second year, he purchased a dedicated tricycle for transportation and 
            added a second threshing machine to expand operations.
            """,
            "key_lessons": [
                "Free demonstrations were crucial for overcoming initial farmer skepticism",
                "Technical knowledge of equipment repair saved significant downtime and costs",
                "Mapping multiple crop seasons extended the business operating period",
                "Building relationships with village leaders created trust and facilitated entry to new communities",
                "Simple recordkeeping on a mobile app helped optimize routes and scheduling"
            ],
            "future_plans": """
            Ibrahim now employs two assistants and plans to expand to neighboring local government areas. 
            He's exploring adding cleaning and weighing services to increase his value proposition and 
            working with a microfinance institution to offer farmers short-term storage options.
            """
        }
    },
    {
        "model_id": "BM-02",
        "model_name": "Aggregation & Quality Control Hub",
        "tagline": "Connecting farmers to markets through quality assurance",
        "description": """
        A youth-managed collection point that aggregates crops from smallholder farmers, ensures 
        quality standards, adds value through sorting, grading, and packaging, and connects to larger 
        markets. This business model reduces post-harvest losses by ensuring proper handling and 
        rapid movement of products through the value chain.
        """,
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
        },
        "geographical_focus": [
            "Strategic locations within major production clusters",
            "Areas with sufficient production but limited market access",
            "Locations with adequate road infrastructure for transportation",
            "Priority states: Benue, Kaduna, Niger, Taraba, Plateau"
        ],
        "equipment_needs": {
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
        },
        "setup_costs": {
            "premises": "N300,000 - N900,000 (annual lease)",
            "equipment": "N785,000 - N1,220,000",
            "licenses_and_permits": "N50,000 - N100,000",
            "staff_training": "N100,000 - N200,000",
            "initial_marketing": "N50,000 - N100,000",
            "working_capital": "N500,000 - N1,500,000",
            "total_initial_investment": "N1,785,000 - N4,020,000"
        },
        "revenue_model": {
            "primary_revenue_streams": [
                {
                    "stream": "Aggregation margin",
                    "description": "Difference between buying price from farmers and selling price to buyers",
                    "typical_margin": "5-15% depending on crop and quality"
                }
            ]
        }
    }
]

# Function to create JSON implementation guides
def generate_json_implementation_guides(models):
    for model in models:
        # Create the implementation guide JSON file
        filepath = f"results/youth_opportunities/implementation_guides/{model['model_id']}_implementation_guide.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(model, f, indent=4)
        print(f"Created implementation guide JSON for {model['model_id']}: {model['model_name']}")
        
        # Also create a separate case study file if available
        if "case_study" in model:
            case_study_filepath = f"results/youth_opportunities/case_studies/{model['model_id']}_case_study.json"
            with open(case_study_filepath, 'w', encoding='utf-8') as f:
                json.dump(model["case_study"], f, indent=4)
            print(f"Created case study JSON for {model['model_id']}")

# Function to create markdown implementation guides
def generate_markdown_implementation_guides(models):
    for model in models:
        # Create markdown version for better readability
        filepath = f"results/youth_opportunities/implementation_guides/{model['model_id']}_implementation_guide.md"
        
        # Begin constructing the markdown content
        md_content = f"# {model['model_name']} Implementation Guide\n\n"
        md_content += f"**Model ID:** {model['model_id']}\n\n"
        md_content += f"**Tagline:** {model.get('tagline', '')}\n\n"
        
        # Description
        if "description" in model:
            md_content += "## Overview\n\n"
            md_content += f"{model['description'].strip()}\n\n"
        
        # Value proposition
        if "value_proposition" in model:
            md_content += "## Value Proposition\n\n"
            for item in model['value_proposition']:
                md_content += f"- {item}\n"
            md_content += "\n"
        
        # Target crops and customers
        if "target_crops" in model:
            md_content += "## Target Crops\n\n"
            md_content += ", ".join(model['target_crops']) + "\n\n"
        
        if "target_customers" in model:
            md_content += "## Target Customers\n\n"
            if isinstance(model['target_customers'], list):
                for customer in model['target_customers']:
                    md_content += f"- {customer}\n"
            elif isinstance(model['target_customers'], dict):
                for category, customers in model['target_customers'].items():
                    md_content += f"### {category.title()}\n\n"
                    for customer in customers:
                        md_content += f"- {customer}\n"
                    md_content += "\n"
            md_content += "\n"
        
        # Geographical focus
        if "geographical_focus" in model:
            md_content += "## Geographical Focus\n\n"
            for area in model['geographical_focus']:
                md_content += f"- {area}\n"
            md_content += "\n"
        
        # Equipment needs
        if "equipment_needs" in model:
            md_content += "## Equipment Needs\n\n"
            
            if "essential" in model['equipment_needs']:
                md_content += "### Essential Equipment\n\n"
                md_content += "| Item | Specifications | Estimated Cost | Lifespan |\n"
                md_content += "|------|---------------|----------------|----------|\n"
                for item in model['equipment_needs']['essential']:
                    md_content += f"| {item['item']} | {item['specifications']} | {item['estimated_cost']} | {item['lifespan']} |\n"
                md_content += "\n"
            
            if "optional" in model['equipment_needs']:
                md_content += "### Optional Equipment\n\n"
                md_content += "| Item | Specifications | Estimated Cost | Lifespan |\n"
                md_content += "|------|---------------|----------------|----------|\n"
                for item in model['equipment_needs']['optional']:
                    md_content += f"| {item['item']} | {item['specifications']} | {item['estimated_cost']} | {item['lifespan']} |\n"
                md_content += "\n"
        
        # Setup costs
        if "setup_costs" in model:
            md_content += "## Setup Costs\n\n"
            md_content += "| Category | Cost |\n"
            md_content += "|----------|------|\n"
            for category, cost in model['setup_costs'].items():
                md_content += f"| {category.replace('_', ' ').title()} | {cost} |\n"
            md_content += "\n"
        
        # Revenue model
        if "revenue_model" in model:
            md_content += "## Revenue Model\n\n"
            for key, value in model['revenue_model'].items():
                if isinstance(value, list):
                    md_content += f"### {key.replace('_', ' ').title()}\n\n"
                    for item in value:
                        if isinstance(item, dict):
                            for k, v in item.items():
                                md_content += f"**{k.replace('_', ' ').title()}:** {v}\n\n"
                        else:
                            md_content += f"- {item}\n"
                    md_content += "\n"
                else:
                    md_content += f"**{key.replace('_', ' ').title()}:** {value}\n\n"
        
        # Operating costs
        if "operating_costs" in model:
            md_content += "## Operating Costs\n\n"
            md_content += "| Category | Cost |\n"
            md_content += "|----------|------|\n"
            for category, cost in model['operating_costs'].items():
                md_content += f"| {category.replace('_', ' ').title()} | {cost} |\n"
            md_content += "\n"
        
        # Profitability
        if "profitability" in model:
            md_content += "## Profitability\n\n"
            for key, value in model['profitability'].items():
                md_content += f"**{key.replace('_', ' ').title()}:** {value}\n\n"
        
        # Key success factors
        if "key_success_factors" in model:
            md_content += "## Key Success Factors\n\n"
            for factor in model['key_success_factors']:
                md_content += f"- {factor}\n"
            md_content += "\n"
        
        # Challenges and solutions
        if "challenges_and_solutions" in model:
            md_content += "## Challenges and Solutions\n\n"
            for item in model['challenges_and_solutions']:
                md_content += f"### Challenge: {item['challenge']}\n\n"
                md_content += "**Solutions:**\n\n"
                for solution in item['solutions']:
                    md_content += f"- {solution}\n"
                md_content += "\n"
        
        # Implementation steps
        if "implementation_steps" in model:
            md_content += "## Implementation Steps\n\n"
            for item in model['implementation_steps']:
                md_content += f"### {item['step']}\n\n"
                md_content += "**Activities:**\n\n"
                for activity in item['activities']:
                    md_content += f"- {activity}\n"
                md_content += "\n"
                md_content += f"**Timeframe:** {item['timeframe']}\n\n"
                md_content += f"**Resources Needed:** {item['resources_needed']}\n\n"
                md_content += f"**Success Indicators:** {item['success_indicators']}\n\n"
        
        # Digital enhancements
        if "digital_enhancements" in model:
            md_content += "## Digital Enhancements\n\n"
            
            if "essential" in model['digital_enhancements']:
                md_content += "### Essential Digital Tools\n\n"
                for tool in model['digital_enhancements']['essential']:
                    md_content += f"#### {tool['technology']}\n\n"
                    md_content += f"**Description:** {tool['description']}\n\n"
                    md_content += f"**Benefits:** {tool['benefits']}\n\n"
                    md_content += f"**Implementation:** {tool['implementation']}\n\n"
            
            if "advanced" in model['digital_enhancements']:
                md_content += "### Advanced Digital Tools\n\n"
                for tool in model['digital_enhancements']['advanced']:
                    md_content += f"#### {tool['technology']}\n\n"
                    md_content += f"**Description:** {tool['description']}\n\n"
                    md_content += f"**Benefits:** {tool['benefits']}\n\n"
                    md_content += f"**Implementation:** {tool['implementation']}\n\n"
        
        # Financing options
        if "financing_options" in model:
            md_content += "## Financing Options\n\n"
            for option in model['financing_options']:
                md_content += f"### {option['option']}\n\n"
                md_content += f"**Providers:** {option['providers']}\n\n"
                md_content += f"**Features:** {option['features']}\n\n"
                md_content += f"**Requirements:** {option['requirements']}\n\n"
                md_content += f"**Application Process:** {option['application_process']}\n\n"
        
        # Write the markdown file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Created implementation guide markdown for {model['model_id']}: {model['model_name']}")
        
        # Create case study markdown if available
        if "case_study" in model:
            case_study_filepath = f"results/youth_opportunities/case_studies/{model['model_id']}_case_study.md"
            
            cs_md_content = f"# Case Study: {model['case_study']['title']}\n\n"
            cs_md_content += f"**Entrepreneur:** {model['case_study']['entrepreneur']}\n\n"
            cs_md_content += "## Background\n\n"
            cs_md_content += f"{model['case_study']['background'].strip()}\n\n"
            cs_md_content += "## Starting Point\n\n"
            cs_md_content += f"{model['case_study']['starting_point'].strip()}\n\n"
            cs_md_content += "## Implementation\n\n"
            cs_md_content += f"{model['case_study']['implementation'].strip()}\n\n"
            cs_md_content += "## Challenges Faced\n\n"
            cs_md_content += f"{model['case_study']['challenges_faced'].strip()}\n\n"
            cs_md_content += "## Results\n\n"
            cs_md_content += f"{model['case_study']['results'].strip()}\n\n"
            
            cs_md_content += "## Key Lessons\n\n"
            for lesson in model['case_study']['key_lessons']:
                cs_md_content += f"- {lesson}\n"
            cs_md_content += "\n"
            
            cs_md_content += "## Future Plans\n\n"
            cs_md_content += f"{model['case_study']['future_plans'].strip()}\n\n"
            
            with open(case_study_filepath, 'w', encoding='utf-8') as f:
                f.write(cs_md_content)
            
            print(f"Created case study markdown for {model['model_id']}")

# Create visualizations for the business models
def create_business_model_visualizations(models):
    # Prepare data for charts
    model_ids = [model['model_id'] for model in models]
    model_names = [model['model_name'] for model in models]
    
    # Investment ranges
    min_investments = []
    max_investments = []
    for model in models:
        if 'setup_costs' in model and 'total_investment' in model['setup_costs']:
            cost_range = model['setup_costs']['total_investment']
            min_val, max_val = parse_cost_range(cost_range)
            min_investments.append(min_val)
            max_investments.append(max_val)
        elif 'setup_costs' in model and 'total_initial_investment' in model['setup_costs']:
            cost_range = model['setup_costs']['total_initial_investment']
            min_val, max_val = parse_cost_range(cost_range)
            min_investments.append(min_val)
            max_investments.append(max_val)
        else:
            min_investments.append(0)
            max_investments.append(0)
    
    # Create investment comparison chart
    plt.figure(figsize=(12, 8))
    width = 0.35
    x = np.arange(len(model_ids))
    
    plt.bar(x - width/2, min_investments, width, label='Minimum Investment')
    plt.bar(x + width/2, max_investments, width, label='Maximum Investment')
    
    plt.xlabel('Business Model')
    plt.ylabel('Investment Amount (N)')
    plt.title('Investment Requirements by Business Model')
    plt.xticks(x, model_names, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('results/youth_opportunities/investment_comparison.png', dpi=300)
    plt.close()
    print("Created investment comparison visualization")
    
    # Create ROI comparison chart if available
    roi_values = []
    for model in models:
        if 'profitability' in model and 'roi' in model['profitability']:
            roi_text = model['profitability']['roi']
            # Extract numeric part from text like "15-30% annually"
            if '-' in roi_text:
                parts = roi_text.split('-')
                if '%' in parts[1]:
                    max_roi = float(parts[1].split('%')[0])
                    roi_values.append(max_roi)
                else:
                    roi_values.append(0)
            else:
                roi_values.append(0)
        else:
            roi_values.append(0)
    
    if any(roi_values):
        plt.figure(figsize=(12, 8))
        plt.bar(model_names, roi_values, color='green')
        plt.xlabel('Business Model')
        plt.ylabel('Maximum ROI (%)')
        plt.title('Maximum Annual ROI Potential by Business Model')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save the chart
        plt.savefig('results/youth_opportunities/roi_comparison.png', dpi=300)
        plt.close()
        print("Created ROI comparison visualization")

# Helper function to parse cost ranges like "N955,000 - N1,625,000"
def parse_cost_range(cost_range):
    parts = cost_range.split(' - ')
    
    # Remove "N" and commas, then convert to float
    min_val = float(parts[0].replace('N', '').replace(',', ''))
    max_val = float(parts[1].replace('N', '').replace(',', ''))
    
    return min_val, max_val

# Create an index file for all implementation guides
def create_index_file(models):
    # Create JSON index
    index = {
        "title": "YouthHarvest Business Model Implementation Guides",
        "description": """
        Comprehensive guides for youth-led post-harvest loss reduction businesses. Each model includes 
        detailed implementation steps, investment requirements, profitability analysis, and success factors.
        """,
        "available_models": []
    }
    
    for model in models:
        model_info = {
            "model_id": model["model_id"],
            "model_name": model["model_name"],
            "tagline": model.get("tagline", ""),
            "description": model["description"].strip() if "description" in model else "",
            "investment_range": model["setup_costs"]["total_investment"] if "setup_costs" in model and "total_investment" in model["setup_costs"] else model["setup_costs"].get("total_initial_investment", "N/A"),
            "has_case_study": "case_study" in model,
            "implementation_guide_url": f"{model['model_id']}_implementation_guide.json",
            "markdown_url": f"{model['model_id']}_implementation_guide.md"
        }
        index["available_models"].append(model_info)
    
    # Save JSON index
    with open('results/youth_opportunities/implementation_guides/index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=4)
    print("Created index JSON for implementation guides")
    
    # Create markdown index
    md_content = "# YouthHarvest Business Model Implementation Guides\n\n"
    md_content += """
    This directory contains comprehensive implementation guides for youth-led businesses focused on
    reducing post-harvest losses in Nigeria. Each guide provides detailed information on setup costs, 
    equipment needs, implementation steps, and financial projections.
    
    ## Available Business Models
    
    """
    
    for model in models:
        md_content += f"### {model['model_id']}: {model['model_name']}\n\n"
        md_content += f"**{model.get('tagline', '')}**\n\n"
        
        if "description" in model:
            md_content += f"{model['description'].strip()}\n\n"
        
        if "setup_costs" in model:
            if "total_investment" in model["setup_costs"]:
                md_content += f"**Investment Range:** {model['setup_costs']['total_investment']}\n\n"
            elif "total_initial_investment" in model["setup_costs"]:
                md_content += f"**Investment Range:** {model['setup_costs']['total_initial_investment']}\n\n"
        
        md_content += f"- [View Implementation Guide (JSON)](./{model['model_id']}_implementation_guide.json)\n"
        md_content += f"- [View Implementation Guide (Markdown)](./{model['model_id']}_implementation_guide.md)\n"
        
        if "case_study" in model:
            md_content += f"- [View Case Study (JSON)](./../case_studies/{model['model_id']}_case_study.json)\n"
            md_content += f"- [View Case Study (Markdown)](./../case_studies/{model['model_id']}_case_study.md)\n"
        
        md_content += "\n"
    
    # Save markdown index
    with open('results/youth_opportunities/implementation_guides/README.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("Created README index for implementation guides")

# Execute the functions to generate all outputs
generate_json_implementation_guides(priority_business_models)
generate_markdown_implementation_guides(priority_business_models)
create_business_model_visualizations(priority_business_models)
create_index_file(priority_business_models)

print("\nBusiness implementation guides successfully created!")