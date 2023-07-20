from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routes.system.taxes import router as taxesRouter
from routes.system.quartierAffichage import router as quartierAffichageRouter

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