import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        # represents the URL bar, doesn't render anything
        dcc.Location(id="url", refresh=False),
        dcc.Link("Navigate to index", href=app.get_relative_path("/")),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href=app.get_relative_path("/page-2")),
        html.Br(),
        dcc.Link('Navigate to "/page-3"', href=app.get_relative_path("/page-3")),
        # content will be rendered in this element
        html.Div(id="page-content"),
    ]
)


@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")],
)
def display_page(pathname):
    pathname = app.strip_relative_path(pathname)
    return html.Div([html.H3("You are on page {}".format(pathname or "index"))])


if __name__ == "__main__":
    app.run_server(debug=True)