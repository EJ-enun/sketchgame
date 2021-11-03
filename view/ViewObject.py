import os
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

#Generic View Objects
class ViewObject():
        def __init__(self):
                self.title = None
                        
        #Reusable Graph.
        def new_graph(id_):
                return dbc.Col(children=[dbc.Card(dbc.Col(children=[dcc.Graph(id=id_),html.Br()])),])

        def graph(id_, figure_, layout_, margin_, width_, height_):
                return dbc.Col(children=[dbc.Card(dbc.Col(children=[dcc.Graph(id=id_, figure=figure_,layout=layout_, margin=margin_, style={'width':width_, 'height':height_}),html.Br()])),])                                                       
        #Reusable Uploader object.
        def upload(id_, text_, width_='100%', height_='60px', _lineHeight='60px', _borderWidth='1px', _borderStyle='dashed', _borderRadius='5px', _textAlign='center'):
                return dbc.Col(children=[dcc.Upload([text_,html.A('Select a File')], id=id_, style={'width': width_,'height': height_,'lineHeight': _lineHeight,'borderWidth': _borderWidth,'borderStyle': _borderStyle,'borderRadius': _borderRadius,'textAlign': _textAlign})])

        def dropdown(id_, text_, dict_, value_, multi_= False):
                return dbc.Form([html.H4(text_),dcc.Dropdown(id=id_, value=value_, multi = multi_, options=[{'label':x,'value':x} for x in dict_])])

        def progress_bar(id_, id_int_, n_interval, interval):
                return html.Div([dcc.Interval(id=id_int_, n_intervals = n_interval, interval = interval), dbc.Progress(id=id_)])

        def radio_item(id_, dict_, value_, label_style_dict_= {'display': 'inline-block'}):
                return dcc.RadioItems(id=id_, options=dict_, value=value_,labelStyle=label_style_dict_)
                                                                                                                    
        def checklist(id_, dict_, value_, label_style_dict_= {'display': 'inline-block'}):                      
                return dcc.Checklist(id=id_, options=dict_, value=value_, labelStyle=label_style_dict_ )
                                                                                                                                #labelStyle=label_style_dict_
        def slider(id_, min_, max_, step_, value_):
                return html.Div([dcc.Slider(id=id_, min=min_, max=max_, step=step_, value=value_)])

        def marks_slider(id_, min_, max_, marks_, value_):
                return html.Div([dcc.Slider(id=id_, min=min_, max=max_, marks={i:i for i in range(marks_)}, value=value_)])
        
        def range_slider(id_, count_,  min_, max_, step_, value_):
                return html.Div([dcc.RangeSlider(id=id_, count = count_, min=min_, max=max_, step=step_, value=value_)])

        def range_marks_slider(id_, count_,  min_, max_, marks_, value_):
                return html.Div([dcc.RangeSlider(id=id_, count = count_, min=min_, max=max_, marks={i:i for i in range(marks_)}, value=value_)])

        def text_input(id_, type_, placeholder_, value_): 
                return html.Div([dcc.Input(id= id_, type = type_, placeholder = placeholder_, value=value_)])

        def audio(src_, controls_=True):
                return html.Div([html.Audio(src=src_, controls=controls_ )])
        def textarea(id_,  placeholder_, value_, width_, height_):
                return html.Div([dcc.Textarea(id=id_, value=value_, style={'width':width_, 'height':height_}, placeholder=placeholder_)])

        def button(id_, btn_name, width_, height_, n_clicks_= 0):
                return html.Button(btn_name, id=id_, n_clicks=n_clicks_, style={'width':width_, 'height':height_})
            
        def date_picker_single(id_, date_):
                return html.Div([dcc.DatePickerSingle(id=id_, date = date_)])
    
        def date_picker_range(id_, start_date_, end_placeholder_text_):
                return html.Div([dcc.DatePickerRange(id=id_, start_date = date_, end_date_placeholder_text=end_placeholder_text_)])

        def markdown(_value): 
                return html.Div([dcc.Markdown(_value)])

        def tabs(no_of_tabs_, id_, value_):
                tabs = [dcc.Tab(label="Tab {}".format(x)) for x in range(0, no_of_tabs_)]
                return dcc.Tabs(id=id_, value=value_, children=[tabs])


        def loading(id_, child_id_, value_, type_="default"):   
                return html.Div([dcc.Loading(id=id_, type=type_, value=value_, children=html.Div(id=child_id_))])

        def confirm_dialog_provider(id_, btn_name_, message_):
                return html.Div([dcc.ConfirmDialogProvider(id=id_, message=message_, children=[html.Button(btn_name_)])])

        def confirm_dialog(id_, message_):
                return html.Div([dcc.ConfirmDialog(id=id_, message=message_)])

                                                                                                                                                                                                                                    
        def store(id_,storage_type_):
                return html.Div([dcc.Store(id=id_, storage_type=storage_type_)])
        def navbar_with_search():
                PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
                search_bar = dbc.Row([dbc.Col(dbc.Input(type="search", placeholder="Search")),dbc.Col(dbc.Button("Search", color="primary", className="ml-2", n_clicks=0), width="auto",),],no_gutters=True,className="ml-auto flex-nowrap mt-3 mt-md-0",align="center",)
                navbar = dbc.Navbar([html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row([dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),],align="center",no_gutters=True,),href="https://plotly.com",),dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),dbc.Collapse(search_bar, id="navbar-collapse", navbar=True, is_open=False),],color="dark",dark=True,)
                return navbar

        def navbar():
                navbar = dbc.NavbarSimple(children=[dbc.NavItem(dbc.NavLink("Explore", href="#")),dbc.DropdownMenu(children=[dbc.DropdownMenuItem("About", header=True),dbc.DropdownMenuItem("Logo Maker", href="#"),dbc.DropdownMenuItem("Contact Me", href="#"),],nav=True,in_navbar=True,label="Menu",),],brand="Dataset Rebalancing",brand_href="#",color="primary",dark=True,)
                return navbar

        def navbar_pre():
                navbar = dbc.NavbarSimple(children=[dbc.NavItem(dbc.NavLink("Home", href="#")), dbc.NavItem(dbc.NavLink("Photosketch", href="#")), dbc.NavItem(dbc.NavLink("CUHK Database", href="#"))], brand='GAN Versus Cuhk', brand_href="#", color="c9e265")
                return navbar
#if __name__ = "__main__":
#        ViewObject()
