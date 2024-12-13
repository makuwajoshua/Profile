# Unsupervised Learning: PCA and Clustering for US Arrests Dataset

This repository demonstrates the application of unsupervised learning techniques, including Principal Component Analysis (PCA) and clustering, on the US Arrests dataset. 
The objective is to explore, understand, and segment the data effectively.

## 🗒️ Project Overview
This project explores the US Arrests dataset using unsupervised learning techniques to uncover patterns and structure within the data. The analysis includes:
- Exploratory Data Analysis (EDA)
- Dimensionality Reduction using PCA
- Clustering analysis

##  Dataset Information
The US Arrests dataset contains data on arrests in the US across different states for various crimes. It includes the following features:
- **Murder**: Murder arrests (per 100,000 residents)
- **Assault**: Assault arrests (per 100,000 residents)
- **UrbanPop**: Percent urban population
- **Rape**: Rape arrests (per 100,000 residents)

## Exploratory Data Analysis

### Data Understanding
- **Dimensions**: Examined the number of rows and columns.
- **Data Types**: Differentiated between numerical and categorical data.

### Data Cleaning
- No missing values, duplicates, or inconsistencies were found in the dataset.

### Data Visualization
- **Histograms**: Used to understand the distribution of each numerical variable.
- **Boxplots**: Helped identify the spread and potential outliers in the data.


### Relationship Identification
- **Correlation Analysis**: Measured the strength and direction of relationships between variables.

### Data Transformation
- The data was normalized to ensure that all variables contribute equally to the analysis, as most variables did not exhibit a natural distribution.

## Unsupervised Learning

### Principal Component Analysis (PCA)
- PCA was performed to reduce dimensionality while retaining most of the variance in the dataset.
- Visualized the principal components to identify dominant patterns.

### Clustering
- Applied clustering techniques (k-means and hierarchical clustering) to segment states into groups based on arrest patterns.
- Evaluated the optimal number of clusters using methods like the elbow method and silhouette scores.

## 📉 Results
- **PCA**: Reduced dimensionality with minimal loss of information.
- **Clustering**: Identified distinct clusters of states based on arrest data.


