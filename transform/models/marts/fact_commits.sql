SELECT event_date, repo_id
From {{ ref("stg_gharchive") }}
WHERE event_type = 'Push' 