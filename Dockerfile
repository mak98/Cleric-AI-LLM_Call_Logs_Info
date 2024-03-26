FROM python:3.9
WORKDIR bot/
COPY . .
RUN pip install --no-cache-dir -r  requirements.txt
ENV PORT 8080
CMD ["python", "backend.py"]