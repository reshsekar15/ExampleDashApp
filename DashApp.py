# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()
colors = {
    'background': '#ececec',
    'text': 'black',
    'font': 'Verdana'
    
}
data = pd.read_csv("C:/Users/resekar/Downloads/titanicdata.csv")

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
    
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Welcome to my personal Dash App',
        style={
        'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    generate_table(data)
        
])

if __name__ == '__main__':
    app.run_server(debug=True)