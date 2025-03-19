# Astronomical Event Visualizer

## Overview
The **Astronomical Event Visualizer** is a Python-based application designed to display and analyze celestial events. It provides interactive visualizations of astronomical phenomena such as planetary positions, eclipses, meteor showers, and more.

## Features
- **Celestial Event Visualization**: Graphical representation of astronomical events.
- **Planetary Positions**: Track the positions of planets in the solar system.
- **Eclipse Simulation**: Visualize solar and lunar eclipses.
- **Meteor Shower Data**: Display peak dates and visibility details for meteor showers.
- **Interactive UI**: User-friendly interface with zoom and pan features.
- **Time-based Animations**: Simulate celestial movements over time.

## Installation
To use the Astronomical Event Visualizer, follow these steps:

### Prerequisites
- Python 3.8+
- Required libraries: `matplotlib`, `numpy`, `pandas`, `skyfield`, `tkinter`

### Steps to Install
1. Clone the repository:
   ```sh
   git clone https://github.com/adityavpatil09/astronomical-event-visualizer.git
   cd astronomical-event-visualizer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Starting the Server
If the application includes a server component, follow these steps:

### **Check the Server Framework**
- If using **Flask**, **FastAPI**, or **Django**, ensure all dependencies are installed.

### **Starting the Server (Based on Framework)**

#### **Flask (Common for Lightweight APIs)**
If using Flask, start the server with:
```sh
python app.py
```
Or, if using `flask run`:
```sh
export FLASK_APP=app.py
flask run
```
By default, Flask runs on `http://127.0.0.1:5000/`.

#### **FastAPI (For High-Performance APIs)**
If using **FastAPI**, start the server with:
```sh
uvicorn app:app --reload
```
This runs on `http://127.0.0.1:8000/`.

#### **Django (For Full-Scale Web Apps)**
If using **Django**, run:
```sh
python manage.py runserver
```
This starts the server on `http://127.0.0.1:8000/`.

### **Open in a Browser**
Once the server is running, open:
- `http://127.0.0.1:5000/` for Flask
- `http://127.0.0.1:8000/` for FastAPI or Django

### **Debugging**
- If you see **port in use** errors, try changing the port:
  ```sh
  flask run --port=5050
  uvicorn app:app --port 8080
  python manage.py runserver 8080
  ```
- Use `--reload` for live updates while developing.

## Usage
1. **Launch the Application**: Run `python main.py`.
2. **Select an Astronomical Event**: Choose an event from the menu.
3. **Customize Date & Time**: Adjust the simulation settings.
4. **View and Analyze**: Observe celestial movements and events.

## Contributing
We welcome contributions! If you’d like to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push the changes: `git push origin feature-name`
5. Create a pull request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For any questions or suggestions, please reach out via GitHub issues.

---

Enjoy exploring the universe with **Astronomical Event Visualizer**! 🚀🌌

