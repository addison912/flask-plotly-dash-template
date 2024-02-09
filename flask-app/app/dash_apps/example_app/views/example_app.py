# This is an example "dashboard" component which will be displayed if the user is logged in.

from dash import dcc
from dash import html
from dash import dash_table
import numpy as np
import pandas as pd

from ..data import create_dataframe
from ..layout import html_layout


# Load DataFrame
df = create_dataframe()


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table


# Create Layout
dashboard = html.Div(
    children=[
        dcc.Graph(
            id="histogram-graph",
            figure={
                "data": [
                    {
                        "x": df["complaint_type"],
                        "text": df["complaint_type"],
                        "customdata": df["key"],
                        "name": "311 Calls by region.",
                        "type": "histogram",
                    }
                ],
                "layout": {
                    "title": "NYC 311 Calls category.",
                    "height": 500,
                    "padding": 150,
                },
            },
        ),
        create_data_table(df),
    ],
    id="dash-container",
)
