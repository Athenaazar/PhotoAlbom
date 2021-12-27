# set timezone
FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
# ENV TZ Asia/Tehran
RUN apt install tzdata
RUN apt-get update && apt install nano
RUN mkdir /home/AthenaPhotoProject
WORKDIR /home/AthenaPhotoProject

# ==========================================

COPY AthenaPhoto/requirements.txt /home/AthenaPhotoProject/
# =========================================
RUN pip install --upgrade pip

# ------------------------------------------

RUN pip install -r requirements.txt
# ------------------------------------------

COPY . /home/AthenaPhotoProject/

