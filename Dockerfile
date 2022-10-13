FROM python:3.7.3

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /vtrust
COPY requirements.txt /vtrust/requirements.txt

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /vtrust

# running migrations
RUN python manage.py migrate

# runserver
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]

