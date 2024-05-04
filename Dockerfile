FROM python:3-slim as builder

COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --target=/app -r requirements.txt

FROM gcr.io/distroless/python3
COPY --from=builder /app /app
ENTRYPOINT ["python"]
CMD ["/app/main.py"]