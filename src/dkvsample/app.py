from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from dkvsample.model.echo_model import EchoModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check() -> Response:
    '''
    Health check endpoint.

    Returns: 
    fastapi.Response: Basic response with 'status' value 'ok'.
    '''
    res = JSONResponse(
        content={'status': 'ok'},
        status_code=200
    )
    return res


@app.post("/echo")
async def echo_check(payload: EchoModel) -> Response:
    '''
    Echo endpoint.

    Parameters:
    payload (EchoModel): Request payload, contains 'skey1' and 'skey2' for testing.

    Returns:
    fastapi.Response: Response duplicating the request payload.
    '''
    return payload


def main(port: int) -> None:
    uvicorn.run(app, host='0.0.0.0', port=port)


def run_local() -> None:
    main(8320)


if __name__ == "__main__":
    main(8320)
