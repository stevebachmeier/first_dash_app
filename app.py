# -*- coding: utf-8 -*-
"""
Dash app

@author: Steve Bachmeier
"""

#==============================================================================
#
# dash_core_components.graph() class
# Plot a histogram
#
#==============================================================================

# ---- IMPORT LIBRARIES ----
# Example 1, 2
import dash
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go 
from dash.dependencies import Input, Output

# ---- DATA (EXAMPLE 2)----
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

# ---- MARKDOWN TEXT (EXAMPLE 3) ----
markdown_text = '''
# Heading 1

## Heading 2

### Heading 3
 
All work and no play make Jack a dull boy. All work and no play make Jack a dull boy. 
All work and no play make Jack a dull boy. All work and no play make Jack a dull boy. 
All work and no play make Jack a dull boy. All work and no play make Jack a dull boy. \n
*All work and no play make Jack a dull boy.* \n
All work and no play make Jack a dull boy. \n
All work and no play make Jack a dull boy. \n 
**All work and no play make Jack a dull boy.**

* All work and no play make Jack a dull boy. 
    * All work and no play make Jack a dull boy. 
        * All work and no play make Jack a dull boy. 
* All work and no play make Jack a dull boy. 
        
1. All work and no play make Jack a dull boy. 
2. All work and no play make Jack a dull boy. 
    1. All work and no play make Jack a dull boy. 
    2. All work and no play make Jack a dull boy. 
        1. All work and no play make Jack a dull boy. 
    3. All work and no play make Jack a dull boy. 
3. All work and no play make Jack a dull boy. 
'''

# ---- CREATE LAYOUT ----

# Initialize dash
app = dash.Dash()

# Define colors
colors = {'background': '#5f6670', 'heading':'#ff69b4', 'text': 'white'}
          
    
# Layout
app.layout = html.Div(
    style={'backgroundColor':colors['background']},
    children=[
            
#==============================================================================
    
        # Example 1
        html.H1('EXAMPLE 1', 
            style={'textAlign':'left', 'color':colors['heading'],
                   'margin':'1em 0 0 1em'}),
        html.H2('Plot a histogram using dash_core_components.graph()',
            style={'textAlign':'left', 'color':colors['heading'],
                   'margin':'1em 0 0 1em'}),
        dcc.Graph(id='Graph1', figure={
            'data':[
                {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'Montreal'}],
                'layout':{
                    'plot_bgcolor':colors['background'],
                    'paper_bgcolor':colors['background'],
                    'font':{'color':colors['text']}}}),

#==============================================================================

        # Example 2
        html.H1('EXAMPLE 2',
            style={'textAlign':'left', 'color':colors['heading'],
                   'margin':'1em 0 0 1em'}),
        html.H2('Plot a scatterplot using plotly.graph_objs.Scatter()',
            style={'textAlign':'left', 'color':colors['heading'],
                   'margin':'1em 0 0 1em'}),
        dcc.Graph(id='life-exp-vs-gdp', figure={
             'data':[
                 go.Scatter(
                     x=df[df['continent'] == i]['gdp per capita'],
                     y=df[df['continent'] == i]['life expectancy'],
                     text=df[df['continent'] == i]['country'],
                     mode='markers', opacity=0.8,
                     marker={'size': 15, 'line': {'width': 0.5, 'color': 'white'}},
                     name=i
                 ) for i in df.continent.unique()],
             'layout': go.Layout(
                 xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                 yaxis={'title': 'Life Expectancy'},
                 margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                 legend={'x': 0, 'y': 1}, hovermode='closest')}),

#==============================================================================
                 
        # Example 3
        html.H1('EXAMPLE 3',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H2('Markdowns',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        dcc.Markdown(markdown_text),
        
#==============================================================================
        
        # Example 4
        html.H1('EXAMPLE 4',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H2('Dropdown menus and radio buttons',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H3('Dropdown menu', style={'margin':'1em 0 0 1em'}),
        html.Div(dcc.Dropdown(
            options=[{'label':'New York City', 'value': 'NYC'},
                     {'label':'Montreal', 'value':'MTL'},
                     {'label':'San Francisco', 'value':'SF'}],
            value='SF'), 
            style={'width': '25%', 'display': 'inline-block', 
                   'margin':'1em 0 1em 1em'}),

        html.H3('Multi-select dropdown menu', style={'margin':'1em 0 0 1em'}),
        html.Div(dcc.Dropdown(
            options=[{'label':'New York City', 'value': 'NYC'},
                     {'label':'Montreal', 'value':'MTL'},
                     {'label':'San Francisco', 'value':'SF'}],
            value=['NYC','SF'], multi=True), 
            style={'width': '25%', 'display': 'inline-block', 
                   'margin':'1em 0 1em 1em'}),

        html.H3('Radio buttons', style={'margin':'1em 0 0 1em'}),
        html.Div(dcc.RadioItems(options=[{'label':'New York City', 'value':'NYC'},
                                {'label':'Montreal', 'value':'MTL'},
                                {'label':'San Francisco', 'value':'SF'}],
                    value='SF')),
        
                                
        html.H3('Checkboxes', style={'margin':'1em 0 0 1em'}),
        dcc.Checklist(options=[{'label': 'New York City', 'value': 'NYC'},
                               {'label': u'Montréal', 'value': 'MTL'},
                               {'label': 'San Francisco', 'value': 'SF'}],
            values=['NYC', 'SF']),

#==============================================================================

        html.H1('EXAMPLE 5',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H2('Aligning divs side by side',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),                     
        html.Div([
            html.Div([
                html.H3('Radio buttons', style={'color':'white', 'textAlign':'center'}),
                dcc.RadioItems(options=[{'label':'New York City', 'value':'NYC'},
                                        {'label':'Montreal', 'value':'MTL'},
                                        {'label':'San Francisco','value':'SF'}],
                    value='SF')],
                style={'width':'50%', 'display':'table-cell'}),
            html.Div([
                html.H3('Checkboxes', style={'color':'white', 'textAlign':'center'}),
                dcc.Checklist(options=[{'label': 'New York City', 'value': 'NYC'},
                                       {'label': u'Montréal', 'value': 'MTL'},
                                       {'label': 'San Francisco', 'value': 'SF'}],
                    values=['NYC', 'SF'])],
                style={'width':'50%', 'display':'table-cell'})],
            style={'width':'80%', 'dislay':'table'}),

#==============================================================================

        html.H1('EXAMPLE 6',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H2('User input',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}), 
        html.Label('Song or band: '), 
        dcc.Input(value='Guns \'n Roses', type='text'),

#==============================================================================

        html.H1('EXAMPLE 7',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}),
        html.H2('User input plus button',
            style={'color':colors['heading'], 'margin':'1em 0 0 1em'}), 
        html.Div([
            dcc.Input(id='user_input', type='text', placeholder='Song/band',
                      style={'width':'25%'}),
            html.Button('Submit', id='button', style={'margin':'0 0 0 1em'}),
            html.Div(id='output_container_button', children='Click submit!',
                     style={'color':'white', 'margin':'1em 0 0 0'})],
            style={'width':'100%', 'display':'float', 'textAlign':'center'})
    ] # close parent div children
) # close parent div

@app.callback(
    dash.dependencies.Output('output_container_button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('user_input', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value, n_clicks)

    
    
    



             
             
             
#==============================================================================
#
# RUN SERVER
#
#==============================================================================                 
if __name__ == '__main__':
    app.run_server(debug=True)
#    app2.run_server(debug=True)
#    app3.run_server(debug=True)