import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('results/interventions/stakeholders', exist_ok=True)

# Define key stakeholders and their roles, influence, and interests
stakeholders = [
    {
        'Stakeholder': 'Smallholder Farmers',
        'Role': 'Primary beneficiaries and implementers of post-harvest technologies',
        'Influence': 'Medium',
        'Interest': 'High',
        'Expectations': 'Reduced crop losses, increased income, simple and affordable technologies',
        'Engagement Strategy': 'Participatory design, demonstration plots, farmer field schools, peer-to-peer learning'
    },
    {
        'Stakeholder': 'Ministry of Agriculture',
        'Role': 'Policy formulation, program oversight, extension services',
        'Influence': 'High',
        'Interest': 'High',
        'Expectations': 'Improved food security, economic development, reduced import dependency',
        'Engagement Strategy': 'Policy dialogues, joint implementation, data sharing, regular project updates'
    },
    {
        'Stakeholder': 'State Agricultural Development Programs',
        'Role': 'Local implementation, extension, monitoring',
        'Influence': 'High',
        'Interest': 'High',
        'Expectations': 'Measurable results, alignment with state priorities, capacity building',
        'Engagement Strategy': 'Collaborative planning, implementation partnerships, joint monitoring'
    },
    {
        'Stakeholder': 'Research Institutions',
        'Role': 'Technology development, testing, validation, impact assessment',
        'Influence': 'Medium',
        'Interest': 'Medium',
        'Expectations': 'Research opportunities, publication outcomes, capacity building',
        'Engagement Strategy': 'Research partnerships, student involvement, technology co-development'
    },
    {
        'Stakeholder': 'Private Sector Technology Providers',
        'Role': 'Technology supply, service provision, market development',
        'Influence': 'Medium',
        'Interest': 'Medium',
        'Expectations': 'Market expansion, profitable business opportunities, clear regulations',
        'Engagement Strategy': 'Business forums, market development support, technology showcases'
    },
    {
        'Stakeholder': 'Financial Institutions',
        'Role': 'Financing for farmers and agribusinesses, financial product development',
        'Influence': 'High',
        'Interest': 'Low',
        'Expectations': 'Viable investment opportunities, risk mitigation, scalable products',
        'Engagement Strategy': 'Risk sharing arrangements, data on technology performance, business case development'
    },
    {
        'Stakeholder': 'Processors and Aggregators',
        'Role': 'Purchase of farm outputs, value addition, market linkage',
        'Influence': 'High',
        'Interest': 'Medium',
        'Expectations': 'Consistent quality, reliable supply, competitive pricing',
        'Engagement Strategy': 'Quality standards development, contract farming models, processor-led interventions'
    },
    {
        'Stakeholder': 'NGOs and Development Partners',
        'Role': 'Funding, technical assistance, implementation support',
        'Influence': 'High',
        'Interest': 'High',
        'Expectations': 'Sustainable impact, alignment with development goals, cost-effectiveness',
        'Engagement Strategy': 'Regular coordination meetings, joint planning, shared learning platforms'
    },
    {
        'Stakeholder': 'Community Leaders',
        'Role': 'Local mobilization, cultural alignment, sustainability',
        'Influence': 'Medium',
        'Interest': 'Medium',
        'Expectations': 'Community benefits, inclusive approaches, respect for local norms',
        'Engagement Strategy': 'Early consultation, traditional authority engagement, visibility in success stories'
    },
    {
        'Stakeholder': 'Women\'s Groups',
        'Role': 'Gender-responsive implementation, specific value chain activities',
        'Influence': 'Low',
        'Interest': 'High',
        'Expectations': 'Gender equality, economic empowerment, appropriate technologies',
        'Engagement Strategy': 'Women-focused design sessions, targeted training, leadership development'
    },
    {
        'Stakeholder': 'Youth Organizations',
        'Role': 'Innovation adoption, service provision, future sustainability',
        'Influence': 'Low',
        'Interest': 'Medium',
        'Expectations': 'Employment opportunities, skills development, innovative approaches',
        'Engagement Strategy': 'Agripreneurship training, technology-focused roles, digital engagement'
    },
    {
        'Stakeholder': 'Consumer Associations',
        'Role': 'Demand creation, quality standards, feedback',
        'Influence': 'Low',
        'Interest': 'Low',
        'Expectations': 'Food safety, quality improvement, fair pricing',
        'Engagement Strategy': 'Awareness campaigns, quality certification participation, consumer feedback mechanisms'
    }
]

# Create DataFrame for stakeholders
stakeholder_df = pd.DataFrame(stakeholders)

# Export stakeholder information to CSV
stakeholder_df.to_csv('results/interventions/stakeholders/stakeholder_analysis.csv', index=False)
print("Stakeholder analysis saved to 'results/interventions/stakeholders/stakeholder_analysis.csv'")

# Convert influence and interest to numerical scales for power-interest grid
influence_scale = {'Low': 1, 'Medium': 2, 'High': 3}
interest_scale = {'Low': 1, 'Medium': 2, 'High': 3}

stakeholder_df['Influence_Score'] = stakeholder_df['Influence'].map(influence_scale)
stakeholder_df['Interest_Score'] = stakeholder_df['Interest'].map(interest_scale)

# Create power-interest grid
plt.figure(figsize=(12, 10))

# Create scatter plot
plt.scatter(
    stakeholder_df['Interest_Score'],
    stakeholder_df['Influence_Score'],
    s=100,
    c=stakeholder_df['Influence_Score'] * stakeholder_df['Interest_Score'],
    cmap='viridis',
    alpha=0.7
)

# Add stakeholder labels
for i, row in stakeholder_df.iterrows():
    plt.annotate(
        row['Stakeholder'],
        (row['Interest_Score'], row['Influence_Score']),
        xytext=(5, 5),
        textcoords='offset points',
        fontsize=9
    )

# Set up the grid
plt.xlim(0.5, 3.5)
plt.ylim(0.5, 3.5)
plt.xticks([1, 2, 3], ['Low', 'Medium', 'High'])
plt.yticks([1, 2, 3], ['Low', 'Medium', 'High'])
plt.grid(True, alpha=0.3)

# Add quadrant labels
plt.text(1, 3, 'Keep Satisfied\n(High Influence, Low Interest)', ha='center', va='center', bbox=dict(facecolor='lightblue', alpha=0.5))
plt.text(3, 3, 'Key Players\n(High Influence, High Interest)', ha='center', va='center', bbox=dict(facecolor='lightgreen', alpha=0.5))
plt.text(1, 1, 'Minimal Effort\n(Low Influence, Low Interest)', ha='center', va='center', bbox=dict(facecolor='lightgray', alpha=0.5))
plt.text(3, 1, 'Keep Informed\n(Low Influence, High Interest)', ha='center', va='center', bbox=dict(facecolor='lightyellow', alpha=0.5))

plt.xlabel('Interest Level', fontsize=14)
plt.ylabel('Influence Level', fontsize=14)
plt.title('Stakeholder Power-Interest Grid for Post-Harvest Loss Interventions', fontsize=16)

plt.tight_layout()
plt.savefig('results/interventions/stakeholders/power_interest_grid.png', dpi=300, bbox_inches='tight')
plt.close()
print("Power-interest grid saved to 'results/interventions/stakeholders/power_interest_grid.png'")

# Create engagement strategy plan
engagement_activities = [
    {
        'Activity': 'Stakeholder Inception Workshop',
        'Timing': 'Project Start',
        'Target Stakeholders': 'All stakeholders',
        'Purpose': 'Share project objectives, gather input, establish coordination mechanisms',
        'Expected Outcomes': 'Shared understanding, initial buy-in, roles clarification'
    },
    {
        'Activity': 'Quarterly Coordination Meetings',
        'Timing': 'Quarterly',
        'Target Stakeholders': 'Ministry of Agriculture, State ADPs, NGOs, Development Partners',
        'Purpose': 'Share progress, address challenges, coordinate activities',
        'Expected Outcomes': 'Alignment of efforts, problem-solving, synergy'
    },
    {
        'Activity': 'Farmer Field Days',
        'Timing': 'Seasonal (2-3 per year)',
        'Target Stakeholders': 'Farmers, Community Leaders, Extension Agents, Technology Providers',
        'Purpose': 'Demonstrate technologies, gather feedback, promote adoption',
        'Expected Outcomes': 'Technology awareness, adoption decisions, user feedback'
    },
    {
        'Activity': 'Policy Dialogue Forums',
        'Timing': 'Bi-annually',
        'Target Stakeholders': 'Ministry of Agriculture, Regulatory Bodies, Financial Institutions, Private Sector',
        'Purpose': 'Identify policy barriers, propose solutions, advocate for enabling environment',
        'Expected Outcomes': 'Policy recommendations, regulatory improvements, public-private alignment'
    },
    {
        'Activity': 'Technology Innovation Fairs',
        'Timing': 'Annually',
        'Target Stakeholders': 'Technology Providers, Farmers, Processors, Research Institutions, Youth Groups',
        'Purpose': 'Showcase innovations, connect supply and demand, stimulate market development',
        'Expected Outcomes': 'Market linkages, technology refinement, innovation adoption'
    },
    {
        'Activity': 'Gender-Focused Design Workshops',
        'Timing': 'Project Start and Mid-term',
        'Target Stakeholders': 'Women\'s Groups, Gender Specialists, Technology Designers',
        'Purpose': 'Ensure technologies address women\'s needs, roles, and constraints',
        'Expected Outcomes': 'Gender-appropriate technologies, increased women\'s participation'
    },
    {
        'Activity': 'Value Chain Stakeholder Platforms',
        'Timing': 'Quarterly',
        'Target Stakeholders': 'Farmers, Processors, Aggregators, Transporters, Retailers',
        'Purpose': 'Address systemic value chain issues, improve coordination',
        'Expected Outcomes': 'Value chain efficiency, reduced bottlenecks, improved relationships'
    },
    {
        'Activity': 'Financial Product Design Sessions',
        'Timing': 'Early Implementation Phase',
        'Target Stakeholders': 'Financial Institutions, Farmers, Technology Providers',
        'Purpose': 'Design appropriate financial products for technology adoption',
        'Expected Outcomes': 'New financial products, increased access to finance'
    },
    {
        'Activity': 'Community Engagement Meetings',
        'Timing': 'Monthly',
        'Target Stakeholders': 'Community'
        }
    ]