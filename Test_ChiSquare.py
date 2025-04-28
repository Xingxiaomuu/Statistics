from scipy.stats import chisquare
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, chi2

# 1.Perform Chi-Squared test 
# Goodness of fit
observed = [135 ,441    ,1899   ,55     ,502    ]
expected = [91  ,303.2  ,2061.8 ,60.6   ,515.4  ]
chi2_stat_gof, p_value_gof = chisquare(observed, f_exp=expected)
print(f"Goodness of fit - Chi-square Statistic = {chi2_stat_gof:.2f}")
print(f"Goodness of fit - P-value = {p_value_gof:.4f}")
if p_value_gof < 0.05:
    print("Reject the null hypothesis: The observed frequencies differ significantly from the expected frequencies.")
else:
    print("The observed frequencies do not differ significantly from the expected frequencies.")
# Test of Independence 5种鸟类，3个地区，举例一个独立性检验，构建列联表（contingency table）
data = np.array([
    [20,30,25],
    [15,25,20],
    [25,35,30],
    [10,20,15],
    [30,40,35],
])
chi2_stat_ind, p_value_ind, dof_ind, expected_table = chi2_contingency(data)
print(f"Test of Independence - Chi2 Statistic: {chi2_stat_ind:.2f}")
print(f"Test of Independence - p-value: {p_value_ind:.4f}")
print(f"Test of Independence - Degrees of Freedom: {dof_ind}")
if p_value_ind < 0.05:
    print("Reject the null hypothesis: The two categorical variables are not independent.鸟类分布与地区有关.")
else:
    print("The two categorical variables are independent.鸟类分布与地区无关.")


# 2. Visualization
x_labels = ['Bird1', 'Bird2', 'Bird3', 'Bird4', 'Bird5']
x = np.arange(len(x_labels))
width = 0.35
fig, axs = plt.subplots(2, 2, figsize=(18,9))
# 绘制 Goodness of fit 可视化
axs[0,0].bar(x - width/2, observed, width, label='Observed', color='skyblue')
axs[0,0].bar(x + width/2, expected, width, label='Expected', color='lightgreen')
axs[0,0].set_xlabel('Bird Species')
axs[0,0].set_ylabel('Count')
axs[0,0].set_title('Goodness of Fit: Observed vs Expected')
axs[0,0].set_xticks(x)
axs[0,0].set_xticklabels(x_labels)
axs[0,0].legend()
# 绘制 独立性检验 可视化（热力图）
sns.heatmap(data, annot=True, fmt='d', cmap='YlGnBu', ax=axs[0,1], cbar=False)
axs[0,1].set_title('Contingency Table: Bird Species vs Regions')
axs[0,1].set_xlabel('Region')
axs[0,1].set_ylabel('Bird Species')
axs[0,1].set_xticklabels(['A', 'B', 'C'])
axs[0,1].set_yticklabels(['Bird1', 'Bird2', 'Bird3', 'Bird4', 'Bird5'])


# 3. Goodness of Fit 卡方分布曲线
dof_gof = len(observed) - 1
x_vals = np.linspace(0,100,500)
y_vals = chi2.pdf(x_vals, dof_gof)

axs[1,0].plot(x_vals, y_vals, label = 'Chi-Squared Distribution (df={dof_gof})', color='blue')
axs[1,0].axvline(chi2_stat_gof, color='red', linestyle='--', label='Observed Chi2 Statistic = {chi2_stat_gof:.2f}') 
critical_value = chi2.ppf(0.95, dof_gof)
axs[1,0].axvline(critical_value, color='green', linestyle='--', label='Critical Value (alpha=0.05)')
axs[1,0].set_title('Chi-Squared Distribution (Goodness of Fit)')
axs[1,0].set_xlabel('Chi-Squared Value')
axs[1,0].set_ylabel('Probability Density')
axs[1,0].legend()


# 4. Test of Independence 卡方分布曲线
x_vals2 = np.linspace(0,20,500)
y_vals2 = chi2.pdf(x_vals2, dof_ind)

axs[1,1].plot(x_vals2, y_vals2, label = 'Chi-Squared PDF (df={dof_ind})', color='purple')
axs[1,1].axvline(chi2_stat_ind, color='red',linestyle='--', label='Observed Chi2 Statistic = {chi2_stat_ind:.2f}')
critical_value_ind = chi2.ppf(0.95, dof_ind)
axs[1,1].axvline(critical_value_ind, color='green', linestyle='--', label='Critical Value (alpha=0.05)')
axs[1,1].set_title('Chi-Squared Distribution (Test of Independence)')
axs[1,1].set_xlabel('Chi-Squared Value')
axs[1,1].set_ylabel('Probability Density')
axs[1,1].legend()

plt.tight_layout()
plt.show()