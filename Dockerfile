FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
EXPOSE 5000
ENV ACCOUNT_SID=AC01ba999c6eea0e5eabdfd6e27115844d
ENV AUTH_TOKEN=0a6faabbc7d826ed739d73895aaaa830
CMD ["python", "./uber4movers/flask-sqlalchemy/run.py", "-p 5000"]
