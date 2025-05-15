import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json

# Ensure directory structure exists
os.makedirs('results/interventions/risks', exist_ok=True)

# Define a comprehensive risk assessment framework specific to post-harvest interventions
risk_categories = {
    "Implementation Risks": {
        "description": "Risks that affect the deployment and operation of post-harvest interventions",
        "risks": [
            {
                "risk_id": "IR-01",
                "risk_name": "Technology Adoption Resistance",
                "description": "Farmers and youth entrepreneurs hesitant to adopt new post-harvest technologies",
                "likelihood": "High",
                "impact": "High",
                "risk_score": 9,
                "affected_interventions": ["Storage Solutions", "Processing Technologies", "Digital Platforms"],
                "root_causes": [
                    "Cultural preferences for traditional methods",
                    "Fear of unknown technologies",
                    "Previous negative experiences with interventions",
                    "Lack of evidence of effectiveness in local context"
                ],
                "mitigation_strategies": [
                    "Implement participatory technology design with youth and farmer input",
                    "Setup demonstration sites showing clear before/after results",
                    "Identify and support early adopters as local champions",
                    "Provide risk-reduction guarantees for initial adoption period"
                ],
                "monitoring_indicators": [
                    "Technology adoption rates among target groups",
                    "User satisfaction surveys",
                    "Rate of continued use after 6 months"
                ]
            },
            {
                "risk_id": "IR-02",
                "risk_name": "Infrastructure Limitations",
                "description": "Inadequate supporting infrastructure (electricity, roads, internet) for technology deployment",
                "likelihood": "High",
                "impact": "Medium",
                "risk_score": 6,
                "affected_interventions": ["Cold Chain Solutions", "Processing Facilities", "Digital Platforms"],
                "root_causes": [
                    "Limited rural electrification",
                    "Poor road networks in agricultural areas",
                    "Limited internet connectivity",
                    "Inadequate water supply for processing"
                ],
                "mitigation_strategies": [
                    "Design solutions with minimal infrastructure dependencies",
                    "Incorporate renewable energy components (solar, biogas)",
                    "Develop offline-first digital solutions",
                    "Create hub-and-spoke models centered around available infrastructure"
                ],
                "monitoring_indicators": [
                    "Hours of operational downtime due to infrastructure",
                    "Additional costs attributed to infrastructure limitations",
                    "Successful adaptations implemented"
                ]
            },
            {
                "risk_id": "IR-03",
                "risk_name": "Technical Skills Gap",
                "description": "Insufficient technical knowledge among youth entrepreneurs to operate or maintain technologies",
                "likelihood": "Medium",
                "impact": "High",
                "risk_score": 6,
                "affected_interventions": ["Processing Technologies", "Quality Testing Equipment", "Cold Chain Systems"],
                "root_causes": [
                    "Limited technical education in rural areas",
                    "Brain drain of technically skilled youth to urban centers",
                    "Mismatch between educational curricula and required skills",
                    "Lack of hands-on training opportunities"
                ],
                "mitigation_strategies": [
                    "Develop comprehensive skills training program for each technology",
                    "Create apprenticeship opportunities with experienced operators",
                    "Establish technical support hotlines and troubleshooting guides",
                    "Build technology maintenance into business models as a service"
                ],
                "monitoring_indicators": [
                    "Number of youth trained on each technology",
                    "Technical problem resolution time",
                    "Equipment downtime due to technical issues"
                ]
            }
        ]
    },
    "Financial Risks": {
        "description": "Risks related to financial viability and sustainability of interventions",
        "risks": [
            {
                "risk_id": "FR-01",
                "risk_name": "Limited Access to Startup Capital",
                "description": "Youth entrepreneurs unable to secure initial funding for post-harvest businesses",
                "likelihood": "High",
                "impact": "High",
                "risk_score": 9,
                "affected_interventions": ["Storage Facilities", "Processing Equipment", "Transport Solutions"],
                "root_causes": [
                    "Traditional financial institutions view youth and agriculture as high-risk",
                    "Limited collateral among youth entrepreneurs",
                    "High interest rates for agricultural investments",
                    "Complex loan application procedures"
                ],
                "mitigation_strategies": [
                    "Design low-cost entry business models with phased investment",
                    "Develop equipment leasing and pay-as-you-earn models",
                    "Create risk-sharing arrangements with equipment suppliers",
                    "Establish rotating savings groups among youth entrepreneurs",
                    "Facilitate access to agricultural grants and impact investment"
                ],
                "monitoring_indicators": [
                    "Number of youth securing startup funding",
                    "Average startup capital requirements",
                    "Diversity of funding sources accessed"
                ]
            },
            {
                "risk_id": "FR-02",
                "risk_name": "Irregular Cash Flow",
                "description": "Seasonal variations in agricultural activities leading to inconsistent revenue",
                "likelihood": "High",
                "impact": "Medium",
                "risk_score": 6,
                "affected_interventions": ["Service-Based Businesses", "Processing Enterprises", "Storage Services"],
                "root_causes": [
                    "Seasonality of harvests and processing needs",
                    "Delayed payments from farmers or buyers",
                    "Fluctuating demand throughout the year",
                    "Limited crop diversification in served areas"
                ],
                "mitigation_strategies": [
                    "Design multi-crop business models that operate year-round",
                    "Develop complementary off-season services",
                    "Create flexible payment terms and subscription models",
                    "Establish reserve funds for lean periods",
                    "Integrate with value-added processing to extend service period"
                ],
                "monitoring_indicators": [
                    "Monthly revenue fluctuation rates",
                    "Cash reserve adequacy during low seasons",
                    "Diversity of income sources"
                ]
            },
            {
                "risk_id": "FR-03",
                "risk_name": "Rising Operating Costs",
                "description": "Increases in fuel, electricity, or maintenance costs threatening business viability",
                "likelihood": "Medium",
                "impact": "Medium",
                "risk_score": 4,
                "affected_interventions": ["Mobile Services", "Processing Facilities", "Cold Chain Solutions"],
                "root_causes": [
                    "Fuel price volatility",
                    "Inconsistent electricity costs and supply",
                    "Import-dependent spare parts subject to currency fluctuations",
                    "Increasing labor costs"
                ],
                "mitigation_strategies": [
                    "Transition to renewable energy sources where possible",
                    "Implement preventive maintenance schedules to reduce major repairs",
                    "Develop local fabrication of common spare parts",
                    "Create service bundling to optimize operational costs",
                    "Implement energy efficiency measures"
                ],
                "monitoring_indicators": [
                    "Energy cost as percentage of operating expenses",
                    "Maintenance cost trends",
                    "Cost reduction from efficiency measures"
                ]
            }
        ]
    },
    "Market Risks": {
        "description": "Risks related to market access, pricing, and competition",
        "risks": [
            {
                "risk_id": "MR-01",
                "risk_name": "Price Volatility",
                "description": "Significant fluctuations in crop prices affecting ROI calculations",
                "likelihood": "High",
                "impact": "High",
                "risk_score": 9,
                "affected_interventions": ["Storage Services", "Aggregation Businesses", "Processing Enterprises"],
                "root_causes": [
                    "Seasonal supply variations",
                    "Limited market information",
                    "External market disruptions (imports, policy changes)",
                    "Weak bargaining position of smallholder farmers"
                ],
                "mitigation_strategies": [
                    "Develop market information systems for price monitoring",
                    "Create storage strategies tied to price forecasting",
                    "Establish forward contracts where possible",
                    "Diversify crop portfolios to spread risk",
                    "Focus on value addition to reduce commodity price exposure"
                ],
                "monitoring_indicators": [
                    "Price volatility index by crop",
                    "Forecast accuracy measurements",
                    "Business resilience to price shocks"
                ]
            },
            {
                "risk_id": "MR-02",
                "risk_name": "Limited Market Access",
                "description": "Difficulties connecting improved post-harvest products to premium markets",
                "likelihood": "Medium",
                "impact": "High",
                "risk_score": 6,
                "affected_interventions": ["Quality Testing Services", "Storage Solutions", "Processing Businesses"],
                "root_causes": [
                    "Physical distance from major markets",
                    "Lack of aggregation and bulking systems",
                    "Limited market information on quality requirements",
                    "Poor transportation infrastructure",
                    "Established market relationships that exclude newcomers"
                ],
                "mitigation_strategies": [
                    "Develop digital market linkage platforms",
                    "Establish collective marketing arrangements",
                    "Create quality certification systems with market recognition",
                    "Facilitate contract farming arrangements with processors",
                    "Support development of local market infrastructure"
                ],
                "monitoring_indicators": [
                    "Premium market access rate",
                    "Price differentials achieved for quality products",
                    "Contract fulfillment rates"
                ]
            },
            {
                "risk_id": "MR-03",
                "risk_name": "Competition from Established Players",
                "description": "Existing market actors may resist entry of youth businesses or engage in unfair competition",
                "likelihood": "Medium",
                "impact": "Medium",
                "risk_score": 4,
                "affected_interventions": ["Processing Services", "Aggregation Businesses", "Storage Facilities"],
                "root_causes": [
                    "Entrenched interests in existing value chains",
                    "Information asymmetry favoring established players",
                    "Economic power imbalances",
                    "Limited differentiation in service offerings"
                ],
                "mitigation_strategies": [
                    "Focus on underserved market segments",
                    "Develop technology-based competitive advantages",
                    "Create strategic partnerships with established players",
                    "Emphasize quality differentiation and specialized services",
                    "Build strong farmer relationships and loyalty programs"
                ],
                "monitoring_indicators": [
                    "Market share trends",
                    "Service differentiation metrics",
                    "Customer retention rates"
                ]
            }
        ]
    },
    "Environmental and Climate Risks": {
        "description": "Risks related to environmental conditions and climate change",
        "risks": [
            {
                "risk_id": "ER-01",
                "risk_name": "Extreme Weather Events",
                "description": "Floods, droughts, or extreme temperatures affecting crop quality and post-harvest operations",
                "likelihood": "Medium",
                "impact": "High",
                "risk_score": 6,
                "affected_interventions": ["Drying Technologies", "Storage Facilities", "Field-Based Services"],
                "root_causes": [
                    "Increasing climate variability",
                    "Limited early warning systems",
                    "Infrastructure vulnerabilities",
                    "Limited climate adaptation in technology design"
                ],
                "mitigation_strategies": [
                    "Design climate-resilient infrastructure (elevated storage, water-resistant materials)",
                    "Integrate weather monitoring into service delivery planning",
                    "Develop flexible scheduling systems for climate-dependent operations",
                    "Create emergency response protocols for extreme events",
                    "Implement climate-smart post-harvest practices"
                ],
                "monitoring_indicators": [
                    "Service disruptions due to weather events",
                    "Climate resilience score of facilities",
                    "Recovery time after disruptions"
                ]
            },
            {
                "risk_id": "ER-02",
                "risk_name": "Pest and Disease Outbreaks",
                "description": "Storage pests or diseases affecting product quality and safety",
                "likelihood": "High",
                "impact": "Medium",
                "risk_score": 6,
                "affected_interventions": ["Storage Services", "Aggregation Businesses", "Quality Testing Services"],
                "root_causes": [
                    "Changing climate conditions favoring pest development",
                    "Limited integrated pest management knowledge",
                    "Poor hygiene in storage and handling",
                    "Inappropriate use of pesticides"
                ],
                "mitigation_strategies": [
                    "Implement comprehensive integrated pest management systems",
                    "Develop early detection protocols and regular monitoring",
                    "Train youth entrepreneurs in pest identification and management",
                    "Design storage facilities with pest prevention features",
                    "Establish quarantine protocols for infested products"
                ],
                "monitoring_indicators": [
                    "Infestation rates in stored products",
                    "Economic losses due to pest damage",
                    "Effectiveness of pest management interventions"
                ]
            },
            {
                "risk_id": "ER-03",
                "risk_name": "Resource Constraints",
                "description": "Limited availability of water, energy, or other resources for post-harvest operations",
                "likelihood": "Medium",
                "impact": "Medium",
                "risk_score": 4,
                "affected_interventions": ["Processing Technologies", "Cold Chain Solutions", "Washing Facilities"],
                "root_causes": [
                    "Water scarcity in some regions",
                    "Limited access to reliable energy",
                    "Competition for resources with other sectors",
                    "Poor resource management practices"
                ],
                "mitigation_strategies": [
                    "Design resource-efficient technologies (water recycling, energy-efficient equipment)",
                    "Incorporate renewable energy solutions (solar, biogas)",
                    "Implement resource management and conservation plans",
                    "Develop alternative processing methods requiring fewer resources",
                    "Create resource-sharing arrangements among businesses"
                ],
                "monitoring_indicators": [
                    "Resource efficiency metrics",
                    "Renewable energy percentage of total consumption",
                    "Resource cost as percentage of operating expenses"
                ]
            }
        ]
    },
    "Social and Organizational Risks": {
        "description": "Risks related to social dynamics and organizational structures",
        "risks": [
            {
                "risk_id": "SR-01",
                "risk_name": "Gender Barriers",
                "description": "Cultural norms limiting women's participation in post-harvest businesses",
                "likelihood": "High",
                "impact": "Medium",
                "risk_score": 6,
                "affected_interventions": ["All youth-led interventions, especially in traditional communities"],
                "root_causes": [
                    "Traditional gender roles in agriculture",
                    "Limited asset ownership among women",
                    "Time poverty due to household responsibilities",
                    "Lower literacy and education levels in some regions"
                ],
                "mitigation_strategies": [
                    "Design women-specific business models accounting for constraints",
                    "Develop household dialogue approaches for shared decision-making",
                    "Create women-led peer groups and mentorship programs",
                    "Implement gender-sensitive training schedules and locations",
                    "Promote women's leadership in cooperatives and associations"
                ],
                "monitoring_indicators": [
                    "Percentage of women-led businesses",
                    "Income levels of female entrepreneurs",
                    "Women's participation in decision-making"
                ]
            },
            {
                "risk_id": "SR-02",
                "risk_name": "Youth Migration",
                "description": "Rural-urban migration reducing skilled youth available for agribusiness",
                "likelihood": "High",
                "impact": "Medium",
                "risk_score": 6,
                "affected_interventions": ["All youth-led interventions, especially in remote areas"],
                "root_causes": [
                    "Perception of agriculture as unattractive",
                    "Limited rural economic opportunities",
                    "Urban lifestyle aspirations",
                    "Poor rural infrastructure and services"
                ],
                "mitigation_strategies": [
                    "Create modern, technology-enabled business models appealing to youth",
                    "Develop clear progression pathways and growth opportunities",
                    "Facilitate peer-to-peer learning and support networks",
                    "Highlight and promote successful youth agripreneurs as role models",
                    "Integrate digital and modern elements into traditional agricultural practices"
                ],
                "monitoring_indicators": [
                    "Youth retention rate in rural agribusiness",
                    "Age profile of post-harvest entrepreneurs",
                    "Perception surveys on agricultural careers"
                ]
            },
            {
                "risk_id": "SR-03",
                "risk_name": "Collective Action Challenges",
                "description": "Difficulties in coordinating multiple stakeholders for effective value chain integration",
                "likelihood": "Medium",
                "impact": "Medium",
                "risk_score": 4,
                "affected_interventions": ["Cooperative-Based Models", "Shared Facilities", "Collective Marketing"],
                "root_causes": [
                    "History of failed cooperative ventures",
                    "Limited business management capacity",
                    "Trust issues among value chain actors",
                    "Inadequate governance structures"
                ],
                "mitigation_strategies": [
                    "Develop transparent governance systems with clear roles",
                    "Start with small, achievable collective actions to build trust",
                    "Provide training in cooperative management and governance",
                    "Implement digital tools for transparency and accountability",
                    "Create appropriate incentive structures for participation"
                ],
                "monitoring_indicators": [
                    "Member participation rates",
                    "Governance effectiveness scores",
                    "Benefit distribution equity",
                    "Conflict resolution effectiveness"
                ]
            }
        ]
    },
    "Policy and Regulatory Risks": {
        "description": "Risks related to government policies, regulations, and institutional support",
        "risks": [
            {
                "risk_id": "PR-01",
                "risk_name": "Policy Inconsistency",
                "description": "Changing government policies affecting agricultural investments and market conditions",
                "likelihood": "Medium",
                "impact": "High",
                "risk_score": 6,
                "affected_interventions": ["Long-term Investments", "Export-Oriented Businesses", "Subsidized Services"],
                "root_causes": [
                    "Political cycles affecting policy continuity",
                    "Limited evidence-based policy making",
                    "Multiple competing priorities in agricultural sector",
                    "External pressure from international markets or donors"
                ],
                "mitigation_strategies": [
                    "Design business models resilient to policy changes",
                    "Engage in policy dialogue through youth associations",
                    "Diversify markets to reduce dependence on policy-sensitive channels",
                    "Monitor policy trends and develop scenario-based plans",
                    "Build relationships with policy implementers at local levels"
                ],
                "monitoring_indicators": [
                    "Policy tracking index",
                    "Business model adaptations to policy changes",
                    "Participation in policy dialogue forums"
                ]
            },
            {
                "risk_id": "PR-02",
                "risk_name": "Regulatory Compliance Challenges",
                "description": "Difficulty meeting food safety, quality, or business regulations",
                "likelihood": "Medium",
                "impact": "Medium",
                "risk_score": 4,
                "affected_interventions": ["Processing Businesses", "Storage Services", "Market Aggregation"],
                "root_causes": [
                    "Complex regulatory requirements",
                    "Limited awareness of applicable regulations",
                    "Costly compliance procedures",
                    "Weak regulatory enforcement creating uneven playing field"
                ],
                "mitigation_strategies": [
                    "Develop regulatory compliance guides for youth businesses",
                    "Create step-by-step formalization pathways with support",
                    "Facilitate group-based certification and compliance",
                    "Advocate for simplified procedures for small-scale enterprises",
                    "Provide training on quality and safety standards"
                ],
                "monitoring_indicators": [
                    "Compliance rate among youth businesses",
                    "Regulatory violations and penalties",
                    "Cost of compliance as percentage of revenue"
                ]
            },
            {
                "risk_id": "PR-03",
                "risk_name": "Land Tenure Insecurity",
                "description": "Uncertain land rights affecting investment in fixed post-harvest infrastructure",
                "likelihood": "Medium",
                "impact": "High",
                "risk_score": 6,
                "affected_interventions": ["Storage Facilities", "Processing Centers", "Permanent Structures"],
                "root_causes": [
                    "Informal land arrangements common in rural areas",
                    "Limited youth access to land ownership",
                    "Complex or costly land formalization processes",
                    "Competing land uses in peri-urban areas"
                ],
                "mitigation_strategies": [
                    "Develop mobile or temporary infrastructure options",
                    "Create community-based ownership models",
                    "Facilitate formal agreements with landowners or communities",
                    "Partner with local governments for land allocation",
                    "Implement modular designs that can be relocated if necessary"
                ],
                "monitoring_indicators": [
                    "Percentage of businesses with secure land tenure",
                    "Land-related disputes affecting operations",
                    "Investment levels in fixed versus mobile infrastructure"
                ]
            }
        ]
    }
}

# Convert to dataframe for analysis and export
risk_data = []
for category, category_data in risk_categories.items():
    for risk in category_data["risks"]:
        risk_dict = risk.copy()
        risk_dict["category"] = category
        risk_dict["mitigation_strategies"] = "; ".join(risk_dict["mitigation_strategies"])
        risk_dict["root_causes"] = "; ".join(risk_dict["root_causes"])
        risk_dict["monitoring_indicators"] = "; ".join(risk_dict["monitoring_indicators"])
        risk_dict["affected_interventions"] = "; ".join(risk_dict["affected_interventions"])
        risk_data.append(risk_dict)

risk_df = pd.DataFrame(risk_data)

# Export comprehensive risk register to CSV
risk_df.to_csv('results/interventions/risks/comprehensive_risk_register.csv', index=False)
print("Comprehensive risk register saved to CSV")

# Create a risk heat map based on likelihood and impact
# Convert likelihood and impact to numerical scores for visualization
likelihood_map = {"Low": 1, "Medium": 2, "High": 3}
impact_map = {"Low": 1, "Medium": 2, "High": 3}

risk_df["likelihood_score"] = risk_df["likelihood"].map(likelihood_map)
risk_df["impact_score"] = risk_df["impact"].map(impact_map)

# Create the heat map visualization
plt.figure(figsize=(12, 10))

# Create a scatter plot with risk IDs as markers
for idx, risk in risk_df.iterrows():
    plt.scatter(
        risk["impact_score"], 
        risk["likelihood_score"], 
        s=200, 
        alpha=0.7,
        c=plt.cm.YlOrRd(risk["risk_score"]/9)
    )
    plt.annotate(
        risk["risk_id"], 
        (risk["impact_score"], risk["likelihood_score"]),
        ha='center', va='center', fontsize=9, color='white',
        fontweight='bold'
    )

# Add risk names with lines connecting to points
for idx, risk in risk_df.iterrows():
    plt.annotate(
        risk["risk_name"],
        (risk["impact_score"], risk["likelihood_score"]),
        xytext=(10 if risk["impact_score"] < 2.5 else -10, 
                5 if risk["likelihood_score"] < 2.5 else -5),
        textcoords="offset points",
        ha='left' if risk["impact_score"] < 2.5 else 'right',
        va='center',
        fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color="gray")
    )

# Set up the grid for the risk matrix
plt.xlim(0.5, 3.5)
plt.ylim(0.5, 3.5)
plt.xticks([1, 2, 3], ['Low', 'Medium', 'High'])
plt.yticks([1, 2, 3], ['Low', 'Medium', 'High'])
plt.grid(True, alpha=0.3)

# Add risk zones
plt.axhspan(2.5, 3.5, xmin=2/3, xmax=1, color='red', alpha=0.2)  # High-High
plt.axhspan(2.5, 3.5, xmin=1/3, xmax=2/3, color='orange', alpha=0.2)  # High-Medium
plt.axhspan(1.5, 2.5, xmin=2/3, xmax=1, color='orange', alpha=0.2)  # Medium-High
plt.axhspan(0.5, 1.5, xmin=2/3, xmax=1, color='yellow', alpha=0.2)  # Low-High
plt.axhspan(2.5, 3.5, xmin=0, xmax=1/3, color='yellow', alpha=0.2)  # High-Low
plt.axhspan(1.5, 2.5, xmin=1/3, xmax=2/3, color='yellow', alpha=0.2)  # Medium-Medium
plt.axhspan(0.5, 1.5, xmin=1/3, xmax=2/3, color='green', alpha=0.2)  # Low-Medium
plt.axhspan(1.5, 2.5, xmin=0, xmax=1/3, color='green', alpha=0.2)  # Medium-Low
plt.axhspan(0.5, 1.5, xmin=0, xmax=1/3, color='green', alpha=0.2)  # Low-Low

# Add zone labels
plt.text(3, 3, 'Critical\nRisks', ha='center', va='center', fontsize=10, fontweight='bold')
plt.text(2, 2, 'Significant\nRisks', ha='center', va='center', fontsize=10, fontweight='bold')
plt.text(1, 1, 'Low\nRisks', ha='center', va='center', fontsize=10, fontweight='bold')

plt.xlabel('Impact', fontsize=12)
plt.ylabel('Likelihood', fontsize=12)
plt.title('Post-Harvest Intervention Risk Matrix', fontsize=14)

plt.tight_layout()
plt.savefig('results/interventions/risks/risk_heat_map.png', dpi=300, bbox_inches='tight')
plt.close()
print("Risk heat map visualization saved")

# Create a mitigation strategy effectiveness analysis
# We'll analyze key mitigation approaches across risk categories

# Count the number of times different mitigation approaches appear
mitigation_keywords = {
    "Participatory Design": ["participatory", "user input", "co-creation", "collaborative design"],
    "Capacity Building": ["training", "skills", "capacity", "knowledge"],
    "Technology Adaptation": ["adapt", "flexible", "modular", "resilient design"],
    "Financial Innovation": ["financing", "leasing", "pay-as-you", "credit", "loans"],
    "Market Linkages": ["market", "linkage", "buyer", "contract", "aggregation"],
    "Digital Solutions": ["digital", "mobile", "app", "online", "software"],
    "Partnership Models": ["partnership", "collaboration", "cooperative", "collective"],
    "Diversification": ["diversif", "multiple crops", "variety", "portfolio"],
    "Policy Engagement": ["policy", "advocacy", "regulatory", "compliance"],
    "Resource Efficiency": ["efficient", "conservation", "renewable", "sustainable"]
}

# Function to count keyword occurrences
def count_keyword_occurrences(text, keywords):
    text = text.lower()
    count = 0
    for keyword in keywords:
        if keyword.lower() in text:
            count += 1
    return min(count, 1)  # Count only presence, not multiple occurrences

# Analyze mitigation strategies
mitigation_by_category = {}
for category, category_data in risk_categories.items():
    mitigation_by_category[category] = {approach: 0 for approach in mitigation_keywords}
    for risk in category_data["risks"]:
        mitigation_text = " ".join(risk["mitigation_strategies"])
        for approach, keywords in mitigation_keywords.items():
            if any(keyword.lower() in mitigation_text.lower() for keyword in keywords):
                mitigation_by_category[category][approach] += 1

# Convert to DataFrame for visualization
mitigation_df = pd.DataFrame(mitigation_by_category)

# Create a heatmap of mitigation approaches by risk category
plt.figure(figsize=(14, 10))
ax = plt.gca()
im = ax.imshow(mitigation_df.values, cmap='YlGnBu')

# Set ticks and labels
ax.set_xticks(np.arange(len(mitigation_df.columns)))
ax.set_yticks(np.arange(len(mitigation_df.index)))
ax.set_xticklabels(mitigation_df.columns)
ax.set_yticklabels(mitigation_df.index)

# Rotate the x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add value annotations
for i in range(len(mitigation_df.index)):
    for j in range(len(mitigation_df.columns)):
        text = ax.text(j, i, mitigation_df.iloc[i, j],
                      ha="center", va="center", color="black" if mitigation_df.iloc[i, j] < 2 else "white")

plt.colorbar(im)
plt.title('Mitigation Strategy Approaches by Risk Category', fontsize=14)
plt.tight_layout()
plt.savefig('results/interventions/risks/mitigation_strategy_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("Mitigation strategy heatmap saved")

# Create a risk mitigation planning tool template in JSON format
risk_mitigation_template = {
    "business_model": "",
    "location": "",
    "risk_assessment": {
        "instructions": "Rate each risk from 1 (low) to 5 (high) for both likelihood and impact in your specific context",
        "implementation_risks": [
            {"risk": "Technology Adoption Resistance", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Infrastructure Limitations", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Technical Skills Gap", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ],
        "financial_risks": [
            {"risk": "Limited Access to Startup Capital", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Irregular Cash Flow", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Rising Operating Costs", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ],
        "market_risks": [
            {"risk": "Price Volatility", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Limited Market Access", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Competition from Established Players", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ],
        "environmental_risks": [
            {"risk": "Extreme Weather Events", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Pest and Disease Outbreaks", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Resource Constraints", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ],
        "social_risks": [
            {"risk": "Gender Barriers", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Youth Migration", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Collective Action Challenges", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ],
        "policy_risks": [
            {"risk": "Policy Inconsistency", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Regulatory Compliance Challenges", "likelihood": 0, "impact": 0, "mitigation_plan": ""},
            {"risk": "Land Tenure Insecurity", "likelihood": 0, "impact": 0, "mitigation_plan": ""}
        ]
    },
    "risk_monitoring_plan": {
        "monitoring_frequency": "",
        "key_indicators_to_track": [],
        "trigger_points_for_action": [],
        "responsible_person": ""
    },
    "contingency_planning": {
        "emergency_response_procedures": "",
        "backup_systems_and_processes": "",
        "alternative_business_strategies": ""
    }
}

# Save the template
with open('results/interventions/risks/risk_mitigation_planning_template.json', 'w') as f:
    json.dump(risk_mitigation_template, f, indent=4)
print("Risk mitigation planning template created")

# Create a guide document for using the risk mitigation framework
risk_management_guide = {
    "title": "Risk Management Guide for Youth Agripreneurs in Post-Harvest Businesses",
    "sections": [
        {
            "section_name": "Introduction to Risk Management",
            "content": """
            Risk management is a critical skill for successful agripreneurs. This guide will help you identify, 
            assess, and mitigate risks specific to post-harvest businesses in Nigeria. By systematically addressing 
            potential challenges before they occur, you can increase your business resilience and improve your 
            chances of success.
            """
        },
        {
            "section_name": "Step 1: Risk Identification",
            "content": """
            Begin by reviewing the comprehensive risk register provided in this toolkit. Consider which risks are most 
            relevant to your specific:
            
            1. Business model (e.g., mobile threshing service, storage facility)
            2. Location (region, state, rural vs. urban)
            3. Crop focus (maize, rice, vegetables, etc.)
            4. Customer segments (smallholders, medium-scale farmers, other businesses)
            
            Add any additional risks specific to your context that may not be covered in the general register.
            """
        },
        {
            "section_name": "Step 2: Risk Assessment",
            "content": """
            For each identified risk:
            
            1. Rate the likelihood of occurrence (Low, Medium, High)
            2. Rate the potential impact on your business (Low, Medium, High)
            3. Calculate a risk score by multiplying likelihood and impact ratings
            4. Prioritize risks with the highest scores for immediate attention
            
            Use the risk assessment template provided in the toolkit to document your analysis.
            """
        },
        {
            "section_name": "Step 3: Mitigation Strategy Development",
            "content": """
            For each high-priority risk:
            
            1. Review the suggested mitigation strategies in the risk register
            2. Adapt these strategies to your specific context
            3. Consider the cost and feasibility of implementing each strategy
            4. Develop an action plan with clear responsibilities and timelines
            
            Remember that some mitigation strategies can address multiple risks simultaneously.
            """
        },
        {
            "section_name": "Step 4: Implementation",
            "content": """
            Put your risk mitigation plan into action:
            
            1. Integrate risk management activities into your regular business operations
            2. Allocate necessary resources (time, money, personnel) to mitigation measures
            3. Communicate risks and mitigation strategies to relevant stakeholders
            4. Document your risk management processes for future reference
            """
        },
        {
            "section_name": "Step 5: Monitoring and Review",
            "content": """
            Risk management is an ongoing process:
            
            1. Regularly review your risk register (quarterly is recommended)
            2. Monitor the effectiveness of your mitigation strategies
            3. Update your risk assessment based on changing circumstances
            4. Learn from any risk events that occur and refine your approach
            
            Use the monitoring template provided to track key risk indicators.
            """
        },
        {
            "section_name": "Example: Mobile Rice Threshing Service",
            "content": """
            Risk Scenario: A youth entrepreneur operating a mobile rice threshing service identified 
            "Irregular Cash Flow" as a high-priority risk due to the seasonal nature of rice harvesting.
            
            Mitigation Strategy: 
            1. Mapped multiple rice-growing areas with different harvest schedules to extend the service period
            2. Added maize shelling services to diversify income (complementary service during rice off-season)
            3. Established a reserve fund by saving 15% of peak season revenues
            4. Developed maintenance services for agricultural equipment as an off-season revenue stream
            5. Created a booking system allowing farmers to pre-pay for services with discounts
            
            Result: Extended revenue-generating period from 4 months to 10 months per year, reducing cash flow volatility.
            """
        }
    ],
    "additional_resources": [
        {
            "name": "Risk Register Template",
            "file_location": "results/interventions/risks/comprehensive_risk_register.csv",
            "description": "Comprehensive list of potential risks with suggested mitigation strategies"
        },
        {
            "name": "Risk Mitigation Planning Template",
            "file_location": "results/interventions/risks/risk_mitigation_planning_template.json",
            "description": "Template for documenting your risk assessment and mitigation plans"
        },
        {
            "name": "Risk Heat Map",
            "file_location": "results/interventions/risks/risk_heat_map.png",
            "description": "Visual representation of risks by likelihood and impact"
        }
    ]
}

# Save the guide document
with open('results/interventions/risks/risk_management_guide.json', 'w') as f:
    json.dump(risk_management_guide, f, indent=4)
print("Risk management guide created")

# Create a summary of the risk analysis for executive documentation
risk_analysis_summary = {
    "title": "Risk Analysis Summary for Post-Harvest Loss Interventions",
    "key_findings": [
        "Most critical risks facing youth post-harvest businesses include technology adoption resistance, limited access to capital, and price volatility",
        "Financial risks represent the highest barrier to youth entrepreneurship in the post-harvest sector",
        "Diversification (crop types, services, markets) is the most effective cross-cutting risk mitigation strategy",
        "Digital solutions offer significant risk reduction potential, particularly for market and information-related risks",
        "Collective action and partnership models effectively reduce individual exposure to capital-intensive risks"
    ],
    "risk_category_insights": {
        "Implementation Risks": "Technical skills gaps and infrastructure limitations require integrated capacity building approaches",
        "Financial Risks": "Innovative financing models and phased investment approaches can overcome capital constraints",
        "Market Risks": "Digital market linkages and quality differentiation strategies offer protection against volatility",
        "Environmental Risks": "Climate-resilient designs and early warning systems are increasingly essential",
        "Social Risks": "Gender-sensitive approaches and youth engagement strategies address key social barriers",
        "Policy Risks": "Diversified market channels reduce exposure to policy inconsistency"
    },
    "recommendations": [
        "Integrate risk assessment into business model development from the earliest stages",
        "Design youth business models with phased investment requirements to manage financial risks",
        "Build climate resilience features into all post-harvest technologies and practices",
        "Develop youth peer support networks to share risk management knowledge and resources",
        "Create bundled service offerings to diversify revenue streams and reduce seasonal variability"
    ]
}

# Save the summary document
with open('results/interventions/risks/risk_analysis_summary.json', 'w') as f:
    json.dump(risk_analysis_summary, f, indent=4)
print("Risk analysis summary created")

print("\nRisk analysis and mitigation component completed successfully!")