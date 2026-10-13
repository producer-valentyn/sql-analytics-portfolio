# SQL Analytics Portfolio

This repository contains SQL projects demonstrating analytical skills using complex queries and real-world business scenarios.
This repository contains SQL and Python projects demonstrating analytical skills using real-world business scenarios.

## Tools and Concepts
---

## 🛠 Tools and Concepts

- SQL
- BigQuery
- Python (Pandas, Matplotlib)
- Python (Pandas, Matplotlib, NumPy, Seaborn)
- CTE (Common Table Expressions)
- Window Functions
- Aggregations
@@ -16,131 +18,128 @@ This repository contains SQL projects demonstrating analytical skills using comp

---

# Projects

## Email Campaign Country Analysis
## 📊 Projects

**Goal**
### 📧 Email Campaign Country Analysis (SQL)

**Goal:**  
Analyze email campaign performance by country and account attributes.

**Business Questions**
**Business Questions:**
- Which countries generate the most accounts?
- Which countries receive the most emails?
- How do engagement metrics differ across countries?

* Which countries generate the most accounts?
* Which countries receive the most emails?
* How do email engagement metrics differ across segments?
**Metrics:**
- `account_cnt` — number of accounts  
- `sent_msg` — sent emails  
- `open_msg` — opened emails  
- `visit_msg` — visits after email  

**Metrics Calculated**
**Techniques Used:**
- CTEs for query structure  
- Window functions for totals  
- `DENSE_RANK()` for ranking  
- `UNION ALL` to combine metrics  
- Aggregations with `GROUP BY`  

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
---

**Dataset**
### 👤 User Session Analysis (SQL)

Data Analytics Mate training dataset.
Analysis of website sessions by:
- country
- device type

---

## User Session Analysis
Analysis of website sessions by country and device type.
### 🔄 Conversion Funnel Analysis (SQL)

## Conversion Funnel Analysis
Email marketing funnel analysis including send, open and visit stages.
Email marketing funnel analysis including:
- send → open → visit stages

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

### 🛒 Online Store Sales Analysis (Python)

**Goal:**  
Analyze sales data to identify key revenue drivers and regional performance.

**Dataset:**
- `events` — orders and sales  
- `products` — product categories  
- `countries` — country mapping  

**Key Metrics:**
- revenue  
- cost  
- profit  
- shipping_days  
- profit_margin  

**Analysis:**
- Revenue by category  
- Revenue by region  
- Revenue by channel  
- Top 10 countries  
- Shipping time analysis  
- Profit vs shipping time  
- Revenue trends  

**Tools:**
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

### 📈 Online Store Analytics Project (Python)

**Goal:**  
Analyze user behavior and sales performance.

**Dataset includes:**
- sessions  
- users  
- traffic sources  
- orders  
- device  
- regions  

**Analysis:**
- Sales trends  
- Sessions vs orders correlation  
- A/B test (registered vs non-registered users)  
- Conversion rate by device  
- Conversion by traffic channel  
- Sessions by continent  

**Key Insights:**
- Americas generate the most traffic and purchases  
- Desktop users have the highest conversion  
- Search channels drive most orders  
- Social traffic has high conversion rate  
- Strong correlation between sessions and orders (~0.99)  
- No significant difference in A/B test  

**Tools:**
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google BigQuery
- Tableau
- BigQuery
- Tableau  

---

## Interactive Dashboard
## 📊 Dashboards

Interactive Tableau Dashboard:
- Tableau Dashboard:  
https://public.tableau.com/app/profile/valentyn.fedyk/viz/OnlineStoreSalesDashboard_17730847310630/OnlineStoreSalesDashboard

---

More SQL projects will be added to this repository.
## 📌 Notes

More projects will be added over time.
