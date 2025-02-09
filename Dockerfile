# Use a lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 10000

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
