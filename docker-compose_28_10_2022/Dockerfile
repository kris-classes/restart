FROM python

RUN apt update && apt upgrade && pip install fastapi uvicorn redis
WORKDIR /app
COPY main.py main.py
COPY sakila.db sakila.db
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# To build: docker build -t my-api .
# To run: docker run -p 8000:8000 my-api
