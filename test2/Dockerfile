FROM python:3.9

WORKDIR /code

COPY src/ /code/src
COPY specs/ /code/specs
COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir -p /code/output

# Run the command to start the application
CMD [ "python3", "src/main.py" ]
