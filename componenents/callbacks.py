from dash import Input, Output, State
from model.predict import predict_success
import numpy as np

feature_list = [
    'goal', 'log_goal',
    'category_name', 'subcategory', 'currency',
    'country_displayable_name', 'city', 'month',
    'staff_pick'
]
def register_callbacks(app):
    @app.callback(
        Output("prediction-output", "children"),
        Input("predict-button","n_clicks"),
        State("input-goal","value"),
        State("input-category-name","value"),
        State("input-subcategory","value"),
        State("input-currency","value"),
        State("input-country","value"),
        State("input-city","value"),
        State("input-month","value"),
        State("input-staff_pick","value")
    )

    def update_prediction(n_clicks,goal,category,subcategory,currency,country,city,month,staff_pick):
        if n_clicks is None:
            return ""
        input_dict = {
            "goal": goal,
            "log_goal": np.log1p(goal) if goal is not None else 0,
            "category_name": category,
            "subcategory": subcategory,
            "currency": currency,
            "country_displayable_name": country,
            "city": city,
            "month": month,
            "staff_pick": staff_pick

        }
        pred, prob = predict_success(input_dict)
        return f"Predicted Outcome: {'Success' if pred else 'Failure'} - Probability: {prob}"



