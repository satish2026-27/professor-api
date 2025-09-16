from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from app.api.deps import auth_guard
from app.services.processor import processor

router = APIRouter(prefix="/process", tags=["process"])

class ProcessIn(BaseModel):
    data: Dict[str, Any] = Field(default_factory=dict, description="Generic input payload")

class ProcessOut(BaseModel):
    ok: bool
    summary: Optional[str] = None
    note: Optional[str] = None
    received: Dict[str, Any]

@router.post("", response_model=ProcessOut, dependencies=[Depends(auth_guard)])
def process_sync(body: ProcessIn):
    out = processor.process(body.data)
    return ProcessOut(**out)

def _heavy_job(data: Dict[str, Any]):
    processor.process_heavy(data)

@router.post("/async", response_model=dict, dependencies=[Depends(auth_guard)])
def process_async(body: ProcessIn, tasks: BackgroundTasks):
    tasks.add_task(_heavy_job, body.data)
    return {"queued": True}
