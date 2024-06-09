{% macro fact_event_type(event_type) -%} 
  select 
    event_date, 
    repo_id, 
    user 
  from {{ ref('stg_gharchive') }} 
  where event_type = '{{ event_type }}' 
{%- endmacro %}