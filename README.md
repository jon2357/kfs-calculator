# kfs-calculator
Back end calculator for calculating KFS investment opportunities. Currently as a POC.

## Docker Commands
docker build --tag kfs .
docker run -dp 8080:80 --name kfsapi kfs
docker logs -ft kfsapi 
docker rm -f kfsapi

## Non-Docker Run commands
uvicorn app.main:app --reload --port 8000
## Testing Commands
http://localhost:8000/docs
curl http://localhost

http://127.0.0.1:8000/calculator/assessmentQuick?arv=35&pp=115&rc=10


uvicorn app.main:app --reload 