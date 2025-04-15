import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from flask import Flask
from pages.page_404 import get_404_page
from pages.page_analysis import get_analysis_page
from pages.page_main import get_main_page

server = Flask(__name__)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

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


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
