\## Student Exam Analysis



A Python project for exploring and analyzing student exam scores. This repository performs data preprocessing, statistical analysis, and creates insightful visualizations to understand trends, distributions, and relationships between different academic performance metrics. The analysis highlights how factors like gender and test preparation courses may influence scores, providing actionable insights for educators and researchers.



---



\## Features



\*\*Data Preprocessing:\*\*  

&nbsp; - Displays summary statistics for all numeric columns  

&nbsp; - Identifies missing values to ensure data quality  



\*\*Statistical Analysis:\*\*  

&nbsp; - Computes key metrics: mean, standard deviation, skewness, and kurtosis  

&nbsp; - Interprets distribution shapes (e.g., right-skewed, leptokurtic) for better understanding  



\- \*\*Visualizations:\*\*  

&nbsp; - \*\*Scatter plots\*\* of Math vs Reading scores, colored by gender with regression line and correlation coefficient  

&nbsp; - \*\*Bar plots\*\* showing average Writing scores grouped by test preparation course  

&nbsp; - \*\*Correlation heatmaps\*\* to identify relationships between Math, Reading, and Writing scores  

&nbsp; - \*\*Histograms\*\* of Math scores with mean lines for quick visual insights  



&nbsp;\*\*Interpretation:\*\*  

&nbsp; - Provides plain-language explanations of statistical moments to aid understanding of score distributions and potential performance patterns  



---



\## Dataset



The project expects a CSV file named `data.csv` with at least the following columns:  



\- `gender`  

\- `math score`  

\- `reading score`  

\- `writing score`  

\- `test preparation course`  





---



\## Plots Generated



-relational\_plot.png — Scatter plot of Math vs Reading scores with correlation



\-categorical\_plot.png — Bar plot of average Writing scores by test preparation



\-statistical\_heatmap.png — Correlation heatmap of all exam scores



\-math\_score\_histogram.png — Histogram of Math scores with mean line



These plots provide a visual summary of performance trends and relationships, helping identify patterns in student achievement.



---





\## Conclusion



This project demonstrates a structured approach to exploratory data analysis (EDA) for student exam scores. By combining statistical metrics with clear visualizations, it provides a deeper understanding of the dataset, highlights trends and correlations, and interprets data distributions in a meaningful way. The workflow and methods used here can be easily adapted for analyzing other academic or performance datasets.

