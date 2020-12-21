# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:52:36 2020

@author: anura
"""

import pandas as pd
import seaborn as sns


lbj_df = pd.read_excel('./data.xlsx', sheet_name=0)
lbj_df['Efficiency'] = (lbj_df['PTS'] + (lbj_df['AST']*1.5) + (lbj_df['TRB']*1.2) + (lbj_df['STL']*3) + (lbj_df['BLK']*3) - (lbj_df['TOV']) - (lbj_df['PF']*0.5))
sns.set_theme(style="darkgrid")
lbj = sns.relplot(x='MP', y='Efficiency', hue='Tm', data=lbj_df, palette=['brown','red','gold'])


mj_df = pd.read_excel('./data.xlsx', sheet_name=1)
mj_df['Efficiency'] = (mj_df['PTS'] + (mj_df['AST']*1.5) + (mj_df['TRB']*1.2) + (mj_df['STL']*3) + (mj_df['BLK']*3) - (mj_df['TOV']) - (mj_df['PF']*0.5))
sns.set_theme(style="darkgrid")
mj = sns.relplot(x='MP', y='Efficiency', hue='Tm', data=mj_df, palette=['red','blue'])


sc_df = pd.read_excel('./data.xlsx', sheet_name=2)
sc_df['Efficiency'] = (sc_df['PTS'] + (sc_df['AST']*1.5) + (sc_df['TRB']*1.2) + (sc_df['STL']*3) + (sc_df['BLK']*3) - (sc_df['TOV']) - (sc_df['PF']*0.5))
sns.set_theme(style="darkgrid")
sc = sns.relplot(x='MP', y='Efficiency', hue='Tm', data=sc_df, palette=['orange'])


cp_df = pd.read_excel('./data.xlsx', sheet_name=3)
cp_df['Efficiency'] = (cp_df['PTS'] + (cp_df['AST']*1.5) + (cp_df['TRB']*1.2) + (cp_df['STL']*3) + (cp_df['BLK']*3) - (cp_df['TOV']) - (cp_df['PF']*0.5))
sns.set_theme(style="darkgrid")
cp = sns.relplot(x='MP', y='Efficiency', hue='Name', data=cp_df)


avg_df = pd.read_excel('./data.xlsx', sheet_name=4)
sns.set_theme(style='darkgrid')
avgplt = sns.relplot(x='Avg_Efficiency', y='Name',hue='Name',data=avg_df)

old_df = pd.read_excel('./data.xlsx', sheet_name=5)
old_df['Efficiency'] = (old_df['PTS'] + (old_df['AST']*1.5) + (old_df['TRB']*1.2) - (old_df['PF']*0.5))
sns.set_theme(style='darkgrid')
oldplt = sns.relplot(x='MP', y='Efficiency', hue='Name', data=old_df)
oldplt.set(x_lim=(0,48),y_lim=(0,100))