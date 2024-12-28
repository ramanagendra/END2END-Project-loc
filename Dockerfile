FRom python:3.8-slim-buster
WORKDIR / service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txtENTRYPOINT ["python3", "app.py"]