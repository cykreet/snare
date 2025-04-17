from dash import html, dcc


def get_analysis_page():
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
