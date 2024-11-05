MOD 1:
Data Warehouse:
storing large volumes of structured and unstructured data 

Architecture: 
three layers:
the source layer (where data is collected),
the staging layer (where data is processed), 
and the presentation layer (where data is made available for analysis).

Data Warehouse versus Data Marts: 
A data warehouse is a storage system for an entire organization, while data marts are smaller based on specific areas.

E-R Modeling versus Dimensional Modeling:
E-R (Entity-Relationship) modeling focuses on the relationships between data entities,
while dimensional modeling is designed for data warehouses.(analysis and things)

Data Warehouse Schemas:
Star Schema: A simple design where a central fact table is surrounded by dimension tables, resembling a star.
Snowflake Schema: An extension of the star schema where dimension tables are normalized in simpler tables.
Factless Fact Table: No data in dimension table only keys present in fact table.
Fact Constellation Schema: A complex schema that contains multiple fact tables sharing dimension tables.

ETL Process: The ETL (Extract, Transform, Load)
process consists of extracting data from sources,
transforming it into a suitable format,
and loading it into the data warehouse

OLAP vs OLTP:
olap: historical data, uses data warehouse, operations slice, dice ....,its not normalized
oltp: current data,uses rdbms, opartions insert, delete,...,its normalized

OLAP Operations:

Slice: Selecting a single dimension from a data cube to view.
Dice: Creating a sub-cube by selecting two or more dimensions.
Rollup: Aggregating data ,summarizing it at a higher level.
Drilldown: Breaking down data into more detail or lower levels
Pivot: Rotating the data axes in a data cube to provide an alternative view of the data.

MOD 2:

KDD: Knowledge Discovery Cycle
CISTMEP

DM Applications: Lie Detection, Market Basket Analysis

Type of attributes:
Qualitative Attributes such as Nominal,Binary and Ordinal Attributes.
Quantitative Attributes such as Numeric ,Discrete and Continuous Attributes.

Regression: given a particular dataset predict the range
a)linear regression:finds the best line to fit two variables, one var used to predict other var.
b)multiple linear regression: more attr. are involved.

Values that fall outside of the set of clusters may be considered outliers.

data transformation techniques:
data aggregation,discretization,smoothing, generalization, normalization

MOD 3:

Decision Tree Induction:
A decision tree splits data into branches based on feature values, making decisions at each split. This creates a tree-like structure

Naïve Bayesian Classification: Probabilistic algo
This classifier uses probability to predict categories based on prior knowledge of conditions related to each category.

Supervised: Naive Bayes(Classification and Regression), requires learning previous dataset to make predictions
Unsupervised: Clustering and Association, doesn't require.

Evaluating the Accuracy of a Classifier: 
Holdout & Random Subsampling:
In holdout, data is split into training and testing sets, while random subsampling repeats this process multiple times. 


MOD 4:

Cluster: subset of similar objects.
two types :
1) hierarchical -> agglomerative .....bottom-up,(dendrogram)
                                      types: single, complete, avg, centroid linkages
2) Partitioned ->k medoids ....manhattan distance  |x1-x2|+|y1-y2|
                 k means ......euclidean distance  sqrt[(x-a)^2 + (y-b)^2]


MOD 5 & 6:

Data mining is the discovery of knowledge and useful information from db.

Market basket analysis:
“if you buy a certain group of items, you are more (or less) likely to buy another groupof items”.

Apriori Algo: to find association rules, frequent item sets.

Web mining is an application of data mining to find patterns from the web data.

Data mining: extracting info from datasets. data accessed priv
Web mining: extracting info fromweb docs. data accessed publicly

Page rank algorithm is a way of measuring the importance of website pages.(Google Search to rank many web-sites)

C: outbound links
teleportation factor: set between 0 & 1.
damping factor is the probability that a web surfer will continue browsing by clicking on the linked pages.

association rule mining: used to identify relationships between items.
