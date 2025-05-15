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
    
    return save_path