from fastapi import FastAPI

app = FastAPI(title="DevOps Pipeline API")

@app.get("/")
def read_root():
    return {
        "status": "healthy", 
        "message": "Welcome to the Secure CI/CD Pipeline API"
    }
