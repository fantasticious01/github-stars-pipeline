{% macro fact_event_type(event_type) -%} 
  SELECT 
    event_date, 
    repo_id, 
    user 
  FROM {{ ref('stg_gharchive') }} 
  WHERE event_type = '{{ event_type }}' 
{%- endmacro %}