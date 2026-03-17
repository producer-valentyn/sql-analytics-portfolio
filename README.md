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
## Online Store Sales Analysis (Python)

### Goal
Analyze online store sales data to identify key revenue drivers, regional performance, and customer purchasing patterns.

### Dataset
Three datasets were used:
- events — order and sales information
- products — product categories
- countries — country and region mapping

### Key Metrics
- revenue
- cost
- profit
- shipping_days
- profit_margin

### Analysis Performed
- Revenue by product category
- Revenue by region
- Revenue by sales channel
- Top 10 countries by revenue
- Shipping time analysis
- Profit vs shipping time relationship
- Revenue trends over time
- Revenue by day of week

### Tools
- Python
- Pandas
- Matplotlib

---

# Online Store Analytics Project (Python)

## Goal
Analyze online store user behavior and sales performance to identify key drivers of revenue, traffic efficiency, and customer purchasing patterns.

## Dataset
Data was extracted from Google BigQuery and includes information about:

- sessions
- users
- traffic sources
- orders
- device type
- geographic regions

## Analysis Performed

- Sales trends over time
- Correlation between sessions and orders
- A/B test: registered vs non-registered users
- Conversion rate by device
- Conversion rate by traffic channel
- Sessions distribution by continent
- Orders by device and traffic source

## Key Insights

- The Americas region generates the highest share of traffic and purchases.
- Desktop users generate the majority of orders and have the highest conversion rate.
- Search channels (Organic and Paid Search) generate a large share of orders.
- Social traffic shows the highest conversion rate among channels.
- There is a very strong correlation between sessions and orders (≈0.99).
- The A/B test shows no statistically significant difference between registered and non-registered users.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google BigQuery
- Tableau

## Interactive Dashboard

Interactive Tableau Dashboard:
https://public.tableau.com/app/profile/valentyn.fedyk/viz/OnlineStoreSalesDashboard_17730847310630/OnlineStoreSalesDashboard
---

More SQL projects will be added to this repository.
