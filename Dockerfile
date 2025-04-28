FROM python:3.12.0

WORKDIR ./

COPY ./ .
RUN python -m venv /venv
RUN source venv/bin/activate
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 8000
RUN uvicorn main:app --host 0.0.0.0 --port 8000
