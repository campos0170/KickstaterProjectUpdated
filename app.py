import dash
from dash import html
import pandas as pd
from componenents.layout import get_layout
from componenents.callbacks import register_callbacks
#
# Data

df = pd.read_csv("data/cleaned_kickstarter.csv")
# App Initialization

app = dash.Dash(__name__)
app.title = "Kickstarter Success Dashboard"

# App Layout

app.layout = get_layout(df)

# Register Callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)



