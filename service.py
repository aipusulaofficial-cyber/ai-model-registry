from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from opentelemetry import trace
from registry_domain import *
try:
 from opentelemetry.sdk.resources import Resource
 from opentelemetry.sdk.trace import TracerProvider
 from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
 p=TracerProvider(resource=Resource.create({"service.name":"ai-model-registry"}));p.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()));trace.set_tracer_provider(p)
except Exception: pass
app=FastAPI(title="ai-model-registry",version="1.0.0");tracer=trace.get_tracer("ai-model-registry")
class Request(BaseModel): key:str; payload:dict={}
@app.get("/health/live")
def live(): return {"status":"ok"}
@app.get("/health/ready")
def ready(): return {"status":"ready"}
@app.post("/v1/registry")
def handle(r:Request):
 with tracer.start_as_current_span("ai-model-registry.domain"):
  try: v=Version(r.key,r.payload.get("version","1"),r.payload.get("digest",""));return {"model":v.model,"version":v.version,"lifecycle":v.lifecycle}
  except (ValueError,KeyError,RuntimeError) as e: raise HTTPException(status_code=400,detail=str(e)) from e
