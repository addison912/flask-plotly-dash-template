"""Instantiate a Dash app."""
import dash
import os
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from ..dash_config import Dash


from flask_login import logout_user, current_user
from app.models import User
from app.lib import auth

from .layout import html_layout

from .views.example_app import dashboard

base_url = os.environ.get("BASE_URL")

def init_dash(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/example-app/',
        external_stylesheets=[
            "/static/css/index.css",
            "https://fonts.googleapis.com/css?family=Lato",
            dbc.themes.BOOTSTRAP
        ],
    )

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Main Layout
    dash_app.layout = html.Div([
        html.Div(id="user_info"),
        dcc.Location(id='url', refresh=False),
        dcc.Location(id='redirect', refresh=True),
        dcc.Store(id='login-status', storage_type='session'),
        dcc.Store(id='user', storage_type='session'),
        html.Br(),
        html.Br(),
        html.Div(id='page-content'),
    ])
    
    login_redirect = html.Div(
        dcc.Location(id="auth_url", href='/login', refresh=True)
    )

    # Display welcome message
    @dash_app.callback(Output('user_info', 'children'),
                       [Input('url', 'pathname')])
    def show_welcome(url):
        user = auth.get_user()
        if user and auth.is_authenticated:
            welcome_message = html.H1(
                f"Welcome to your dashboard {user.fname}!", id="welcome_message")
            return welcome_message
        else:
            return login_redirect

    # Main router
    # If the user is authenticated the router returns the dashboard otherwise it returns the logout page which promts the user to log back in.
    @dash_app.callback(Output('page-content', 'children'), Output('redirect', 'pathname'),
                       [Input('url', 'pathname')])
    def display_page(pathname):
        ''' callback to determine layout to return '''
        view = None
        url = dash.no_update

        if pathname == '/logout':
            if current_user.is_authenticated:
                logout_user()
                view = login_redirect
        elif auth.is_authenticated():
            view = dashboard
        else:
            view = login_redirect
        return view, url

    return dash_app.server
