FROM python:3.12

COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/app/main.py"]