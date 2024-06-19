SELECT DISTINCT 
  repo_id, 
  repo_name, 
  MIN(event_date) AS start_date, 
  LEAD(start_date) OVER (PARTITION BY repo_id ORDER BY start_date ASC) AS date_end 
FROM {{ ref("stg_gharchive") }}
GROUP BY 1, 2