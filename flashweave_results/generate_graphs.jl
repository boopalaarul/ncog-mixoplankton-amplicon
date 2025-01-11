#parallel mode
using Distributed; addprocs(4) # can be skipped if julia was started with -p
@everywhere using FlashWeave

#serial mode
#using FlashWeave

#ARGS array stores script arguments coming *after the script name*
counts_path = ARGS[1]
meta_data_path = ARGS[2]
netw_results = learn_network(counts_path, meta_data_path, sensitive=true, heterogeneous=true)
#results of this operation are discarded. is that intentional?
G = graph(netw_results)
#save to file
save_network(ARGS[3], netw_results)

