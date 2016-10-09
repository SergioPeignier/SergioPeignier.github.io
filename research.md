# Research 
## Bio-inspired data mining techniques incorporating Evolution-of-Evolution 
According to [Banzhaf et al. 2006](https://www.ncbi.nlm.nih.gov/pubmed/16894364), bio-inspired optimization algorithms could be improved by incorporating knowledge from molecular and evolutionary biology. A promising source of advances in optimization is one of the important phenomena in evolutionary biology: the dynamic evolution of the genome structure. Several studies showed for instance that an evolvable genome structure allows evolution to modify the effects that evolution operators (e.g., mutations) have on individuals, a phenomenon known as evolution of evolution [Hindré et al. 2012](https://www.ncbi.nlm.nih.gov/pubmed/22450379). We aim to take advantage of evolution of evolution mechanisms to achieve data mining tasks on dynamic data sets.

## Chameleoclust: Subspace Clustering Using Evolvable Genome Structure
A first major step in this project was to design and assess Chameleoclust, 
a subspace clustering evolutionnary algorithm. The subspace clustering task 
is recognized as more difficult than standard clustering since it requires 
to identify not only the clusters but also the various subspaces where the 
clusters hold. We proposed to tackle this problem with Chameleoclust, 
a bio-inspired algorithm that incorporates a genome with an evolvable structure
 to allow for evolution of evolution. The results obtained with this algorithm 
suggest that evolution of evolution, through an evolvable genome structure, is 
usefull to solve a difficult problem such as subspace clustering. The reader
 is refered to [Peignier et al.](http://dl.acm.org/citation.cfm?id=2754709) for
 a detailed description of Chameleoclust. This work was presented at the international 
ACM conference of Genetic and Evolutionary Computation Conference where it received the 
[best paper award](http://www.sigevo.org/gecco-2015/papers.html) in the category 
Evolutionary Machine Learning. 

## Applications
### Clustering of chemical compounds
In order to assess the algorithm we also decided to use it in a more practical application.
Chameleoclust was used to clusterize a set of chemical molecules described in a high 
dimensional space of physical and chemical descriptors. This work has been carried out 
in collaboration with the Theoretical Chemistry team of the Universidad Mayor de San Andres. Readers are refered to 
[Peignier and Cantañeta 2015](http://www.scielo.org.bo/scielo.php?script=sci_arttext&pid=S0250-54602015000500002) for a detailled description of this work (spanish version only).

### Live music performance
The clustering algorithm designed  was also applied to analyze human motion in order to 
perform live music.  Preliminary results were presented at the International Conference 
on Computer Simulation of Musical Creativity (CSMC 2016). More information about this 
application can be found in [Abernot et al. 2016](https://hal.inria.fr/hal-01368034). 
Two demonstration videos realized with the dance company Anouskan have also been uploaded on
Youtube:

+ [Anouskan 1](https://www.youtube.com/watch?v=p_eJFiQfW1E)
+ [Anouskan 2](https://www.youtube.com/watch?v=E85B1jJOiBQ)
