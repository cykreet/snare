import os
import dash_bootstrap_components as dbc
import pandas as pd

from dash import html

file_dir = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(file_dir, "../students.csv"))


def get_main_page():
	return html.Div(
		[
			dbc.Row(
				[
					dbc.Col(
						[
							html.H1("Student Evaluator"),
							html.P(
								"Welcome to the snare student evaluator. This tool has been trained on a dataset of students which consists of their academic performance, extracirricular activities, and academic/parental support systems.",
							),
							html.P(
								[
									"View the ",
									html.A(children="Analysis", href="/analysis"),
									" page for a detailed breakdown of the data.",
								]
							),
							dbc.Form(
								[
									html.P("Enter a student's information below to get started."),
									html.Div(
										[
											dbc.Label("Age", html_for="age"),
											dbc.Input(type="number", id="age", placeholder="Enter age"),
										]
									),
									html.Div(
										[
											dbc.Label("Gender", html_for="gender"),
											dbc.Select(
												id="gender",
												options=[
													{
														"label": "Male",
														"value": 0,
													},
													{"label": "Female", "value": 1},
												],
											),
										]
									),
									html.Div(
										[
											dbc.Label("Etnicity", html_for="ethnicity"),
											dbc.Select(
												id="ethnicity",
												options=[
													{
														"label": "Caucasion",
														"value": 0,
													},
													{
														"label": "African American",
														"value": 1,
													},
													{
														"label": "Asian",
														"value": 2,
													},
													{
														"label": "Other",
														"value": 3,
													},
												],
											),
										]
									),
									html.Div(
										[
											dbc.Label("Study Time (Weekly)", html_for="study-time"),
											dbc.Input(
												type="number", id="study-time", placeholder="Enter weekly study time"
											),
											dbc.FormText(
												"Student's weekly study time in hours",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Absences", html_for="abences"),
											dbc.Input(
												type="number", id="absences", placeholder="Enter number of absences"
											),
										]
									),
									html.Div(
										[
											dbc.Label("Tutoring", html_for="tutoring"),
											dbc.Select(
												id="tutoring",
												options=[
													{"label": "Yes", "value": 1},
													{
														"label": "No",
														"value": 0,
													},
												],
											),
											dbc.FormText(
												"Is the student currently enrolled in tutoring services?",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Parental Support", html_for="parent-support"),
											dbc.Select(
												id="parent-support",
												options=[
													{
														"label": "None",
														"value": 0,
													},
													{
														"label": "Low",
														"value": 1,
													},
													{
														"label": "Moderate",
														"value": 2,
													},
													{
														"label": "High",
														"value": 3,
													},
													{"label": "Very High", "value": 4},
												],
											),
											dbc.FormText(
												"What is the student's level of parental support?",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Extracurricular", html_for="extra"),
											dbc.Select(
												id="extra",
												options=[
													{"label": "Yes", "value": 1},
													{
														"label": "No",
														"value": 0,
													},
												],
											),
											dbc.FormText(
												"Does the student participate in any extracurricular activities?",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Sports Participation", html_for="sports"),
											dbc.Select(
												id="sports",
												options=[
													{"label": "Yes", "value": 1},
													{
														"label": "No",
														"value": 0,
													},
												],
											),
											dbc.FormText(
												"Does the student participate in any sports activities?",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Musical Participation", html_for="music"),
											dbc.Select(
												id="music",
												options=[
													{"label": "Yes", "value": 1},
													{
														"label": "No",
														"value": 0,
													},
												],
											),
											dbc.FormText(
												"Does the stdent participate in any musical activities?",
												color="secondary",
											),
										]
									),
									html.Div(
										[
											dbc.Label("Volunteering", html_for="volunteer"),
											dbc.Select(
												id="volunteer",
												options=[
													{"label": "Yes", "value": 1},
													{
														"label": "No",
														"value": 0,
													},
												],
											),
											dbc.FormText(
												"Does the student participate in any volunteering activities?",
												color="secondary",
											),
										]
									),
									# html.Div(
									# 	[
									# 		dbc.Label("GPA", html_for="gpa"),
									# 		dbc.Input(type="number", id="gpa", placeholder="Enter GPA"),
									# 	]
									# ),
									dbc.Button("Evaluate Student", color="primary", disabled=True),
								],
								className="form-spacer",
							),
						]
					),
					dbc.Col(
						html.Div(
							[
								html.H1(
									[
										html.Span(
											children="A",
											id="prediction",
											style={
												"color": "green",
												"fontWeight": "bold",
												"border": "2px solid green",
												"paddingLeft": "0.2em",
												"paddingRight": "0.2em",
												"borderRadius": "0.1em",
											},
										),
									],
									style={"marginBottom": "0.3em"},
								),
								html.Span("This student shows potential for good academic performance."),
							]
						)
					),
				],
				style={"marginTop": "2em", "gap": "5em"},
			),
		]
	)
