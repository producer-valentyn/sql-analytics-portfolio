# SQL Analytics Portfolio

This repository contains SQL and Python projects demonstrating analytical skills using real-world business scenarios.

---

## 🛠 Tools and Concepts

- SQL
- BigQuery
- Python (Pandas, Matplotlib, NumPy, Seaborn)
- CTE (Common Table Expressions)
- Window Functions
- Aggregations
- Joins
- Data Transformation
- Exploratory Data Analysis

---

## 📊 Projects

### 📧 Email Campaign Country Analysis (SQL)

**Goal:**  
Analyze email campaign performance by country and account attributes.

**Business Questions:**
- Which countries generate the most accounts?
- Which countries receive the most emails?
- How do engagement metrics differ across countries?

**Metrics:**
- `account_cnt` — number of accounts  
- `sent_msg` — sent emails  
- `open_msg` — opened emails  
- `visit_msg` — visits after email  

**Techniques Used:**
- CTEs for query structure  
- Window functions for totals  
- `DENSE_RANK()` for ranking  
- `UNION ALL` to combine metrics  
- Aggregations with `GROUP BY`  

---

### 👤 User Session Analysis (SQL)

Analysis of website sessions by:
- country
- device type

---

### 🔄 Conversion Funnel Analysis (SQL)

Email marketing funnel analysis including:
- send → open → visit stages

---

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
- BigQuery
- Tableau  

---

## 📊 Dashboards

- Tableau Dashboard:  
https://public.tableau.com/app/profile/valentyn.fedyk/viz/OnlineStoreSalesDashboard_17730847310630/OnlineStoreSalesDashboard

---

## 📌 Notes

More projects will be added over time.
