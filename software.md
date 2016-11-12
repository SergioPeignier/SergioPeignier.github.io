# Software and side projects
## Recent software developed

### Chameleoclust+ 
ChameleoClust+ is a bio-inspired algorithm implementing an evolvable genome structure, including several bio-like features such as a variable genome length, both functional and non-functional elements and mutation operators including chromosomal rearrangements. The main purpose of the design of ChameleoClust+ is to take advantage of the large degree of freedom provided by its evolvable structure to detect various number of clusters in subspaces of various dimensions.

Chameleoclust+ runs as a python module implemented internally in C++. The software can be downloaded in the webpage of the [EvoEvo Project](http://evoevo.liris.cnrs.fr/chameleoclust/).

### NayesDog: RSS reader with Naive Bayes powered recommendations

Have You Ever Felt Like You Were Drowning in an endless sea of data while you try to retrieve valuable information?  [NayesDog](https://github.com/MLdog/nayesdog) is a recent project developed with [Ilya Prokin](https://iprokin.github.io/index.html) that aims to provide a smart and helpful [RSS](https://en.wikipedia.org/wiki/RSS) reader.
As for most RSS readers, users can subscribe to their favorite feeds by entering the feed's URI and then the reader inspects and shows the chosen feeds when required. However, unlike most readers, NayesDog reads the entries and sorts them according to your preferences before showing them. Therefore users may focus on news that have been classified as more interesting for them by the algorithm. NayesDog first converts feed entries into  bag of words and then uses a Naive Bayes classifier to correlate words with the user preferences. Indeed, preference buttons (like / dislike) allows users to give a feedback to the algorithm regarding their preferences. The algorithm has been designed to adapt to evolvable preferences of users.

### Adventurous Social Science

[Adventurous Social Science](https://github.com/AdventurousSocialScience) is a recent project we started some months ago with [Moises Arizpe Rojo](https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=8&cad=rja&uact=8&ved=0ahUKEwiNtZKhxP7PAhUSahoKHV4aDOUQFgg4MAc&url=https%3A%2F%2Fmx.linkedin.com%2Fin%2Fmois%25C3%25A9s-arizpe-rojo-05640b99&usg=AFQjCNHw4CDnIzotIwSAADhwBiaI952-aQ&sig2=_PIR36AemgjiQ2Q95cgvCw&bvm=bv.136811127,d.d2s).  The name of this project describe it well, we try to address social science questions but in a more adventurous and less conventional way. Our first goal is always to build an interesting question we will address. The we proceeds to collect data from social network (e.g., through Twitter API) and then we apply state-of-the-art machine learning techniques to understand better the collected observations. Finally we analyze our results and compare them to stablished theory from Social Sciences in order to give a possible answer to our initial problem (e.g. [most recent posts](https://medium.com/adventurous-social-science)).

### Kernels for graph comparisons
The development of new drugs is a expensive and slow procedure. An important step in new molecules development is the "test" phase. This particularly slow and expensive step is significantly accelerated and cheapened if Structure-Activity Relationship Analysis (SAR) is applied to the tested chemical compounds. We studied here how to predict molecular activity with graph Kernels.
Kernels4graphs implements several kernel based methods for classification of graphs. A basic SVM algorithm and 4 different graph Kernels implementations (Nth order walk kernel, Geometric walk kernel, Markovian random walk kernel and Subtree kernel) are provided. The different approaches have been applied to Structure-Activity Relationship Analysis (SAR) to predict the molecular activity of differente chemical compounds described as labeled graphs.
This project can be found in its github [repository](https://github.com/SergioPeignier/kernels4graphs).

### Secondary structure RNA prediction