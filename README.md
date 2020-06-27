# stoke-futures

Predicting surf slightly well with ML

## Info

Using data from stoke-archives, I'm looking to predict the surf. The most important data is from the top 6 swells. Including their height, period and direction favorability (does the beach work best with that direction).

I don't have much data but the results have been okay so far.

## Predict

Given a set of swell data, a set of predictions for nearshore wave heights will be returned in the same order as received.

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
      "swell1_is_favorable_direction": "Y",
      "swell2_height": 1.77,
      "swell2_period": 12,
      "swell2_is_favorable_direction": "N",
      "swell3_height": 1.25,
      "swell3_period": 12,
      "swell3_is_favorable_direction": "Y",
      "swell4_height": 0,
      "swell4_period": 0,
      "swell4_is_favorable_direction": "N",
      "swell5_height": 0,
      "swell5_period": 0,
      "swell5_is_favorable_direction": "N",
      "swell6_height": 0,
      "swell6_period": 0,
      "swell6_is_favorable_direction": "N"
    }
  ]
}
```

**Response:**

```json
{
  "predictions": [2.6722583770751953]
}
```
