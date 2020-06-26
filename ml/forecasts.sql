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
        forecasts.swell3_direction,
        forecasts.swell4_height,
        forecasts.swell4_period,
        forecasts.swell4_direction,
        forecasts.swell5_height,
        forecasts.swell5_period,
        forecasts.swell5_direction,
        forecasts.swell6_height,
        forecasts.swell6_period,
        forecasts.swell6_direction
    FROM forecasts
    JOIN spots
        ON forecasts.spot_id = spots.id
) TO STDOUT DELIMITER ',' CSV HEADER
