# 1. Official lightweight Python base image
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your project files
COPY . .

# 5. The command to run your app (change app.py to your main file name, e.g. main.py)
CMD ["python", "app.py"]