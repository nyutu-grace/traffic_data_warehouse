{{ config(materialized='view') }}


with vehicles as (
    select * from {{ref('data_model')}} 
),
vehicle_dist as ( select 
        vehicles.type,
        count(*) as total,
        sum(vehicles.avg_speed) as total_avg_speed,
        avg(vehicles.avg_speed) as avg_speed_per_type,
        (sum(vehicles.traveled_distance) / 1000 ) as total_traveled_d_km

        from
            vehicles
        
        group by vehicles.type
        
    )
    select * from vehicle_dist
