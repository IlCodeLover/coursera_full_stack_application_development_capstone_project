FROM python:3.9.18-slim-bookworm


WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN ls
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# Expose port 5050
EXPOSE 5050
# Set the Flask app to listen on port 3031
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050"]
