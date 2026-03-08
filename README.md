# SQL Analytics Portfolio

This repository contains SQL projects demonstrating analytical skills using complex queries and real-world business scenarios.

## Tools and Concepts

- SQL
- BigQuery
- Python (Pandas, Matplotlib)
- CTE (Common Table Expressions)
- Window Functions
- Aggregations
- Joins
- Data Transformation
- Exploratory Data Analysis

---

# Projects

## Email Campaign Country Analysis

**Goal**

Analyze email campaign performance by country and account attributes.

**Business Questions**

* Which countries generate the most accounts?
* Which countries receive the most emails?
* How do email engagement metrics differ across segments?

**Metrics Calculated**

* account_cnt — number of accounts
* sent_msg — number of sent emails
* open_msg — number of opened emails
* visit_msg — number of visits after email

**Key SQL Techniques**

* CTEs for structured query logic
* Window functions for country-level totals
* DENSE_RANK() for ranking top countries
* UNION ALL for combining account and email metrics
* Aggregation with GROUP BY

**Dataset**

Data Analytics Mate training dataset.

---

## User Session Analysis
Analysis of website sessions by country and device type.

## Conversion Funnel Analysis
Email marketing funnel analysis including send, open and visit stages.

---

More SQL projects will be added to this repository.
