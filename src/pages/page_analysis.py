import pandas as pd

from dash import html, dcc, dash_table


def get_analysis_page():
	metric_data = [
		{"Model": "Logistic Regression", "Accuracy": 0.81, "RMSE": 0.44},
		{"Model": "Random Forest", "Accuracy": 0.79, "RMSE": 0.48},
		{"Model": "XGBoost", "Accuracy": 0.77, "RMSE": 0.48},
		{"Model": "Deep Learning (Coral)", "Accuracy": 0.82, "RMSE": 0.42},
	]

	df = pd.DataFrame(metric_data)

	return html.Div(
		[
			html.H1("Analysis"),
			dcc.Markdown("""
				This page contains a detailed breakdown of the student data and how it was collected and transformed to train classification models, which were then evaluated for their performance.
			"""),
			html.H2("Understanding The Data"),
			dcc.Markdown("""
				In the initially provided student dataset we have 15 total columns.
								
				| Column | Data Type | Statistical Type | Description | Values | Analysis |
				| --- | --- | --- | --- | --- | --- |
				| `StudentID` | `int64` | Nominal (Categorical) | Unique identifier for each student | Unique integers | Unique identifier, insignificant for analysis |
				| `Age` | `int64` | Discrete Ordinal | Age of students | 15, 16, 17, 18 | Age distribution, correlation with performance metrics |
				| `Gender` | `int64` | Binary Categorical | Gender of students | `0` (Male), `1` (Female) | Gender distribution, performance differences by gender |
				| `Ethnicity` | `int64` | Nominal (Categorical) | Ethnicity of students | `0` to `3` | Demographic analysis, check for performance gaps |
				| `ParentalEducation` | `int64` | Ordinal | Parental education level | `0` to `4` | Impact on student performance, socioeconomic indicator |
				| `StudyTimeWeekly` | `float64` | Continuous | Hours of study per week | Positive real numbers | Distribution, correlation with GPA, optimal study time |
				| `Absences` | `int64` | Discrete Count | Number of absences during the school year | `0` to `30` | Impact on performance, identify at-risk students |
				| `Tutoring` | `int64` | Binary Categorical | Whether student receives tutoring | `0` (No), `1` (Yes) | Effectiveness of tutoring on performance |
				| `ParentalSupport` | `int64` | Ordinal | Parental support level | `0` to `4` | Impact on student outcomes, interaction with other factors |
				| `Extracurricular` | `int64` | Binary Categorical | Student involvement in extracurricular activities | `0` (No), `1` (Yes) | Impact on academic performance |
				| `Sports` | `int64` | Binary Categorical | Student involvement in sports | `0` (No), `1` (Yes) | Relationship with GPA, time management |
				| `Music` | `int64` | Binary Categorical | Student involvement in music | `0` (No), `1` (Yes) | Relationship with GPA, cognitive benefits |
				| `Volunteering` | `int64` | Binary Categorical | Student involvement in volunteering | `0` (No), `1` (Yes) | Impact on personal development and academics |
				| `GPA` | `float64` | Continuous | GPA of the student | Typically 0.0-4.0 | Key outcome variable, distribution analysis |
				| `GradeClass` | `float64` | Ordinal | Grade class based on GPA | `0` to `4` | Alternative categorical outcome variable |

				---
	
				The dataset contains `2392` rows, while `GradeClass` is determined to be the target variable for the classification models.
			"""),
			html.H2("Exploratory Data Analysis"),
			html.H3("Univariate Analysis"),
			dcc.Markdown("""
				We have performed a univariate analysis to better understand the distribution and characteristics of our target variable. Focusing primarily on the grade class attribute, this process involves both descriptive statistics and visualization techniques. Below are the steps we took: 

				- **Overview:** we made use of the info() function to inspect the dataset's internal structure. This involved checking for null values and data types. 
				- **Descriptions:** the describe() function was used to provide statistical values including count, mean, and quartiles. This allowed for a quick overview of central tendency and potential outliers. 
				- **Outlier detection:** we made use of boxplots to visually identify potential outliers and values that were not within the interquartile range. We supplemented this visualisation with programmed calculations to explicitly find and label outliers. 
				- **Distribution:** our second visualisation was a histogram to illustrate the distribution within the grade class attribute. This helped identify the frequency of grade class ranges. 

				This analysis provided a comprehensive overview of students' performance. It helped identify skewness in our data and highlighted the most populous grade class. 
			"""),
			html.Img(src="/assets/graphs/univariate/analysis.png"),
			html.H3("Bivariate Analysis"),
			html.P(
				"The relationship between continuous columns (StudyTimeWeekly and Absences) and the target variable “GradeClass”. These plots visualized that the distribution of study time and absences varied across the different grade categories. For example, students with higher grades (like A or B) tend to study more or have fewer absences."
			),
			html.Img(src="/assets/graphs/bivariate/predictors.png"),
			html.Img(src="/assets/graphs/bivariate/predictors2.png"),
			html.P(
				"Heatmap for cross-tabulation visualises how grade categories are distributed across different levels of parental support. It visually highlighted any trends, such as whether higher parental support corresponded to better grades."
			),
			html.Img(src="/assets/graphs/bivariate/heatmap.png"),
			html.H2("Data Cleaning"),
			dcc.Markdown("""
				**Checking for Data Quality Issues:**

				We have also checked if our dataset contains any missing values or duplicate entries using the duplicate () and isnull() functions. This cleans our data and ensures it remains consistent bu avoiding error or bias in our ML models. 

				**Outlier Detection and Removal:**

				We used the Interquartile Range (IQR) method to detect and remove any outliers that are higher or lower than most data points in our dataset. 
			"""),
			html.H2("Feature Engineering"),
			dcc.Markdown("""
				**Target Variable Transformation (Creating Grade Categories):**

				For the target column “GradeClass” to have more accurate records we mapped the values in the “GPA” column to the target column where we converted the mapped data into ordinal data. We used a function which transformed the data into a new categorical variable called “GradeClass”. This function grouped students into five categories based on their GPA: 
				
				- **A (Excellent)**: GPA of 3.5 and above.
				- **B (Good)**: GPA between 2.5 and 3.5.
				- **C (Average)**: GPA between 2.0 and 2.5.
				- **D (Below Average)**: GPA between 0.5 and 2.0.
				- **F (Fail)**: GPA below 0.5.
								
				**Removing Irrelevant or Redundant Features:**

				We removed all the columns that did not influence the target variable “GradeClass” such as identifiers (like Student ID), demographic data (like age, gender, and ethnicity). We also removed the “GPA” columns because it can also be perceived as output data which can't be used for training our ML models. These changes simplify our dataset and focuses on the important features. 
			"""),
			html.H2("Model Building"),
			dcc.Markdown(
				"For this solution, we employed the use of 3 different classification models: **Logistic Regression**, **Random Forest**, and **XGBoost**. The models were trained on the training dataset and evaluated on the validation dataset, and the best model was selected based on the evaluation metrics."
			),
			html.H3("Logistic Regression"),
			dcc.Markdown("""
				Logistic regression is a statistical method used for binary classification. It predicts the probability that a given inputs belongs  to a particular class this can 0 or 1. Unlike linearreg regression, which predicts continuous values, logistic regression uses the logistic(sigmoid) function to map predictions to probabilities between 1 and 0.
								
				The confusion matrix shows the number of predictions for each actual vs. predicted class pair. Normalizing by row (cm.sum(axis=1)) converts counts to proportions, making it easier to see the model's performance for each class. The plot visualizes where the model is making errors (e.g., if it often predicts GradeClass 3 instead of 2). 
			"""),
			html.Img(src="/assets/graphs/log-confusion.png", width=500),
			html.H3("Random Forest"),
			dcc.Markdown("""
				This is a supervised machine learning algorithm which we will use for the classification of students regarding our target attribute, grade class. We tested for accuracy and applied measures to test the effect on accuracy of both changing the number of trees and the number of attributes. We train, test, and rebuild the model to find the highest achievable accuracy using the steps below.  

				- **Preparation**: this is where we import our dataset and get a quick glance over it. We also pick out our target attribute as it will be isolated from the other attributes as seen in the steps to follow 

				- **Training**, testing, and fitting: this is where we introduced the random forest classifier function. We split the data into thirds with the training set taking up two thirds and the test set only taking a third of our data. We have also made use of a 42 random state to randomise the executions of the model in each iteration of the algorithm. This allows for maximum achievable accuracy with lowered chance of the model underperforming. Finally, we fit the model to the training set to start the categorisation. 

				- **Evaluation**: we have made use of confusion matrix and classification report to assess the model’s accuracy and performance, all with precision, recall f-1 score and others all bundled in. 

				This is all because the model handles categorical targets well. It excels at identifying the most influential attribute all while greatly reducing overfitting due to its ensemble and averaging nature. All while handling various data types well. 
			"""),
			html.Img(src="/assets/graphs/forest-confusion.png", width=500),
			html.H3("XGBoost"),
			dcc.Markdown("""
				XGBoost is a performant and flexible gradient boosting implementation, which can be utilised for various tasks ranging from tabular data to large-scale datasets. It allows for faster iteration and experimentation with more features and hyperparameters.

				In order to utilise XGBoost for multi-class classifications problems, such as the one expressed in this project, we use the `multi:softprob` objective, which outputs a vector of class probabilities. Additionally, we configure our `num_class` parameter to specify the number of classes in our target variable (which is `5`). This dataset also required assigning sample weights to adjust for the imbalanced data, by setting the `sample_weight` parameter when training in order to balance the importance of underrepresented classes.

				Model parameters are then further tuned with Bayesian optimisation within the defined search space to determine the optimal parameters, which ultimately yields an accuracy of 77%. This normalised confusion matrix provides a visual overview of the model's performance in predicting different classes.
			"""),
			html.Img(src="/assets/graphs/xgboost-confusion.png", width=500),
			html.H3("Deep Learning (CORAL)"),
			html.P(
				'The ANN model allows us to take multiple inputs and predict how well they \'re likely to perform in terms of the "GradeClass" or ordinal values. This model focuses on the natural ranking between the “GradeClass” values because it can capture non-linear patterns and interactions between variables more effectively than simpler models. With the help of the CORAL technique the ANN model can be guided to treat predictions as ordered rather than flat categories by transforming the ordinal target variable values into a series of binary threshold values. This leads to more realistic and informed predictions.'
			),
			html.Img(src="/assets/graphs/deep-confusion.png", width=500),
			html.H2("Model Evaluation"),
			dcc.Markdown("""
				Directly comparing the accuracy and root mean squared error (RMSE), we can evaluate the performance of the models.
			"""),
			dash_table.DataTable(
				columns=[{"name": col, "id": col} for col in df.columns],
				data=df.to_dict("records"),
				style_header={
					"backgroundColor": "#2a3f5f",
					"color": "white",
					"fontWeight": "bold",
					"textAlign": "center",
				},
				style_table={
					"maxWidth": "700px",
					"margin": "0 auto",
					"overflow": "hidden",
				},
			),
			dcc.Markdown(
				"From the metrics listed above, model performance is marginally similar. The deep learning model following the CORAL method, shows the highest accuracy, with the lowest RMSE. This model is what we've decided to utilise in our student evaluator tool."
			),
		],
	)
