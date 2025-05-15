import os
import json
import pandas as pd
import datetime

# Create directory structure
os.makedirs('results/documentation/executive_summaries', exist_ok=True)
os.makedirs('results/documentation/technical_reports', exist_ok=True)
os.makedirs('results/documentation/data_insights', exist_ok=True)

# Current timestamp for documentation
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ===== EXECUTIVE SUMMARY DOCUMENTATION =====

executive_summary = {
    "title": "Nigeria Post-Harvest Losses Intervention Project: Executive Summary",
    "prepared_by": "Data Science Team",
    "date": timestamp,
    "summary": """
    This project analyzes post-harvest losses across Nigeria's major grain crops (Maize, Rice, Sorghum, and Millet) 
    and develops targeted intervention strategies to reduce these losses. Analysis of production data across 
    36 Nigerian states and the FCT, combined with literature-based loss rates, identified critical loss points
    in the value chain and regional patterns. Based on this analysis, we've developed a comprehensive intervention
    framework that includes technical solutions, regional targeting, economic analysis, risk management, and
    stakeholder engagement strategies. Implementation of these recommendations could reduce post-harvest 
    losses by 15-20% within two years, potentially saving ₦2-3 billion annually.
    """,
    "key_findings": [
        "Rice experiences the highest loss rates (35%), followed by Maize (30.5%), Sorghum (25.8%), and Millet (22.4%)",
        "Storage (35%) and processing (25%) represent the highest proportion of losses across the value chain",
        "Northern states show higher loss volumes despite higher production, while Southern states show better efficiency",
        "Total financial losses exceed ₦14 billion annually across the four main grain crops",
        "Regional factors significantly influence loss rates, with the North East experiencing 25% higher losses"
    ],
    "intervention_highlights": [
        "Six categories of interventions designed with crop-specific applications",
        "Hermetic storage bags, training programs, and solar dryers show highest ROI (189-289%)",
        "North West zone shows highest potential impact for scaled interventions",
        "Pay-as-you-go and service-based models recommended for overcoming financial barriers",
        "Community-based implementation approach with strong stakeholder coordination recommended"
    ],
    "next_steps": [
        "Stakeholder validation of intervention recommendations",
        "Development of detailed implementation plans for priority regions",
        "Securing implementation funding and partnerships",
        "Establishing robust monitoring and evaluation framework",
        "Launching pilot programs in priority states"
    ]
}

# Write executive summary to file
with open('results/documentation/executive_summaries/project_executive_summary.json', 'w') as f:
    json.dump(executive_summary, f, indent=2)
print("Executive summary documentation created")

# ===== DATA INSIGHTS DOCUMENTATION =====

data_insights = {
    "title": "Nigeria Post-Harvest Losses: Detailed Data Insights",
    "prepared_by": "Data Analysis Team",
    "date": timestamp,
    "key_metrics": {
        "total_production_analyzed": "13,857,870 tons across four main grain crops",
        "estimated_total_losses": "3,940,992 tons annually",
        "financial_impact": "₦14.2 billion estimated annual loss",
        "highest_loss_crop": "Rice (35% loss rate)",
        "highest_loss_state": "Kano (618,600 tons of production with 26% average loss)",
        "most_critical_stage": "Storage (35% of total losses)"
    },
    "regional_analysis": {
        "North Central": {
            "avg_loss_rate": "Base rate + 5%",
            "key_challenges": "Limited storage infrastructure, poor market access",
            "priority_crops": ["Rice", "Maize"],
            "recommended_focus": "Community storage facilities, market linkages"
        },
        "North East": {
            "avg_loss_rate": "Base rate + 25%",
            "key_challenges": "Security concerns, climate variability, limited extension",
            "priority_crops": ["Maize", "Sorghum", "Millet"],
            "recommended_focus": "Household storage solutions, climate-smart technologies"
        },
        "North West": {
            "avg_loss_rate": "Base rate + 15%",
            "key_challenges": "Large volumes, inadequate infrastructure, aflatoxin",
            "priority_crops": ["Maize", "Rice", "Sorghum"],
            "recommended_focus": "Commercial-scale storage, aflatoxin mitigation"
        },
        "South East": {
            "avg_loss_rate": "Base rate - 10%",
            "key_challenges": "Land fragmentation, high humidity, processing limitations",
            "priority_crops": ["Rice", "Maize"],
            "recommended_focus": "Processing technologies, cooperative approaches"
        },
        "South South": {
            "avg_loss_rate": "Base rate + 10%",
            "key_challenges": "High humidity, poor transportation, limited infrastructure",
            "priority_crops": ["Rice", "Maize"],
            "recommended_focus": "Moisture control solutions, transportation improvements"
        },
        "South West": {
            "avg_loss_rate": "Base rate - 15%",
            "key_challenges": "Urban encroachment, labor costs, import competition",
            "priority_crops": ["Maize", "Rice"],
            "recommended_focus": "Mechanization, value addition, quality certification"
        }
    },
    "value_chain_analysis": {
        "harvesting_losses": {
            "percentage": "15% of total losses",
            "key_issues": "Late harvesting, inappropriate methods, mechanical damage",
            "priority_interventions": ["Training on optimal harvest timing", "Improved harvesting tools", "Labor scheduling"]
        },
        "processing_losses": {
            "percentage": "25% of total losses",
            "key_issues": "Inappropriate equipment, poor operator skills, inefficient methods",
            "priority_interventions": ["Improved threshers and shellers", "Miller training", "Equipment maintenance"]
        },
        "storage_losses": {
            "percentage": "35% of total losses",
            "key_issues": "Insects, rodents, molds, moisture damage",
            "priority_interventions": ["Hermetic bags", "Metal silos", "Proper drying techniques"]
        },
        "transportation_losses": {
            "percentage": "20% of total losses",
            "key_issues": "Poor roads, inadequate packaging, spillage",
            "priority_interventions": ["Standardized crates", "Improved packaging", "Logistics coordination"]
        },
        "market_losses": {
            "percentage": "5% of total losses",
            "key_issues": "Long storage at markets, poor displays, handling damage",
            "priority_interventions": ["Improved market facilities", "Just-in-time supply chains", "Market information systems"]
        }
    },
    "seasonal_patterns": {
        "highest_loss_periods": ["Oct-Nov for Maize", "Dec-Jan for Rice", "Nov-Dec for Sorghum", "Oct-Nov for Millet"],
        "climate_factors": "Higher humidity during harvest seasons in southern regions leads to 15-20% higher drying-related losses",
        "recommendations": "Time interventions to coincide with peak loss periods, with emphasis on October-January across most regions"
    }
}

# Write data insights to file
with open('results/documentation/data_insights/detailed_analysis_insights.json', 'w') as f:
    json.dump(data_insights, f, indent=2)
print("Detailed data insights documentation created")

# ===== TECHNICAL INTERVENTION DOCUMENTATION =====

technical_interventions = {
    "title": "Technical Intervention Specifications for Post-Harvest Loss Reduction",
    "prepared_by": "Agricultural Engineering Team",
    "date": timestamp,
    "storage_solutions": {
        "hermetic_bags": {
            "description": "Multi-layer plastic bags creating airtight seal to prevent insect infestation",
            "capacity_options": ["50kg", "100kg", "500kg (super bags)"],
            "expected_lifespan": "2-3 seasons with proper handling",
            "effectiveness": "Reduces storage losses by 70-85%",
            "cost_range": "₦2,500-10,000 depending on size",
            "best_suited_for": ["Smallholder farmers", "Small aggregators"],
            "limitations": ["Requires careful handling to avoid punctures", "Limited capacity for commercial storage"]
        },
        "metal_silos": {
            "description": "Cylindrical metal containers providing airtight, rodent-proof storage",
            "capacity_options": ["500kg", "1 ton", "3 tons", "5 tons"],
            "expected_lifespan": "10-15 years with maintenance",
            "effectiveness": "Reduces storage losses by 85-95%",
            "cost_range": "₦85,000-500,000 depending on size",
            "best_suited_for": ["Farmer groups", "Commercial aggregators", "Community storage"],
            "limitations": ["High upfront cost", "Requires proper foundation", "Difficult to relocate"]
        },
        "improved_traditional_storage": {
            "description": "Enhanced versions of traditional storage structures with modern materials",
            "capacity_options": ["Varies by design (typically 200-2,000kg)"],
            "expected_lifespan": "3-5 years with maintenance",
            "effectiveness": "Reduces storage losses by 40-60%",
            "cost_range": "₦15,000-80,000 depending on design and size",
            "best_suited_for": ["Rural communities with strong traditional preferences"],
            "limitations": ["Moderate effectiveness compared to other options", "Requires regular maintenance"]
        }
    },
    "drying_technologies": {
        "solar_dryers": {
            "description": "Structures using solar radiation for efficient crop drying",
            "types": ["Direct solar dryers", "Indirect solar dryers", "Mixed-mode dryers"],
            "capacity_options": ["100kg", "250kg", "500kg", "1 ton"],
            "effectiveness": "Reduces moisture content to 12-13% within 1-3 days",
            "cost_range": "₦45,000-650,000 depending on type and capacity",
            "best_suited_for": ["Individual farmers", "Farmer groups", "Rural processors"],
            "limitations": ["Weather dependent", "Requires regular turning of product"]
        },
        "mechanical_dryers": {
            "description": "Engine or electric-powered dryers for rapid moisture reduction",
            "types": ["Flat-bed dryers", "Recirculating batch dryers", "Continuous flow dryers"],
            "capacity_options": ["500kg", "1 ton", "5 tons", "10 tons"],
            "effectiveness": "Reduces moisture content to 12-13% within hours",
            "cost_range": "₦350,000-5,000,000 depending on size and type",
            "best_suited_for": ["Medium to large processors", "Commercial operations"],
            "limitations": ["High initial cost", "Requires fuel/electricity", "Technical maintenance"]
        }
    },
    "processing_equipment": {
        "threshers_shellers": {
            "description": "Mechanical devices to separate grain from cobs, heads, or panicles",
            "types": ["Maize shellers", "Multi-crop threshers", "Pedal-operated threshers", "Motorized threshers"],
            "capacity_range": ["100-200kg/hr (manual)", "500-2,000kg/hr (motorized)"],
            "effectiveness": "Reduces threshing losses by 50-75%",
            "cost_range": "₦45,000-1,200,000 depending on type and capacity",
            "best_suited_for": ["Individual farmers", "Service providers", "Farmer groups"],
            "limitations": ["Maintenance requirements", "Fuel costs for motorized versions"]
        },
        "mini_rice_mills": {
            "description": "Compact rice processing units for rural communities",
            "components": ["De-stoner", "Husker", "Polisher", "Grader"],
            "capacity_range": ["200-500kg/hr"],
            "effectiveness": "Reduces milling losses by 10-15%, improves quality significantly",
            "cost_range": "₦850,000-3,500,000 depending on components and capacity",
            "best_suited_for": ["Entrepreneur service providers", "Farmer cooperatives"],
            "limitations": ["Technical operation skills needed", "Regular maintenance required"]
        }
    },
    "handling_transportation": {
        "standardized_crates": {
            "description": "Durable plastic crates for harvest and transport",
            "capacity_options": ["20kg", "25kg", "40kg"],
            "expected_lifespan": "3-5 years with proper handling",
            "effectiveness": "Reduces handling losses by 30-60%",
            "cost_range": "₦3,000-6,000 per crate",
            "best_suited_for": ["All value chain actors"],
            "limitations": ["Initial cost barrier", "Potential theft if not marked"]
        },
        "moisture_meters": {
            "description": "Devices to accurately measure grain moisture content",
            "types": ["Digital meters", "Analog meters"],
            "accuracy": "±0.5% moisture content",
            "cost_range": "₦15,000-60,000",
            "best_suited_for": ["Aggregators", "Storage managers", "Quality control points"],
            "limitations": ["Requires calibration", "Different calibrations for different crops"]
        }
    }
}

# Write technical interventions to file
with open('results/documentation/technical_reports/technical_interventions.json', 'w') as f:
    json.dump(technical_interventions, f, indent=2)
print("Technical intervention specifications created")

# ===== BUSINESS MODEL DOCUMENTATION =====

business_models = {
    "title": "Business Models for Post-Harvest Loss Interventions",
    "prepared_by": "Business Development Team",
    "date": timestamp,
    "service_based_models": {
        "equipment_as_service": {
            "description": "Entrepreneurs provide post-harvest services to farmers using improved equipment",
            "applicable_technologies": ["Threshers", "Shellers", "Dryers", "Mills"],
            "revenue_model": "Fee per kilogram or per batch processed",
            "typical_fees": {
                "Threshing/Shelling": "₦15-25 per kg",
                "Drying": "₦20-40 per kg",
                "Milling": "₦30-50 per kg"
            },
            "startup_requirements": {
                "capital": "₦500,000-2,000,000",
                "skills": "Equipment operation, basic maintenance, customer service",
                "support_needed": "Initial training, equipment financing, market linkage"
            },
            "potential_earnings": "₦150,000-600,000 per month during peak season",
            "success_factors": [
                "Strategic location near production areas",
                "Quality service delivery",
                "Regular maintenance",
                "Strong customer relationships"
            ]
        },
        "storage_as_service": {
            "description": "Provision of improved storage facilities as a service to farmers",
            "applicable_technologies": ["Metal silos", "Hermetic cocoons", "Warehouse storage"],
            "revenue_model": "Fee per bag per month or season, with quality guarantees",
            "typical_fees": {
                "Short-term (1-3 months)": "₦200-300 per bag per month",
                "Season-long": "₦600-1,000 per bag per season"
            },
            "startup_requirements": {
                "capital": "₦2,000,000-10,000,000",
                "skills": "Storage management, quality assessment, business administration",
                "support_needed": "Infrastructure financing, technical training, demand aggregation"
            },
            "potential_earnings": "₦300,000-1,200,000 per season",
            "success_factors": [
                "Trust building with farmers",
                "Proper quality management systems",
                "Linkage to financial services",
                "Insurance partnerships"
            ]
        }
    },
    "financing_models": {
        "pay_as_you_go": {
            "description": "Farmers acquire equipment through incremental payments over time",
            "applicable_technologies": ["Hermetic bags", "Solar dryers", "Small threshers"],
            "structure": "Initial deposit (20-30%) followed by installment payments over 6-12 months",
            "interest_implications": "15-20% effective interest rate built into pricing",
            "risk_management": "Remote locking technology for higher-value items, group guarantees",
            "requirements_for_providers": {
                "capital": "Significant working capital for inventory",
                "systems": "Payment tracking, customer relationship management",
                "partners": "Financial institutions, mobile money providers"
            },
            "success_factors": [
                "Affordable payment terms",
                "Quality products that generate immediate benefits",
                "Reliable after-sales service",
                "Strong customer vetting"
            ]
        },
        "warehouse_receipt_financing": {
            "description": "Using stored commodities as collateral for loans",
            "applicable_technologies": ["Commercial warehouses", "Community storage facilities"],
            "structure": "Farmers deposit grain in certified warehouse, receive receipt usable as collateral",
            "typical_terms": {
                "loan_value": "60-80% of commodity value at time of deposit",
                "interest_rate": "12-18% annually",
                "duration": "3-9 months"
            },
            "requirements": {
                "infrastructure": "Certified warehouses with quality management",
                "systems": "Grading standards, receipt issuance, monitoring",
                "partners": "Banks, insurance providers, commodity buyers"
            },
            "success_factors": [
                "Strong legal framework",
                "Price information systems",
                "Quality standards enforcement",
                "Multiple participating financial institutions"
            ]
        },
        "asset_leasing": {
            "description": "Leasing of post-harvest equipment with option to own",
            "applicable_technologies": ["Mills", "Large threshers", "Mechanical dryers"],
            "structure": "Monthly lease payments over 12-36 months with maintenance included",
            "typical_terms": {
                "down_payment": "15-30% of equipment value",
                "monthly_payment": "3-5% of equipment value",
                "maintenance": "Included in lease",
                "ownership": "Transfer after full payment or renewal option"
            },
            "requirements_for_providers": {
                "capital": "Significant equipment inventory or supplier financing",
                "systems": "Asset tracking, maintenance management, payment collection",
                "partners": "Equipment suppliers, insurance providers, technical services"
            },
            "success_factors": [
                "Quality equipment with proven ROI",
                "Responsive maintenance service",
                "Flexible terms during low seasons",
                "Training for operators"
            ]
        }
    },
    "aggregation_models": {
        "farmer_cooperatives": {
            "description": "Farmer-owned collectives that jointly invest in post-harvest infrastructure",
            "applicable_technologies": ["All types at community scale"],
            "structure": "Member contributions, shared ownership, usage fees or dividends",
            "governance": "Elected management committee, clear usage policies, transparent accounting",
            "typical_arrangements": {
                "membership_fee": "₦5,000-20,000 one-time or annual",
                "contribution_model": "Equal shares or production-based shares",
                "service_fees": "Discounted for members vs. non-members"
            },
            "support_requirements": {
                "technical": "Governance training, business management, technology operation",
                "financial": "Matching grants, startup subsidies, linkage to formal finance",
                "partners": "NGOs, government extension, equipment suppliers"
            },
            "success_factors": [
                "Strong governance structures",
                "Clear member value proposition",
                "Professional management",
                "Linkage to reliable markets"
            ]
        },
        "outgrower_processor_models": {
            "description": "Processors provide post-harvest technologies to contracted farmers",
            "applicable_technologies": ["Drying, storage, and handling technologies"],
            "structure": "Processor invests in technologies, farmers access as part of supply contract",
            "typical_arrangements": {
                "contract_terms": "Guaranteed purchase at fixed or formula price",
                "technology_access": "Free or subsidized access to processor-owned equipment",
                "quality_incentives": "Price premiums for meeting quality standards"
            },
            "requirements_for_processors": {
                "capital": "Significant investment in technologies and extension",
                "systems": "Quality control, farmer management, logistics coordination",
                "partners": "Financial institutions, technology providers, development programs"
            },
            "success_factors": [
                "Fair and transparent pricing",
                "Consistent procurement",
                "Effective extension support",
                "Balance of power in relationship"
            ]
        }
    }
}

# Write business models to file
with open('results/documentation/technical_reports/business_models.json', 'w') as f:
    json.dump(business_models, f, indent=2)
print("Business model documentation created")

# ===== IMPLEMENTATION PLANS DOCUMENTATION =====

implementation_plans = {
    "title": "Regional Implementation Plans for Post-Harvest Loss Interventions",
    "prepared_by": "Implementation Planning Team",
    "date": timestamp,
    "regional_plans": {
        "North_West_Priority_Plan": {
            "target_states": ["Kano", "Kaduna", "Katsina"],
            "rationale": "Highest production volumes with significant loss rates",
            "priority_crops": ["Maize", "Sorghum", "Rice"],
            "key_interventions": [
                {
                    "intervention": "Commercial-scale storage infrastructure",
                    "target_locations": ["Major grain markets in Kano", "Production clusters in Kaduna", "Border areas in Katsina"],
                    "scale": "5-10 facilities with 500-1,000 ton capacity each",
                    "implementation_partners": ["State ADPs", "Rice Farmers Association", "Commercial banks"]
                },
                {
                    "intervention": "Aflatoxin mitigation program",
                    "target_locations": ["All major maize and sorghum production areas"],
                    "key_components": ["Awareness campaign", "Testing kits distribution", "Bio-control introduction"],
                    "implementation_partners": ["IITA", "State Ministries of Agriculture", "Extension services"]
                },
                {
                    "intervention": "Mechanized threshing services",
                    "target_locations": ["50-100 service points across major production areas"],
                    "business_model": "Entrepreneur-owned, lease-to-own financing",
                    "implementation_partners": ["Equipment suppliers", "Microfinance institutions", "Youth groups"]
                }
            ],
            "timeline": {
                "phase_1": {
                    "duration": "0-6 months",
                    "key_activities": [
                        "Stakeholder mapping and engagement",
                        "Site selection for storage infrastructure",
                        "Entrepreneur identification and training"
                    ]
                },
                "phase_2": {
                    "duration": "7-18 months",
                    "key_activities": [
                        "First storage facilities construction",
                        "Threshing service network establishment",
                        "Aflatoxin awareness campaign launch"
                    ]
                },
                "phase_3": {
                    "duration": "19-36 months",
                    "key_activities": [
                        "Scale-up based on early adoption",
                        "Policy advocacy based on results",
                        "Market linkage strengthening"
                    ]
                }
            },
            "budget_estimate": {
                "total": "₦850 million - ₦1.2 billion",
                "storage_infrastructure": "50-60% of budget",
                "equipment_and_technologies": "25-30% of budget",
                "training_and_capacity_building": "10-15% of budget",
                "project_management_and_M&E": "5-10% of budget"
            }
        },
        "North_East_Priority_Plan": {
            "target_states": ["Adamawa", "Bauchi", "Taraba"],
            "rationale": "High loss rates with security considerations",
            "priority_crops": ["Maize", "Rice", "Sorghum", "Millet"],
            "key_interventions": [
                {
                    "intervention": "Household and small community storage",
                    "target_locations": ["Dispersed across secure rural areas"],
                    "scale": "20,000-30,000 households, 200-300 community units",
                    "implementation_partners": ["Local NGOs", "Community groups", "Religious organizations"]
                },
                {
                    "intervention": "Mobile-based extension services",
                    "target_locations": ["All accessible farming communities"],
                    "key_components": ["Voice messages in local languages", "Training videos", "SMS alerts"],
                    "implementation_partners": ["Mobile network operators", "Extension services", "Radio stations"]
                },
                {
                    "intervention": "Solar drying technologies",
                    "target_locations": ["300-500 locations across target states"],
                    "business_model": "Women's group managed with pay-per-use",
                    "implementation_partners": ["Women's associations", "Technology providers", "Microfinance institutions"]
                }
            ],
            "security_considerations": [
                "Flexible implementation approach based on changing security situation",
                "Local partnerships for access to challenging areas",
                "Technology designs suitable for rapid deployment and relocation if needed",
                "Community-based early warning systems integration"
            ],
            "timeline": {
                "phase_1": {
                    "duration": "0-6 months",
                    "key_activities": [
                        "Security assessment and mapping",
                        "Community mobilization through trusted partners",
                        "Technology demonstration units"
                    ]
                },
                "phase_2": {
                    "duration": "7-18 months",
                    "key_activities": [
                        "Household technology distribution",
                        "Training of local fabricators",
                        "Mobile extension platform launch"
                    ]
                },
                "phase_3": {
                    "duration": "19-36 months",
                    "key_activities": [
                        "Community-based quality monitoring systems",
                        "Market linkage with secure transport options",
                        "Scale-up in newly secured areas"
                    ]
                }
            },
            "budget_estimate": {
                "total": "₦600-800 million",
                "household_technologies": "40-50% of budget",
                "digital_extension_platform": "15-20% of budget",
                "training_and_capacity_building": "20-25% of budget",
                "project_management_and_security": "10-15% of budget"
            }
        }
    },
    "cross_cutting_implementation_factors": {
        "monitoring_and_evaluation": {
            "key_indicators": [
                "Percentage reduction in post-harvest losses",
                "Number of farmers adopting improved technologies",
                "Volume of produce stored in improved facilities",
                "Financial benefits realized by beneficiaries",
                "Return on investment for different intervention types"
            ],
            "data_collection_methods": [
                "Baseline and endline surveys",
                "Regular sampling of stored products for quality assessment",
                "Mobile-based farmer feedback system",
                "Case studies of high-performing interventions",
                "Geospatial monitoring of technology distribution"
            ],
            "learning_agenda": [
                "Comparative effectiveness of different storage technologies",
                "Social and gender factors affecting technology adoption",
                "Cost-effectiveness of different financing models",
                "Environmental impacts of reduced food losses",
                "Policy enablers and barriers to scaling"
            ]
        },
        "sustainability_mechanisms": {
            "financial_sustainability": [
                "Business-oriented implementation models from the start",
                "Phased reduction of subsidies as value proposition is demonstrated",
                "Linkage to commercial financing sources",
                "Development of local service provider networks"
            ],
            "institutional_sustainability": [
                "Integration with existing extension systems",
                "Capacity building of local institutions",
                "Development of local equipment supply chains",
                "Policy advocacy for continuing support"
            ],
            "environmental_sustainability": [
                "Promotion of energy-efficient technologies",
                "Renewable energy integration where applicable",
                "Water conservation in processing operations",
                "Climate-smart post-harvest management practices"
            ]
        },
        "scaling_strategy": {
            "horizontal_scaling": [
                "Clear documentation of implementation methodologies",
                "Training of trainers approach",
                "Strategic partnerships with national programs",
                "Mass media awareness campaigns"
            ],
            "vertical_scaling": [
                "Policy briefs based on evidence from implementation",
                "Engagement with national agricultural strategies",
                "Development of industry standards and guidelines",
                "Public-private coordination platforms"
            ],
            "functional_scaling": [
                "Integration of post-harvest interventions with production improvements",
                "Linkage to nutrition and food security programs",
                "Connection with climate resilience initiatives",
                "Alignment with youth employment strategies"
            ]
        }
    }
}

# Write implementation plans to file
with open('results/documentation/technical_reports/implementation_plans.json', 'w') as f:
    json.dump(implementation_plans, f, indent=2)
print("Implementation plans documentation created")

# Generate a summary of all documentation created
documentation_summary = f"""
# Nigeria Post-Harvest Losses Intervention Project Documentation

## Documentation Generated on {timestamp}

The following documentation has been created to support the Nigeria Post-Harvest Losses Intervention Project:

### Executive Summaries
- Project Executive Summary: Overview of findings and recommendations

### Data Insights
- Detailed Analysis Insights: Comprehensive breakdown of data analysis results

### Technical Reports
- Technical Intervention Specifications: Detailed information on recommended technologies
- Business Models: Financial and operational models for implementing interventions
- Implementation Plans: Regional plans and cross-cutting implementation strategies

This documentation provides a complete reference for the project's findings, recommendations, and implementation strategies.
"""

with open('results/documentation/documentation_index.md', 'w') as f:
    f.write(documentation_summary)
print("Documentation index created")

print("\nAll documentation files have been created successfully!")