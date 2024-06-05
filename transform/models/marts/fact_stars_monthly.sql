SELECT
  d.date_month, 
  s.repo_id, 
  COUNT(*) AS count_stars, 
  lag(count_stars, 12) OVER (PARTITION BY s.repo_id ORDER BY d.date_month) AS last_year_count_stars, 
  count_stars / last_year_count_stars AS yoy_growth, 
FROM {{ ref('dim_date') }} AS d 
  LEFT JOIN {{ ref('fact_stars') }} AS s 
  ON d.date_month = DATE_TRUNC('month', s.event_date) 
GROUP BY 1, 2