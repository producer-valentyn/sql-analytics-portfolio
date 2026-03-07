WITH session_events AS (
    SELECT
        s.date,
        sp.country,
        COUNT(DISTINCT s.ga_session_id) AS sessions
    FROM `data-analytics-mate.DA.session` s
    JOIN `data-analytics-mate.DA.session_params` sp
        ON s.ga_session_id = sp.ga_session_id
    GROUP BY 1,2
),

email_sent AS (
    SELECT
        COUNT(DISTINCT id_message) AS sent_emails
    FROM `data-analytics-mate.DA.email_sent`
),

email_open AS (
    SELECT
        COUNT(DISTINCT id_message) AS opened_emails
    FROM `data-analytics-mate.DA.email_open`
),

email_visit AS (
    SELECT
        COUNT(DISTINCT id_message) AS visits_from_email
    FROM `data-analytics-mate.DA.email_visit`
)

SELECT
    e.sent_emails,
    o.opened_emails,
    v.visits_from_email,
    
    ROUND(o.opened_emails / e.sent_emails * 100,2) AS open_rate_pct,
    ROUND(v.visits_from_email / o.opened_emails * 100,2) AS visit_rate_pct

FROM email_sent e
JOIN email_open o ON TRUE
JOIN email_visit v ON TRUE;
