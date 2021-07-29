FROM python:3.8-slim-buster
WORKDIR C:\Users\Alistair\InterviewTests\exchange-rate-test
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . .
CMD [ "python3", "AlertMonitor.py"]