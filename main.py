from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routes.system.taxes import router as taxesRouter
from routes.system.quartierAffichage import router as quartierAffichageRouter
from routes.system.tiers import router as tiersRouter
from routes.system.reglements import router as ReglementRouter
from routes.system.zoneAffichage import router as zoneAffichageRouter
from routes.system.produitConcession import router as produitConcessionRouter
from routes.system.emplacementAffichage import router as emplacementAffichageRouter
from routes.system.dispositif import router as dispositifRouter

from dotenv import load_dotenv
import os
load_dotenv()
allowed_origins_str = os.getenv("ALLOWED_ORIGINS")
origins = allowed_origins_str.split(',')


app = FastAPI(title="REGUL PUB", version="1.0.0", description="tHIS api IS DESIGNED TOP MANAGE ADS REGULATIONS",docs_url="/regul_pub/docs") 

@app.get('/', tags=["Welcome"], include_in_schema=False)
def welcome(): return {"Message": "Welcome to regul pub platform", "Version": "1.0.0", "Build by": "BAD INC"}

# use routes
app.include_router(quartierAffichageRouter)
app.include_router(taxesRouter)
app.include_router(tiersRouter)
app.include_router(ReglementRouter)
app.include_router(zoneAffichageRouter)
app.include_router(produitConcessionRouter)
app.include_router(emplacementAffichageRouter)
app.include_router(dispositifRouter)

# cors
app.add_middleware( 
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)