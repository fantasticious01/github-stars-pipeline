{% macro fact_event_type_monthly(fact_table) -%} 
SELECT
  d.date_month, 
  f.repo_id, 
  COUNT(*) AS year_count, 
  nullif((lag(year_count, 12) OVER (PARTITION BY f.repo_id ORDER BY d.date_month)), 0) AS last_year_count, 
  year_count / last_year_count -1 AS yoy_growth, 
FROM {{ ref('dim_date') }} AS d 
  LEFT JOIN {{ ref(fact_table) }} AS f
  ON d.date_month = DATE_TRUNC('month', f.event_date)
GROUP BY 1, 2


{%- endmacro %}