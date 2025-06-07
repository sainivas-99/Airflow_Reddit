# Reddit-Bitcoin Data Collection Pipeline using Airflow and Docker
## Project Overview

This project is a fully automated data pipeline designed to collect live Reddit posts related to Bitcoin and retrieve the current Bitcoin price from the CoinGecko API. The pipeline is built using Apache Airflow for orchestration and runs inside a Docker environment. It is scheduled to run every hour and is conditionally controlled to proceed with downstream tasks only if at least 3 Reddit posts are collected in a cycle.

This pipeline is particularly useful as a data source for a downstream project focused on Natural Language Processing and Machine Learning-based sentiment analysis. That project uses the collected Reddit data to classify user sentiment and analyze its relationship to Bitcoin price trends.

You can view the sentiment analysis project here:  
([Reddit Sentiment Analysis using NLP and ML](https://github.com/sainivas-99/Stock-Prediction-using-Reddit-and-Twitter-Posts))

---

## Problem Statement

Public sentiment plays a crucial role in influencing cryptocurrency prices, especially Bitcoin. Reddit is a popular platform for real-time discussions among investors and traders. Extracting and analyzing this sentiment data at scale requires an automated, reliable, and maintainable pipeline. This project solves that problem by using Airflow to schedule and monitor data extraction, ensuring consistent and timely collection of sentiment data and Bitcoin pricing information.

---

## Techniques Used

- Apache Airflow for workflow orchestration and task scheduling
- Docker Compose for containerized deployment and environment consistency
- Reddit API (PRAW) for real-time Reddit data extraction
- CoinGecko API for live Bitcoin price retrieval
- Python scripting for data collection and processing
- Airflow SwitchOperator for conditional task execution
- Volume mounting for shared access to scripts and output data

---

## How It Works

1. The pipeline is triggered every hour by Apache Airflow.
2. Reddit posts related to Bitcoin are collected using the Reddit API from selected subreddits.
3. If at least 3 posts are collected, the pipeline continues:
   - Fetches the current price of Bitcoin using the CoinGecko API
   - Applies sentiment analysis on the collected Reddit posts
4. All outputs are saved in a shared directory mounted into the container to ensure persistent access.

---

## Target Achieved

- Built a production-ready pipeline that automates data collection with minimal manual intervention
- Ensured task efficiency using conditional logic in the Airflow DAG
- Scheduled the pipeline to run every hour to ensure near real-time data availability
- Maintained clean separation of concerns with modular Python scripts for each task
- Provided a consistent and replicable environment using Docker and Airflow

---

## Future Improvements

- Store data in a PostgreSQL or NoSQL database for long-term analysis
- Add data quality checks and alerts within Airflow
- Build a web dashboard to visualize sentiment trends alongside price data
- Expand the list of subreddits or keywords being tracked
