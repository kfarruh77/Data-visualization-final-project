import pandas as pd 
import plotly
import plotly.express as px
import plotly.io as pio
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

#New York Data
# df = pd.read_csv('Total_New.csv')
# df_total = pd.read_csv('TotalWeekly3.csv')
# dff = df.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()

# df_drugs = pd.read_csv('DrugsWeekly3.csv')
# df_violent = pd.read_csv('ViolentWeekly3.csv')
# df_theft = pd.read_csv('TheftWeekly3.csv')

#Phoenix Data
# dfPh = pd.read_csv('Phoenix_Total.csv')
# df_totalPh = pd.read_csv('Phoenix_TotalWeekly31.csv')
# dffPh = dfPh.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()

# df_drugsPh = pd.read_csv('Phoenix_DrugsWeekly3.csv')
# df_violentPh = pd.read_csv('Phoenix_ViolentWeekly3.csv')
# df_theftPh = pd.read_csv('Phoenix_TheftWeekly3.csv')

#Seattle Data
# dfSt = pd.read_csv('Seattle_data2.csv')
# df_totalSt = pd.read_csv('Seattle_weekly_total.csv')
# dffSt = dfSt.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()

# df_drugsSt = pd.read_csv('Seattle_weekly_drug.csv')
# df_violentSt = pd.read_csv('Seattle_weekly_violent.csv')
# df_theftSt = pd.read_csv('Seattle_weekly_theft.csv')

#Chicago Data
# dfCh = pd.read_csv('Chicago2.csv')
# df_totalCh = pd.read_csv('chicago-total.csv')
# dffCh = dfCh.groupby('Year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()

# df_drugsCh = pd.read_csv('chicago-drugs.csv')
# df_violentCh = pd.read_csv('chicago-violence.csv')
# df_theftCh = pd.read_csv('chicago-theft.csv')


app.layout = html.Div([
    html.H4('Choose City:'),
    dcc.Dropdown(
        id="main-dropdown",
        options=["New York", "Phoenix", "Seattle", "Chicago", "Los Angeles"],
        value="New York",
        clearable=False,
    ),
    html.H4('Number of crimes'),
    dcc.Dropdown(
        id="dropdown",
        options=["Total", "Drugs", "Violent", "Theft"],
        value="Total",
        clearable=False,
    ),
    dcc.Graph(id="graph"),

    html.Div([
    html.H4('Crime Timeline'),
    dcc.Dropdown(
        id="dropdown2",
        options=["Total", "Drugs", "Violent", "Theft"],
        value="Total",
        clearable=False,
    ),
    dcc.Graph(id="graph2"),
])
])


@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value"),
    Input("main-dropdown", "value")])
def update_bar_chart(crime_type, city):
    if city == "New York":
        df = pd.read_csv('Total_New.csv')
        
        dff = df.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()
      
        if crime_type=='Total':
            fig = px.bar(
                data_frame=dff,
                x = ['2018', '2019', '2020', '2021'],
                y = ['Drugs', 'Violent', 'Theft'],
                labels={'value': 'Total', 'variable': 'Crime Type', 'x': 'year'},
                title='Number of crimes in NYC'
            )
        else:
            fig = px.bar(
                dff, 
                x=['2018', '2019', '2020', '2021'],
                y=crime_type,
                labels= {'x' : 'year'},
                title='Number of crimes in NYC'
            )
    elif city == "Phoenix":
        dfPh = pd.read_csv('Phoenix_Total.csv')
        
        dffPh = dfPh.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()
      
        if crime_type=='Total':
            fig = px.bar(
                data_frame=dffPh,
                x = ['2018', '2019', '2020', '2021'],
                y = ['Drugs', 'Violent', 'Theft'],
                labels={'value': 'Total', 'variable': 'Crime Type', 'x': 'year'},
                title='Number of crimes in Phoenix'
            )
        else:
            fig = px.bar(
                dffPh, 
                x=['2018', '2019', '2020', '2021'],
                y=crime_type,
                labels= {'x' : 'year'},
                title='Number of crimes in Phoenix'
            )
    elif city == "Seattle":
        dfSt = pd.read_csv('Seattle_data2.csv')
       
        dffSt = dfSt.groupby('year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()
       

        if crime_type=='Total':
            fig = px.bar(
                data_frame=dffSt,
                x = ['2018', '2019', '2020', '2021'],
                y = ['Drugs', 'Violent', 'Theft'],
                labels={'value': 'Total', 'variable': 'Crime Type', 'x': 'year'},
                title='Number of crimes in Seattle'
            )
        else:
            fig = px.bar(
                dffSt, 
                x=['2018', '2019', '2020', '2021'],
                y=crime_type,
                labels= {'x' : 'year'},
                title='Number of crimes in Seattle'
            )
    elif city == "Chicago":
        dfCh = pd.read_csv('Chicago2.csv')
        
        dffCh = dfCh.groupby('Year', as_index=False)[['Total', 'Drugs', 'Violent', 'Theft']].sum()
        
        if crime_type=='Total':
            fig = px.bar(
                data_frame=dffCh,
                x = ['2018', '2019', '2020', '2021'],
                y = ['Drugs', 'Violent', 'Theft'],
                labels={'value': 'Total', 'variable': 'Crime Type', 'x': 'year'},
                title='Number of crimes in Chicago'
            )
        else:
            fig = px.bar(
                dffCh, 
                x=['2018', '2019', '2020', '2021'],
                y=crime_type,
                labels= {'x' : 'year'},
                title='Number of crimes in Chicago'
            )
    elif city == "Los Angeles":
        df = pd.read_csv('la-total.csv')       
        if crime_type=='Total':
            fig = px.bar(
                data_frame=df,
                x = ['2018', '2019', '2020', '2021'],
                y = ['Drugs', 'Violent', 'Theft'],
                labels={'value': 'Total', 'variable': 'Crime Type', 'x': 'year'},
                title='Number of crimes in Los Angeles'
            )
        else:
            fig = px.bar(
                df, 
                x=['2018', '2019', '2020', '2021'],
                y=crime_type,
                labels= {'x' : 'year'},
                title='Number of crimes in Los Angeles'
            )
    return fig
    




#fig = px.line(df2, x='day', y=['2018', '2019', '2020', '2021'],  labels={'value': 'Number of crimes', 'variable': 'Crime Type', 'ARREST_DATE':'Date'},)
@app.callback(
    Output("graph2", "figure"), 
    [Input("dropdown2", "value"),
    Input("main-dropdown", "value")])
def update_line_chart(crime_type, city):
    if city == "New York":
        df_total = pd.read_csv('TotalWeekly3.csv')
        df_drugs = pd.read_csv('DrugsWeekly3.csv')
        df_violent = pd.read_csv('ViolentWeekly3.csv')
        df_theft = pd.read_csv('TheftWeekly3.csv')
        df = df_total
        if crime_type == 'Total':
            df = df_total
        elif crime_type == 'Drugs':
            df= df_drugs
        elif crime_type == 'Theft':
            df= df_theft
        elif crime_type == 'Violent':
            df= df_violent
        fig = px.line(
            df, 
            x="day", 
            y=['2018', '2019', '2020', '2021'],
            labels= {'value' : 'Number of Crimes', 'variable' : 'year'})
    elif city == "Phoenix":
        df_totalPh = pd.read_csv('Phoenix_TotalWeekly31.csv')
        df_drugsPh = pd.read_csv('Phoenix_DrugsWeekly3.csv')
        df_violentPh = pd.read_csv('Phoenix_ViolentWeekly3.csv')
        df_theftPh = pd.read_csv('Phoenix_TheftWeekly3.csv')
        df = df_totalPh
        if crime_type == 'Total':
            df = df_totalPh
        elif crime_type == 'Drugs':
            df= df_drugsPh
        elif crime_type == 'Theft':
            df= df_theftPh
        elif crime_type == 'Violent':
            df= df_violentPh
        fig = px.line(
            df, 
            x="day", 
            y=['2018', '2019', '2020', '2021'],
            labels= {'value' : 'Number of Crimes', 'variable' : 'year'})
    elif city == "Seattle":
        df_totalSt = pd.read_csv('Seattle_weekly_total.csv')
        df_drugsSt = pd.read_csv('Seattle_weekly_drug.csv')
        df_violentSt = pd.read_csv('Seattle_weekly_violent.csv')
        df_theftSt = pd.read_csv('Seattle_weekly_theft.csv')
        df = df_totalSt
        if crime_type == 'Total':
            df = df_totalSt
        elif crime_type == 'Drugs':
            df= df_drugsSt
        elif crime_type == 'Theft':
            df= df_theftSt
        elif crime_type == 'Violent':
            df= df_violentSt
        fig = px.line(
            df, 
            x="day", 
            y=['2018', '2019', '2020', '2021'],
            labels= {'value' : 'Number of Crimes', 'variable' : 'year'})
    elif city == "Chicago":
        df_totalCh = pd.read_csv('chicago-total.csv')
        df_drugsCh = pd.read_csv('chicago-drugs.csv')
        df_violentCh = pd.read_csv('chicago-violence.csv')
        df_theftCh = pd.read_csv('chicago-theft.csv')
        df = df_totalCh
        if crime_type == 'Total':
            df = df_totalCh
        elif crime_type == 'Drugs':
            df= df_drugsCh
        elif crime_type == 'Theft':
            df= df_theftCh
        elif crime_type == 'Violent':
            df= df_violentCh
        fig = px.line(
            df, 
            x="Day", 
            y=['2018', '2019', '2020', '2021'],
            labels= {'value' : 'Number of Crimes', 'variable' : 'year'})
    elif city == "Los Angeles":
        df_total = pd.read_csv('la-all.csv')
        df_drugs = pd.read_csv('la-drugs.csv')
        df_violent = pd.read_csv('la-violent.csv')
        df_theft = pd.read_csv('la-theft.csv')
        df = df_total
        if crime_type == 'Total':
            df = df_total
        elif crime_type == 'Drugs':
            df= df_drugs
        elif crime_type == 'Theft':
            df= df_theft
        elif crime_type == 'Violent':
            df= df_violent
        fig = px.line(
            df, 
            x="Day", 
            y=['2018', '2019', '2020', '2021'],
            labels= {'value' : 'Number of Crimes', 'variable' : 'year'})
    return fig



app.run_server(debug=True)