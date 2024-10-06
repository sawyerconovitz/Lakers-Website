import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

# Data
franchise_value = {
    "2003": 426, "2004": 447, "2005": 510, "2006": 529, "2007": 568,
    "2008": 560, "2009": 584, "2010": 607, "2011": 643, "2012": 900,
    "2013": 1000, "2014": 1350, "2015": 2600, "2016": 2700, "2017": 3300,
    "2019": 3700, "2020": 4400, "2021": 5500, "2022": 5900, "2023": 6400
}


## in millions of dollars
Attendence = {

"2003":	19040,
"2004":	19175,
"2005":	18801,
"2006":	18847,
"2007":	18951,
"2008":	18834,
"2009":	19130,
"2010":	19131,
"2011":	19042,
"2012":	19015,
"2013":	18931,
"2014":	18337,
"2015":	18306,
"2016":	19073,
"2017":	18570,
"2018":	18796,
"2019":	18929,
"2020":	18936,
"2021":	2762,
"2022":	18414,
"2023":	18695,
}
Allstars={
"2003":	2,
"2004":	1,
"2005":	1,
"2006":	1,
"2007":	1,
"2008":	2,
"2009":	2,
"2010":	2,
"2011":	2,
"2012":	2,
"2013":	2,
"2014":	1,
"2015":	1,
"2016":	0,
"2017":	0,
"2018":	1,
"2019":	2,
"2020":	2,
"2021":	1,
"2022":	1,
"2023":	2,
}
Wins={
"2003":	56,
"2004":	34,
"2005":	45,
"2006":	42,
"2007":	57,
"2008":	65,
"2009":	57,
"2010":	57,
"2011":	41,
"2012":	45,
"2013":	27,
"2014":	21,
"2015":	17,
"2016":	26,
"2017":	35,
"2018":	37,
"2019":	52,
"2020":	42,
"2021":	33,
"2022":	43,
"2023":	47,
}

data_options = {
    'Franchise Value': franchise_value,
    'Attendence': Attendence,
    'Allstars': Allstars,
    'Wins':Wins,
}

labels = ['Lebron James', 'Davis', 'Russell', 'Reaves', 'Hachimura','Prince','Wood','Dinwiddie','Reddish','Vanderbilt','Hayes','Christie', 'Vincent', 'Hodge','Hood-Schifino', 'Windler', 'Castleton', ' Mayes', 'Fudge', 'Lewis', 'Giles III']

Points = [25.7,24.7,18.0,15.9,13.6,8.9,6.9,6.8,5.4,5.2,4.3,4.3,3.2,2,1.6,1.5,1.5,1.3,1.0,0.3,0.3]




Rebounds = [7.3, 12.6, 3.1, 4.3, 4.3, 2.9, 5.1, 1.7, 2.1, 4.8, 3.0, 2.1, 0.8, 0, 0.6,0.4, 0.8, 0.4, 0.5, 0.1, 0.6]
Assists = [8.3, 3.5, 6.3, 5.5, 1.2, 1.5, 1.0, 2.4, 1.0, 1.2, 0.5, 0.9, 1.9, 0.7, 0.4, 0.8, 0.2, 0.6, 0, 0.2, 0]


data_optionspi={
    'Points':Points,
    'Rebounds':Rebounds,
    'Assists':Assists,
}


## NEW SECTION: DEPTH CHART
# Starters, second, third, fourth, and fifth

# Keys: position, values: [name, height, weight]
starters = {
    "PG": ["D'angelo Russell",6.25, 193, "https://www.espn.com/nba/player/_/id/3136776/dangelo-russell"],
    "SG" :["Austin Reaves" ,6.4, 197, "https://www.espn.com/nba/player/_/id/4066457/austin-reaves"],
    "SF": ["Lebron James", 6.75, 250, " https://www.espn.com/nba/player/_/id/1966/lebron-james"],
    "PF": ["Rui Hachimura", 6.7, 230, " https://www.espn.com/nba/player/_/id/4066648/rui-hachimura"],
    "C": ["Anthony Davis", 6.8, 253, "https://www.espn.com/nba/player/_/id/6583/anthony-davis"]
}

second = {
    "PG": ["Gabe Vincent",6.2, 200,"https://www.espn.com/nba/player/_/id/3137259/gabe-vincent"],
    "SG" :["Max Christe" ,6.4, 190, "https://www.espn.com/nba/player/_/id/4432582/max-christie"],
    "SF": ["Cam Reddish",6.7, 217, "https://www.espn.com/nba/player/_/id/4395627/cam-reddish"],
    "PF": ["Jarred Vanderbilt",6.4, 190, "https://www.espn.com/nba/player/_/id/4278077/jarred-vanderbilt"],
    "C": ["Anthony Davis", 6.8, 253, " https://www.espn.com/nba/player/_/id/6583/anthony-davis"],
}

third = {
    "PG": ["Bronny James",6.1, 210, "https://www.espn.com/nba/player/_/id/4683774/bronny-james"],
     "SG" :["Gabe Vincent",6.2, 200, "https://www.espn.com/nba/player/_/id/3137259/gabe-vincent"],
    "SF": ["Dalton Knecht",6.4, 204, "https://www.espn.com/nba/player/_/id/4897943/dalton-knecht"],
    "PF": ["Lebron James", 6.75, 250, "https://www.espn.com/nba/player/_/id/1966/lebron-james"],
    "C": ["Jaxson Hayses", 7.0, 220, "https://www.espn.com/nba/player/_/id/4397077/jaxson-hayes"],
}

# Combine the lineups into a dictionary
lineups = {
    "First": starters,
    "Second": second,
    "Third": third
}
# Initialize the Dash app
app = dash.Dash(__name__)
server=app.server
app.layout = html.Div(children=[
    html.H1(children='Lakers Analytics Website', style={'textAlign': 'center'}),

    html.Div(children='''
        Sawyer Conovitz
    ''', style={'textAlign': 'center'}),

    html.Div(style={'height': '20px'}),

    html.Div(children='''
        The history of the Los Angeles Lakers traces back to 1947 when they were originally established as the Minneapolis Lakers in Minnesota, named after the state's nickname, the "Land of 10,000 Lakes." The team quickly became a powerhouse in the early years of professional basketball, winning five championships in the Basketball Association of America (BAA) and National Basketball Association (NBA) combined, before relocating to Los Angeles in 1960. Under the ownership of Jack Kent Cooke and later Dr. Jerry Buss, the Lakers cemented their status as one of the most successful franchises in NBA history. Led by iconic players such as Jerry West, Wilt Chamberlain, Magic Johnson, Kareem Abdul-Jabbar, Shaquille O'Neal, and Kobe Bryant, the team has captured a total of 17 NBA championships, tying them for the most titles in league history with the Boston Celtics. The Lakers' legacy is not just defined by their victories but also by their cultural impact and the vibrant basketball culture they helped cultivate in Los Angeles and beyond.
    ''', style={'textAlign': 'center'}),

    html.Div(style={'height': '20px'}),

    ## BAR CHART
    html.Button('Toggle Bar Graph', id='toggle-button-graph', n_clicks=0, style={'backgroundColor': 'Gold', 'float': 'right', 'color': 'purple'}),

    html.Div(
        children=[
            dcc.Dropdown(
                id='data-dropdown',
                options=[{'label': key, 'value': key} for key in data_options.keys()],
                value='Franchise Value'
            ),
            dcc.Graph(
                id='franchise-value-graph'
            )
        ],
        id='Bar-Chart-Container',
        style={'display': 'none', 'backgroundColor': "Gold"}  # Initially hidden
    ),

    ## PIE CHART
    html.Button('Toggle Pie Chart', id='toggle-button', n_clicks=0, style={'backgroundColor': 'Gold', 'color': 'purple'}),

    html.Div(
        children=[
            dcc.Dropdown(
                id='data-dropdown-Pi',
                options=[{'label': key, 'value': key} for key in data_optionspi.keys()],
                value='Points'
            ),
            dcc.Graph(
                id='Pi-Chart'
            )
        ],
        id='pi-chart-container',
        style={'display': 'none', 'backgroundColor': "Gold"}  # Initially hidden
    ),

    ## LINEUP CHART
    html.Div(style={'height': '20px'}),
    html.H2('Select Lineup', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='lineup-dropdown',
        options=[
            {'label': 'First', 'value': 'First'},
            {'label': 'Second', 'value': 'Second'},
            {'label': 'Third', 'value': 'Third'}
        ],
        value='First',
        style={'width': '50%', 'margin': '0 auto'}
    ),
    dcc.Graph(id='lineup-graph')
], style={'backgroundColor': "Gold"})
# Define callback to update graph
@app.callback(
    Output('franchise-value-graph', 'figure'),
    [Input('data-dropdown', 'value')]
)
def update_graph(selected_data):
    x = list(data_options[selected_data].keys())
    y = list(data_options[selected_data].values())

    # Create a list of colors alternating between dark yellow and purple
    colors = ['#FFD700', 'purple'] * ((len(x) // 2) + 1)

    # Create the figure with alternating colors and styled markers
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode="markers",
                                    marker=dict(color=colors,
                                                size=10,  # Adjust size of markers
                                                line=dict(color='black', width=1)  # Outline color and width
                                               )))

    # Update the layout to set background colors, title, and axis labels
    fig.update_layout(
        title={
            'text': 'Lakers: ' + selected_data,
            'x': 0.5,  # Center the title
            'y': 0.9,  # Adjust the vertical position if needed
            'xanchor': 'center',  # Center alignment
            'yanchor': 'top',  # Align to the top of the title
            'font': {'size': 16, 'color': 'black'}  # Font style and weight
        },
        xaxis_title='Years',
        yaxis_title='Amount of Money in Millions',
        plot_bgcolor='purple',
        paper_bgcolor='gold'
    )

    return fig


@app.callback(
    Output('Pi-Chart', 'figure'),
    [Input('data-dropdown-Pi', 'value')]
)
def update_graphpi(selected_data):
    # Define colors
    values = data_optionspi[selected_data]

    # values is either points, rebounds, or assists, depending on what the user chose
    labels_and_values = list(zip(labels, values))

    # labels_and_values = [(lebron, 25), (davis, 22), (russel, 15)]

    labels_and_values = sorted(labels_and_values,key=lambda x:x[1])

    new_labels = [x[0] for x in labels_and_values]
    values = [x[1] for x in labels_and_values]


    colors = ['purple', 'gold'] * ((len(labels) + 1) // 2)

    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=new_labels, values=values, marker=dict(colors=colors))])

    # Customize layout (optional)
    fig.update_layout(title_text="Pie Chart Example")

    # Show the chart
   
 
    return fig


@app.callback(
    Output('pi-chart-container', 'style'),
    [Input('toggle-button', 'n_clicks')],
    [State('pi-chart-container', 'style')]
)
def toggle_pie_chart(n_clicks, current_style):
    if n_clicks % 2 == 1:
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output('Bar-Chart-Container', 'style'),
    [Input('toggle-button-graph', 'n_clicks')],
    [State('Bar-Chart-Container', 'style')]
)
def toggle_bar_graph(n_clicks, current_style):
    if n_clicks % 2 == 1:
        return {'display': 'block'}
    else:
        return {'display': 'none'}




## DEPTH CHART GRAPH

@app.callback(
    Output('lineup-graph', 'figure'),
    [Input('lineup-dropdown', 'value')]
)
def update_lineup_graph(selected_lineup):
    lineup = lineups[selected_lineup]
    positions = list(lineup.keys())

    # Extract player names, heights, and weights
    player_names = [player[0] for player in list(lineup.values())]
    player_heights = [player[1] for player in list(lineup.values())]
    player_weights = [player[2] for player in list(lineup.values())]
    player_link = [player[3] for player in list(lineup.values())]


    ## player_weights = [180, 200, 220, ...]
    ## player_names = [LBJ, Anthony Davis, Deangelo russel, ...]

    ## desired_data = [(LBJ, 180), (anthony davis, 200), ...]

    # what were printing is this: (anthony davis, 200) = test_data

    # test_data[0]

    # Create the figure
    fig = go.Figure(data=[go.Bar(
        x=positions, 
        y=player_heights, 
        marker_color='purple',
        customdata=list(zip(player_weights, player_names, player_link)), # Add weights to customdata
        hovertemplate='<b>Position: %{x}</b><br>Height: %{y} ft<br>Weight: %{customdata[0]} lbs<br>Name: %{customdata[1]} <br>Link: %{customdata[2]}'  # Customize hover info
        
    )])


    fig.update_layout(
        title='Selected Lineup: ' + selected_lineup,
        xaxis_title='Position',
        yaxis_title='Height (ft)',
        plot_bgcolor='gold',
        paper_bgcolor='gold'
    )

    return fig


# Add a client-side callback to handle click events
app.clientside_callback(
    """
    function(clickData) {
        if(clickData) {
            const link = clickData.points[0].customdata[2];
            window.open(link, '_blank');
        }
    }
    """,
    Output('lineup-graph', 'clickData'),  # This is just a placeholder to trigger the callback
    Input('lineup-graph', 'clickData')
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)