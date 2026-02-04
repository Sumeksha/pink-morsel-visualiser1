import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the CSV file
df = pd.read_csv("final_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize the Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center", "color": "#2c3e50", "margin-bottom": "30px"}
    ),
    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold", "margin-right": "10px"}),
        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin-right": "15px"},
            inputStyle={"margin-right": "5px"}
        )
    ], style={"textAlign": "center", "margin-bottom": "30px"}),
    dcc.Graph(id="sales-line-chart")
], style={"font-family": "Arial", "margin": "50px", "backgroundColor": "#f5f5f5"})

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]
    
    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Date": "Date", "Sales": "Total Sales"}
    )
    
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top right"
    )
    
    fig.update_layout(
        plot_bgcolor="#ecf0f1",
        paper_bgcolor="#ecf0f1",
        font_color="#34495e"
    )
    
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
