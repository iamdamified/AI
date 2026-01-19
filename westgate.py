""" Printer Revenue Growth Map (2024 vs. 2025)
Visual Graphic: A Clustered Bar Chart showing branches on the Y-axis and Revenue on the X-axis. Use Blue for 2024 and Orange for 2025.

Highlight Callouts: * Top Performer: Adepele (+61.68%)

Emerging Hub: Online (+52.45%)

Key Insight: Printer revenue is shifting toward "Online" and "Adepele" hubs, while traditional hubs like Enugu and P/Harcourt saw a contraction."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Handle encoding for proper display
sys.stdout.reconfigure(encoding='utf-8')

# Load the Excel file
df = pd.read_excel('printer.xlsx')

# Data Preparation
branches = df['Branch']
revenue_2024 = df['2024 Printer Revenue (₦)']
revenue_2025 = df['2025 Printer Revenue (₦)']

# Calculate growth percentages for verification
growth_percentages = ((revenue_2025 - revenue_2024) / revenue_2024 * 100).round(2)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Set up bar positions
x = np.arange(len(branches))
width = 0.35

# Create bars
bars1 = ax.barh(x - width/2, revenue_2024, width, label='2024', color='#1f77b4', alpha=0.8)  # Blue
bars2 = ax.barh(x + width/2, revenue_2025, width, label='2025', color='#ff7f0e', alpha=0.8)  # Orange

# Customize the plot
ax.set_xlabel('Revenue (₦)', fontsize=12, fontweight='bold')
ax.set_ylabel('Branch', fontsize=12, fontweight='bold')
ax.set_title('Printer Revenue Growth Map (2024 vs. 2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_yticks(x)
ax.set_yticklabels(branches)
ax.legend(fontsize=11, loc='lower right')

# Format x-axis with thousands separator
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₦{x/1e6:.0f}M'))

# Add grid for better readability
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add value labels on bars
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    # 2024 value
    width1 = bar1.get_width()
    ax.text(width1, bar1.get_y() + bar1.get_height()/2, f' ₦{width1/1e6:.1f}M',
            va='center', fontsize=9, alpha=0.7)
    
    # 2025 value
    width2 = bar2.get_width()
    ax.text(width2, bar2.get_y() + bar2.get_height()/2, f' ₦{width2/1e6:.1f}M',
            va='center', fontsize=9, alpha=0.7)

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('printer_revenue_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Chart saved as 'printer_revenue_comparison.png'")

# Display the chart
plt.show()

# Analysis and Insights
print("\n" + "="*70)
print("PRINTER REVENUE GROWTH ANALYSIS (2024 vs. 2025)")
print("="*70)

# Sort by growth percentage
df['Growth (%)'] = growth_percentages
df_sorted = df.sort_values('Growth (%)', ascending=False)

print("\nTOP 5 PERFORMERS (Highest Growth):")
print("-" * 70)
for idx, (i, row) in enumerate(df_sorted.head(5).iterrows(), 1):
    print(f"{idx}. {row['Branch']:20} | 2024: ₦{row['2024 Printer Revenue (₦)']/1e6:>7.2f}M | 2025: ₦{row['2025 Printer Revenue (₦)']/1e6:>7.2f}M | Growth: {row['Growth (%)']:>7.2f}%")

print("\nBOTTOM 5 PERFORMERS (Lowest Growth/Contraction):")
print("-" * 70)
for idx, (i, row) in enumerate(df_sorted.tail(5).iterrows(), 1):
    print(f"{idx}. {row['Branch']:20} | 2024: ₦{row['2024 Printer Revenue (₦)']/1e6:>7.2f}M | 2025: ₦{row['2025 Printer Revenue (₦)']/1e6:>7.2f}M | Growth: {row['Growth (%)']:>7.2f}%")

# Key insights
print("\n" + "="*70)
print("KEY INSIGHTS & HIGHLIGHT CALLOUTS")
print("="*70)

# Top performer
top_performer = df_sorted.iloc[0]
print(f"\n★ TOP PERFORMER: {top_performer['Branch']}")
print(f"  Growth: {top_performer['Growth (%)']:.2f}%")
print(f"  Revenue 2024: ₦{top_performer['2024 Printer Revenue (₦)']/1e6:.2f}M")
print(f"  Revenue 2025: ₦{top_performer['2025 Printer Revenue (₦)']/1e6:.2f}M")
print(f"  Additional Revenue: ₦{(top_performer['2025 Printer Revenue (₦)'] - top_performer['2024 Printer Revenue (₦)'])/1e6:.2f}M")

# Emerging hub (Online)
online_row = df[df['Branch'] == 'Online'].iloc[0]
print(f"\n★ EMERGING HUB: Online")
print(f"  Growth: {growth_percentages[df[df['Branch'] == 'Online'].index[0]]:.2f}%")
print(f"  Revenue 2024: ₦{online_row['2024 Printer Revenue (₦)']/1e6:.2f}M")
print(f"  Revenue 2025: ₦{online_row['2025 Printer Revenue (₦)']/1e6:.2f}M")
print(f"  Additional Revenue: ₦{(online_row['2025 Printer Revenue (₦)'] - online_row['2024 Printer Revenue (₦)'])/1e6:.2f}M")

# Contracting branches
contracting = df_sorted[df_sorted['Growth (%)'] < 0]
print(f"\n⚠ CONTRACTING BRANCHES ({len(contracting)} branches):")
for i, (idx, row) in enumerate(contracting.iterrows(), 1):
    print(f"  {i}. {row['Branch']:20} | Contraction: {row['Growth (%)']:>7.2f}%")

# Overall summary
total_2024 = revenue_2024.sum()
total_2025 = revenue_2025.sum()
overall_growth = ((total_2025 - total_2024) / total_2024 * 100)

print(f"\n" + "="*70)
print("OVERALL SUMMARY")
print("="*70)
print(f"Total Revenue 2024:     ₦{total_2024/1e6:>10.2f}M")
print(f"Total Revenue 2025:     ₦{total_2025/1e6:>10.2f}M")
print(f"Overall Growth:         {overall_growth:>10.2f}%")
print(f"Additional Revenue:     ₦{(total_2025 - total_2024)/1e6:>10.2f}M")
print("="*70)

print("\n✓ KEY INSIGHT: Printer revenue is shifting toward 'Online' and 'Adepele' hubs,")
print("  while traditional hubs like Enugu and P/Harcourt saw a contraction.")


# End of westgate.py
# Output saved as 'printer_revenue_comparison.png' and analysis printed to console.