# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR ./

# Copy project files
COPY ./ ./

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
