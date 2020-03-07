import csv

def main():
    new_header_row = ['surfline_spot_id', 'name', 'timestamp', 'avg_height', 'swell1_height', 'swell1_period', 'swell1_direction', 'swell1_is_favorable_direction', 'swell2_height', 'swell2_period', 'swell2_direction', 'swell2_is_favorable_direction', 'swell3_height', 'swell3_period', 'swell3_direction', 'swell3_is_favorable_direction']
    new_rows = [new_header_row]

    # surfline_spot_id,name,favorable_swells,timestamp,am_min_height,am_max_height,pm_min_height,pm_max_height,swell1_height,swell1_period,swell1_direction,swell2_height,swell2_period,swell2_direction,swell3_height,swell3_period,swell3_direction
    with open('ml/raw_forecasts.csv') as raw_forecasts_csvfile:
        reader = csv.reader(raw_forecasts_csvfile, delimiter=',', quotechar='"')
        header = True
        for row in reader:
            if header:
                header = False
            else:
                favorable_swells = row[2]
                new_row = [
                    row[0],
                    row[1],
                    row[3],
                    average_height(int(row[4]), int(row[5]), int(row[6]), int(row[7])),
                    row[8],
                    row[9],
                    row[10],
                    is_favorable_direction(favorable_swells, convert_degrees_to_direction(float(row[10]))),
                    row[11],
                    row[12],
                    row[13],
                    is_favorable_direction(favorable_swells, convert_degrees_to_direction(float(row[13]))),
                    row[14],
                    row[15],
                    row[16],
                    is_favorable_direction(favorable_swells, convert_degrees_to_direction(float(row[16])))
                ]

                new_rows.append(new_row)

    with open('ml/forecasts.csv', 'w') as forecasts_csvfile:
        writer = csv.writer(forecasts_csvfile)
        writer.writerows(new_rows)

def convert_degrees_to_direction(degrees):
    if degrees >= 11.25 and degrees < 33.75:
        return 'NNE'
    elif degrees >= 33.75 and degrees < 56.25:
        return 'NE'
    elif degrees >= 56.25 and degrees < 78.75:
        return 'ENE'
    elif degrees >= 78.75 and degrees < 101.25:
        return 'E'
    elif degrees >= 101.25 and degrees < 123.75:
        return 'ESE'
    elif degrees >= 123.75 and degrees < 146.25:
        return 'SE'
    elif degrees >= 146.25 and degrees < 168.75:
        return 'SSE'
    elif degrees >= 168.75 and degrees < 191.25:
        return 'S'
    elif degrees >= 191.25 and degrees < 213.75:
        return 'SSW'
    elif degrees >= 213.75 and degrees < 236.25:
        return 'SW'
    elif degrees >= 236.25 and degrees < 258.75:
        return 'WSW'
    elif degrees >= 258.75 and degrees < 281.25:
        return 'W'
    elif degrees >= 281.25 and degrees < 303.75:
        return 'WNW'
    elif degrees >= 303.75 and degrees < 326.25:
        return 'NW'
    elif degrees >= 326.25 and degrees < 348.75:
        return 'NNW'
    else:
        return 'Unknown'

def is_favorable_direction(favorable_swells, direction):
    favorable_swell_directions = favorable_swells.replace('{', '').replace('}', '').split(',')

    if direction in favorable_swell_directions:
        return 'Y'
    else:
        return 'N'

def average_height(am_min, am_max, pm_min, pm_max):
    return (am_min + am_max + pm_min + pm_max) / 4

main()