# 1. Base Image
# Use an official Python slim image.
# Check your `runtime.txt` file and use that version if it's different!
FROM python:3.11-slim

# 2. Set Environment Variables
# Ensures that Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED=1
# Set the default port. Railway will override this with its own $PORT.
ENV PORT=8000

# 3. Set Working Directory
# All commands will run from this directory inside the container
WORKDIR /app

# 4. Install Dependencies
# Copy *only* the requirements file first to leverage Docker cache
COPY requirements.txt .
# Install production dependencies
RUN pip install -r requirements.txt

# 5. Copy Application Code
# Copy the rest of your project code into the container
# The .dockerignore file will ensure venv, .git, etc., are NOT copied
COPY . .

# 6. Run Django Collectstatic
# This gathers all your static files (CSS, JS, images)
RUN python manage.py collectstatic --no-input

# 7. Expose the Port
# Informs Docker that the container listens on this port
EXPOSE $PORT

# 8. Run the Application
# Use gunicorn to run the Django app.
# It binds to all interfaces (0.0.0.0) on the port provided by the $PORT env var.
# It looks for the wsgi application inside the `brandonsway` directory.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "brandonsway.wsgi"]