#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:24:18 2020

@author: analyticengineering
"""

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
#from analyticsengineering.mysql_module import replace_to_sql_table
from analyticsengineering.mysql_module import insert_to_sql_table

dset=pd.read_csv('tempdata.csv')

dset.loc[:,'temp4F']=dset.loc[:,'temp4']*9/5+32
dset.loc[:,'temp17F']=dset.loc[:,'temp17']*9/5+32
dset.loc[:,'temp22F']=dset.loc[:,'temp22']*9/5+32

dset.drop(columns=['Unnamed: 0'], inplace=True)
#replace_to_sql_table('../config/dbfile.json','rasberrypi','camper3sensor', dset)
insert_to_sql_table('../config/dbfile.json','rasberrypi','camper3sensor17outside',dset,'replace',False)
output_file("temp.html")

TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
]

p=figure(plot_width=800, plot_height=400,tooltips=TOOLTIPS)
p.circle(dset.EPOCH,dset.temp4F,legend="Inside",color='black')
p.circle(dset.EPOCH,dset.temp17F,legend='Outside',color='blue')
p.circle(dset.EPOCH,dset.temp22F,legend='Inside',color='red')

p1=figure(plot_width=800, plot_height=400, y_range=(0,100),tooltips=TOOLTIPS)
p1.circle(dset.EPOCH,dset.humd4,color='black')
p1.circle(dset.EPOCH,dset.humd17,color='blue')
p1.circle(dset.EPOCH,dset.humd17,color='red')

show(column(p,p1))
