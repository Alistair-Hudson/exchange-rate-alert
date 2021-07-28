FROM python:3.8-slim-buster
WORKDIR C:\Users\Alistair\InterviewTests\exchange-rate-test
RUN pip install requests --user
RUN pip install dnspython --user
RUN pip install pymongo --user
RUN pip install pymongo[srv] --user
COPY . .
CMD [ "python3", "Main.py"]