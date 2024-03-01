import plotly
import json
import re

def read_from_json(json_file_name):
    return plotly.io.read_json(json_file_name)


def read_from_html(html_file_name):
    with open(html_file_name) as f:
        html = f.read()
    call_arg_str = re.findall(r'Plotly\.newPlot\((.*)\)', html[-2**16:])[0]
    call_args = json.loads(f'[{call_arg_str}]')
    plotly_json = {'data': call_args[1], 'layout': call_args[2]}    
    return plotly.io.from_json(json.dumps(plotly_json))