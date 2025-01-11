#parallel mode
using Distributed; addprocs(4) # can be skipped if julia was started with -p
@everywhere using FlashWeave

#serial mode
#using FlashWeave

#ARGS array stores script arguments coming *after the script name*
counts_path_16S = ARGS[1]
counts_path_18S = ARGS[2]
meta_data_path = ARGS[3]
output_path = ARGS[4]
netw_results = learn_network([counts_path_16S, counts_path_18S], meta_data_path, sensitive=true, heterogeneous=true)
#results of this operation are discarded. makes sure results were generated correctly
G = graph(netw_results)
#save to file
save_network(output_path, netw_results)

