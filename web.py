from starlette.applications import Starlette
from starlette.responses import JSONResponse
from fastai.tabular import (
    load_learner,
    DataFrame
)
from pathlib import Path

path = Path('ml')
learn = load_learner(path)
app = Starlette()

@app.route("/predict", methods=["POST"])
async def classify_url(request):
    json = await request.json()
    data = json['data']
    df = DataFrame.from_dict(data)

    predictions = []
    for _, row in df.iterrows():
        _, _, tensor = learn.predict(row)
        height = tensor.item()
        predictions.append(height)

    return JSONResponse({'predictions': predictions})