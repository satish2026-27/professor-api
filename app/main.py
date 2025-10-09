from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict
from app.services.idpdesigner import run_professor_code   # adjust path if you moved it

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RunRequest(BaseModel):
    start_seq: str
    target_scaling_exp: Optional[float] = Field(default=0.3)
    target_rg: Optional[float] = None
    target_asphericity: Optional[float] = Field(default=0.3)
    buffer_size: int = 2
    disorder_weight: float = 0.5
    compaction_weight: float = 0.5
    max_edit_percentage: float = 0.15
    tolerance: float = 0.01
    c: float = 0.003
    penalty: float = 0.01
    pH: float = 7.0
    boundaries: Optional[Dict[str, tuple]] = None

@app.post("/run")
def run_idp(req: RunRequest):
    out = run_professor_code(**req.model_dump())
    if not out.get("ok"):
        raise HTTPException(status_code=400, detail=out.get("error", "Unknown error"))
    return out


'''from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.services.processor import run_professor_code

app = FastAPI()

#---CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/run")
def run_idp(start_seq: str, target: float = 0.3):
    """
    API endpoint to run professor's IDP Designer.
    Example: /run?start_seq=VLTKTKYT...&target=0.3
    """
    return run_professor_code(start_seq, target)

#new:post endpoint
class RunPayload(BaseModel):
    start_seq: str
    target: float
    tolerance: float = 0.01
    scalingMethod: str = "exp"
    bufferSize: int = 2
    penalty: float = 0.01


@app.post("/run")
async def run(payload: RunPayload):
    result = run_professor_code(
        start_seq=payload.start_seq,
        target=payload.target,
        tolerance=payload.tolerance,
        scalingMethod=payload.scalingMethod,
        bufferSize=payload.bufferSize,
        penalty=payload.penalty,
    )
'''#    return result













#from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
#from app.core.config import settings
#from app.core.logging import setup_logging
#from app.api.routes.health import router as health_router
#from app.api.routes.process import router as process_router
#from app.api.routes.files import router as files_router

#logger = setup_logging(settings.APP_NAME)

#def create_app() -> FastAPI:
 #   app = FastAPI(
  #      title=settings.APP_NAME,
   #     version=settings.APP_VERSION,
   #     docs_url=f"{settings.API_PREFIX}/docs",
   #     openapi_url=f"{settings.API_PREFIX}/openapi.json",
    #)

#       allow_origins=settings.CORS_ORIGINS,
 #       allow_credentials=True,
  #      allow_methods=["*"],
 #       allow_headers=["*"],
  #  )

   # app.include_router(health_router, prefix=settings.API_PREFIX)
    #app.include_router(process_router, prefix=settings.API_PREFIX)
   # app.include_router(files_router, prefix=settings.API_PREFIX)

   # return app

#app = create_app()
