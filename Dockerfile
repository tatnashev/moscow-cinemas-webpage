FROM python:3
WORKDIR /app
COPY static /app/
COPY templates /app/
COPY app.py /app/
COPY requirements.txt /app/
COPY .idea /app/
COPY venv /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
