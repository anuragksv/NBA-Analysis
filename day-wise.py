# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 11:33:29 2020

@author: anura
"""

from nba_api.stats.endpoints import boxscoretraditionalv2
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

def min_int(arg):
    minuite, sec = map(int, arg.split(':'))
    if sec >= 30: minuite += 1
    return minuite

def efficiency_plot(gameID):
    stat_req = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id = gameID)
    main_df = stat_req.player_stats.get_data_frame()

    stat_df = main_df[['TEAM_ABBREVIATION','PLAYER_NAME','MIN','PTS','AST','REB','STL','BLK','TO','PF']]

    df = stat_df[stat_df['PTS'] >= 0]

    df['Efficiency'] = (df['PTS'] + (df['AST']*1.5) + (df['REB']*1.2) + (df['STL']*3) + (df['BLK']*3) - (df['TO']) - (df['PF']*0.5))

    df['MIN'] = df['MIN'].apply(min_int)

    sns.set_theme(style="darkgrid")
    sns.relplot(x='MIN', y='Efficiency', hue='TEAM_ABBREVIATION', data=df)

def driver_code(x, no):
    for i in range(no):
        efficiency_plot('00'+str(x))
        print('00'+str(x))
        x += 1


st_game = int(input('Enter first game ID: '))
num = int(input('Enter number of games: '))
driver_code(st_game, num)
