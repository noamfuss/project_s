FROM python:3.12-slim as builder

WORKDIR /app

RUN pip install uv
COPY requirements.txt /app/requirements.txt

RUN uv pip install --system --no-cache -r requirements.txt

FROM python:3.12-slim
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

USER 1000
COPY . /app

EXPOSE 8501

CMD python /app/run_app.py
