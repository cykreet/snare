from dash import html, dcc


def get_analysis_page():
	return html.Div(
		[
			html.H1("Analysis"),
			dcc.Markdown("""
				This page contains a detailed breakdown of the student data and how it was collected and transformed to train classification models, which were then evaluated for their performance.
			"""),
			html.H2("Problem Statement"),
			html.H2("Hypthesis Generation"),
			html.P("Initially we had formulated the following hypothesis:"),
			dcc.Markdown("""
				- **Study Time and Academic Performance**: Students who spend more hours studying every week are more likely to achieve higher Grade Class categories compared to those with lower study time.
				- **The impact of Absence when it comes to grades**: The higher number of absences are associated with lower GradeClass categories, this indicates a negative impact on academic performance.
				- **Extracurricular activities and academic success**: Participation in extracurricular activities positively correlates with higher GradeClass categories, this suggests that engagement in these activities supports academic performance.
				- **Parental support and student outcomes**: Higher levels of parental support are associated with better GradeClass categories, indicating that parental involvement is a significant factor in academic success.
				- **Tutoring effectiveness**: Students who receive tutoring are more likely to achieve higher GradeClass categories compared to those who do not, suggesting that tutoring is an effective for improving grades.
			"""),
			html.H2("Understanding The Data"),
			dcc.Markdown("""
				In the initially provided student dataset we have 15 total columns.
								
				| Column | Description |
				| --- | --- |
				| `StudentID` | Unique identifier for each student |
				| `Age` | Age of students from 15 to 18 |
				| `Gender` | Gender of students, `0` represents Male and `1` represents Female |
				| `Ethnicity` | Ethnicity of students from `0` to `3` |
				| `ParentalEducation` | Parental education level from `0` to `4` |
				| `StudyTimeWeekly` | Hours of study per week |
				| `Absences` | Number of absences during the school year from `0` to `30` |
				| `Tutoring` | Binary variable indicating whether the student is being tutored |
				| `ParentalSupport` | Parental support level from `0` to `4` |
				| `Extracurricular` | Binary variable indicating whether the student is involved in extracurricular activities |
				| `Sports` | Binary variable indicating whether the student is involved in sports |
				| `Music` | Binary variable indicating whether the student is involved in music |
				| `Volunteering` | Binary variable indicating whether the student is involved in volunteering |
				| `GPA` | GPA of the student |
				| `GradeClass` | Grade class of the student based on the GPA, from `0` to `4` |

				---
	
				`GradeClass` is determined to be the target variable for the classification models.
			"""),
			html.H2("Preparing and Loading Data"),
			html.H2("Exploratory Data Analysis"),
			html.H2("Data Cleaning"),
			html.H2("Evaluation Metrics"),
			html.H2("Feature Engineering"),
			html.H2("Model Building"),
			dcc.Markdown(
				"For this solution, we employed the use of 3 different classification models: **Logistic Regression**, **Random Forest**, and **XGBoost**. The models were trained on the training dataset and evaluated on the validation dataset, and the best model was selected based on the evaluation metrics."
			),
			html.H2("Model Evaluation"),
		],
	)
