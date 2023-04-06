FROM python:3.8.10

ADD drs_test.py .
ADD requirements.txt .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./drs_test.py"]
