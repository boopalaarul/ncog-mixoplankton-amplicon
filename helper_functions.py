import pandas as pd
import math

"""Preprocessing functions"""

def proportional_frequencies(series : pd.Series):
    """When applied to columns or rows of a dataframe, return a new series where each value equals
    old value divided by sum of all values in that row/column."""
    if sum(series) != 0:
        return series / sum(series)
    return series

def shannon_index(series : pd.Series):
    """Takes in series representing ASV proportions in a sample and computes Shannon index."""
    #formula sum(pi * log(pi)), if pi = 0 then pi * log(pi) = 0
    #entropy 0 when all ASVs are 0 and one is 1, max = n*((1/n)*log(1/n)) when all n ASVs have equal proportions
    shannon = 0
    for proportion in series:
        if proportion != 0:
            #log default base = e
            shannon -= (proportion * math.log(proportion))
    return shannon

def asv_richness(series : pd.Series):
    """ASV richness = # nonzero ASVs *per column* in selected rows"""
    return sum(series != 0) #every cell where this condition is true = +1