from fastapi import FastAPI
from app.services.processor import run_professor_code

app = FastAPI()

@app.get("/run")
def run_idp(start_seq: str, target: float = 0.3):
    """
    API endpoint to run professor's IDP Designer.
    Example: /run?start_seq=VLTKTKYT...&target=0.3
    """
    return run_professor_code(start_seq, target)












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
