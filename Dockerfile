FROM python:3.13-alpine

WORKDIR /backend

COPY ./requirements/dev.txt /backend/requirements/dev.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements/dev.txt

COPY ./src /backend/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
