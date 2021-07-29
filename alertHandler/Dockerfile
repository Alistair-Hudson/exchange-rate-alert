FROM python:3.8-slim-buster
WORKDIR C:\Users\Alistair\InterviewTests\exchange-rate-test
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python3", "AlertHandler.py"]