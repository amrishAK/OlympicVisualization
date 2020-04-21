import dash
import dash_core_components as dcc
import dash_html_components as html
from Charts.Map import Map
from Charts.NightingaleMedal import NightingaleMedal
from Charts.LineGraph import SvsWCount
from Charts.LineGraph import Expense

import pandas as pd
df = pd.read_csv('https://query.data.world/s/4kxatdwqf2mhdohjdblorjfj77w67a')

a,b,c = Expense().CreateCombined()
pl,pl1 =  NightingaleMedal().Create()
app = dash.Dash()
app.layout = html.Div([
    html.Center([html.H1(children='Olympics Visualization')]),
    dcc.Graph(figure= Map().CreateMap()),
    html.Ul([html.H1(children='Expense Analysis')]),
    html.Br(),
    dcc.Graph(figure= a),
    html.Br(),
    dcc.Graph(figure= b),
    html.Br(),
    dcc.Graph(figure= c),
    dcc.Graph(figure= Map().CreateCountryWise()),
    html.Ul([html.H1(children='Performance Analysis')]),
    dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': f"{i['NOC']} - {i['region']}", 'value': i['NOC']} for _,i in df.iterrows()],
                value='Life expectancy at birth, total (years)'
            ),
    html.Br(),
    html.Div([html.Div([dcc.Graph(figure=pl[0])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),html.Div([dcc.Graph(figure=pl1[0])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})]),
    html.Div([html.Div([dcc.Graph(figure=pl[1])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),html.Div([dcc.Graph(figure=pl1[1])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})]),
    html.Div([html.Div([dcc.Graph(figure=pl[2])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),html.Div([dcc.Graph(figure=pl1[2])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})]),
    html.Div([html.Div([dcc.Graph(figure=pl[3])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),html.Div([dcc.Graph(figure=pl1[3])], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})]),

])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

