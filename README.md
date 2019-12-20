# Time series analysis on IBM stock data and classification

Data Mining project of the homonymous course held at University of Pisa (Master's degree in Computer Science, spring/summer 2018). Equally relevant contributions were made by [anferico](https://github.com/anferico).

This work gathers concepts of time series analysis and sequential pattern mining of IBM stock data set, as well as classification and outlier detection tasks on the UCI Abalone data set.

## Time series analysis

The goal of this specific task is to find trends and similarities among the time series data set of IBM stocks. Each series represents the annual trend of IBM's stock prices during a period of time of about 50 years. By analyzing them, we plan to identify the exact years where the company had a decline, a substantial growth or a period of stability.

The source code can be found under the `Time series` folder.

## Sequential pattern mining

In this module of the project we are going to find meaningful, day-by-day patterns that somehow describe interesting oscillations of prices throughout the year. To do so, we are going to group the entire dataset into monthly time series and look for frequent patterns inside each of them. 

The corresponding Jupyter notebooks are [sequential_patterns.ipynb](sequential_patterns.ipynb) and [sequential_patterns_discretizzazione_subito.ipynb](sequential_patterns_discretizzazione_subito.ipynb).

## Outlier detection

This part of the project deals with the application of outliers identification techniques to extract the 1% of the most noisy data among the UCI Abalone data set. We conduct our experiments using three different algorithms: *Local Outlier Factor* (LOF), DBSCAN and depth-based approaches.

Results and source Jupyter notebooks can be found under the `outliers` folder.

# Written report

A written report of our experiments is available in Italian language ([report/report_DM2.pdf](report/report_DM2.pdf)).
