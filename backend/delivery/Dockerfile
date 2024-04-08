FROM python3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /delivery

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt