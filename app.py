import numpy as np
import pandas as pd

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import dodge
from bokeh.embed import components


from bottle import Bottle, \
     template, debug, static_file

import os


def get_df_from_source():
    ''' get dataframes from the source dataset, only take the data of some big cities
    '''
    cities = ['上海', '北京', '杭州', '宁波', '保定', '南京', '苏州', '深圳', '厦门', '广州']
    df = pd.read_csv(dirname+'/dataset/AQI_merged.csv')
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date').reset_index(drop=True)
    df = df[df['type']=='AQI']
    return df

def draw_daily_AQI(mini_date, df):
    year = mini_date.split('-')[0]
    df_day = df[df['date']>=mini_date]
    source = ColumnDataSource(df_day)

    p = figure(x_axis_type="datetime", title="{}年AQI日均平均变化曲线".format(year), plot_width=1150, plot_height=400)
    p.line('date', '上海', line_color='blue', legend_label='上海', source=source)
    p.line('date', '北京', line_color='green', legend_label='北京', source=source)
    p.line('date', '深圳', line_color='orange', legend_label='深圳', source=source)

    p.legend.location = "top_right"
    p.add_tools(HoverTool(tooltips=[("AQI", "$y")]))

    return p
        
def draw_month_AQI(mini_date, df):
    year = mini_date.split('-')[0]
    df_day = df[df['date']>=mini_date]

    df_day['month'] = df_day['date'].apply(lambda x: x.strftime('%Y-%m'))
    df_month = df_day.groupby(by='month').mean().reset_index()

    source = ColumnDataSource(df_month)

    p = figure(x_range=list(df_month['month']), title="2019年AQI", plot_width=1150, plot_height=400)
    p.vbar(x=dodge('month', -0.25, range=p.x_range), top='上海', width=0.2, color="#c9d9d3", legend_label="上海", source=source)
    p.vbar(x=dodge('month', 0, range=p.x_range), top='北京', width=0.2, color="#718dbf", legend_label="北京", source=source)
    p.vbar(x=dodge('month', 0.25, range=p.x_range), top='深圳', width=0.2, color="#e84d60", legend_label="深圳", source=source)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.add_tools(HoverTool(tooltips=[("时间", "@month"), ("上海平均AQI", "@{上海}"), ("北京平均AQI", "@{北京}"), ("深圳平均AQI", "@{深圳}")]))
        
    return p

def draw_year_AQI(df):
    df['date_ym'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    df_month = df.groupby(by='date_ym').mean().reset_index()
    df_month['month'] = df_month['date_ym'].apply(lambda x: x.split('-')[-1])
    df_month['year'] = df_month['date_ym'].apply(lambda x: x.split('-')[0])

    df_2017 = df_month[df_month['year']=='2017'][['month', '北京']]
    df_2018 = df_month[df_month['year']=='2018'][['month', '北京']]
    df_2019 = df_month[df_month['year']=='2019'][['month', '北京']]

    source_2017 = ColumnDataSource(df_2017)
    source_2018 = ColumnDataSource(df_2018)
    source_2019 = ColumnDataSource(df_2019)

    p = figure(x_range=list(df_2017['month']), title="2017-2019年北京AQI对比", plot_width=1150, plot_height=400)

    p.vbar(x=dodge('month', -0.25, range=p.x_range), top='北京', width=0.2, color="#c9d9d3", legend_label="2017", source=source_2017)
    p.vbar(x=dodge('month', 0, range=p.x_range), top='北京', width=0.2, color="#718dbf", legend_label="2018", source=source_2018)
    p.vbar(x=dodge('month', 0.25, range=p.x_range), top='北京', width=0.2, color="#e84d60", legend_label="2019", source=source_2019)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    p.add_tools(HoverTool(tooltips=[("时间", "@month"), ("AQI", "@{北京}")]))

    return p

pd.options.mode.chained_assignment = None
dirname = '.'

app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/asset/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/asset/js')

@app.route('/')
def index():
    df = get_df_from_source()
    plot1 = draw_daily_AQI('2019-01-01', df=df)
    plot2 = draw_month_AQI('2019-01-01', df=df)
    plot3 = draw_year_AQI(df=df)
    plots_data = components((plot1, plot2, plot3))

    data = {
            "plot_script":plots_data[0],
            "plot1_div":plots_data[1][0],
            "plot2_div":plots_data[1][1],
            "plot3_div":plots_data[1][2],
            "developer_organization":"pythonlibrary.net"}
    return template('index', data = data)


if __name__ == "__main__":
    port=int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)