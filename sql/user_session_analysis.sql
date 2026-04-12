WITH sessions AS (
    SELECT
        s.date,
        sp.country,
        sp.device,
        COUNT(DISTINCT s.ga_session_id) AS session_cnt
    FROM `data-analytics-mate.DA.session` s
    JOIN `data-analytics-mate.DA.session_params` sp
        ON s.ga_session_id = sp.ga_session_id
    GROUP BY 1,2,3
),

daily_totals AS (
    SELECT
        date,
        SUM(session_cnt) AS total_sessions
    FROM sessions
    GROUP BY date
)

SELECT
    s.date,
    s.country,
    s.device,
    s.session_cnt,
    d.total_sessions,
    ROUND(s.session_cnt / d.total_sessions * 100, 2) AS session_share_pct
FROM sessions s
JOIN daily_totals d
    ON s.date = d.date
ORDER BY s.date, session_cnt DESC;
