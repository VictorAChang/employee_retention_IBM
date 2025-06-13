

<h1 style="font-size: 400%; text-align:center;"> Driving Strategic Decisions with Data </h1>

<div style="font-size: 125%; text-align:center;"> Employee Retention </div>

<div style="font-size: 125%; text-align:center;"> Written by Victor Chang | MBA 610 - Foundations of Data Analytics </div>

</br><br>

<h1 style="text-align:center;"> Executive Summary </h1>

Employee retention remains one of the most pressing challenges in today’s competitive labor market. High turnover rates not only increase recruitment and training costs but also disrupt organizational continuity and morale. This paper explores employee retention by examining its scope, causes, and business impact. It uses a relevant dataset to uncover patterns and root causes through descriptive and diagnostic analytics, with recommendations aimed at helping organizations improve employee engagement and reduce turnover.

<h1 style="text-align:center;"> Introduction </h1>

<b style="font-size: 125%;"> Employee Retention </b>

Employee retention refers to an organization’s ability to keep its employees over time. It is a critical aspect of workforce management, directly influencing operational efficiency, company culture, and financial performance. Retention issues often arise from dissatisfaction with leadership, limited growth opportunities, inadequate compensation, or poor work-life balance (Ramos, 2019). High employee turnover often leads to elevated recruitment and training expenses, reduced productivity, and a loss of experienced personnel. When employees frequently resign, it also undermines team stability and hinders long-term strategic planning (Anvari, JianFu, & Chermahini, 2014).

<b style="font-size: 125%;"> Scope of the Problem and Business Impact </b>

High employee turnover costs businesses significantly. According to Gallup (2023), replacing an employee can cost one-half to two times the employee’s annual salary. For a mid-sized organization, this could mean hundreds of thousands to millions of dollars annually. U.S. companies lose about $1 trillion annually due to voluntary turnover (Gallup, 2023).

High employee turnover also negatively impacts businesses in non-direct non-financial ways that can hinder long term success. One major consequence is the loss of institutional knowledge, which disrupts operations and reduces overall efficiency when experienced employees leave (Lancaster, 2024). Turnover also burdens remaining staff, increasing workloads and stress levels, which can lead to burnout and lower morale. This environment often fosters a toxic workplace culture where engagement and collaboration suffer (Lancaster, 2024). 

<h1 style="text-align:center;"> Data Exploration </h1>

<b style="font-size: 125%;"> Data Source </b>

Data is produced by Portobello Tech, an app innovator that has devised an intelligent way of predicting employee turnover within the company. The data source is from Kaggle at https://www.kaggle.com/datasets/akshayhedau/employee-turnover-analytics-dataset?resource=download. Data from prior evaluations show the employee’s satisfaction at the workplace. The data could be used to identify patterns in work style and their interest to continue to work in the company. The HR Department owns the data and uses it to predict employee turnover. Employee turnover refers to the total number of workers who leave a company over a certain time period. 

<b style="font-size: 125%;"> Data Description </b>

<i> First Five rows of the dataset </i>

![alt text](images/head.png)

<i> Data Columns </i>

* satisfaction_level: From 0-1, how satisfied employees are since 
* last_evaluation: Unsure, but most likely from 0-1, measuring employee performance
* number_project = From 2-7, how many project the employee has work on
* average_monthly_hours = Average number of hours worked each month
* time_spend_company = How long they have been at the company in years
* Work_accident = If the employee has had an accident at work
* left = If the employee has left the company
* promotion_last_5years = If the employee has had a promotion in the last 5 years
* sales = Unsure, but most likely the role within sales that each employee works in
* salary = employee salary

<div align="center">

<b style="font-size: 110%;"> Data Information </b>

| #  | Column                 | Non-Null Count | Dtype   |
|----|------------------------|----------------|---------|
| 0  | `satisfaction_level`   | 14,999         | float64 |
| 1  | `last_evaluation`      | 14,999         | float64 |
| 2  | `number_project`       | 14,999         | int64   |
| 3  | `average_montly_hours` | 14,999         | int64   |
| 4  | `time_spend_company`   | 14,999         | int64   |
| 5  | `Work_accident`        | 14,999         | int64   |
| 6  | `left`                 | 14,999         | int64   |
| 7  | `promotion_last_5years`| 14,999         | int64   |
| 8  | `sales`                | 14,999         | object  |
| 9  | `salary`               | 14,999         | object  |

</div>

<i> Data Statistics </i>

![alt text](images/describe.png)


<h1 style="text-align:center;"> Analytical Techniques </h1>

<b style="font-size: 125%;"> Descriptive Analytics </b>

Expected analysis: Use frequency counts, distributions, and cross-tabulations. You’ll likely observe that:
•	Younger employees and those with fewer years at the company have higher attrition.
•	Roles with high travel requirements or lower job satisfaction correlate with higher turnover.
•	Departments like Sales or Human Resources might show higher attrition rates.

<div align="center">

<b style="font-size: 110%;"> Histogram </b> </br>

<img src="image-1.png">

</div>

<b style="font-size: 125%;"> Diagnostic Analytics </b>

Expected analysis: Multivariate analysis and correlation. Common findings include:
•	Low job satisfaction and poor work-life balance are strong predictors of attrition.
•	Employees with lower income or fewer opportunities for promotion are more likely to leave.


What to look for in Python:
•	Heatmaps of correlations
•	Logistic regression to quantify feature importance
•	Decision trees or SHAP values for explainability


<div align="center">

<b style="font-size: 110%;"> Heatmap </b>

<img src="image.png">

</div>

</br>

<h1 style="text-align:center;"> Insights and Recommendations </h1>

<b style="font-size: 125%;"> Actionable Insights </b>

Based on expected trends:
•	Employees with less tenure, lower salaries, and poor job satisfaction are most likely to leave.
•	Work-life balance and career development opportunities are consistent drivers of retention.

<b style="font-size: 125%;"> Solutions and Strategies </b>

Recommendations include:
•	Implement targeted retention strategies such as mentorship for new employees.
•	Increase transparency around career progression and provide continuous learning.
•	Use predictive analytics models to identify at-risk employees early and intervene (SHRM, 2022).

<h1 style="text-align:center;"> Communication </h1>

<b style="font-size: 125%;"> Findings </b>

Create dashboards or infographics that highlight:
•	Top 5 features most associated with attrition
•	Summary of employee demographics vs. attrition likelihood
•	“What-if” scenarios using model predictions
Ensure visuals are intuitive for a non-technical audience by minimizing jargon and emphasizing takeaways.

<h1 style="text-align:center;"> Conclusion </h1>

Employee retention is both a human and business imperative. With the right data and analytics, organizations can understand why employees leave and implement strategies to increase engagement and loyalty. By proactively addressing root causes, companies can create a more stable and productive workforce. 

<h1 style="text-align:center;"> References </h1>

* Anvari, R., JianFu, Z., & Chermahini, S. H. (2014). Effective Strategy for Solving Voluntary Turnover Problem among Employees. Procedia, Social and Behavioral Sciences, 129, 186–190. https://doi.org/10.1016/j.sbspro.2014.03.665
* Gallup. (2023). The True Cost of Employee Turnover. https://www.gallup.com/workplace
* Lancaster, L. (2024, August 16). Effects of High Turnover Among Employees. https://stratus.hr/resources/effects-of-high-employee-turnover
* Kaggle. (n.d.). Employee Turnover Analystics Dataset. https://www.kaggle.com/datasets/akshayhedau/employee-turnover-analytics-dataset?resource=download
* Ramos, P. R. (2019). The effectiveness of compensation in maintaining employee retention. Social Sciences & Humanities Open, 1, Article 100001. https://doi.org/10.1016/j.ssaho.2019.100001

 

