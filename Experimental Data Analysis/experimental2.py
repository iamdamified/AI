"""Obaakran Performance Snapshot
Visual Graphic: A Waterfall Chart starting with 2024 Total Revenue and ending with 2025 Total Revenue, 
showing the growth contribution of each category (Inks and Mobiles being the steepest positive steps).

Highlight Callouts: * Growth Driver: Inks & Consumables (+25.46%)

Strategic Shift: Decrease in Laptop volume offset by high-margin Printer and Mobile growth.

Key Insight: Consumables (Inks/Toners) are becoming a more stable revenue anchor for the branch compared to hardware.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Handle encoding for proper display
sys.stdout.reconfigure(encoding='utf-8')

# Load the Excel file
df = pd.read_excel('Obaakran.xlsx')

# Data Preparation
categories = df['Category']
revenue_2024 = df['2024 Revenue (₦)']
revenue_2025 = df['2025 Revenue (₦)']

# Calculate growth contributions (difference for waterfall)
growth_values = revenue_2025 - revenue_2024

# Total revenues
total_2024 = revenue_2024.sum()
total_2025 = revenue_2025.sum()

# Create waterfall chart
fig, ax = plt.subplots(figsize=(14, 8))

# Prepare data for waterfall chart
x_pos = np.arange(len(categories) + 2)  # +2 for totals
labels = ['2024 Total'] + list(categories) + ['2025 Total']

# Calculate cumulative values for waterfall positioning
cumulative = np.zeros(len(categories) + 2)
cumulative[0] = 0
cumulative[1:-1] = total_2024

# Create the waterfall values and colors
values = np.zeros(len(categories) + 2)
values[0] = total_2024  # Starting value
values[1:-1] = growth_values  # Growth contributions
values[-1] = total_2025  # Ending total

colors = []
for i, val in enumerate(values):
    if i == 0:
        colors.append('#2E86AB')  # Starting bar - blue
    elif i == len(values) - 1:
        colors.append('#A23B72')  # Ending bar - purple
    elif val >= 0:
        colors.append('#06A77D')  # Positive growth - green
    else:
        colors.append('#D62828')  # Negative growth - red

# Create horizontal bars for waterfall
for i in range(len(x_pos)):
    if i == 0:
        # Starting bar
        ax.barh(i, values[i], color=colors[i], alpha=0.8, edgecolor='black', linewidth=1.5, height=0.6)
        ax.text(values[i] / 2, i, f'₦{values[i]/1e6:.1f}M', va='center', ha='center', fontweight='bold', fontsize=10, color='white')
    elif i == len(x_pos) - 1:
        # Ending bar
        ax.barh(i, values[i], color=colors[i], alpha=0.8, edgecolor='black', linewidth=1.5, height=0.6)
        ax.text(values[i] / 2, i, f'₦{values[i]/1e6:.1f}M', va='center', ha='center', fontweight='bold', fontsize=10, color='white')
    else:
        # Individual contribution bars
        if values[i] >= 0:
            start_pos = total_2024 if i == 1 else cumulative[i-1] + values[i-1]
            # Recalculate based on running total
            start_pos = cumulative[i]
            ax.barh(i, values[i], left=start_pos, color=colors[i], alpha=0.85, edgecolor='black', linewidth=1, height=0.6)
            ax.text(start_pos + values[i] / 2, i, f'₦{values[i]/1e6:.1f}M\n({df.iloc[i-1]["Growth %"]})', 
                   va='center', ha='center', fontweight='bold', fontsize=9, color='white')
            cumulative[i+1] = start_pos + values[i]
        else:
            start_pos = cumulative[i]
            ax.barh(i, values[i], left=start_pos + values[i], color=colors[i], alpha=0.85, edgecolor='black', linewidth=1, height=0.6)
            ax.text(start_pos + values[i] / 2, i, f'₦{values[i]/1e6:.1f}M\n({df.iloc[i-1]["Growth %"]})', 
                   va='center', ha='center', fontweight='bold', fontsize=9, color='white')
            cumulative[i+1] = start_pos + values[i]

# Connect bars with lines
for i in range(len(x_pos) - 1):
    if i == 0:
        end_y_val = total_2024
    else:
        end_y_val = cumulative[i+1]
    ax.plot([end_y_val, end_y_val], [i + 0.3, i + 0.7], 'k--', linewidth=1, alpha=0.5)

# Customize the plot
ax.set_ylabel('Category', fontsize=12, fontweight='bold')
ax.set_xlabel('Revenue (₦)', fontsize=12, fontweight='bold')
ax.set_title('Obaakran Performance Snapshot - Waterfall Chart (2024 vs. 2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_yticks(x_pos)
ax.set_yticklabels(labels, fontsize=10)
ax.invert_yaxis()

# Format x-axis with thousands separator
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₦{x/1e6:.0f}M'))

# Add grid for better readability
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2E86AB', alpha=0.8, label='2024 Total'),
    Patch(facecolor='#06A77D', alpha=0.8, label='Positive Growth'),
    Patch(facecolor='#D62828', alpha=0.8, label='Negative Growth'),
    Patch(facecolor='#A23B72', alpha=0.8, label='2025 Total')
]
ax.legend(handles=legend_elements, fontsize=10, loc='lower right')

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('obaakran_performance_waterfall.png', dpi=300, bbox_inches='tight')
print("✓ Chart saved as 'obaakran_performance_waterfall.png'")

# Display the chart
plt.show()

# Analysis and Insights
print("\n" + "="*80)
print("OBAAKRAN PERFORMANCE SNAPSHOT - WATERFALL ANALYSIS (2024 vs. 2025)")
print("="*80)

# Calculate growth rates
df['2024 Revenue (₦)'] = revenue_2024
df['2025 Revenue (₦)'] = revenue_2025
df['Revenue Change (₦)'] = growth_values
df['Growth Rate %'] = ((revenue_2025 - revenue_2024) / revenue_2024 * 100).round(2)

# Sort by revenue change
df_sorted_change = df.sort_values('Revenue Change (₦)', ascending=False)

print("\nREVENUE CHANGE BY CATEGORY (Sorted by Impact):")
print("-" * 80)
for idx, (i, row) in enumerate(df_sorted_change.iterrows(), 1):
    change = row['Revenue Change (₦)']
    if change >= 0:
        print(f"{idx}. {row['Category']:20} | 2024: ₦{row['2024 Revenue (₦)']/1e6:>7.2f}M | 2025: ₦{row['2025 Revenue (₦)']/1e6:>7.2f}M | Change: +₦{change/1e6:>6.2f}M | Growth: {row['Growth Rate %']:>7.2f}%")
    else:
        print(f"{idx}. {row['Category']:20} | 2024: ₦{row['2024 Revenue (₦)']/1e6:>7.2f}M | 2025: ₦{row['2025 Revenue (₦)']/1e6:>7.2f}M | Change: -₦{abs(change)/1e6:>6.2f}M | Growth: {row['Growth Rate %']:>7.2f}%")

print("\n" + "="*80)
print("KEY INSIGHTS & HIGHLIGHT CALLOUTS")
print("="*80)

# Growth drivers (top contributors)
print("\n★ GROWTH DRIVERS (Highest Positive Contributors):")
top_contributors = df_sorted_change[df_sorted_change['Revenue Change (₦)'] > 0].head(3)
for idx, (i, row) in enumerate(top_contributors.iterrows(), 1):
    print(f"  {idx}. {row['Category']:20} | Revenue increase: ₦{row['Revenue Change (₦)']/1e6:>6.2f}M | Growth Rate: {row['Growth Rate %']:>7.2f}%")

# Highlight: Inks & Consumables as growth driver
inks_growth = df[df['Category'] == 'Inks'].iloc[0]
toners_growth = df[df['Category'] == 'Toners'].iloc[0]
total_consumables_2024 = inks_growth['2024 Revenue (₦)'] + toners_growth['2024 Revenue (₦)']
total_consumables_2025 = inks_growth['2025 Revenue (₦)'] + toners_growth['2025 Revenue (₦)']
consumables_growth_rate = ((total_consumables_2025 - total_consumables_2024) / total_consumables_2024 * 100)

print(f"\n★ GROWTH DRIVER: Inks & Consumables")
print(f"  Inks Growth: {inks_growth['Growth Rate %']:.2f}% (₦{inks_growth['Revenue Change (₦)']/1e6:.2f}M)")
print(f"  Toners Growth: {toners_growth['Growth Rate %']:.2f}% (₦{toners_growth['Revenue Change (₦)']/1e6:.2f}M)")
print(f"  Combined Consumables 2024: ₦{total_consumables_2024/1e6:.2f}M")
print(f"  Combined Consumables 2025: ₦{total_consumables_2025/1e6:.2f}M")
print(f"  Combined Growth Rate: {consumables_growth_rate:.2f}%")

# Strategic shift analysis
laptops = df[df['Category'] == 'Laptops'].iloc[0]
print(f"\n★ STRATEGIC SHIFT: Hardware Dynamics")
print(f"  Laptops (Declining): {laptops['Growth Rate %']:.2f}% | Loss: -₦{abs(laptops['Revenue Change (₦)'])/1e6:.2f}M")

printers = df[df['Category'] == 'Printers'].iloc[0]
mobiles = df[df['Category'] == 'Mobile Phones'].iloc[0]
print(f"  Printers (Growing): {printers['Growth Rate %']:.2f}% | Gain: +₦{printers['Revenue Change (₦)']/1e6:.2f}M")
print(f"  Mobile Phones (Growing): {mobiles['Growth Rate %']:.2f}% | Gain: +₦{mobiles['Revenue Change (₦)']/1e6:.2f}M")
print(f"  → Hardware offset: Laptop decline (-₦{abs(laptops['Revenue Change (₦)'])/1e6:.2f}M) offset by Printer & Mobile growth (+₦{(printers['Revenue Change (₦)'] + mobiles['Revenue Change (₦)'])/1e6:.2f}M)")

# Contracting categories
print(f"\n⚠ CONTRACTING CATEGORIES:")
declining = df[df['Revenue Change (₦)'] < 0]
for idx, (i, row) in enumerate(declining.iterrows(), 1):
    print(f"  {idx}. {row['Category']:20} | Decline: {row['Growth Rate %']:>7.2f}% | Loss: -₦{abs(row['Revenue Change (₦)'])/1e6:>6.2f}M")

# Overall summary
print(f"\n" + "="*80)
print("OVERALL SUMMARY")
print("="*80)
print(f"Total Revenue 2024:          ₦{total_2024/1e6:>10.2f}M")
print(f"Total Revenue 2025:          ₦{total_2025/1e6:>10.2f}M")
overall_growth = ((total_2025 - total_2024) / total_2024 * 100)
print(f"Overall Growth:              {overall_growth:>10.2f}%")
print(f"Total Revenue Increase:      ₦{(total_2025 - total_2024)/1e6:>10.2f}M")
print("="*80)

# Key insight about consumables
consumables_2024_share = (total_consumables_2024 / total_2024) * 100
consumables_2025_share = (total_consumables_2025 / total_2025) * 100
print(f"\n✓ KEY INSIGHT: Consumables (Inks/Toners) Revenue Share")
print(f"  2024 Share: {consumables_2024_share:.2f}% (₦{total_consumables_2024/1e6:.2f}M of ₦{total_2024/1e6:.2f}M)")
print(f"  2025 Share: {consumables_2025_share:.2f}% (₦{total_consumables_2025/1e6:.2f}M of ₦{total_2025/1e6:.2f}M)")
print(f"  Change in Share: {consumables_2025_share - consumables_2024_share:+.2f} percentage points")
print(f"  ✓ Consumables (Inks/Toners) are becoming a more stable revenue anchor for the Obaakran branch")
print(f"    compared to hardware, with consistent growth despite hardware category volatility.")
print("="*80)



# End of westgate2.py
# Output saved as 'obaakran_performance_waterfall.png' and analysis printed to console.
