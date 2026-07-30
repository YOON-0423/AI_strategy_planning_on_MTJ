
## workflow

To forecast research trends in MTJ-based neuromorphic computing, we first developed a node-based classification framework that represents the technological structure of the field. The framework defines the primary technological domains as Blue nodes and the detailed technological elements that enable or support each domain as Green nodes. Based on these node definitions, we constructed node-specific search queries and collected publication metadata through the Elsevier API. We then removed duplicate records to ensure that each publication contributed only once within each node dataset.

To calculate the Number of Mentions (NoM), we defined node-specific keywords and regular-expression patterns for a word frequency counter. The counter measured the occurrences of these expressions in publication titles, abstracts, and author keywords. We calculated the Total NoM for each publication as the sum of the Title NoM, Abstract NoM, and Author Keyword NoM.

We subsequently retrieved additional publication date information through the OpenAlex API and merged it with the publication-level NoM records. When the APIs did not provide sufficient date information, we manually verified and supplemented the missing dates using available publication sources. We then retained records with a Total NoM of at least 1 and converted the publication dates into a consistent year-month format.

Finally, we aggregated the publication-level NoM values into monthly time series for each Blue and Green node. We added months with no detected mentions to maintain a continuous monthly index and assigned a NoM value of zero to those months. We then applied double exponential smoothing (DES) to reduce short-term fluctuations and produce the finalized time-series dataset for the subsequent forecasting analysis.
