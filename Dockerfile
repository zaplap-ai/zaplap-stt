FROM python:3.12.0

WORKDIR ./

COPY ./ .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8000
CMD ["fastapi", "run", "main.py"]