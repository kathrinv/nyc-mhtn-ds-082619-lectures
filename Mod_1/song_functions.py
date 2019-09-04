#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:45:13 2019

@author: kathringo
"""

def find_by_name(name, data):
    for item in data:
        if 'album' in item:
            if item['album'] == name: 
                return item 
        else:
            if item['name'] == name:
                return item
            
def find_by_rank(rank, data):
    for item in data:
        if 'rank' in item:
            if int(item['rank']) == rank:
                return item['name']
        else:
            if int(item['number']) == rank:
                return item['album']
            
            
def find_by_year(year, data):
    names = []
    for item in data:
        if int(item['year']) == year:
            if 'album' in item:
                names.append(item['album'])
            else:
                names.append(item['name'])
    return names 

def find_by_years(start_year, end_year, data):
    names = []
    for item in data:
        if (int(start_year) <= int(item['year'])) and (int(end_year) >= int(item['year'])):
            if 'album' in item:
                names.append(item['album'])
            else:
                names.append(item['name'])
    return names

def find_by_ranks(start_rank, end_rank, data):
    names = []
    for item in data:
        if 'number' in item:
            if (int(start_rank) <= int(item['number'])) and (int(end_rank) >= int(item['number'])):
                names.append(item['album'])
        else:
            if (int(start_rank) <= int(item['rank'])) and (int(end_rank) >= int(item['rank'])):
                names.append(item['name'])
    return names

def artists(data):
    names = []
    for item in data:
        names.append(item['artist'])
    return names

def titles(data):
    titles = []
    for item in data: 
        if 'album' in item:
            titles.append(item['album'])
        else:
            titles.append(item['name'])
    return titles

def most_frequent_artist(data):
    artist_dict = {}
    
    for item in data:
        if item['artist'] in artist_dict:
            artist_dict[item['artist']]+=1
        else:
            artist_dict[item['artist']]=1
            
    item_max_value = max(artist_dict.values())
    return [k for k,v in artist_dict.items() if artist_dict[k] == item_max_value]


