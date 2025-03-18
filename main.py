from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from astropy.coordinates import get_sun, get_body, AltAz, EarthLocation, solar_system_ephemeris
from astropy.time import Time
import numpy as np
import plotly.graph_objs as go
import astropy.units as u
import os

app = FastAPI()

# CORS Middleware for frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Create necessary folders
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 Templates for frontend rendering
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/plotly-visualize/{object_name}/{date}")
def plotly_visualize(object_name: str, date: str, lat: float = 0.0, lon: float = 0.0):
    supported_objects = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]
    object_name = object_name.lower()

    if object_name not in supported_objects:
        raise HTTPException(status_code=404, detail="Object not supported.")

    times = Time(f"{date} 00:00") + np.linspace(0, 24, 100) * u.hour
    location = EarthLocation(lat=lat * u.deg, lon=lon * u.deg)
    altaz_frame = AltAz(obstime=times, location=location)

    with solar_system_ephemeris.set('builtin'):
        positions = get_sun(times).transform_to(altaz_frame) if object_name == 'sun' else get_body(object_name, times, location).transform_to(altaz_frame)

    altitudes = positions.alt.degree

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times.datetime, y=altitudes, mode='lines+markers'))

    fig.update_layout(
        title=f"{object_name.title()} Altitude on {date}",
        xaxis_title='Time (UTC)',
        yaxis_title='Altitude (degrees)',
        template='plotly_dark'
    )

    filename = f"static/{object_name}_interactive_{date}.html"
    fig.write_html(filename)

    return {
        "object": object_name,
        "date": date,
        "latitude": lat,
        "longitude": lon,
        "interactive_url": f"/{filename}"
    }
