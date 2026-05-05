# Python 3.9 environment
FROM python:3.9-slim

# internal folder where our app will live
WORKDIR /usr/src/app

# installs dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code files into container
COPY . .

# app inside listens on 8000
EXPOSE 8000

# Startup cmd
#--host 0.0.0.0 allows external traffic
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]