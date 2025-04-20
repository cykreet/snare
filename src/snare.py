import os
import numpy as np
import dash_bootstrap_components as dbc

from dash import Dash, Input, Output, State, dcc, html
from keras import models
from flask import Flask
from helpers.evaluate_grade import evaluate_grade
from pages.page_404 import get_404_page
from pages.page_analysis import get_analysis_page
from pages.page_main import get_main_page

server = Flask(__name__)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

file_dir = os.path.dirname(__file__)

model = models.load_model(os.path.join(file_dir, "coral.h5"))

app.title = "Student Evaluator"
app.layout = [
	dcc.Location(id="url", refresh=False),
	html.Link(rel="stylesheet", href="styles.css"),
	html.Div(
		[
			html.A(
				children=[dbc.Badge("SNARE.", color="primary", style={"fontSize": "1.4em", "userSelect": "none"})],
				href="/",
			),
			dbc.Nav(
				id="nav-items",
				pills=True,
				style={"marginTop": "auto", "gap": "1em"},
			),
		],
		style={
			"display": "flex",
			"flexDirection": "row",
			"justifyContent": "space-between",
			"alignItems": "center",
			"marginTop": "2em",
		},
		className="page-container",
	),
	html.Div(
		children=[html.Div(id="page-content", children=get_main_page())],
		className="page-container",
		style={"marginTop": "2em"},
	),
]


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_content(pathname):
	if pathname == "/analysis":
		return get_analysis_page()
	else:
		return get_main_page() if pathname == "/" else get_404_page()


@app.callback(Output("nav-items", "children"), Input("url", "pathname"))
def get_nav_items(pathname):
	if pathname == "/analysis":
		return [
			dbc.NavItem(
				dbc.NavLink("Home", href="/"),
			),
			dbc.NavItem(
				dbc.NavLink("Analysis", href="/analysis", active=True),
			),
		]
	else:
		return [
			dbc.NavItem(
				dbc.NavLink("Home", href="/", active=True),
			),
			dbc.NavItem(
				dbc.NavLink("Analysis", href="/analysis"),
			),
		]


@app.callback(
	[
		Output("eval-result", "style"),
		Output("prediction", "children"),
		Output("prediction", "style"),
		Output("eval-message", "children"),
		Output("actions", "children"),
	],
	Input("evaluate_button", "n_clicks"),
	[
		State("study-time", "value"),
		State("absences", "value"),
		State("tutoring", "value"),
		State("parent-support", "value"),
		State("extra", "value"),
		State("sports", "value"),
		State("music", "value"),
		State("volunteer", "value"),
	],
)
def on_evaluate_click(n, study_time, absences, tutoring, parent_support, extra, sports, music, volunteer):
	if (
		n is None
		or n == 0
		or study_time is None
		or absences is None
		or tutoring is None
		or parent_support is None
		or extra is None
		or sports is None
		or music is None
		or volunteer is None
	):
		return (
			{"display": "block"},
			"?",
			{
				"border": "2px solid gray",
				"fontWeight": "bold",
				"paddingLeft": "0.2em",
				"paddingRight": "0.2em",
				"borderRadius": "0.1em",
			},
			None,
			"No recommended actions.",
		)

	def to_binary(value):
		return 1 if value == "1" else 0

	input_features = np.array(
		[
			[
				float(study_time),
				float(absences),
				to_binary(tutoring),
				int(parent_support),
				to_binary(extra),
				to_binary(sports),
				to_binary(music),
				to_binary(volunteer),
			]
		]
	)

	# todo: outputs not higher than C
	prediction = model.predict(input_features)
	predClass = np.sum(prediction > 0.5, axis=1)
	print(prediction)
	print(predClass)
	evaluation = evaluate_grade(
		predClass[0], study_time, absences, tutoring, parent_support, extra, sports, music, volunteer
	)

	if evaluation["actions"]:
		action_children = [
			html.Div(
				[html.Span(action["title"], style={"font-weight": "bold"}), html.Span(action["message"])],
				style={
					"padding": "1em",
					"border": "2px solid gray",
					"display": "flex",
					"flex-direction": "column",
					"border-radius": "0.4em",
					"gap": "0.4em",
				},
			)
			for action in evaluation["actions"]
		]
	else:
		action_children = "No recommended actions."

	return (
		{"display": "block"},
		evaluation["grade"],
		{
			"color": evaluation["grade_colour"],
			"border": f"2px solid {evaluation['grade_colour']}",
			"fontWeight": "bold",
			"paddingLeft": "0.2em",
			"paddingRight": "0.2em",
			"borderRadius": "0.1em",
		},
		evaluation["grade_message"],
		action_children,
	)


if __name__ == "__main__":
	# https://render.com/docs/environment-variables#all-runtimes
	app.run(host="0.0.0.0", debug=os.environ.get("RENDER", "false") != "true")
