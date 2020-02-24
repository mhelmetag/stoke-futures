COPY (
    SELECT
        spots.surfline_spot_id,
        spots.name,
        spots.favorable_swells,
        forecasts.timestamp,
        forecasts.am_min_height,
        forecasts.am_max_height,
        forecasts.pm_min_height,
        forecasts.pm_max_height,
        forecasts.swell1_height,
        forecasts.swell1_period,
        forecasts.swell1_direction,
        forecasts.swell2_height,
        forecasts.swell2_period,
        forecasts.swell2_direction,
        forecasts.swell3_height,
        forecasts.swell3_period,
        forecasts.swell3_direction
    FROM forecasts
    JOIN spots
        ON forecasts.spot_id = spots.id
) TO STDOUT DELIMITER ',' CSV HEADER