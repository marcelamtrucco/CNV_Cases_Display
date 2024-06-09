from dash import Dash, dash_table, dcc, html, Input, Output, callback
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('allgenes-results.txt',sep='\t')

app = Dash(__name__)
server=app.server

app.layout = html.Div([(html.H1("DataTable with Hypopituitarism Patient CNVs")),(html.H4("QS= Quality Score  NP =Number of Exons affected")),
    dash_table.DataTable(id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-interactivity-container')
])

@callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@callback(
    Output('datatable-interactivity-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
    
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []


if __name__ == '__main__':
    app.run(debug=True)
    
