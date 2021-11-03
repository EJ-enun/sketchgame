import os
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import  dcc
from dash import  html
from settings import config, about
from flask import Flask
from application.view.ViewObject import ViewObject
#from application.pcap.p2s import p2s
#from application.pcap.p2s import p2s, showSketch, showGrayscale, grayscaleing, getImage, readImage, dodging

#from fastbook import * 
#from fastai.vision.widgets import *

#######-------------INITIAL APPLICATION SETUP-----------################

#StyleSheets
external_stylesheiets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Server Instantiation 
server = Flask(__name__)        

#Prompts users for prediction on which image is real or fake
def userPredDropDown():
    return html.Div([ html.H4('Which picture is real?', style={'textAlign':'center'} ), html.Br(), dcc.Dropdown(id='_answer',options=[{'label': i, 'value': i} for i in ['Picture Zero', 'Picture One', 'Picture Two']],value='LA'),html.Div(id='display-value')])

#Prompts user for input on how realistic the GAN's sketch is.

def userRealisticSketchDropdown():
    return html.Div([ html.H4('Is the sketch realistic??', style={'textAlign':'center'} ), html.Br(), dcc.Dropdown(id='_sketch',options=[{'label': i, 'value': i} for i in ['Yes', 'Hell No!']],value='Yes')])


def storeFace():
    return html.Div([ html.H4("Become Part of this exciting project's database and help improve technology which eliminates human trafficking.", style={'textAlign':'center'} ),dcc.Dropdown(id='submit',options=[{'label': i, 'value': i} for i in ['Yes', 'No']],value='Yes')])
def predict(image):

        return image

#Shows GAN output
def showGanOutput():
        return dbc.Row([
                    dbc.Col(html.Div([html.Img(id='no_1', src=app.get_asset_url('ai_brain.jpeg'), width='50%')])),
                    dbc.Col(html.Div([html.Img(id='no_2', src=app.get_asset_url('images.jpg'), width='50%')])),
                    dbc.Col(html.Div([html.Img(id='no_3', src=app.get_asset_url('ai_black.jpeg'), width='50%')]))])

#App Instance
app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.LUX, config.fontawesome], server=server)
app.title = config.name

#####-------dash viewobject instantiation---------#####
app.layout = html.Div([ html.Br(), html.Br(), 
    ViewObject.navbar_pre(), html.Br(), 
    dbc.Row([html.Br(), html.Br(), 
        dbc.Col( html.Div([html.H1('What does it mean to be "REAL"? ', style={'textAlign':'center'} ), html.Br(),html.H5('Sketch Game is an attempt to help humans discern the level ot trust they should have in their visual cortex', style={'textAlign':'center'})]),
            dbc.Col(html.Div([html.Img(src=app.get_asset_url('ai_brain.jpeg'), width='60%')]))]),html.Br(), 
        ViewObject.upload('data','Drag and Drop OR'),html.Br(),html.Br(), showGanOutput(), html.Br(), html.Br(), userPredDropDown(), html.Br(), userRealisticSketchDropdown(), html.Br(), storeFace()])
def parse_contents(contents, filename, date):

#content_type, content_string = contents.split(',')
#decoded = base64.b64decode(content_string)
#read_pcap = read_pcap_data(content_string)
            return html.Div([html.H5(filename),
                html.H6(datetime.datetime.fromtimestamp(date)),
        # HTML images accept base64 encoded strings in the same format# that is supplied by the upload
                html.Img(src=contents),
                html.Hr(),
                html.Div('Raw Content'),
                html.Pre(contents[0:200] + '...', style={'whiteSpace': 'pre-wrap','wordBreak': 'break-all'})])

        
@app.callback(Output('display-value', 'children'),Input('data', 'contents'),
                                    State('data', 'filename'),
                                    State('data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [ parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]
            return children

#@app.callback(dash.dependencies.Output('display-value', 'children'),
#                      [dash.dependencies.Input('dropdown', 'value')])
#def display_value(value):
#        return 'You have selected "{}"'.format(value)

#@app.callback(dash.dependencies.Output('display-value', 'children'),
#                      [dash.dependencies.Input('dropdown', 'value')])
#def display_value(value):
#        return 'You have selected "{}"'.format(value)

#@app.callback(dash.dependencies.Output('display-value', 'children'),
#                      [dash.dependencies.Input('dropdown', 'value')])
#def display_value(value):
#        return 'You have selected "{}"'.format(value)
