SELECT REPLACE(type, 'Event', '') AS event_type,
  actor.login AS user,
  repo.id AS repo_id,
  repo.name AS repo_name,
  created_at AS event_date
FROM {{ source ("gharchive", "gharchive") }}