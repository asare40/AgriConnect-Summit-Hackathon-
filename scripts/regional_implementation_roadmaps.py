import os
import json
import pandas as pd
from datetime import datetime

# Ensure directories exist
os.makedirs('results/interventions/regional', exist_ok=True)

# Define the regional implementation roadmaps
regional_roadmaps = [
    {
        "region": "North West",
        "states": ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "Zamfara"],
        "priority_level": "Very High",
        "key_crops": ["Maize", "Rice", "Sorghum", "Millet"],
        "regional_context": """
        The North West zone is Nigeria's largest grain production region, contributing approximately 
        40-45% of total grain output. The region is characterized by large production volumes but also 
        faces significant post-harvest challenges. High levels of informal aggregation create quality 
        inconsistencies, while limited modern storage and processing infrastructure contribute to 
        losses of 25-35% across key crops. 
        
        Key contextual factors include:
        - Sizable marketable surpluses produced by smallholder and medium-scale farmers
        - Strong grain trading networks with established market channels
        - Hot, dry climate favorable for grain storage but requiring proper moisture management
        - Significant aflatoxin challenges, especially in maize
        - Variable road infrastructure affecting transportation efficiency
        """,
        "estimated_annual_losses": {
            "volume_tons": "1,250,000 - 1,450,000 tons",
            "financial_value": "₦4.2 - ₦4.8 billion",
            "percentage_of_production": "28-32%"
        },
        "priority_value_chain_stages": [
            {
                "stage": "Storage",
                "loss_percentage": "35% of total losses",
                "key_issues": "Insect infestations, inadequate moisture management, aflatoxin contamination",
                "intervention_priority": "Very High"
            },
            {
                "stage": "Processing",
                "loss_percentage": "30% of total losses",
                "key_issues": "Inefficient threshing and milling, poor equipment maintenance, power challenges",
                "intervention_priority": "High"
            },
            {
                "stage": "Transportation",
                "loss_percentage": "20% of total losses",
                "key_issues": "Inadequate packaging, spillage, delays at checkpoints",
                "intervention_priority": "Medium"
            },
            {
                "stage": "Harvesting",
                "loss_percentage": "10% of total losses",
                "key_issues": "Timing issues, mechanical damage, labor shortages",
                "intervention_priority": "Medium"
            },
            {
                "stage": "Market",
                "loss_percentage": "5% of total losses",
                "key_issues": "Poor display conditions, excessive handling",
                "intervention_priority": "Low"
            }
        ],
        "priority_business_models": [
            {
                "model_id": "BM-02",
                "model_name": "Aggregation & Quality Control Hub",
                "rationale": """
                The high production volumes and existing strong trade networks make quality-focused 
                aggregation hubs particularly valuable in this region. These hubs can address quality 
                inconsistency challenges while creating significant value through improved market access 
                and price premiums for quality products.
                """,
                "target_locations": "Major grain markets in Kano, Kaduna, and Katsina; production cluster areas",
                "scale": "Medium to large operations (300+ tons monthly capacity)",
                "adaptation_requirements": "Strong focus on aflatoxin testing and management; integration with existing trade networks"
            },
            {
                "model_id": "BM-01",
                "model_name": "Mobile Threshing/Shelling Service",
                "rationale": """
                With large production volumes and significant mechanization gaps, mobile threshing services 
                can dramatically reduce losses while saving farmers time and labor costs. The large farmer 
                base ensures sufficient service demand throughout the season.
                """,
                "target_locations": "Production clusters across all states, with priority in Kano, Kaduna, and Zamfara",
                "scale": "Multiple service units per location to meet high demand",
                "adaptation_requirements": "Robust equipment suitable for high-volume operations; efficient scheduling systems"
            },
            {
                "model_id": "BM-05",
                "model_name": "Storage Facility Management",
                "rationale": """
                The region's position as a major grain supplier to southern Nigeria and neighboring countries 
                creates opportunities for storage businesses that can maintain quality while capitalizing on 
                seasonal price variations. Proper storage is also critical for addressing the region's aflatoxin challenges.
                """,
                "target_locations": "Strategic points along major trade routes, community centers in high production areas",
                "scale": "Medium to large facilities (50-200 ton capacity)",
                "adaptation_requirements": "Strong focus on moisture and temperature control; integration with warehouse receipt systems"
            }
        ],
        "implementation_approach": {
            "implementation_sequence": [
                {
                    "phase": "Phase 1: Foundation Building (Months 1-6)",
                    "activities": [
                        "Establish regional coordination center in Kano with satellite offices in Kaduna and Sokoto",
                        "Conduct detailed mapping of production clusters and existing service providers",
                        "Identify and engage with key aggregators, processors, and market actors",
                        "Develop training curriculum tailored to regional dynamics",
                        "Initialize awareness campaigns focusing on quality standards and aflatoxin risks"
                    ],
                    "expected_outcomes": "Regional infrastructure established, baseline data collected, stakeholders engaged"
                },
                {
                    "phase": "Phase 2: Initial Implementation (Months 7-18)",
                    "activities": [
                        "Launch first wave of youth-led businesses (40-50 entrepreneurs) focusing on mobile threshing",
                        "Establish 5-8 aggregation hubs in strategic locations",
                        "Implement quality standards and testing protocols across all interventions",
                        "Develop linkages with financial institutions for youth business financing",
                        "Create mentor networks connecting experienced aggregators with youth entrepreneurs"
                    ],
                    "expected_outcomes": "Initial business operations established, quality standards implemented, financing channels opened"
                },
                {
                    "phase": "Phase 3: Scaling and Integration (Months 19-36)",
                    "activities": [
                        "Scale to 150-200 youth-led businesses across all priority models",
                        "Integrate operations vertically (linking threshing services with aggregation hubs)",
                        "Establish quality certification systems recognized by major buyers",
                        "Develop digital platforms for service coordination and market information",
                        "Engage with policy stakeholders on quality standards enforcement"
                    ],
                    "expected_outcomes": "Comprehensive service network established, measurable reduction in PHL, improved market access"
                }
            ],
            "stakeholder_engagement": {
                "critical_stakeholders": [
                    "State Agricultural Development Programs (ADPs)",
                    "Grain Traders Associations",
                    "Equipment suppliers and maintenance providers",
                    "Financial institutions with agricultural portfolios",
                    "Major processors and institutional buyers"
                ],
                "engagement_strategy": """
                Create a multi-stakeholder platform co-chaired by respected grain traders and agricultural 
                officials. Hold quarterly coordination meetings, establish working groups for specific 
                technical areas (quality standards, financing, etc.), and develop formal partnerships for 
                youth business support. Leverage existing trader networks for market linkages.
                """
            },
            "risk_management": {
                "key_risks": [
                    "Seasonal price volatility affecting business viability",
                    "Security challenges in some areas",
                    "Resistance from established aggregation networks",
                    "Variable production due to climate factors"
                ],
                "mitigation_strategies": """
                Develop diversified business models that can adapt to seasonal variations; create 
                security protocols for business operations; emphasize value addition for existing 
                aggregators rather than competition; implement climate information services for 
                adapting to production variability.
                """
            }
        },
        "resource_requirements": {
            "physical_infrastructure": [
                "Regional coordination office with training facilities",
                "Demonstration sites for technologies in each state",
                "Quality testing laboratories in major aggregation points"
            ],
            "human_resources": [
                "Regional Program Manager and team (5-7 staff)",
                "Technical specialists in grain quality, storage, and processing",
                "Business development advisors for youth entrepreneurs",
                "State-level coordinators (one per state)"
            ],
            "financial_resources": {
                "administrative_costs": "₦85-120 million annually",
                "training_and_capacity_building": "₦150-200 million annually",
                "business_startup_support": "₦500-750 million (revolving fund)",
                "infrastructure_and_equipment": "₦300-450 million",
                "total_estimated_budget": "₦1.035-1.52 billion over 3 years"
            }
        },
        "monitoring_framework": {
            "key_performance_indicators": [
                "Number of youth-led businesses established and operational",
                "Volume of crops processed through improved channels",
                "Percentage reduction in post-harvest losses",
                "Increased income for participating farmers and entrepreneurs",
                "Quality improvements in targeted crops (particularly aflatoxin reduction)",
                "Number of jobs created through youth businesses"
            ],
            "measurement_methodology": """
            Establish baseline measurements in target clusters before intervention; implement quarterly 
            monitoring using sampling and surveys; conduct annual comprehensive impact assessment; 
            use digital tools for ongoing data collection from supported businesses.
            """,
            "learning_agenda": [
                "Comparative effectiveness of different business models in the North West context",
                "Impact of quality improvements on market access and pricing",
                "Effectiveness of youth-led versus traditional service provision",
                "Scalability factors for different intervention types"
            ]
        },
        "sustainability_strategy": {
            "business_viability": """
            Focus on developing robust business models with clear value propositions and revenue 
            streams from the start. Transition from subsidized services to fully commercial operations 
            by the end of Year 2. Foster competitive service quality and differentiation rather than 
            price competition among youth entrepreneurs.
            """,
            "institutional_arrangements": """
            Establish a transition plan for program oversight, with increasing leadership from local 
            business associations and state entities. Develop formal linkages between youth businesses 
            and established market actors through contracting and partnership arrangements.
            """,
            "policy_engagement": """
            Work with state governments to develop supportive policies for youth agripreneurs in the 
            post-harvest sector. Advocate for quality standards enforcement and incentives for loss 
            reduction practices. Support development of business environment improvements specific to 
            youth-led agricultural enterprises.
            """
        }
    },
    {
        "region": "North East",
        "states": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
        "priority_level": "High",
        "key_crops": ["Maize", "Sorghum", "Millet", "Rice"],
        "regional_context": """
        The North East region faces unique challenges due to ongoing security concerns in parts of 
        the region, which have disrupted agricultural production and market systems. Nevertheless, 
        the region has significant agricultural potential and produces substantial volumes of grains 
        and legumes. Post-harvest losses in the region are among the highest in Nigeria, estimated 
        at 30-45% depending on the crop and locale.
        
        Key contextual factors include:
        - Security challenges affecting movement of goods and market access
        - Fragmented production with limited aggregation infrastructure
        - Significant displacement of farming communities in some areas
        - Limited extension services and technical support
        - Challenging transportation infrastructure
        - Emerging recovery and reconstruction efforts creating new opportunities
        """,
        "estimated_annual_losses": {
            "volume_tons": "850,000 - 1,000,000 tons",
            "financial_value": "₦2.8 - ₦3.3 billion",
            "percentage_of_production": "30-45%"
        },
        "priority_value_chain_stages": [
            {
                "stage": "Processing",
                "loss_percentage": "40% of total losses",
                "key_issues": "Limited access to processing equipment, inefficient manual methods, power challenges",
                "intervention_priority": "Very High"
            },
            {
                "stage": "Storage",
                "loss_percentage": "30% of total losses",
                "key_issues": "Inadequate storage facilities, pest infestations, moisture management",
                "intervention_priority": "High"
            },
            {
                "stage": "Transportation",
                "loss_percentage": "15% of total losses",
                "key_issues": "Poor packaging, long distances to markets, security concerns",
                "intervention_priority": "Medium"
            },
            {
                "stage": "Harvesting",
                "loss_percentage": "10% of total losses",
                "key_issues": "Labor shortages, timing constraints, inadequate equipment",
                "intervention_priority": "Medium"
            },
            {
                "stage": "Market",
                "loss_percentage": "5% of total losses",
                "key_issues": "Limited market information, poor display conditions",
                "intervention_priority": "Low"
            }
        ],
        "priority_business_models": [
            {
                "model_id": "BM-01",
                "model_name": "Mobile Threshing/Shelling Service",
                "rationale": """
                The acute shortage of processing equipment and high reliance on manual methods in 
                the region creates an immediate opportunity for mobile processing services. These 
                services can significantly reduce losses during the critical post-harvest phase 
                while creating youth employment in a region with high youth unemployment.
                """,
                "target_locations": "Stable areas with high production in Adamawa, Bauchi, Gombe, and Taraba",
                "scale": "Small to medium operations with potential for expansion",
                "adaptation_requirements": "Security considerations in movement planning; robust, low-maintenance equipment"
            },
            {
                "model_id": "BM-03",
                "model_name": "Solar Drying as a Service",
                "rationale": """
                The North East's high solar radiation potential combined with significant drying 
                challenges makes solar drying services particularly viable. These services can help 
                address moisture-related quality issues while utilizing renewable energy in a region 
                with limited energy infrastructure.
                """,
                "target_locations": "All states, with focus on areas with vegetable and fruit production",
                "scale": "Small-scale operations with modular expansion potential",
                "adaptation_requirements": "Mobile designs for flexibility; integration with local drying practices"
            },
            {
                "model_id": "BM-07",
                "model_name": "Digital Market Linkage Platform",
                "rationale": """
                Market disruptions and security challenges make digital market linkages particularly 
                valuable in the North East. Such platforms can help reconnect broken market systems 
                and reduce the need for physical movement of people in insecure areas while providing 
                critical market information.
                """,
                "target_locations": "Regional coverage with hubs in major urban centers",
                "scale": "Start with key commodities and expand progressively",
                "adaptation_requirements": "Offline functionality options; simple user interfaces; voice capabilities for low literacy users"
            }
        ],
        "implementation_approach": {
            "implementation_sequence": [
                {
                    "phase": "Phase 1: Security Assessment and Safe Zone Mapping (Months 1-3)",
                    "activities": [
                        "Conduct detailed security assessment in collaboration with local authorities",
                        "Map 'safe zones' for initial implementation in each state",
                        "Identify secure transportation routes and market access points",
                        "Establish security protocols for all program activities",
                        "Develop contingency plans for various security scenarios"
                    ],
                    "expected_outcomes": "Security framework established, implementation zones identified, risk management protocols developed"
                },
                {
                    "phase": "Phase 2: Initial Implementation in Secure Zones (Months 4-12)",
                    "activities": [
                        "Establish coordination centers in Bauchi and Adamawa",
                        "Launch mobile processing services in high-production secure areas",
                        "Develop prototype digital market linkage platform",
                        "Train initial cohort of 30-40 youth entrepreneurs",
                        "Implement solar drying demonstrations in 15-20 communities"
                    ],
                    "expected_outcomes": "Core services established in secure areas, initial results demonstrated, youth engagement initiated"
                },
                {
                    "phase": "Phase 3: Adaptive Expansion (Months 13-24)",
                    "activities": [
                        "Scale services based on security situation and success of initial implementation",
                        "Expand to additional secure areas as they become available",
                        "Refine business models based on early implementation experiences",
                        "Strengthen market linkages between production areas and regional markets",
                        "Integrate with recovery and reconstruction efforts where possible"
                    ],
                    "expected_outcomes": "Expanded service coverage, improved business models, stronger market linkages"
                },
                {
                    "phase": "Phase 4: Consolidation and Resilience Building (Months 25-36)",
                    "activities": [
                        "Establish youth business networks for mutual support and security",
                        "Develop long-term financing mechanisms for sustainable operations",
                        "Integrate post-harvest interventions with broader agricultural recovery",
                        "Create formal market linkages with buyers in more secure regions",
                        "Implement comprehensive quality management systems"
                    ],
                    "expected_outcomes": "Sustainable business networks established, resilient market linkages created, reduced dependency on external support"
                }
            ],
            "stakeholder_engagement": {
                "critical_stakeholders": [
                    "State security and administrative authorities",
                    "Humanitarian and development organizations active in the region",
                    "Religious and community leaders",
                    "Mobile network operators and technology providers",
                    "Financial institutions with presence in the region"
                ],
                "engagement_strategy": """
                Create a comprehensive stakeholder engagement platform with strong emphasis on security 
                collaboration. Involve security stakeholders in planning from the outset. Leverage existing 
                humanitarian networks for initial entry points. Work through trusted community leaders for 
                local acceptance and participation. Establish clear communication protocols for rapid 
                response to changing conditions.
                """
            },
            "risk_management": {
                "key_risks": [
                    "Deteriorating security situation disrupting implementation",
                    "Limited access to certain areas due to insecurity",
                    "Theft or damage to equipment in insecure environments",
                    "Displacement of participating communities",
                    "Market disruptions affecting business viability"
                ],
                "mitigation_strategies": """
                Implement tiered risk management approach with different modalities for different security 
                levels. Prioritize mobile assets over fixed infrastructure in less secure areas. Develop 
                community-based security arrangements for equipment protection. Create flexible implementation 
                plans that can adapt to population movements. Design business models that can function in 
                fragmented market conditions.
                """
            }
        },
        "resource_requirements": {
            "physical_infrastructure": [
                "Secure coordination centers in Bauchi and Adamawa",
                "Mobile training units that can deploy to different communities",
                "Solar-powered business hubs in key market towns"
            ],
            "human_resources": [
                "Regional Program Manager with security management experience",
                "Security Liaison Officers for each state",
                "Technical specialists in post-harvest technologies",
                "Community engagement facilitators with local knowledge",
                "Digital platform developers with experience in challenging environments"
            ],
            "financial_resources": {
                "administrative_costs": "₦100-140 million annually",
                "training_and_capacity_building": "₦120-180 million annually",
                "business_startup_support": "₦400-600 million (revolving fund)",
                "security_management": "₦80-120 million annually",
                "digital_platform_development": "₦100-150 million",
                "total_estimated_budget": "₦1.1-1.7 billion over 3 years"
            }
        },
        "monitoring_framework": {
            "key_performance_indicators": [
                "Number of youth-led businesses established in secure zones",
                "Volume of crops processed through improved methods",
                "Number of farmers accessing market information through digital platforms",
                "Percentage reduction in post-harvest losses in target areas",
                "Income improvement for participating youth entrepreneurs",
                "Number of communities with improved post-harvest services"
            ],
            "measurement_methodology": """
            Implement adaptive monitoring approach suitable for challenging environments; use mobile 
            data collection tools; conduct regular security assessments to adjust monitoring activities; 
            utilize remote sensing where possible; engage local enumerators for continuous data collection.
            """,
            "learning_agenda": [
                "Adaptation of post-harvest business models to insecure environments",
                "Effectiveness of digital tools in reconnecting fragmented markets",
                "Resilience factors for youth businesses in challenging contexts",
                "Integration of post-harvest interventions with humanitarian programming"
            ]
        },
        "sustainability_strategy": {
            "business_viability": """
            Focus on business models with lower capital requirements and higher mobility in less 
            secure areas. Develop phased investment approaches that limit initial exposure. Create 
            business clusters where entrepreneurs can support each other and share resources. 
            Emphasize services with immediate tangible benefits to ensure customer willingness to pay.
            """,
            "institutional_arrangements": """
            Work through existing community structures respected by all groups. Avoid creating 
            parallel systems that might become targets in conflict. Build capacity of local business 
            associations that can continue coordination when external support ends. Focus on practical 
            skills transfer to ensure local repair and maintenance capability.
            """,
            "policy_engagement": """
            Engage with both formal government structures and local governance systems as appropriate. 
            Focus on practical policy improvements that can function even in weak governance contexts. 
            Support development of market governance systems that can operate independently of 
            formal government structures when necessary.
            """
        }
    },
    {
        "region": "South West",
        "states": ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"],
        "priority_level": "Medium-High",
        "key_crops": ["Maize", "Rice", "Cassava", "Vegetables", "Fruits"],
        "regional_context": """
        The South West region is characterized by diverse agricultural production systems and proximity 
        to major urban markets, particularly Lagos. The region has relatively better infrastructure and 
        market access compared to northern regions, but still faces significant post-harvest loss challenges, 
        particularly for perishable crops. The region's post-harvest losses are estimated at 25-40%, with 
        higher rates for fruits and vegetables.
        
        Key contextual factors include:
        - Proximity to major urban markets with high demand for quality products
        - Higher levels of agricultural commercialization and market orientation
        - More developed transportation infrastructure but significant traffic congestion
        - High humidity levels affecting storage and drying
        - Strong presence of small and medium food processing enterprises
        - More developed financial services sector and entrepreneurship ecosystem
        """,
        "estimated_annual_losses": {
            "volume_tons": "700,000 - 900,000 tons",
            "financial_value": "₦3.5 - ₦5.2 billion",
            "percentage_of_production": "25-40%"
        },
        "priority_value_chain_stages": [
            {
                "stage": "Storage",
                "loss_percentage": "30% of total losses",
                "key_issues": "High humidity, inadequate facilities, pest infestations, mold growth",
                "intervention_priority": "High"
            },
            {
                "stage": "Processing",
                "loss_percentage": "25% of total losses",
                "key_issues": "Inefficient processing equipment, bottlenecks in peak harvest periods",
                "intervention_priority": "High"
            },
            {
                "stage": "Transportation",
                "loss_percentage": "25% of total losses",
                "key_issues": "Traffic delays, inadequate packaging, poor handling",
                "intervention_priority": "High"
            },
            {
                "stage": "Market",
                "loss_percentage": "15% of total losses",
                "key_issues": "Oversupply in peak periods, inadequate display facilities",
                "intervention_priority": "Medium"
            },
            {
                "stage": "Harvesting",
                "loss_percentage": "5% of total losses",
                "key_issues": "Timing issues, inadequate labor during peak periods",
                "intervention_priority": "Low"
            }
        ],
        "priority_business_models": [
            {
                "model_id": "BM-04",
                "model_name": "Cold Chain Transport Microfranchise",
                "rationale": """
                The combination of significant perishable crop production and proximity to major urban 
                markets creates an ideal opportunity for cold chain transport services. The region's 
                better road infrastructure supports this model, while heavy traffic and transportation 
                delays make cold chain particularly valuable for preserving quality and extending shelf life.
                """,
                "target_locations": "Major production clusters with focus on routes connecting to Lagos, Ibadan, and other urban centers",
                "scale": "Small to medium operations with fleet expansion potential",
                "adaptation_requirements": "Traffic management strategies; integration with existing transport networks; focus on premium market segments"
            },
            {
                "model_id": "BM-03",
                "model_name": "Solar Drying as a Service",
                "rationale": """
                The region's high humidity levels create significant drying challenges for many crops. 
                Solar drying services can address these challenges while creating value-added products 
                for the region's developed markets. The focus on fruits and vegetables adds particular 
                value in a region with significant horticultural production.
                """,
                "target_locations": "Horticultural production zones in Oyo, Ogun, and Ondo",
                "scale": "Medium-sized operations with quality focus",
                "adaptation_requirements": "Humidity management designs; focus on premium dried products for urban markets; quality certification systems"
            },
            {
                "model_id": "BM-07",
                "model_name": "Digital Market Linkage Platform",
                "rationale": """
                The South West's higher technology adoption rates and better connectivity make digital 
                platforms particularly viable. These platforms can help address market information gaps 
                and connect producers more efficiently to the region's diverse markets, while helping to 
                balance supply and demand to reduce market-stage losses.
                """,
                "target_locations": "Regional coverage with emphasis on peri-urban production areas",
                "scale": "Comprehensive platform with multiple functionalities",
                "adaptation_requirements": "Integration with existing e-commerce platforms; payment system linkages; quality verification components"
            }
        ],
        "implementation_approach": {
            "implementation_sequence": [
                {
                    "phase": "Phase 1: Market Analysis and Business Model Refinement (Months 1-4)",
                    "activities": [
                        "Conduct detailed market analysis focusing on premium and niche opportunities",
                        "Map existing post-harvest service providers and market channels",
                        "Identify specific market gaps and unmet demand for quality products",
                        "Refine business models based on urban market requirements",
                        "Develop quality standards aligned with formal market expectations"
                    ],
                    "expected_outcomes": "Market-responsive business models, identified premium opportunities, mapped service gaps"
                },
                {
                    "phase": "Phase 2: Entrepreneurship Development and Pilot Implementation (Months 5-12)",
                    "activities": [
                        "Establish entrepreneurship hub in Ibadan with satellite locations",
                        "Launch business plan competition for youth entrepreneurs",
                        "Provide intensive entrepreneurship and technical training",
                        "Support first cohort of 30-40 businesses with seed funding and mentoring",
                        "Establish quality management systems and market linkages"
                    ],
                    "expected_outcomes": "Core group of youth businesses established, quality standards implemented, initial market linkages created"
                },
                {
                    "phase": "Phase 3: Market Expansion and Access to Finance (Months 13-24)",
                    "activities": [
                        "Develop relationships with premium buyers and formal markets",
                        "Create linkages with financial institutions for growth financing",
                        "Expand to additional 60-80 youth-led businesses",
                        "Establish business networks for shared resources and market access",
                        "Implement digital platform connecting producers, service providers, and markets"
                    ],
                    "expected_outcomes": "Expanded market access, increased financing options, growing business network"
                },
                {
                    "phase": "Phase 4: Scaling and Ecosystem Development (Months 25-36)",
                    "activities": [
                        "Scale to 150-200 youth-led businesses across all models",
                        "Develop industry association for post-harvest service providers",
                        "Create certification standards for quality services",
                        "Engage with policy makers on enabling environment improvements",
                        "Establish linkages with technical schools and universities for talent pipeline"
                    ],
                    "expected_outcomes": "Sustainable post-harvest services ecosystem, recognized quality standards, enabling policy environment"
                }
            ],
            "stakeholder_engagement": {
                "critical_stakeholders": [
                    "Formal market actors (supermarkets, processors, exporters)",
                    "Financial institutions and investors",
                    "Technology providers and innovation hubs",
                    "State ministries of agriculture and commerce",
                    "Agricultural universities and research institutions"
                ],
                "engagement_strategy": """
                Create a market-driven stakeholder platform with strong private sector leadership. 
                Engage formal market actors in defining quality requirements and standards. Partner 
                with technology hubs and innovation centers for digital solutions. Develop working 
                groups focused on specific value chains and technologies. Create showcase events to 
                demonstrate business models and technologies to potential investors and partners.
                """
            },
            "risk_management": {
                "key_risks": [
                    "Market saturation in certain service categories",
                    "Competition from established service providers",
                    "High youth expectations for quick returns",
                    "Quality consistency challenges affecting market relationships",
                    "Traffic and logistics challenges in urban areas"
                ],
                "mitigation_strategies": """
                Emphasize market differentiation and quality positioning; focus on underserved segments 
                and premium opportunities; provide realistic business planning tools with appropriate 
                timeline expectations; implement strong quality management systems from the outset; 
                develop efficient logistics strategies accounting for urban challenges.
                """
            }
        },
        "resource_requirements": {
            "physical_infrastructure": [
                "Entrepreneurship and innovation hub in Ibadan",
                "Satellite business development centers in other states",
                "Demonstration facilities for cold chain and processing technologies"
            ],
            "human_resources": [
                "Program Director with private sector background",
                "Business development specialists with entrepreneurship experience",
                "Market linkage facilitators with industry connections",
                "Technology specialists for digital platform development",
                "Quality management advisors for premium market access"
            ],
            "financial_resources": {
                "administrative_costs": "₦90-120 million annually",
                "training_and_business_development": "₦150-200 million annually",
                "business_startup_grants_and_loans": "₦400-600 million",
                "technology_platform_development": "₦120-180 million",
                "market_linkage_facilitation": "₦80-120 million",
                "total_estimated_budget": "₦840-1.22 billion over 3 years"
            }
        },
        "monitoring_framework": {
            "key_performance_indicators": [
                "Number of youth-led businesses established and operational after one year",
                "Revenue generation and profitability of supported businesses",
                "Volume and value of produce handled through improved channels",
                "Market price premiums achieved through quality improvements",
                "Percentage reduction in post-harvest losses for participating producers",
                "Access to financing for business growth and expansion"
            ],
            "measurement_methodology": """
            Implement business performance tracking system with regular data collection; conduct 
            market price monitoring for key commodities; utilize mobile data collection tools for 
            business metrics; conduct periodic producer surveys to assess impact; analyze market 
            price differentials for quality graded products.
            """,
            "learning_agenda": [
                "Success factors for youth agripreneurship in peri-urban contexts",
                "Effective approaches for accessing premium urban markets",
                "Balance between technological sophistication and practical business viability",
                "Strategies for competing and collaborating with established market actors"
            ]
        },
        "sustainability_strategy": {
            "business_viability": """
            Emphasize quality differentiation and premium market positioning rather than competing 
            on price alone. Focus on building strong brands and reputation for consistent service. 
            Develop multiple revenue streams within complementary business lines. Build strong 
            relationships with formal market actors who value quality and reliability.
            """,
            "institutional_arrangements": """
            Create industry association led by youth entrepreneurs themselves with minimal external 
            support after initial establishment. Develop relationships with business schools and 
            entrepreneurship programs for ongoing talent development. Foster mentor relationships 
            with established business leaders in related sectors.
            """,
            "policy_engagement": """
            Focus on specific policy barriers affecting post-harvest service businesses, such as 
            transport regulations, market access rules, and quality standards enforcement. Leverage 
            the more developed policy environment in the South West to advocate for model regulations 
            that could be replicated in other regions.
            """
        }
    }
]

# Save each regional roadmap as a separate JSON file
for roadmap in regional_roadmaps:
    region_name = roadmap["region"].replace(" ", "_").lower()
    filename = f"{region_name}_implementation_roadmap.json"
    
    with open(f'results/interventions/regional/{filename}', 'w') as f:
        json.dump(roadmap, f, indent=4)
    print(f"Saved implementation roadmap for {roadmap['region']}")

# Create a regional comparison and overview document
regional_comparison = {
    "title": "Regional Implementation Strategy Comparison",
    "overview": """
    This document provides a comparative analysis of post-harvest loss intervention strategies 
    across Nigeria's geopolitical zones. Each region has unique agricultural systems, post-harvest 
    challenges, and socioeconomic contexts that require tailored implementation approaches. This 
    comparison highlights key differences and similarities to inform national-level planning and 
    coordination.
    """,
    "summarized_data": {
        "estimated_losses": {
            "North West": {
                "volume": "1.25-1.45 million tons",
                "value": "₦4.2-4.8 billion",
                "percentage": "28-32%"
            },
            "North East": {
                "volume": "0.85-1.0 million tons",
                "value": "₦2.8-3.3 billion",
                "percentage": "30-45%"
            },
            "South West": {
                "volume": "0.7-0.9 million tons",
                "value": "₦3.5-5.2 billion",
                "percentage": "25-40%"
            },
            "North Central": {
                "volume": "0.9-1.1 million tons",
                "value": "₦3.0-3.8 billion",
                "percentage": "27-35%"
            },
            "South East": {
                "volume": "0.5-0.65 million tons",
                "value": "₦2.2-3.0 billion",
                "percentage": "30-38%"
            },
            "South South": {
                "volume": "0.4-0.55 million tons",
                "value": "₦2.0-2.8 billion",
                "percentage": "35-45%"
            }
        },
        "priority_business_models": {
            "North West": ["BM-02 (Aggregation Hub)", "BM-01 (Mobile Threshing)", "BM-05 (Storage Facility)"],
            "North East": ["BM-01 (Mobile Threshing)", "BM-03 (Solar Drying)", "BM-07 (Digital Platform)"],
            "South West": ["BM-04 (Cold Chain)", "BM-03 (Solar Drying)", "BM-07 (Digital Platform)"],
            "North Central": ["BM-02 (Aggregation Hub)", "BM-01 (Mobile Threshing)", "BM-06 (Quality Testing)"],
            "South East": ["BM-03 (Solar Drying)", "BM-04 (Cold Chain)", "BM-07 (Digital Platform)"],
            "South South": ["BM-04 (Cold Chain)", "BM-03 (Solar Drying)", "BM-02 (Aggregation Hub)"]
        },
        "implementation_timeframes": {
            "North West": "36 months (3 phases)",
            "North East": "36 months (4 phases)",
            "South West": "36 months (4 phases)",
            "North Central": "30 months (3 phases)",
            "South East": "30 months (3 phases)",
            "South South": "30 months (3 phases)"
        }
    },
    "key_regional_differences": [
        {
            "factor": "Security Considerations",
            "description": """
            Security concerns significantly impact implementation in the North East, requiring special 
            planning and risk management approaches. The North West also faces growing security challenges 
            in some areas. Southern regions generally have lower security risks but may face different 
            challenges related to community relations and land access.
            """
        },
        {
            "factor": "Infrastructure Quality",
            "description": """
            The South West and parts of South South have relatively better transportation and energy 
            infrastructure, enabling more sophisticated cold chain and processing operations. Northern 
            regions require more emphasis on technologies that can function with limited infrastructure, 
            such as solar-powered or mobile solutions.
            """
        },
        {
            "factor": "Market Structures",
            "description": """
            The North has more established grain aggregation networks but less developed formal market 
            channels. Southern regions, especially the South West, have more access to formal markets and 
            premium opportunities but may face higher competition and entry barriers. Digital solutions 
            have higher potential adoption in southern regions due to better connectivity.
            """
        },
        {
            "factor": "Crop Focus",
            "description": """
            Northern regions focus primarily on grains (maize, rice, sorghum, millet), while southern 
            regions have more diverse production including significant horticultural crops. This affects 
            the priority business models, with more emphasis on cold chain and processing in the south, 
            and more focus on threshing, drying, and storage in the north.
            """
        },
        {
            "factor": "Youth Entrepreneurship Ecosystem",
            "description": """
            The South West has a more developed entrepreneurship ecosystem with better access to 
            financial services, mentorship, and business development support. Northern regions require 
            more investment in foundational entrepreneurship capabilities and financial access. This 
            affects implementation approaches and timelines for business development.
            """
        }
    ],
    "common_success_factors": [
        "Strong stakeholder engagement and local ownership",
        "Quality focus throughout the value chain",
        "Phased implementation with clear progression pathways",
        "Integration of digital technologies appropriate to context",
        "Business model viability as primary sustainability strategy",
        "Youth leadership development and mentorship",
        "Access to appropriate financing mechanisms"
    ],
    "national_coordination_recommendations": [
        {
            "recommendation": "Establish National Knowledge Sharing Platform",
            "description": """
            Create a mechanism for regular exchange of experiences and learning across regional 
            implementation teams. Hold quarterly national coordination meetings, maintain a digital 
            knowledge repository, and facilitate cross-regional visits and exchanges.
            """
        },
        {
            "recommendation": "Standardize Core Training Curricula",
            "description": """
            Develop standardized training modules for technical and business skills that can be 
            adapted to regional contexts. This ensures quality consistency while allowing for 
            necessary regional customization based on specific needs and constraints.
            """
        },
        {
            "recommendation": "Coordinate Policy Engagement",
            "description": """
            Develop a coordinated national policy engagement strategy that leverages regional 
            experiences to advocate for supportive policies. Identify policy barriers common 
            across regions and develop unified approaches to addressing them.
            """
        },
        {
            "recommendation": "Centralize Technology Evaluation",
            "description": """
            Establish a national technology assessment and validation process to evaluate 
            post-harvest technologies before regional deployment. This prevents duplication of 
            effort and ensures technologies are appropriately matched to regional needs.
            """
        },
        {
            "recommendation": "Harmonize Monitoring and Evaluation",
            "description": """
            Implement a common set of core indicators and measurement methods across all regions 
            while allowing for region-specific additions. This enables national-level impact 
            assessment and meaningful comparison of intervention effectiveness across regions.
            """
        }
    ],
    "phased_national_implementation": [
        {
            "phase": "Phase 1: Priority Regions (Year 1)",
            "focus": ["North West", "South West", "North East"],
            "rationale": """
            Begin with regions representing different contexts: North West (highest production volume), 
            South West (market access and infrastructure advantages), and North East (highest need due 
            to current challenges). This provides diverse learning environments while addressing significant 
            portions of national post-harvest losses.
            """
        },
        {
            "phase": "Phase 2: Secondary Regions (Year 2)",
            "focus": ["North Central", "South East"],
            "rationale": """
            Expand to North Central (significant production with moderate challenges) and South East 
            (diverse agricultural systems with specific post-harvest needs). Implementation in these 
            regions can build on lessons from Phase 1 regions.
            """
        },
        {
            "phase": "Phase 3: Remaining Region and Integration (Year 3)",
            "focus": ["South South", "National Integration"],
            "rationale": """
            Complete geographic coverage by implementing in South South while focusing on integration 
            of regional efforts into a coherent national approach. Emphasis on scaling successful 
            models and addressing cross-regional challenges.
            """
        }
    ]
}

# Save the regional comparison document
with open('results/interventions/regional/regional_comparison_overview.json', 'w') as f:
    json.dump(regional_comparison, f, indent=4)
print("Saved regional comparison and overview document")

# Create an implementation guide for using the regional roadmaps
implementation_guide = {
    "title": "Using Regional Implementation Roadmaps: A Guide for Practitioners",
    "introduction": """
    This guide is designed to help practitioners effectively utilize the regional implementation 
    roadmaps for post-harvest loss reduction interventions. The roadmaps provide detailed, 
    context-specific guidance for establishing youth-led post-harvest businesses across Nigeria's 
    diverse geopolitical zones. This document explains how to adapt and apply these roadmaps in 
    practical implementation scenarios.
    """,
    "intended_users": [
        "Program managers and field staff of agricultural development projects",
        "Government officials in agricultural departments and agencies",
        "Financial institutions supporting youth entrepreneurship in agriculture",
        "Non-governmental organizations working in post-harvest loss reduction",
        "Youth organizations and entrepreneur support networks"
    ],
    "how_to_use_roadmaps": [
        {
            "step": "1. Context Assessment and Customization",
            "instructions": """
            Begin by assessing your specific implementation context against the regional descriptions 
            provided. Even within regions, there are significant local variations that may require 
            adjustments to the roadmap. Consider factors such as:
            
            - Local security situation and access constraints
            - Specific crops and production patterns in your target area
            - Existing service providers and market actors
            - Available infrastructure and resources
            - Local cultural and social dynamics affecting youth engagement
            
            Based on this assessment, customize the roadmap to your specific context while maintaining 
            the core strategic approach.
            """
        },
        {
            "step": "2. Stakeholder Mapping and Engagement",
            "instructions": """
            Use the stakeholder engagement sections as a starting point to identify critical actors 
            in your specific context. Expand the stakeholder map to include key local entities not 
            captured in the regional overview. For each stakeholder, consider:
            
            - Their specific interests and concerns related to post-harvest interventions
            - Their potential role in supporting or hindering implementation
            - Appropriate engagement approaches and timing
            - Potential for formal partnerships or collaboration
            
            Develop a detailed stakeholder engagement plan based on this mapping, with clear 
            responsibilities and timelines for engagement activities.
            """
        },
        {
            "step": "3. Business Model Selection and Adaptation",
            "instructions": """
            The priority business models identified for each region provide starting points, but 
            should be further refined based on local opportunities and constraints. Consider:
            
            - Which specific value chain stages have the highest losses in your target area
            - Local market demand and willingness to pay for different services
            - Youth interests and existing capabilities
            - Available resources for startup and operations
            
            Select and adapt business models that best match these considerations, potentially 
            combining elements from different models to create localized variations. Refer to the 
            detailed business implementation guides for specific operational guidance.
            """
        },
        {
            "step": "4. Implementation Planning",
            "instructions": """
            Use the phased implementation approach as a framework to develop your specific 
            implementation plan. For each phase:
            
            - Define specific activities with clear responsibilities
            - Establish realistic timeframes based on local conditions
            - Identify resources required for each activity
            - Develop measurable milestones and success indicators
            - Create contingency plans for potential challenges
            
            The implementation sequence should be adapted based on your program timeframe, available 
            resources, and specific priorities.
            """
        },
        {
            "step": "5. Resource Mobilization",
            "instructions": """
            The resource requirements sections provide estimates that should be adjusted based on 
            your scale of implementation and local costs. Develop a detailed resource mobilization 
            strategy that considers:
            
            - Available program resources and budget constraints
            - Potential for leveraging resources from other actors
            - Phased resource allocation aligned with implementation priorities
            - Cost-sharing opportunities with private sector or government partners
            - In-kind contributions that can reduce cash requirements
            
            Prioritize resources that enable youth business viability rather than program 
            administration where possible.
            """
        },
        {
            "step": "6. Monitoring and Learning",
            "instructions": """
            Adapt the monitoring framework to your specific implementation context while maintaining 
            alignment with the core indicators for national consistency. Consider:
            
            - Practical data collection methods suitable for your context
            - Baseline assessment needs before implementation
            - Balancing comprehensive monitoring with practical constraints
            - Participation of youth entrepreneurs in monitoring processes
            - Learning mechanisms to capture and apply insights during implementation
            
            Develop a practical monitoring plan with clear responsibilities and feedback loops to 
            inform ongoing implementation adjustments.
            """
        },
        {
            "step": "7. Risk Management",
            "instructions": """
            Use the identified risks as a starting point to develop a comprehensive risk management 
            plan for your specific context. For each risk:
            
            - Assess likelihood and potential impact in your specific context
            - Develop context-specific mitigation measures
            - Assign risk monitoring responsibilities
            - Establish triggers for implementing contingency measures
            - Create communication protocols for risk-related decisions
            
            Review and update risk assessments regularly throughout implementation.
            """
        }
    ],
    "roadmap_implementation_tips": [
        {
            "tip": "Start Small and Demonstrate Success",
            "description": """
            Begin with focused implementation in areas with high potential for success rather than 
            attempting broad coverage immediately. Use these initial successes to build momentum and 
            credibility for wider implementation.
            """
        },
        {
            "tip": "Build on Existing Structures",
            "description": """
            Identify and leverage existing organizations, networks, and programs rather than creating 
            entirely new structures. This reduces startup time and increases sustainability potential.
            """
        },
        {
            "tip": "Balance Standardization and Adaptation",
            "description": """
            Maintain core elements of the approach while allowing sufficient flexibility for local 
            adaptation. This balance ensures program coherence while respecting local realities.
            """
        },
        {
            "tip": "Emphasize Youth Leadership",
            "description": """
            Ensure youth have meaningful leadership roles throughout implementation, not just as 
            beneficiaries. This builds ownership and sustainability while fostering innovation.
            """
        },
        {
            "tip": "Integrate with Broader Development Efforts",
            "description": """
            Connect post-harvest interventions with other agricultural and youth development 
            initiatives in the area for synergy and efficiency. Avoid creating isolated interventions.
            """
        }
    ],
    "common_implementation_challenges": [
        {
            "challenge": "Limited Youth Interest in Post-Harvest Opportunities",
            "solutions": [
                "Showcase successful young entrepreneurs as role models",
                "Emphasize technology and innovation aspects that appeal to youth",
                "Create clear pathways from startup to growth and expansion",
                "Integrate with popular youth platforms and networks",
                "Use participatory approaches to business model development"
            ]
        },
        {
            "challenge": "Access to Appropriate Financing",
            "solutions": [
                "Develop relationships with financial institutions early in implementation",
                "Create phased investment approaches that limit initial capital requirements",
                "Establish guarantee funds to reduce lender risk",
                "Support youth in developing comprehensive business plans",
                "Explore alternative financing models such as equipment leasing"
            ]
        },
        {
            "challenge": "Coordination Among Multiple Stakeholders",
            "solutions": [
                "Establish clear governance structures with defined roles",
                "Create regular coordination mechanisms with tangible agendas",
                "Develop shared objectives that align with each stakeholder's interests",
                "Document agreements formally but maintain flexibility",
                "Focus on practical collaboration rather than complex structures"
            ]
        },
        {
            "challenge": "Sustainability Beyond Project Support",
            "solutions": [
                "Emphasize business viability from the outset rather than subsidized services",
                "Build local capacity for ongoing technical support and maintenance",
                "Develop peer support networks among youth entrepreneurs",
                "Create linkages with permanent institutions such as universities or business associations",
                "Progressively reduce external support based on clear milestones"
            ]
        }
    ],
    "additional_resources": [
        {
            "resource": "Business Implementation Guides",
            "location": "results/youth_opportunities/implementation_guides/",
            "description": "Detailed guidance on establishing specific post-harvest business models"
        },
        {
            "resource": "Risk Management Framework",
            "location": "results/interventions/risks/risk_management_guide.json",
            "description": "Framework for assessing and managing risks in post-harvest interventions"
        },
        {
            "resource": "PHL Dashboard",
            "location": "results/dashboard/interactive/youthharvest_dashboard.html",
            "description": "Interactive tool for identifying post-harvest loss hotspots and opportunities"
        },
        {
            "resource": "Financial Calculator Templates",
            "location": "results/youth_opportunities/financial_tools/",
            "description": "Tools for financial planning and business projection for different models"
        }
    ]
}

# Save the implementation guide
with open('results/interventions/regional/implementation_guide.json', 'w') as f:
    json.dump(implementation_guide, f, indent=4)
print("Saved regional implementation guide")

print("\nRegional implementation roadmaps and supporting documents created successfully!")
print("Completed development of key components for Phase 3, 4, and 5 of the project.")