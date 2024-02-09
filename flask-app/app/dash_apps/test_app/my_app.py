from ..dash_config import Dash
from dash import html, dcc
from dash.dependencies import Input, Output
from flask_login import current_user
from app.lib import auth
permitted_email_domains = ["gmail.com"]

app_layout = html.Div([
    html.Div(id="welcome"),
    html.Div(id="protected_content"),
    dcc.Location(id='url', refresh=False),
])

protected_el = html.H1('Only users with an email in the permitted_email_domains list can see this element',
                       id="protected_element", className="text-center")


login_redirect = html.Div(
    dcc.Location(id="auth_url", href='/login', refresh=True)
)
 

def init_dash(server):
    # Change the 'routes_pathname_prefix' to change the path where the app is served
    dash_app = Dash(server=server, routes_pathname_prefix="/demo/",)
    dash_app.layout = app_layout

    # Protected element
    @dash_app.callback(Output('protected_content', 'children'),
                       [Input('url', 'pathname')])
    def protected_element(url):
        # elements can also be protected by user.email, user.role, etc. (see user model)
        if auth.is_authenticated() and current_user.get_domain in permitted_email_domains:
            return protected_el
        else:
            return login_redirect
        
    # Display welcome message
    @dash_app.callback(Output('welcome', 'children'),
                       [Input('url', 'pathname')])
    def show_welcome(children):
        if auth.is_authenticated():
            user = auth.get_user()
            message = html.H1(f"Welcome to your dashboard {user.fname}!", id="welcome", className="text-center")
            return message
        else:
            return login_redirect

    return dash_app.server


if __name__ == "__main__":
    app = Dash(__name__)
    app.run_server(debug=True)
