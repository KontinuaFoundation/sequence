import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# aggregate the data
data = {
    'Condition': ['Good', 'Good', 'Poor', 'Poor', 'Total', 'Total'],
    'Hospital': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Survival': [0.98, 0.94, 0.78, 0.40, 0.80, 0.89]
}
df = pd.DataFrame(data)

# split into subgroups and totals for showing different correlations
subgroups = df[df['Condition'] != 'Total']
totals = df[df['Condition'] == 'Total']


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
# regression lines and plots 
ax1.plot([-0.2, 0.8], [0.98, 0.78], 'b--', marker='o', label='Trend A') 
ax1.plot([0.2, 1.2], [0.94, 0.40], 'y--', marker='o', label='Trend B') 
ax1.legend()
ax2.plot([-0.2, 0.2], [0.80, 0.89], 'k-', marker='o', label='Overall Trend')
ax2.legend()
sns.barplot(data=subgroups, x='Condition', y='Survival', hue='Hospital', ax=ax1)
ax1.set_title('Subgroups (A Wins)')

sns.barplot(data=totals, x='Condition', y='Survival', hue='Hospital', ax=ax2)
ax2.set_title('Total (B Wins)')

plt.tight_layout()
plt.show()