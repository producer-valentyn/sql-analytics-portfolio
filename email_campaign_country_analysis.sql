WITH
/* ----------------------------------------------------------------------
   1) account_first_session / account_dim

   The DA.account table does not contain a created_date field.
   Therefore, the "account creation date" is defined as the first
   session date associated with the account.

   Country is also taken from the first session
   (session_params.country).
   ---------------------------------------------------------------------- */
account_first_session AS (
  SELECT
    acs.account_id,
    s.date AS account_created_date,
    sp.country,
    ROW_NUMBER() OVER (PARTITION BY acs.account_id ORDER BY s.date) AS rn
  FROM `data-analytics-mate.DA.account_session` acs
  JOIN `data-analytics-mate.DA.session` s
    ON acs.ga_session_id = s.ga_session_id
  JOIN `data-analytics-mate.DA.session_params` sp
    ON acs.ga_session_id = sp.ga_session_id
),

account_dim AS (
  SELECT
    account_id,
    account_created_date AS date,
    country
  FROM account_first_session
  WHERE rn = 1
),

/* ----------------------------------------------------------------------
   2) accounts_agg

   Account metrics are calculated separately from email metrics
   (as required by the task), so that the date for accounts represents
   the account creation date (first session).

   Here we calculate account_cnt, while email metrics are set to 0.
   ---------------------------------------------------------------------- */
accounts_agg AS (
  SELECT
    ad.date,
    ad.country,
    a.send_interval,
    a.is_verified,
    a.is_unsubscribed,
    COUNT(DISTINCT a.id) AS account_cnt,
    0 AS sent_msg,
    0 AS open_msg,
    0 AS visit_msg
  FROM `data-analytics-mate.DA.account` a
  JOIN account_dim ad
    ON a.id = ad.account_id
  GROUP BY 1,2,3,4,5
),

/* ----------------------------------------------------------------------
   3) emails_agg

   Email metrics are also calculated separately from account metrics:

   - date for an email = send date
     (session.date + sent_date days)

   - country is taken from session_params using ga_session_id

   Here we calculate sent/open/visit metrics,
   while account_cnt is set to 0.
   ---------------------------------------------------------------------- */
emails_agg AS (
  SELECT
    DATE_ADD(s.date, INTERVAL es.sent_date DAY) AS date,
    sp.country,
    a.send_interval,
    a.is_verified,
    a.is_unsubscribed,
    0 AS account_cnt,
    COUNT(DISTINCT es.id_message) AS sent_msg,
    COUNT(DISTINCT eo.id_message) AS open_msg,
    COUNT(DISTINCT ev.id_message) AS visit_msg
  FROM `data-analytics-mate.DA.email_sent` es
  JOIN `data-analytics-mate.DA.account` a
    ON es.id_account = a.id
  LEFT JOIN `data-analytics-mate.DA.email_open` eo
    ON es.id_message = eo.id_message
  LEFT JOIN `data-analytics-mate.DA.email_visit` ev
    ON es.id_message = ev.id_message

  -- Using account_session → session to obtain the base session date
  JOIN `data-analytics-mate.DA.account_session` acs
    ON es.id_account = acs.account_id
  JOIN `data-analytics-mate.DA.session` s
    ON acs.ga_session_id = s.ga_session_id

  -- Country is stored in session_params
  JOIN `data-analytics-mate.DA.session_params` sp
    ON acs.ga_session_id = sp.ga_session_id

  GROUP BY 1,2,3,4,5
),

/* ----------------------------------------------------------------------
   4) unioned + by_dims

   UNION is required by the task to combine the account-related
   metrics and the email-related metrics.

   After UNION, we aggregate using SUM(...) to:
   - combine account_cnt from accounts_agg
   - combine sent/open/visit from emails_agg

   This produces one row per
   (date, country, send_interval, is_verified, is_unsubscribed).
   ---------------------------------------------------------------------- */
unioned AS (
  SELECT * FROM accounts_agg
  UNION ALL
  SELECT * FROM emails_agg
),

by_dims AS (
  SELECT
    date,
    country,
    send_interval,
    is_verified,
    is_unsubscribed,
    SUM(account_cnt) AS account_cnt,
    SUM(sent_msg) AS sent_msg,
    SUM(open_msg) AS open_msg,
    SUM(visit_msg) AS visit_msg
  FROM unioned
  GROUP BY 1,2,3,4,5
),

/* ----------------------------------------------------------------------
   5) with_totals

   Country totals are calculated using window functions
   on top of the by_dims table:

   - total_country_account_cnt:
     total number of accounts per country

   - total_country_sent_cnt:
     total number of sent emails per country
   ---------------------------------------------------------------------- */
with_totals AS (
  SELECT
    *,
    SUM(account_cnt) OVER (PARTITION BY country) AS total_country_account_cnt,
    SUM(sent_msg)    OVER (PARTITION BY country) AS total_country_sent_cnt
  FROM by_dims
),

/* ----------------------------------------------------------------------
   6) with_ranks

   Country rankings are calculated using window functions
   (as required by the task).

   DENSE_RANK assigns the same rank to countries with equal totals
   without gaps in ranking.
   ---------------------------------------------------------------------- */
with_ranks AS (
  SELECT
    *,
    DENSE_RANK() OVER (ORDER BY total_country_account_cnt DESC) AS rank_total_country_account_cnt,
    DENSE_RANK() OVER (ORDER BY total_country_sent_cnt DESC)    AS rank_total_country_sent_cnt
  FROM with_totals
)

-- 7) Final selection: only top 10 countries
-- by total accounts or total sent emails
SELECT
  date,
  country,
  send_interval,
  is_verified,
  is_unsubscribed,
  account_cnt,
  sent_msg,
  open_msg,
  visit_msg,
  total_country_account_cnt,
  total_country_sent_cnt,
  rank_total_country_account_cnt,
  rank_total_country_sent_cnt
FROM with_ranks
WHERE rank_total_country_account_cnt <= 10
   OR rank_total_country_sent_cnt <= 10
ORDER BY date, country, send_interval, is_verified, is_unsubscribed;
