FROM python:3.11-alpine as base

FROM base as builder

COPY requirements.txt .
RUN pip3 install --prefix=/install -r requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY app.py /app/
COPY models.py /app/
COPY scripts/dev-entrypoint.sh /app/dev-entrypoint.sh

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/app/dev-entrypoint.sh"]