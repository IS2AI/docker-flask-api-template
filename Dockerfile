FROM python:3.6

RUN apt update -y
RUN apt install -y vim
RUN apt install -y python3-pip
RUN apt install -y python-pip

RUN /usr/bin/pip install --upgrade pip
RUN pip3 install matplotlib
RUN pip3 install opencv-python
RUN pip3 install flask
RUN apt update && apt install -y libsm6 libxext6

RUN mkdir /program
ADD program /program
COPY program/requirements.txt /program
WORKDIR /program

RUN pip3 install -r /program/requirements.txt

EXPOSE 80
ENTRYPOINT ["python3", "app.py"]

