import pandas as pd
import math

pr2_taxonomies = pd.read_csv("input_data_files/pr2_version_5.0.0_taxonomy.tsv", sep = "\t")
mdb = pd.read_csv("input_data_files/trophic_type_databases/MDB_data.tsv", sep = "\t")

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

"""Identify mixo by taxo: may use this in different notebooks"""

def identify_mixo_by_taxo(name_list : pd.Series, match_by_genus, threshold=5):

    #positional arguments, both required
    if name_list.str.contains("_").any() == False:
        print("No species names delimited by \'_\' found in input \'name_list\'.")
    
    #run the species check on each species.
    #if match by genus, get a list of genuses and match if at least 5 entries in combined species list match with that genus... 
    
    ###format pr2 data
    #nucleomorph and plastid entries are fine, seems like pr2 neive bayes classification may also include them.
    pr2_mixo_species = pr2_taxonomies[["species", "mixoplankton"]].dropna()
    #clean characters that could create false differences
    pr2_mixo_species["species"] = pr2_mixo_species["species"].str.strip(";.")
    pr2_mixo_species.columns = ["species", "MFT"]
                         
    ###format mdb data
    #some of the species names have the wrong unicode char (u'\xa0') for a space, replace those
    mdb_mixo_species = pd.DataFrame({
    "species" : mdb["Species Name"].apply(lambda x: "_".join(x.replace(u'\xa0', u' ').split(" ")).strip(".") ),
    "MFT" : mdb["MFT"].str.strip("*")
    })
    
    ###concat data and remove overlaps: they have to be combined like this because index not checked by drop_duplicates
    #move species name to index after that since it makes searching easier
    combined_mixo_species = pd.concat([pr2_mixo_species, mdb_mixo_species], ignore_index=True).drop_duplicates()
    combined_mixo_species = combined_mixo_species["MFT"].rename(index=combined_mixo_species["species"])

    ###frequency table of genus names
    #throw out genera that don't pass threshold
    #find majority MFT amogn species of passing genera
    if(match_by_genus):
        genus_frequencies = pd.Series(combined_mixo_species.index).apply(lambda x: x.split("_")[0]).value_counts()
        genus_frequencies = genus_frequencies[genus_frequencies >= threshold] #only "threshold or greater" allowed
        genus_majority_mft = pd.Series(genus_frequencies.index, index = genus_frequencies.index).apply(
            lambda x: combined_mixo_species[combined_mixo_species.index.str.contains(f"{x}_")].value_counts().index[0]
        )
                                                                 
    #first pass match species, second pass match genus? or 
    ###one pass: most specific name is either a genus or starts with one...
    def match_name(name):
        if name in combined_mixo_species.index:
            return(combined_mixo_species[name])
        #step into genus checks
        if(match_by_genus):
            if name in genus_majority_mft.index:
                return genus_majority_mft[name]
            #most specific name is neither a matching species name or matching genus name
            #could extract a matching genus name
            genus = name.split("_")[0]
            if genus in genus_majority_mft.index:
                return genus_majority_mft[genus]
        #no match
        return ""
    
    #series with easy to match/"expected" index & MFT values: either MFT directly or relatives                     
    return name_list.apply(match_name)