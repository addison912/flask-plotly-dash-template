import os
from dash import html
import dash_bootstrap_components as dbc
base_url = os.environ.get("BASE_URL")

# logout
logout = html.Div(
    [html.Div([
        html.H2(
              'Please login to view this app.',
              className="text-center"
              ),

        dbc.Button(
            "Login",
            href=f"{base_url}/login",
            external_link=True,
            color="primary",
            className="logout-button"
        ),
    ],
        className="w-100 d-flex justify-content-center flex-column align-items-center"),
    ])
