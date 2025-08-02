from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, PlainTextResponse
from datetime import datetime

app = FastAPI()

# Helper to add ordinal suffix to day
def ordinal(n):
    return f"{n}{'th' if 11 <= n <= 13 else {1:'st', 2:'nd', 3:'rd'}.get(n % 10, 'th')}"

@app.get("/pixel.png")
async def tracking_pixel(request: Request):
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "Unknown")
    referrer = request.headers.get("referer", "No Referrer")
    query_params = dict(request.query_params)

    now = datetime.utcnow()
    time_str = f"Time: {ordinal(now.day)} {now.strftime('%B %Y')} at {now.strftime('%H:%M:%S')}"

    log_output = (
        f"{time_str}\n"
        f"IP: {ip}\n"
        f"User-Agent: {user_agent}\n"
        f"Referrer: {referrer}\n"
        f"Params: {query_params}\n"
        f"{'-'*40}\n"
    )

    print(log_output)

    return FileResponse("pixel.png", media_type="image/png")

@app.get("/favicon.ico")
def serve_favicon():
    return FileResponse("google-drive.ico", media_type="image/x-icon")

@app.get("/")
def home():
    return PlainTextResponse("✅ Tracking Pixel Server is running.\nVisit /pixel.png to test logging.")
