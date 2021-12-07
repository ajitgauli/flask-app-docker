FROM python:3.8.0
RUN mkdir /usr/app/
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

COPY . /usr/app/
WORKDIR /usr/app/
EXPOSE 8080
RUN pip install -r requirements.txt
RUN pip install -r dev_requirements.txt

CMD ["python", "-m", "flask", "run"]
