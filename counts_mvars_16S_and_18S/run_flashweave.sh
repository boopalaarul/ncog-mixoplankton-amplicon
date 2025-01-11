#if this goes wrong: Ctrl+Z, use ps -l to identify process or parent process, then kill
SUCCESS=0

PATH_16S=asv_counts_16S_18Sv4_alldepths.tsv
PATH_18S=asv_counts_18Sv4_alldepths.tsv      
MVARS=mvars_18Sv4_alldepths.tsv

julia -p 4 generate_graphs.jl ${PATH_16S} ${PATH_18S} ${MVARS} network_16S_18Sv4_alldepths.gml

if [ $? -ne ${SUCCESS} ]
then
    exit $?
fi

PATH_16S=asv_counts_16S_18Sv4_MLD.tsv
PATH_18S=asv_counts_18Sv4_MLD.tsv        
MVARS=mvars_18Sv4_MLD.tsv

julia -p 4 generate_graphs.jl ${PATH_16S} ${PATH_18S} ${MVARS} network_16S_18Sv4_MLD.gml

if [ $? -ne ${SUCCESS} ]
then
    exit $?
fi

PATH_16S=asv_counts_16S_18Sv9_alldepths.tsv
PATH_18S=asv_counts_18Sv9_alldepths.tsv  
MVARS=mvars_18Sv9_alldepths.tsv

julia -p 4 generate_graphs.jl ${PATH_16S} ${PATH_18S} ${MVARS} network_16S_18Sv9_alldepths.gml

if [ $? -ne ${SUCCESS} ]
then
    exit $?
fi

PATH_16S=asv_counts_16S_18Sv9_MLD.tsv
PATH_18S=asv_counts_18Sv9_MLD.tsv        
MVARS=mvars_18Sv9_MLD.tsv        

julia -p 4 generate_graphs.jl ${PATH_16S} ${PATH_18S} ${MVARS} network_16S_18Sv9_MLD.gml
