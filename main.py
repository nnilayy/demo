from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from datetime import datetime
import os

app = FastAPI()

LOG_FILE = "logs/pixel_log.txt"
os.makedirs("logs", exist_ok=True)

@app.get("/pixel.png")
async def tracking_pixel(request: Request):
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "Unknown")
    referrer = request.headers.get("referer", "No Referrer")
    query_params = dict(request.query_params)

    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.utcnow()}] IP: {ip} | UA: {user_agent} | Ref: {referrer} | Params: {query_params}\n")

    return FileResponse("pixel.png", media_type="image/png")

# 👇 ADD THIS TO FIX FAVICON ERRORS
@app.get("/favicon.ico")
@app.get("/favicon.png")
async def ignore_favicon():
    return Response(status_code=204)
