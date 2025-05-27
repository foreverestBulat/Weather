FROM python:3.12

# WORKDIR /app

# WORKDIR /src

# COPY . /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000



# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc curl procps net-tools tini \
#     && apt-get -y clean \
#     && rm -rf /var/lib/apt/lists/* \
#     && pip install gunicorn

# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
