List of issues to correct, 10/6/24

some notes in notebook. Also:
- want to redo pr2 on all available barcodes. we can see if the results agree.
- want to use the new dino classifications to see if we can actually get coherent "CM" and "NCM" breakdowns for the CCE, like
an appreciable number of ASVs in each. if we can't then combine categories into one large "NCM" if needed
- make sure noctiluca are characterized as heterotrophs since there's only red noctiluca in the CCE, green noctiluca in the western tropical Pacific and Indian Oceans only.

- rob's paper on biomass diversity curves. except as a proxy for biomass I can use relative abundance. Just scatterplot all the samples regardless of time or whatever.
- however (and this also goes for the rank abundance boxplots): I think there should be a distinction of shallow and DCM! eSNCMs seem to have greater avg abundances in the DCM. GNCM and pSNCM low.


ranked abundance boxplots:

***next steps***

Okay - next step is definitely to start assigning more genera or even families to mixotrophs, because right now 1) most of the classifications are too vague to work with 2) **if the classifications remain this vague, then I'm less confident than before that I'll find some nice & clear result in some paper of "yeah, it's ok to consider this entire genus/family/etc to be a certain type of mixotroph" - even in kareniaceans and dinotoms there's kleptoplastidic odd ones out, so that's important differences at the family level!**

step one: pass all asv trophic types through the name standardizer and define all the unknowables as... to be honest, anything without a genus&species name, but especially anything without a species and also less than 8 of 9 names. These are the unknowables to recluster.

But also - what's the point of reclustering? It still wouldn't be the **true** answer, only the most likely answer given data... and if, given the large amount of sequences in PR2 or some other large database, these 18Sv4 sequences **still** can't be confidently clustered (appear in the same clade in a given proportion of bootstraps, whatever) with (exclusively) a particular species, then that's useful information!! can't disregard that!!

And if that's the case, maybe it's better to leave the uncategorizables out of the analysis from the beginning - so, radically fewer ASVs at every subsequent step. All subsequent analyses focus only on the ASVs that are **most certain** to be mixotrophs, even if that's potentially as few as two or three per trophic type.
- would probably also leave the "rule based" assignments out aside from confirmed parasites, etc.
- are we so sure the parasite clades are exclusively parasites? maybe so-- reduced genomes may not be so easy to re-augment? Yes, this seems to be what defines the apicomplexans. Do I have Hematodinium in my non_mixo db?

Best things to do now is 
1) actually read Faure to see what the methodology; also Leles
2) for a given group I'm reading about, comb for any species/genera/clades which are mentioned in papers as likely mixotrophs but not in MDB or Faure.
3) comb the uncategorized or unknowable (as defined above) asvs and try to find any antiquated names/names unlikely to appear in MDB or in Faure.

===

asvs_per_species #notice that a lot of the old "unknowables" are back! some of the sequences were only classified as far as "Eukaryota" or "Eukaryota; Alveolata" ! Need to filter out every asv with a match score between \[4 and 0\] but also some of the rule based selectors need to be updated: Thalassomyces fagei and prob other members of its clades are parasites... so select some of the rule based ones for updating (match score -1 but still assigned)

or - select everything in trophic_types that has domain but otherwise only has 2 or 3 unique terms. 

Also filter metazoans, even if they're larvae and therefore small - NCOG is environmental DNA no clue if it came from larvae or not... what about size fractions...?

===


***improving our DB search methods***

honestly? current way is slow but not bad. all the matches are really good, on faure at least (matches are either score 7-8, and only score 4 when in some obscure chrysophyte clade that has different names between Faure, old PR2 (what the NCOG data is annotated with) and new PR2.
- can re-do taxonomy on those low matches as well as on the unassigned - both of these together can be our "unknowables"

ncog_trophic_types.loc\[ncog_trophic_types\["trophic_type"\] == "CM",\].to_csv("_out_faure_assigned_CM.tsv", sep="\t")

**maybe instead of doing what i have now, i can make a graph... an adjacency list. each name points to the next -- and if there is a complete path... it can combine some aspects of what we're doing now. 9 layer tree. break at first mismatch.**

**i mean we can literally start with the standardized DBs, and turn them into graphs. some problems: asv is not a complete path, it's patchy: so we may have to skip, and how would we know where to skip to?**

**besides, consider that we're matching backward... with 2 different match conditions. so a graph isn't the most appropriate option here.**

===

#one more thing: it looks like the PR2 used to make the taxonomy classifications was an old version (pre 2023)
#standardize_species_name("Eukaryota;Stramenopiles;Ochrophyta;Chrysophyceae;Chrysophyceae_X;Chrysophyceae_Clade-D;Hydrurus", delimiters=[";"])
#on latest version of PR2 taxonomy, Chrysophyceae_X is named Hydrurales and Chrysophyceae_Clade-D is named Hydruraceae

#so now the problem is that pr2 taxonomies are actually less complete than expected... 
#Ciliophora_X	Ciliophora_XX	Ciliophora_XXX
#i feel like even if the check fails we should be able to fill in the taxon... can overwrite later if needed?

#standardize_species_name("Eukaryota;Alveolata;Dinoflagellata;Dinophyceae;Dinophyceae_X;Dinophyceae_XX;Dinophyceae_XXX;Dinophyceae_XXX_sp.;")
#standardize_species_name('Eukaryota;Alveolata;Dinoflagellata;Syndiniales;Dino-Group-II;Dino-Group-II-Clade-36;Dino-Group-II-Clade-36_X;Dino-Group-II-Clade-36_X_sp.;')
#standardize_species_name("Eukaryota.Alveolata.Ciliophora.Intramacronucleata.Litostomatea.Cyclotrichia.Mesodiniidae.Mesodinium.Mesodinium.chamaeleon")
#standardize_species_name("Eukaryota;Alveolata;Ciliophora;Intramacronucleata;Litostomatea;Cyclotrichia;Mesodiniidae;Mesodinium", delimiters=[";"])
#standardize_species_name('Bispinodinium angelaceum', delimiters=[" "])
#standardize_species_name('Prorocentrum cf. balticum', delimiters=[" "])
#standardize_species_name('Spongodiscus resurgens', delimiters=[" "])
#standardize_species_name("Mesodinium;Mesodinium_rubrum;", delimiters=[";"])

===

**Result discrepancies between Oct and June analysis**

Did my new species-name-search method undercount CMs relative to June? There seems to be a lot less dino CM ASVs on the same data.

Load in the June data and see what the disjoint ASVs are--the ones that uniquely belong to June, and the ones that uniquely belong to Oct. See if the mistake was then or now.

Figured it out: It's all stuff where the ASV is classified as e.g. Gonyaulax fragilis but then the MDB only has other Gonyaulax species. This is predictable behavior: in June method I'd match genus first and break on species, but in Oct method I try to match species first, it doesn't work, then I never check genus

**is this ideal behavior? I'd say yes because if I have a reason to mark a genus as "probably wholly CM" or "CM-star" on the basis that it has mucus traps and mucus traps *probably* mean predation, then I should do so in one of the other databases**

**It's even worse when you look at the eSNCMs - I ended up classifying a bunch of stuff as Noctiluca scintillans for no reason - just because I searched "Noctiluca" first and it matched against "Noctilucaceae"**
