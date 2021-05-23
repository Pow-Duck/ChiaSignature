from fastapi import FastAPI, Response
from pydantic import BaseModel
import src.option as option
import src.plot as plot

app = FastAPI()


@app.get("/")
async def root():
    return "Chia Signature Version: 0.0.1 https://github.com/Pow-Duck/ChiaSignature"


class InputDataModel(BaseModel):
    farmer_public_key: str
    pool_key: str


@app.post("/signature", status_code=200)
async def signature(input_data: InputDataModel, response: Response):
    try:
        plot.create_plots(input_data.farmer_public_key, input_data.pool_key)
        (plot_id1, plot_memo2) = plot.create_plots(input_data.farmer_public_key, input_data.pool_key)
        return option.api_return(plot_id1, plot_memo2, True, None)
    except Exception as e:
        response.status_code = 500
        print("err: ", e)
        return option.api_return(None, None, False, "Failed to generate, please verify that the parameters are correct")
