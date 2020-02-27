# stoke-futures

Predicting surf slightly well with ML

## Info

Using data from stoke-archives, I'm looking to predict the surf. The most important data is from the top 3 swells. Including their height, period and direction favorability (does the beach work best with that direction).

I don't have much data but the results have been okay so far.

## Predict

Most of the reason to have this historic data is for machine learning. So the attributes that're saved off are tailored to predicting future surf forecasts. Or, at least, what I think are important attributes for that.

Times are in UTC and are ISO format.

### Predict Endpoint

`POST /predict`

**Body:**

```json
{
  "data": [
    {
      "surfline_spot_id": "1",
      "name": "Blah",
      "timestamp": "Something",
      "swell1_height": 1.41,
      "swell1_period": 5,
      "swell1_is_favorable_direction": "N",
      "swell2_height": 1.77,
      "swell2_period": 12,
      "swell2_is_favorable_direction": "N",
      "swell3_height": 1.25,
      "swell3_period": 12,
      "swell3_is_favorable_direction": "N"
    }
  ]
}
```

**Response:**

```json
{
  "predictions": [
    2.6722583770751953
  ]
}
```
