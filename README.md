

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

The image above shows the first five rows of the dataset, using python's pandas library to display the data as a dataframe for ease of view. 

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

The columns above describe in more detail what each row means or represents. Some of the values are not exactly known as the dataset in kaggle did not describe exactly what they are and we do not want to assume incorrectly and make wrong predictions based on those columns. 

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

Data information above shows that the dataset does not contain any null or missing values and also displays the data types of each column. It is important to know the data types as they affect the way the data is manipulated to extract insights and predictions about employee retention. 

<i> Data Statistics </i>

![alt text](images/describe.png)

The table above shows important statistic information about our dataset. It is important especially important to pay attention to the difference between mean and median values. Huge differences among these two values is an indicator that the data might have too many outliers and may be skewed, needing further cleaning to derive accurate insights. Looking at the max and min values can also show if there are values that simply do not make sense. Most of the values from this dataset are within normal ranges, and do not need further cleaning to derive important conclusions. 

<h1 style="text-align:center;"> Analytical Techniques </h1>

<b style="font-size: 125%;"> Diagnostic Analytics </b>

Diagnostic analytics is a method in data analysis that digs into historical data to determine why certain events occurred, addressing the question, “Why did this happen?”. It employs techniques such as drill down, data mining, correlations, and regression to reveal underlying causes behind observed trends or anomalies (Investopedia, n.d.; NetSuite, 2021). The value of diagnostic analytics lies in its capacity to uncover root causes and contributing factors, such as changes in customer behavior, operational inefficiencies, or external influences, which empowers businesses to make targeted improvements, prevent issues from reoccurring, and refine strategies for better outcomes (Investopedia, n.d.; NetSuite, 2021).


<div align="center">

<b style="font-size: 110%;"> Heatmap </b>

<img src="image.png">

</div>

The correlation matrix above, which was created using python's library seaborn, displays the different correlation values among all columns in the table. Focusing on employee turnover, which is the "left" column, we see that the columns with the highest correlation to this column are satisfaction level, work accidents, time spent at the company, and salary. Columns with high correlation help derive stronger and more confident insights that demonstrate more value to stakeholders. 

</br>


<b style="font-size: 125%;"> Descriptive Analytics </b>

Descriptive analytics refers to the process of examining historical data to answer the fundamental question: “What happened?” By aggregating, organizing, and visualizing past information, such as sales figures, customer transactions, or operational metrics (Investopedia, n.d.; NetSuite, 2021). This approach helps stakeholders track trends, identify areas of inefficiency, and benchmark results against goals or industry standards. The importance of descriptive analytics lies in its ability to transform raw, complex datasets into digestible insights, enabling decision makers to establish a factual basis for deeper analysis or strategy development (NetSuite, 2021).

<div align="center">

<b style="font-size: 110%;"> Histogram </b> </br>

<img src="image-1.png">

</div>

The histograms above show us different trends compared to employee turnover. 

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

 

