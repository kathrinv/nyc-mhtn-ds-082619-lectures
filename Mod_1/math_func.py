#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:26:25 2019

@author: kathringo
"""

def calc_mean(data):
    mean = sum(data)/len(data)
    return mean

def calc_median(data):
    n = len(data)
    data = sorted(data)
    if n % 2 != 0:
        median = data[n//2]
    else:
        median = (data[n//2-1] + data[n//2]) / 2
    return median

def calc_mode(data):
    mode_counts = {}
    for i in data:
        if i in mode_counts:
            mode_counts[i] += 1
        else:
            mode_counts[i] = 1
    print(mode_counts)
    max_count = max(mode_counts.values())
    mode = [k for k, v in mode_counts.items() if v == max_count]
    return mode

def calc_var(data):
    x_bar = calc_mean(data)
    return sum([(x - x_bar)**2 for x in data])/(len(data)-1)

def calc_std(data):
    variance = calc_var(data)
    return variance **(1/2)

def calc_covar(data1, data2):
    mean1 = calc_mean(data1)
    mean2 = calc_mean(data2)
    sum_of_products = 0
    for n in range(len(data1)):
        sum_of_products += (data1[n] - mean1) * (data2[n] - mean2)
    return sum_of_products / (len(data1)-1)

def calc_corr(data1, data2):
    covar = calc_covar(data1, data2)
    std1 = calc_std(data1)
    std2 = calc_std(data2)
    return covar / (std1 * std2)