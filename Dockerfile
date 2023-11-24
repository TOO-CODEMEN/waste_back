FROM python:3.10 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.10-slim
WORKDIR /

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local:$PATH
ENV ROBO_API="OyP2neHdWvlUWNIy2hD3"

CMD [ "python", "-u", "./main.py"]