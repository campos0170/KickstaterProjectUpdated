from dash import dcc, html
from eda import eda_visuals
import pandas as pd


df1 = pd.read_csv("data/cleaned_kickstarter.csv")
df2 = pd.read_csv("data/edadataset.csv")

def eda_tab_layout():
    return [
        dcc.Graph(figure=eda_visuals.log_pledged_scatter(df2)),
        dcc.Graph(figure=eda_visuals.pledge_success_ratio(df2)),
        dcc.Graph(figure=eda_visuals.success_rate_duration(df2)),


        dcc.Graph(figure=eda_visuals.distribution_of_pledge(df2))
    ]

def predict_tab_layout(df):
    return html.Div([
        html.P("Enter Campaign Details:"),
        #Numberic Inputs
        html.Label("Funding Goal Amount (USD)"),
        dcc.Input(id="input-goal",type="number",min=0,step=100,value=1000),

        html.Label("Main Category"),
        dcc.Dropdown(id="input-category-name",
                  options=[{"label":c,"value":c} for c in sorted(df['category_name'].dropna().unique())],
                  value=df['category_name'].unique()[0],
                  placeholder="Select Category"),

        html.Label("Subcategory:"),
        dcc.Dropdown(id="input-subcategory",
                  options=[{"label":v,"value":v} for v in sorted(df['subcategory'].unique())],
                  placeholder="Select Subcategory"),
        html.Label("Currency:"),
        dcc.Dropdown(id="input-currency",
                  options=[{"label":s,"value":s} for s in sorted(df["currency"].unique())],
                  placeholder="Select Currency",
                  value=df["currency"].unique()[0]),
        html.Label("City:"),
        dcc.Dropdown(
            id="input-city",
            options=[{"label": c, "value": c} for c in df["city"].dropna().unique()],
            value=df["city"].dropna().unique()[0],
            placeholder="Enter City Name",
            style={"width": "100"}
        ),

        html.Label("Launch Month:"),
        dcc.Dropdown(id="input-month",
                  options=[{"label":str(m),"value":m} for m in range(1,13)],
                  placeholder="Select Month"),
        html.Label("Country:"),
        dcc.Dropdown(id="input-country",
                  options=[{"label": c, "value": c} for c in sorted(df['country_displayable_name'].unique())],
                  value=df['country_displayable_name'].unique()[0],
                  placeholder="Select Country"),

        # Binary Input
        html.Label("Staff Pick"),
        dcc.RadioItems(id="input-staff_pick",options=[
            {"label":"Yes","value":1},
            {"label":"No","value":0}
        ],inline=True,value=0),
        html.Br(),
        html.Button("Predict Success",id="predict-button",n_clicks=0),
        html.H4(id="prediction-output",style={"marginTop":"20px","color":"#007BFF"})
    ],style={"width":"50%","margin":"auto"})


def get_layout(df):
    return html.Div([
        html.H1("Kickstarter Success Prediction",style={"textAlign":"center"}),
        dcc.Tabs([
        dcc.Tab(label="Exploratory Data Analysis",children=eda_tab_layout()),
        dcc.Tab(label="Prediction",children=predict_tab_layout(df)),
            ])
    ])



