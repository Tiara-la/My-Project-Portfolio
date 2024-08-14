# Customer-Segmentation-of-Retail-Online-Store
Customer experience is a key component in increasing sales numbers. Customers are important assets that must be kept up for a corporation or firm. Prioritizing customer service is one way to protect client loyalty. To ensure that service priority is right on target, this research was conducted on groups of consumers who are anticipated to have high business prospects. The 2011 retail online shop sales dataset with 379,980 records and eight char-acteristics was used. The length, recency, frequency, and monetary (LRFM) feature selection approach was used in the study process to select features for further segmentation using the K-Means data mining method to define consumer types. Following the completion of the research, clients were divided into four categories: Premium Loyalty, Inertia Loyalty, Latent Loyalty, and No Loyalty. The correct clustering results are displayed in the vali-dation test using the Silhouette Score Index technique, which yielded a score value of 0.943898. Based on the outcomes of this segmentation, business actors may prioritize providing clients with the proper service.

## Introduction

ADVANCES in information technology today make it easier for people to meet their needs. Convenience is obtained in various fields, one of which is shopping.  People use online shopping services, or also known as e-commerce.  E-commerce is another term for an online store, a shopping method involving social networking sites for buying and selling transactions. This activity eliminates the need for consumers and sellers to physically visit stores to view, buy, and sell goods. They can browse items online, make purchases, send payments, and items will be delivered to their homes using courier services without having to leave the comfort of their homes [1].

There are many types of online stores on the internet, both small and large.  Although there are many new online stores, not everyone is interested. Since customers do not see the store as an attractive place to make purchases or sales, many online stores fail to make a profit [2].  A big factor in increasing sales figures is customer experience. Consumers are more likely to believe in using online purchasing services when they have more experience [3]. 

E-commerce companies invest heavily in early detection [4]. Understanding consumer behaviour is very important for business actors. Every transaction that occurs on the internet between sellers and buyers can be recorded as historical data and can be used to predict customer behaviour [5]. Machine learning algorithms can be used to implement this strategy in online retail stores [6].  Sellers should be able to analyze the data to group customers by loyalty level so that information can be obtained to estimate the priority level of customer service. In addition, sellers can develop the best service strategy from these segmentations to maintain customer loyalty.

The K-Means algorithm had weaknesses in previous studies, particularly in estimating the number of clusters [7]. The Elbow method is useful for determining the best number of clusters [8].  Evaluating the SSE value is used to test the consistency of the corresponding number of clusters.  SSE is a technique for evaluating clusters based on the highest error.  In accordance with the concept of the Elbow technique applied to customer groupings using K-Means, SSE generates the maximum distance from a number of k value tests  [9].  The graph will eventually experience a considerable decrease with a curve known as the angle criterion. The optimal value k, then becomes its best number of clusters [10].  

This study used customer segmentation and the K-Means algorithm based on the LRFM (Length, Recency, Frequency, and Monetary) model for feature selection to classify potential customer values. Consumers will be segmented using the K-Means method based on payment information obtained from the LRFM model to determine the level of potential customers. The cluster validation test results will be carried out using the Silhouette Coefficient Index to determine the accuracy of the cluster.
Research Methods
Research methods are procedures that are followed as guidelines when conducting research so that the results can be explained scientifically.  The methods used in this study can be seen in Figure 1.


 
Figure 1. K-Means Method on Customer Segmentation

In the flowchart described above, the first stage carried out is data preprocessing.  Before starting the Data Mining process, data must be cleaned by removing duplicate data, identifying missing values or inconsistent data and correcting errors in the data [11].

After the data processing process, feature selection will be carried out using the L, R, F and M attributes.  The L RFM model was developed from an RFM model created by Arthur Hughes [12]. RFM is a model that is widely used in the process of segmenting customer behaviour. This RFM model consists of Recency, Frequency and Monetary. This model can measure the value of profitability or potential customers [13].  Furthermore, Chang and Tsay added one new variable, namely Length [12].  So that LRFM consists of Length, which is the period of the relationship between the customer and the company which is measured during the analysis period, Recency which is  the period from  the last date of the transaction made  by the customer to the last date  of the transaction at the company during the analysis period,   Frequency is the number of transactions made by the customer during the analyzed period, Monetary, i.e., the amount of money that the customer spends  during the transaction for the company during the analysis period.

The LRFM model has oversight because it is more suitable for analyzing the level of potential customers. The segmentation method with LRFM gives value according to the value of potential customers [12].  Variables in the clustering process will be selected according to the values of L, R, F and M. Then the data is carried out normalization. Data must be standardized to the same scale as the Standard Scaler method because the difference in data between L, R, F, and M is very large.

The segmentation or clustering stage is performed with the K-Means Clustering algorithm for k=1 to k=n.  K-Means is one of the clustering techniques often used to group data based on comparable qualities [14]. These data groups are called clusters. Each input is trained using K-Means to group to the nearest cluster. Based on its input data, K-Means uses weights and all their neighbours to dynamically update their destination functions [15].

The stage in the first K-Means method is to determine the number of clusters.  The number of clusters is determined using the Elbow method.  The Elbow method is used to determine the best number of clusters from the data set, identifying clusters in such a way that the total number of variants in the cluster or the number of squares of the clusters is minimized. This method is a visual method that starts with k = 2 and increases at each step by adding 1 to the value of k. At the value of k = 3, in the event of a sharp change inversely proportional to the previous value, the value before the change is considered the most appropriate number of clusters  [16].  In its use, the Elbow method uses the evaluation of SSE values.  SSE is a way of validating a cluster through the sum of squares of each cluster member towards its centre [17].  The farther the distance that forms the elbow point, the more optimal the number of clusters [18].  The SSE formula is as follows at Equation (1).

SSE=∑_(i=1)^k▒∑_(x∈C_i)▒〖〖dist〗^2 (m_i,x)〗																							(1)

The second step is randomly selecting the initial centroid according to the number of clusters [19]. Furthermore, the distance of the data to the centroid will be calculated by the euclidean distance formula at Equation (2).

dist(x,y)=√(∑_(i=1)^n▒(x_i-y_i )^2 )					 	  																			(2)

After the distance of each record is calculated by the euclidean distance formula, the centroid will be updated by calculating the average value of the value on each cluster. The process will repeat back to stage 3 if there is still data moving clusters or changes in centroid values [20].

The last step in the customer segmentation method is evaluation.  Evaluation is a step to measure the performance of the methods used. In this step use the Silhouette Coefficient Index score matrix. Silhouette Coefficient Index is one of the analytical methods to obtain validation values in a clustering method [21].

Result and discussion
Preprocessing Data
This study used online retail data from Kaggle in the period 04 January 2011 to 10 December 2011 there were 379980 data with 8 attributes in it. These attributes are Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID and Country. 

Before clustering, data pre-processing needs to be done by doing several stages including data cleansing, eliminating missing values, and removing duplicate data. Then data standardization is carried out with a standard scaler process used to standardise each variable's range of values.  The preprocessing process to the clustering process is carried out using the Google Collab IDE. 

Features Selection LRFM
The first process in customer segmentation is to retrieve specific data attributes to segment using the K-Means algorithm. These attributes are Invoice, StockCode, 	Description, Quantity, InvoiceDate, Price, Customer ID, and Country.  In taking attributes or feature selection in this study using LRFM method.

L is the Length which in this case is intended to be the period from the beginning to the last date the customer made the transaction to the company during the analysis period. The period taken in this study is data from January 2011 to December 2011. R is a Recency where in this case it is intended to span from the last date of the transaction made by the customer to the last date of the transaction at the company, which is December 10, 2011. F is a Frequency where in this case it is intended how often customers make transactions within the period of January 2011 to December 2011. Furthermore, M is Monetary where in this case it is intended how much money has been spent by customers in the period from January 2011 to December 2011. Then the data is divided into 2 parts, namely 80% training data and 20% test data. This data share uses train_test_split functions from Python's Sklearn library.

    
Figure 1. Length, Recency, Frequency and Monetary (LRFM) distribution chart
Customer Segmentation with K-Means Clustering
After data sharing, the data train will be used for training the K-Means model. In the segmentation process with K-Means, 9 clusters have been formed. In this test, the performance of each number of clusters is adjusted to the range of values in the Elbow method. Figure 1 is the result of testing with the Elbow method.
 
 
Figure 2. Elbow Chart Results

The results of the SSE calculation used to test the consistency of the corresponding number of clusters in the Elbow method can be seen in Table 1.

TABLE 1
SSE RESULTS ON THE ELBOW METHOD
Cluster	SSE
1	21219,99
2	16166,19
3	12264,03
4	9898,52
5	8349,98
6	6931,56
7	5905,93
8	5155,66
9	4554,50

Based on Figure 1, the decline is seen in cluster-1, cluster-2, cluster-3 and   cluster-4 which are characterized by the most and sharpest graph drops, while at later points there is a steady decline. Then the value of k used is 4.  Segmentation is done based on the LRFM attribute that we have specified. Table 2 shows the results of the clustering obtained.
TABLE 2
LRFM SEGMENTATION RESULTS
Customer ID	Length	Recency	Frequency	Monetary	Cluster
12346	0	325	2	1	3
12347	315	2	151	3598,21	2
12348	243	75	14	904,44	2
...	...	...	...	...	...
18283	334	3	756	2094,88	2
18287	159	42	70	1837,28	2


Based on Table 1 the subscriptions will be grouped into 4 categories [22] the subscriptions will be grouped into 4 categories:
	Premium Loyalty
The level of loyalty to customers if the level of attachment is so high that it can run in harmony with repurchase activity. 
	Inertia Loyalty
The level of loyalty to customers if there is a low attachment to a high repurchase.
	Latent Loyalty
The level of loyalty is hidden in customers if loyalty or attachment is relatively high but the repurchase rate is low.
	No Loyalty
The level of customer loyalty if the level of attachment is low and the purchasing activity is also low.

The results of cluster categorization can be seen in Table 3.

TABLE 3
CLUSTER CATEGORIZATION RESULTS
Customer ID	Length	Recency	Frequency	Monetary	Cluster	Label
12346	0	325	2	1	3	No Loyalty
12347	315	2	151	3598,21	2	Inertia Loyalty
12348	243	75	14	904,44	2	Inertia Loyalty
...	...	...	...	...	...	...
18283	334	3	756	2094,88	2	Inertia Loyalty
18287	159	42	70	1837,28	2	Inertia Loyalty
Evaluation
The result of calculating the value of the Silhouette Index (SI) between -1 to 1. If SI = 1, object i is already in the right cluster. If the value of SI = 0, then object i is between two clusters so that the object is not clear, it should be entered into cluster A or cluster B. However, if SI = -1 it means that the resulting cluster structure is overlapping, so object i is more appropriately inserted into another cluster [23]. Table 4 shows the SI calculation results and Figure 2 shows the SI graph.

TABLE 4
SILHOUETTE COEFFICIENT INDEX RESULTS ON K-MEANS CLUSTERING
Cluster	Silhouette Coefficients Index
1	0,978971
2	0,939537
3	0,913187
4	0,632766
5	0,473583
6	0,480639
7	0,478278
8	0,486042
9	0,405870

 
 
Figure 4. Silhouette Coefficient Index Graph
CONCLUSION
The e-commerce industry has grown rapidly which increases competition among online businesses.  One of the strategies carried out by business people in maintaining their business is improving the quality of customer service quality.  The management of the implementation of service priorities to customers must be adjusted to the level of loyalty. Therefore, a model is needed to analyse the potential customers' level to be able to group customers based on their loyalty level.  The K-Means algorithm and the LRFM method were selected in the study. The K-Means algorithm is used to segment payment behaviour so that the level of potential customers can be measured using LRFM as its feature selection. This segmentation is divided into four groups: Premium Loyalty, Inertia Loyalty, Latent Loyalty and No Loyalty.  Silhouette Score Index test got a result of 0.943898.  From the results of this segmentation, business actors can give priority to the right service to customers.
