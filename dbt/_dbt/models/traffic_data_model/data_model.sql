
{{ config(materialized='view') }}

with source_data as (

    select * from vehicles

)

select *
from source_data
