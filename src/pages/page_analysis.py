from dash import html, dcc


def get_analysis_page():
	return html.Div(
		[
			html.H1("Analysis"),
			dcc.Markdown("""
				We analyse data yipee
			"""),
			html.H2("Understanding the data"),
		],
	)
