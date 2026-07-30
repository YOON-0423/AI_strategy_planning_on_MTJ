# AI strategic planning on MTJ


## Overview

This project investigates future research trends in MTJ-based neuromorphic compute for adaptive and online BCI using publication metadata. 
The study organizes the field into primary technological domains, called Blue nodes, and the detailed technological elements that enable or support them, called Green nodes.

The analysis constructs monthly Number of Mentions (NoM) time series for each node and uses these data to examine the future trajectories of interconnected technology areas. The overall framework combines publication metadata analysis, graph-based forecasting, quantitative gap analysis, and Gartner Hype Cycle interpretation to support strategic research planning.

## Research Workflow

The project follows four main stages:

**Node-based classification framework**
Define the primary technological domains and their supporting technological elements as Blue and Green nodes.

**Publication data preparation**
Collect publication metadata, calculate node-level NoM values, retrieve publication dates, construct monthly time series, and apply data smoothing.

**Trend forecasting and gap analysis**
Forecast the monthly NoM trends and quantify the relative differences between connected Blue and Green nodes.

**Strategic interpretation**
Organize the forecast results using the Gartner Hype Cycle and identify areas that require future research attention and monitoring.

## Repository Structure

**Data Preparation**

This folder contains the files, code, and intermediate results used to construct the monthly NoM time-series dataset. It covers node definitions, publication metadata collection, WFC keyword settings, NoM calculation, publication date retrieval, data integration, monthly time-series construction, and double exponential smoothing.

Detailed instructions and the processing workflow are available in the folder README.

**Scope**

The current repository primarily documents the data preparation process used to generate the input dataset for the subsequent forecasting analysis. The B-MTGNN execution, forecasted gap calculation, and Gartner Hype Cycle visualization follow this data preparation stage.

**Citation**

Citation information will be added after publication of the related research article.
