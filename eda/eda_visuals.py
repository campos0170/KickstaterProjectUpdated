import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go


def plot_success_by_category(df):
    category_success = df.groupby("category_name")["success"].mean().sort_values(ascending=False)
    return px.bar(category_success, title="Success Rate by Category", labels={"value":"Success Rate", "index":"Category"})

def plot_goal_distribution(df):
    return px.histogram(df, x="goal", nbins=50, title="Goal Distribution", log_y=True)

def goal_amount_boxplot(df):
    return px.box(df, x="category_name", y="goal", title="Distribution of Goal Amount by Category")

def logplot_scatterplot(df):
    return px.scatter(df, x="log_goal", y="goal", title="Log Goal vs Goal by Success", color="success")




def pledge_success_ratio(df):
    # Select top 10 categories by count
    top_categories = df['category_name'].value_counts().head(10).index
    filtered = df[df['category_name'].isin(top_categories)]

    # Compute 95th percentile to trim extreme outliers
    upper_limit = np.percentile(filtered["pledged_success_ratio"], 95)

    fig = go.Figure(data=[
        go.Box(
            y=filtered["pledged_success_ratio"],
            x=filtered["category_name"],
            boxpoints="outliers",
            pointpos=-1.8,
            quartilemethod="exclusive",
            marker=dict(color="#007BFF"),
            line=dict(width=1.5)
        )
    ])

    fig.update_layout(
        title={
            'text': "Pledge Success Ratio by Top 10 Categories (Clipped to 95th Percentile)",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            "font": dict(size=18, color="#343a40")
        },
        xaxis=dict(
            title="Category",
            titlefont=dict(size=14),
            tickangle=45,
            tickfont=dict(size=12, color="#343a40"),
            showgrid=False,
            linecolor="#adb5bd",
            mirror=True
        ),
        yaxis=dict(
            title="Pledged Success Ratio",
            titlefont=dict(size=14),
            tickfont=dict(size=12, color="#343a40"),
            range=[0, upper_limit],
            showgrid=True,
            gridcolor="#dee2e6",
            zeroline=True,
            zerolinecolor="#ced4da"
        ),
        plot_bgcolor="#f8f9fa",  # Matches your CSS background
        paper_bgcolor="#f8f9fa",
        margin=dict(l=60, r=40, t=80, b=100),
        template="plotly_white",
        showlegend=False
    )

    return fig

def log_pledged_scatter(df):
    fig = px.scatter(df,x="log_goal",y="log_pledged",title="Log(Goal) vs. Log(Pledged) by Success", color="success")
    return fig




def success_rate_duration(df):
    success_rate_by_duration = df.groupby("duration_bin")["success"].mean().reset_index()

    fig = go.Figure(data=[
        go.Bar(
            x=success_rate_by_duration["duration_bin"],
            y=success_rate_by_duration["success"],
            marker_color="#007bff",  # Bootstrap primary blue
            hovertemplate="Duration: %{x}<br>Success Rate: %{y:.2f}<extra></extra>"
        )
    ])

    fig.update_layout(
        title={
            "text": "Success Rate by Campaign Duration",
            "x": 0.5,
            "xanchor": "center",
            "font": dict(size=18, color="#343a40")
        },
        xaxis=dict(
            title="Duration (Days)",
            titlefont=dict(size=14),
            tickfont=dict(size=12),
            linecolor="#adb5bd",
            mirror=True
        ),
        yaxis=dict(
            title="Average Success Rate",
            titlefont=dict(size=14),
            tickfont=dict(size=12),
            range=[0, 1],
            gridcolor="#dee2e6",
            zeroline=True,
            zerolinecolor="#ced4da"
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        margin=dict(t=80, b=60, l=60, r=40),
        template="plotly_white"
    )

    return fig



def distribution_of_pledge(df):
    # Select top 10 categories by count
    top_categories = df['category_name'].value_counts().head(10).index
    filtered = df[df['category_name'].isin(top_categories)]

    # Compute 95th percentile of goal to limit y-axis
    upper_limit = np.percentile(filtered["goal"], 95)

    fig = go.Figure(data=[
        go.Box(
            y=filtered["goal"],
            x=filtered["state"],
            boxpoints="outliers",
            pointpos=-1.8,
            quartilemethod="exclusive",
            marker=dict(color="#007BFF"),
            line=dict(width=1.5)
        )
    ])

    fig.update_layout(
        title={
            'text': "Distribution of Goal Amounts by Campaign State (95th Percentile Clipped)",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            "font": dict(size=18, color="#343a40")
        },
        xaxis=dict(
            title="Campaign State",
            titlefont=dict(size=14),
            tickangle=0,
            tickfont=dict(size=12, color="#343a40"),
            linecolor="#adb5bd",
            mirror=True
        ),
        yaxis=dict(
            title="Goal Amount (USD)",
            titlefont=dict(size=14),
            tickfont=dict(size=12, color="#343a40"),
            type="log",
            range=[0, np.log10(upper_limit)],
            showgrid=True,
            gridcolor="#dee2e6",
            zeroline=True,
            zerolinecolor="#ced4da"
        ),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        margin=dict(l=60, r=40, t=80, b=100),
        template="plotly_white",
        showlegend=False
    )

    return fig


