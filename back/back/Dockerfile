# Use the official Python base image
FROM python:3.11.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code
EXPOSE 8000

# Copy project files to the container
COPY ./requirements.txt /code/requirements.txt
COPY . /code/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x /code/scripts/entrypoint.sh

CMD /code/scripts/entrypoint.sh