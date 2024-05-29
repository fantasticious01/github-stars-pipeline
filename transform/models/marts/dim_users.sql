SELECT DISTINCT user
FROM {{ ref("stg_gharchive") }}