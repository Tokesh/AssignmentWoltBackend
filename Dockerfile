# base image  
FROM python:3.9.1  
# setup environment variable  
ENV DockerHOME=/AssignmentWoltBackend 
  
RUN mkdir -p $DockerHOME  


WORKDIR $DockerHOME  

RUN pip install --upgrade pip  

COPY . $DockerHOME

RUN pip install -r requirements.txt

EXPOSE 8000  

CMD python3 manage.py test
CMD python3 manage.py runserver 0.0.0.0:8000
