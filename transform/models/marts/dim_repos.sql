Select distinct repo_id,
    repo_name
from {{ ref("stg_gharchive") }}