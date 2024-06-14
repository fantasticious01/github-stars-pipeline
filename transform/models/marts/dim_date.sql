WITH DATE_SPINE AS ({{ dbt_utils.date_spine( 
  datepart="day", 
  start_date="cast('2011-02-01' as date)", 
  end_date="cast('2024-01-01' as date)" 
) }})

SELECT date_day,
  DATE_TRUNC('month', date_day) AS date_month
FROM Date_SPINE